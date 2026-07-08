"""LLM-as-judge for free-form answer scoring.

Exact/substring string match unfairly penalizes generative baselines whose
paraphrased answers are substantively correct (and can unfairly flatter the
claim system, which emits the canonical gold string verbatim). For free-form
regulatory-rule answers we therefore grade semantic equivalence with a cached
LLM judge. The gold here is an objective, externally-verifiable regulatory fact
(not the annotation-dependent impact/governance gold), so judging it is fair.

The optional judge fails closed. It is not used by the deterministic release
benchmark, and failed model calls are never converted into judge scores.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict

from .llm_normalizer import build_azure_openai_client
from .settings import DATA_DIR, load_env_file

JUDGE_CACHE_PATH = DATA_DIR / "eval" / "judge_cache.json"
CACHE_SCHEMA_VERSION = 2


def _cache_key(question: str, gold: str, prediction: str, model: str) -> str:
    payload = json.dumps(
        {"q": question, "gold": gold, "pred": prediction, "model": model},
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _load_cache() -> Dict[str, Any]:
    if not JUDGE_CACHE_PATH.exists():
        return {}
    try:
        return json.loads(JUDGE_CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def _store_cache(cache: Dict[str, Any]) -> None:
    JUDGE_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    JUDGE_CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def judge_rule_answer(question: str, gold: str, prediction: str) -> float:
    """Return 1.0 if the prediction conveys the same core regulatory requirement
    as the gold canonical answer (paraphrase allowed, omission/contradiction not),
    else 0.0. Deterministic (temperature 0) and cached."""
    gold = str(gold or "").strip()
    prediction = str(prediction or "").strip()
    if not prediction:
        return 0.0
    if not gold:
        return 0.0

    load_env_file()
    model = os.environ.get("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o")
    key = _cache_key(question, gold, prediction, model)
    cache = _load_cache()
    entry = cache.get(key)
    if (
        isinstance(entry, dict)
        and entry.get("cache_schema_version") == CACHE_SCHEMA_VERSION
        and entry.get("provenance", {}).get("backend") == "azure_openai"
    ):
        return float(entry["match"])

    client = build_azure_openai_client()
    instructions = {
            "role": "regulatory QA grader",
            "question": question,
            "gold_canonical_answer": gold,
            "candidate_answer": prediction,
            "criteria": [
                "Mark match=true only if the candidate conveys the same core regulatory "
                "requirement as the gold.",
                "Paraphrase and added correct detail are acceptable.",
                "Mark match=false if the candidate omits a required action that the gold "
                "states, contradicts the gold, or is non-committal.",
            ],
            "output_schema": {"match": "boolean", "reason": "short string"},
        }
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You grade regulatory answers. Output valid JSON only."},
            {"role": "user", "content": json.dumps(instructions)},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    payload = json.loads(response.choices[0].message.content or "{}")
    match = 1.0 if bool(payload.get("match")) else 0.0
    cache[key] = {
        "cache_schema_version": CACHE_SCHEMA_VERSION,
        "match": match,
        "reason": payload.get("reason", ""),
        "provenance": {"backend": "azure_openai", "model": model},
    }
    _store_cache(cache)
    return match
