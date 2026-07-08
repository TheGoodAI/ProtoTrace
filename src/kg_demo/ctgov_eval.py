"""Evaluate methods on the real ClinicalTrials.gov amendment benchmark.

We focus on the ``ctgov_changed_modules`` task: given the registry records of two consecutive
versions, predict which study modules changed. The gold is the registry's own declared
``moduleLabels`` -- produced independently of any method here, so this is a genuine, external,
non-circular comparison.

Methods:
  * ``structured_diff``  -- the claim-centered analog: detect changed state by comparing
                            structured fields between versions (no LLM, deterministic).
  * ``llm_over_text``    -- optional fail-closed LLM experiment. It is excluded from the
                            release table unless every row has auditable model provenance.
  * ``predict_all``      -- naive high-recall baseline that always predicts every module.

Reported metric: macro set-F1 against the registry gold, plus precision/recall.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
from typing import Any, Dict, List

from .llm_normalizer import build_azure_openai_client
from .settings import DATA_DIR, load_env_file

BENCHMARK_PATH = DATA_DIR / "eval" / "ctgov_amendment_benchmark.json"
RESULTS_MD = DATA_DIR / "eval" / "ctgov_eval_results.md"
RESULTS_JSON = DATA_DIR / "eval" / "ctgov_eval_results.json"
LLM_CACHE_PATH = DATA_DIR / "eval" / "ctgov_llm_cache.json"
LLM_CACHE_SCHEMA_VERSION = 2

MODULES = ["eligibility", "arms interventions", "outcomes", "design", "status"]
FIELD_TO_MODULE = {
    "eligibility_criteria": "eligibility",
    "minimum_age": "eligibility",
    "maximum_age": "eligibility",
    "sex": "eligibility",
    "healthy_volunteers": "eligibility",
    "study_population": "eligibility",
    "sampling_method": "eligibility",
    "interventions": "arms interventions",
    "arm_groups": "arms interventions",
    "primary_outcomes": "outcomes",
    "secondary_outcomes": "outcomes",
    "enrollment": "design",
    "study_type": "design",
    "phases": "design",
    "allocation": "design",
    "intervention_model": "design",
    "primary_purpose": "design",
    "masking": "design",
    "overall_status": "status",
    "why_stopped": "status",
    "start_date": "status",
    "completion_date": "status",
    "primary_completion_date": "status",
    "status_verified_date": "status",
}


def _set_f1(gold: List[str], pred: List[str]) -> Dict[str, float]:
    g, p = set(gold), set(pred)
    if not g and not p:
        return {"f1": 1.0, "precision": 1.0, "recall": 1.0}
    if not g or not p:
        return {"f1": 0.0, "precision": 0.0 if p else 1.0, "recall": 0.0 if g else 1.0}
    inter = len(g & p)
    precision = inter / len(p)
    recall = inter / len(g)
    f1 = 0.0 if precision + recall == 0 else 2 * precision * recall / (precision + recall)
    return {"f1": f1, "precision": precision, "recall": recall}


def _predict_structured(before: Dict[str, Any], after: Dict[str, Any]) -> List[str]:
    changed = set()
    for field, module in FIELD_TO_MODULE.items():
        if (before.get(field) or "") != (after.get(field) or ""):
            changed.add(module)
    return sorted(changed)


def _predict_all(*_args) -> List[str]:
    return list(MODULES)


def _llm_cache() -> Dict[str, Any]:
    if LLM_CACHE_PATH.exists():
        try:
            return json.loads(LLM_CACHE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _store_llm_cache(cache: Dict[str, Any]) -> None:
    LLM_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    LLM_CACHE_PATH.write_text(json.dumps(cache, indent=2), encoding="utf-8")


def _predict_llm(before: Dict[str, Any], after: Dict[str, Any], cache: Dict[str, Any]) -> List[str]:
    key = hashlib.sha256(json.dumps([before, after], sort_keys=True).encode()).hexdigest()
    entry = cache.get(key)
    if (
        isinstance(entry, dict)
        and entry.get("cache_schema_version") == LLM_CACHE_SCHEMA_VERSION
        and entry.get("provenance", {}).get("backend") == "azure_openai"
    ):
        return list(entry["prediction"])

    client = build_azure_openai_client()
    model = os.environ.get("AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "gpt-4o-mini")
    prompt = {
        "task": "Given a clinical trial record before and after an amendment, list which "
        "modules changed.",
        "allowed_modules": MODULES,
        "before": before,
        "after": after,
        "output_schema": {"changed_modules": ["module"]},
        "rules": ["Only use the allowed module names.", "Output valid JSON only."],
    }
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You compare records and output valid JSON only."},
            {"role": "user", "content": json.dumps(prompt)},
        ],
        temperature=0.0,
        response_format={"type": "json_object"},
    )
    payload = json.loads(resp.choices[0].message.content or "{}")
    pred = [m for m in payload.get("changed_modules", []) if m in MODULES]
    cache[key] = {
        "cache_schema_version": LLM_CACHE_SCHEMA_VERSION,
        "prediction": pred,
        "provenance": {
            "backend": "azure_openai",
            "model": model,
            "cache_hit": False,
        },
    }
    _store_llm_cache(cache)
    return pred


def run_ctgov_eval(use_llm: bool = False, llm_limit: int | None = None) -> Dict[str, Any]:
    load_env_file()
    data = json.loads(BENCHMARK_PATH.read_text(encoding="utf-8"))
    tasks = [t for t in data["tasks"] if t["task_type"] == "ctgov_changed_modules"]

    methods = {
        "structured_diff": _predict_structured,
        "predict_all": _predict_all,
    }
    scores: Dict[str, List[Dict[str, float]]] = {m: [] for m in methods}
    if use_llm:
        scores["llm_over_text"] = []
    cache = _llm_cache()

    for index, task in enumerate(tasks):
        before, after, gold = task["before"], task["after"], task["gold"]["changed_modules"]
        for name, fn in methods.items():
            scores[name].append(_set_f1(gold, fn(before, after)))
        if use_llm and (llm_limit is None or index < llm_limit):
            scores["llm_over_text"].append(_set_f1(gold, _predict_llm(before, after, cache)))

    summary = {
        name: {
            "f1": round(sum(s["f1"] for s in rows) / len(rows), 4),
            "precision": round(sum(s["precision"] for s in rows) / len(rows), 4),
            "recall": round(sum(s["recall"] for s in rows) / len(rows), 4),
            "n": len(rows),
        }
        for name, rows in scores.items()
        if rows
    }
    payload = {"task": "ctgov_changed_modules", "task_count": len(tasks), "summary": summary}
    RESULTS_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    RESULTS_MD.write_text(_markdown(payload), encoding="utf-8")
    return payload


def _markdown(payload: Dict[str, Any]) -> str:
    display = {
        "structured_diff": "Structured state comparison",
        "llm_over_text": "LLM-over-text",
        "predict_all": "Predict-all (naive)",
    }
    lines = [
        "# Real-Data Evaluation: ClinicalTrials.gov Changed-Module Detection",
        "",
        f"Task: `{payload['task']}` over **{payload['task_count']}** real amendments.",
        "Gold = registry-declared changed modules (non-circular, external).",
        "",
        "| Method | Set-F1 | Precision | Recall | N |",
        "| --- | --- | --- | --- | --- |",
    ]
    order = ["structured_diff", "llm_over_text", "predict_all"]
    for name in order:
        if name in payload["summary"]:
            s = payload["summary"][name]
            lines.append(f"| {display.get(name, name)} | {s['f1']:.4f} | {s['precision']:.4f} | {s['recall']:.4f} | {s['n']} |")
    lines += [
        "",
        "Notes:",
        "- `Structured state comparison` deterministically compares the tracked before/after "
        "fields. It is a component-level transfer test, not the full claim-graph system.",
        "- `LLM-over-text` is optional, fail-closed, and reported only when model provenance "
        "is present for every evaluated row.",
        "- `Predict-all (naive)` always predicts every module (high recall, low precision).",
        "- This is real, externally-labeled data, so no method saturates at 1.0; the registry "
        "marks module changes outside our extracted schema, which bounds recall for any "
        "content-based method.",
    ]
    return "\n".join(lines) + "\n"
