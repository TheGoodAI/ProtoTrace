from __future__ import annotations

import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

import requests
import urllib3

from .artifact_store import read_json
from .impact_analyzer import analyze_protocol_impacts, analyze_protocol_impacts_for_subject
from .llm_normalizer import build_azure_openai_client
from .query_engine import GraphQueryEngine
from .settings import DATA_DIR, load_env_file


EVAL_CACHE_PATH = DATA_DIR / "eval" / "rag_answer_cache.json"
CACHE_SCHEMA_VERSION = 2

_RULE_STOPWORDS = {
    "a", "about", "according", "an", "and", "are", "as", "be", "before",
    "beyond", "does", "for", "from", "if", "in", "into", "is", "it", "of",
    "on", "or", "should", "such", "the", "to", "under", "what", "where",
    "which", "with",
}


def _verify_ssl() -> bool:
    return os.environ.get("AZURE_SEARCH_VERIFY_SSL", "false").lower() == "true"


if not _verify_ssl():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def _tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _score_query_against_chunk(query: str, chunk: Dict[str, Any]) -> int:
    query_tokens = set(_tokenize(query))
    chunk_tokens = set(
        _tokenize(
            " ".join(
                [
                    chunk.get("title", ""),
                    chunk.get("heading", ""),
                    chunk.get("text", ""),
                ]
            )
        )
    )
    return len(query_tokens & chunk_tokens)


def local_rag_contexts(question: str, top_k: int = 6) -> List[Dict[str, Any]]:
    chunks: List[Dict[str, Any]] = read_json("chunks/all_chunks.json")
    ranked = sorted(
        chunks,
        key=lambda chunk: (
            _score_query_against_chunk(question, chunk),
            chunk.get("source_id", ""),
            chunk.get("section_index", 0),
        ),
        reverse=True,
    )
    return ranked[:top_k]


def local_temporal_proxy_contexts(question: str, task_type: str, top_k: int = 8) -> List[Dict[str, Any]]:
    base_contexts = local_rag_contexts(question, top_k=max(top_k * 2, 12))
    return temporal_proxy_contexts(base_contexts, task_type, top_k=top_k)


def azure_search_contexts(question: str, top_k: int = 6) -> List[Dict[str, Any]]:
    load_env_file()
    endpoint = os.environ.get("AZURE_SEARCH_ENDPOINT")
    service_name = os.environ.get("AZURE_SEARCH_SERVICE_NAME")
    index_name = os.environ.get("AZURE_SEARCH_INDEX_NAME")
    api_key = os.environ.get("AZURE_SEARCH_API_KEY")
    api_version = os.environ.get("AZURE_SEARCH_API_VERSION", "2025-09-01")

    if not endpoint and service_name:
        endpoint = f"https://{service_name}.search.windows.net"

    if not endpoint or not index_name or not api_key:
        raise RuntimeError("Azure Search is not fully configured. Expected endpoint/service, index name, and API key.")

    response = requests.post(
        f"{endpoint}/indexes/{index_name}/docs/search?api-version={api_version}",
        headers={"api-key": api_key, "Content-Type": "application/json"},
        json={
            "search": question,
            "top": top_k,
            "queryType": "simple",
        },
        verify=_verify_ssl(),
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()
    contexts: List[Dict[str, Any]] = []
    for row in payload.get("value", []):
        contexts.append(
            {
                "chunk_id": row.get("chunk_id") or row.get("id") or row.get("key") or "",
                "source_id": row.get("source_id") or row.get("source") or "unknown_source",
                "title": row.get("title") or row.get("document_title") or row.get("source_id") or "unknown_title",
                "heading": row.get("heading") or row.get("section") or "",
                "text": row.get("text") or row.get("content") or row.get("chunk") or "",
            }
        )
    return contexts


def azure_search_temporal_proxy_contexts(question: str, task_type: str, top_k: int = 8) -> List[Dict[str, Any]]:
    base_contexts = azure_search_contexts(question, top_k=max(top_k * 2, 12))
    return temporal_proxy_contexts(base_contexts, task_type, top_k=top_k)


def temporal_proxy_contexts(contexts: List[Dict[str, Any]], task_type: str, top_k: int = 8) -> List[Dict[str, Any]]:
    """Version-aware retrieval proxy without claim-ledger access.

    The proxy reorders or filters retrieved chunks using source-id version heuristics so we
    can compare plain RAG with a lighter-weight temporal retrieval strategy.
    """

    protocol_rows = [row for row in contexts if _protocol_version(row.get("source_id", "")) is not None]
    regulatory_rows = [row for row in contexts if _protocol_version(row.get("source_id", "")) is None]

    if task_type == "current_fact":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "previous_fact":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "previous", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "dose_history":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "all", top_k=top_k),
            top_k,
        )
    if task_type == "changed_source":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 1) + regulatory_rows[:1],
            top_k,
        )
    if task_type == "current_visit":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "previous_visit":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "previous", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "visit_history":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "all", top_k=top_k),
            top_k,
        )
    if task_type == "changed_source_visit":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 1) + regulatory_rows[:1],
            top_k,
        )
    if task_type == "current_eligibility":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "previous_eligibility":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "previous", top_k=top_k - 2) + regulatory_rows[:2],
            top_k,
        )
    if task_type == "eligibility_history":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "all", top_k=top_k),
            top_k,
        )
    if task_type == "changed_source_eligibility":
        return _merge_unique(
            _select_protocol_versions(protocol_rows, "latest", top_k=top_k - 1) + regulatory_rows[:1],
            top_k,
        )
    if task_type.startswith("impact_sections") or task_type.startswith("governing_sources"):
        scored = sorted(
            contexts,
            key=lambda row: (
                _governance_priority(row),
                _protocol_version(row.get("source_id", "")) or 0,
                _score_query_against_chunk("dose amendment impact protocol section policy governance", row),
            ),
            reverse=True,
        )
        return _merge_unique(scored, top_k)
    if task_type == "rule_answer":
        scored = sorted(
            contexts,
            key=lambda row: (
                _rule_priority(row),
                _score_query_against_chunk("rule requirement amendment guidance regulation policy", row),
            ),
            reverse=True,
        )
        return _merge_unique(scored, top_k)
    return _merge_unique(contexts, top_k)


def available_eval_methods(azure_ready: bool) -> List[Dict[str, str]]:
    methods: List[Dict[str, str]] = [
        {"name": "claim_graph_full", "family": "claim_graph", "mode": "full"},
        {"name": "claim_temporal_only", "family": "claim_graph", "mode": "temporal_only"},
        {"name": "claim_no_governance", "family": "claim_graph", "mode": "no_governance"},
        {"name": "claim_no_impact", "family": "claim_graph", "mode": "no_impact"},
        {"name": "local_temporal_proxy", "family": "temporal_proxy", "retriever": "local_temporal_proxy"},
    ]

    seen_rag: set[str] = set()
    rag_specs = [
        ("local_rag_mini", "local", "AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "AZURE_OPENAI_MINI_API_VERSION"),
        ("local_rag_gpt4o", "local", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"),
        ("local_rag_o4_mini", "local", "AZURE_OPENAI_o4_MINI_DEPLOYMENT_NAME", "AZURE_OPENAI_o4_MINI_API_VERSION"),
        # VersionRAG-style fair baseline: version-aware retrieval (claim-ledger-free)
        # feeding an LLM synthesizer. This approximates the closest prior family
        # (version/temporal RAG) without the explicit temporal claim ledger.
        ("versionrag_style_gpt4o", "local_temporal_proxy", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"),
        ("versionrag_style_mini", "local_temporal_proxy", "AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "AZURE_OPENAI_MINI_API_VERSION"),
    ]
    if azure_ready:
        methods.append({"name": "azure_temporal_proxy", "family": "temporal_proxy", "retriever": "azure_search_temporal_proxy"})
        rag_specs.extend(
            [
                ("azure_search_mini", "azure_search", "AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "AZURE_OPENAI_MINI_API_VERSION"),
                ("azure_search_gpt4o", "azure_search", "AZURE_OPENAI_DEPLOYMENT_NAME", "AZURE_OPENAI_API_VERSION"),
                ("azure_search_o4_mini", "azure_search", "AZURE_OPENAI_o4_MINI_DEPLOYMENT_NAME", "AZURE_OPENAI_o4_MINI_API_VERSION"),
            ]
        )

    for name, retriever, deployment_env, api_version_env in rag_specs:
        deployment = os.environ.get(deployment_env)
        if not deployment:
            continue
        key = f"{retriever}:{deployment}"
        if key in seen_rag:
            continue
        seen_rag.add(key)
        methods.append(
            {
                "name": name,
                "family": "traditional_rag",
                "retriever": retriever,
                "deployment_env": deployment_env,
                "api_version_env": api_version_env,
            }
        )

    method_set = os.environ.get("KG_EVAL_METHOD_SET", "release").lower()
    if method_set == "release":
        keep = {
            "claim_graph_full",
            "claim_temporal_only",
            "claim_no_governance",
            "claim_no_impact",
            "local_temporal_proxy",
        }
        methods = [method for method in methods if method["name"] in keep]
    elif method_set == "fair":
        # Honest demo-paper comparison: claim system + ablations vs. a version-aware
        # retrieval proxy and two LLM retrieval baselines (vanilla RAG and a
        # VersionRAG-style version-aware-retrieval+LLM baseline). No broken Azure-Search
        # strawman; all baselines are run locally on the same corpus.
        keep = {
            "claim_graph_full",
            "claim_temporal_only",
            "claim_no_governance",
            "claim_no_impact",
            "local_temporal_proxy",
            "local_rag_gpt4o",
            "versionrag_style_gpt4o",
        }
        methods = [method for method in methods if method["name"] in keep]
    elif method_set == "core":
        keep = {
            "claim_graph_full",
            "claim_temporal_only",
            "claim_no_governance",
            "claim_no_impact",
            "local_temporal_proxy",
            "local_rag_gpt4o",
            "azure_temporal_proxy",
            "azure_search_gpt4o",
        }
        methods = [method for method in methods if method["name"] in keep]
    elif method_set == "paper":
        keep = {
            "claim_graph_full",
            "claim_temporal_only",
            "claim_no_governance",
            "claim_no_impact",
            "local_temporal_proxy",
            "local_rag_mini",
            "local_rag_gpt4o",
            "azure_temporal_proxy",
            "azure_search_mini",
            "azure_search_gpt4o",
        }
        methods = [method for method in methods if method["name"] in keep]

    return methods


def synthesize_rag_answer(
    question: str,
    task_type: str,
    contexts: List[Dict[str, Any]],
    deployment_name: str | None = None,
    api_version: str | None = None,
) -> Dict[str, Any]:
    load_env_file()
    deployment_name = deployment_name or os.environ.get("AZURE_OPENAI_MINI_DEPLOYMENT_NAME", "gpt-4o-mini")
    api_version = api_version or os.environ.get("AZURE_OPENAI_MINI_API_VERSION", "2025-01-01-preview")
    cache_key = _cache_key(question, task_type, contexts, deployment_name, api_version)
    cached = _load_cached_answer(cache_key)
    if cached is not None:
        answer = dict(cached["answer"])
        answer["_provenance"] = {
            **cached["provenance"],
            "cache_hit": True,
        }
        return answer

    try:
        client = build_azure_openai_client(api_version=api_version)
        prompt = {
            "task_type": task_type,
            "question": question,
            "rules": [
                "Use only the provided contexts.",
                "Do not use any external knowledge.",
                "Return compact JSON only.",
                "If the answer is uncertain, return the best grounded answer from context.",
                "Always include supporting_sources as a list of source_id values from the provided contexts.",
            ],
            "schemas": {
                "current_fact": {"current_dose": "string", "supporting_sources": ["source_id"]},
                "previous_fact": {"previous_dose": "string", "supporting_sources": ["source_id"]},
                "dose_history": {"dose_history": ["string"], "supporting_sources": ["source_id"]},
                "changed_source": {"changed_source": "source_id", "supporting_sources": ["source_id"]},
                "current_visit": {"current_visit": "string", "supporting_sources": ["source_id"]},
                "previous_visit": {"previous_visit": "string", "supporting_sources": ["source_id"]},
                "visit_history": {"visit_history": ["string"], "supporting_sources": ["source_id"]},
                "changed_source_visit": {"changed_source": "source_id", "supporting_sources": ["source_id"]},
                "current_eligibility": {"current_exclusion": "string", "supporting_sources": ["source_id"]},
                "previous_eligibility": {"previous_exclusion": "string", "supporting_sources": ["source_id"]},
                "eligibility_history": {"exclusion_history": ["string"], "supporting_sources": ["source_id"]},
                "changed_source_eligibility": {"changed_source": "source_id", "supporting_sources": ["source_id"]},
                "impact_sections_all": {"impacted_sections": ["section_id"], "supporting_sources": ["source_id"]},
                "impact_sections_dose_only": {"impacted_sections": ["section_id"], "supporting_sources": ["source_id"]},
                "governing_sources_all": {"governing_sources": ["source_id"], "supporting_sources": ["source_id"]},
                "governing_sources_dose_only": {"governing_sources": ["source_id"], "supporting_sources": ["source_id"]},
                "rule_answer": {"answer": "string", "supporting_sources": ["source_id"]},
            },
            "contexts": contexts,
        }
        started_at = time.perf_counter()
        response = client.chat.completions.create(
            model=deployment_name,
            messages=[
                {"role": "system", "content": "You are a precise retrieval baseline evaluator. Output valid JSON only."},
                {"role": "user", "content": json.dumps(prompt)},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        model_latency_ms = round((time.perf_counter() - started_at) * 1000, 3)
        content = response.choices[0].message.content or "{}"
        normalized = _normalize_rag_payload(task_type, json.loads(content), contexts)
        provenance = {
            "backend": "azure_openai",
            "model": deployment_name,
            "api_version": api_version,
            "cache_hit": False,
            "model_latency_ms": model_latency_ms,
        }
        _store_cached_answer(cache_key, normalized, provenance)
        normalized["_provenance"] = provenance
        return normalized
    except Exception as exc:  # noqa: BLE001
        if os.environ.get("KG_ALLOW_HEURISTIC_FALLBACK", "false").lower() != "true":
            raise RuntimeError(
                f"LLM baseline {deployment_name!r} failed; no fallback result was recorded"
            ) from exc
        normalized = _heuristic_rag_answer(task_type, contexts)
        provenance = {
            "backend": "heuristic_fallback",
            "model": None,
            "api_version": None,
            "cache_hit": False,
            "fallback_error": f"{type(exc).__name__}: {exc}",
        }
        _store_cached_answer(cache_key, normalized, provenance)
        normalized["_provenance"] = provenance
        return normalized


def run_claim_graph_method(task: Dict[str, Any], mode: str = "full") -> Dict[str, Any]:
    engine = GraphQueryEngine()
    impacts = analyze_protocol_impacts()
    dose_impacts = analyze_protocol_impacts_for_subject("protocol.current_dose")
    task_type = task["task_type"]

    if task_type == "current_fact":
        result = engine.answer_current_dose()
        return {
            "current_dose": result.claims[0]["normalized_object"] if result.claims else None,
            "supporting_sources": _claim_sources(result.claims),
        }
    if task_type == "previous_fact":
        claim = engine.get_direct_predecessor_claim("protocol.current_dose")
        return {
            "previous_dose": claim["normalized_object"] if claim else None,
            "supporting_sources": claim["source_ids"] if claim else [],
        }
    if task_type == "dose_history":
        factual_claims = [
            claim
            for claim in engine.claims
            if claim["normalized_subject"] == "protocol.current_dose" and claim["claim_type"] == "factual"
        ]
        factual_claims.sort(key=lambda claim: claim.get("created_at", ""))
        return {
            "dose_history": [claim["normalized_object"] for claim in factual_claims],
            "supporting_sources": _claim_sources(factual_claims),
        }
    if task_type == "changed_source":
        claims = engine.get_active_claims("protocol.current_dose")
        return {
            "changed_source": claims[0]["source_ids"][0] if claims else None,
            "supporting_sources": claims[0]["source_ids"] if claims else [],
        }
    if task_type == "changed_source_visit":
        claims = engine.get_active_claims("protocol.visit_interval")
        return {
            "changed_source": claims[0]["source_ids"][0] if claims else None,
            "supporting_sources": claims[0]["source_ids"] if claims else [],
        }
    if task_type == "current_visit":
        result = engine.answer_current_visit_interval()
        return {
            "current_visit": result.claims[0]["normalized_object"] if result.claims else None,
            "supporting_sources": _claim_sources(result.claims),
        }
    if task_type == "previous_visit":
        claim = engine.get_direct_predecessor_claim("protocol.visit_interval")
        return {
            "previous_visit": claim["normalized_object"] if claim else None,
            "supporting_sources": claim["source_ids"] if claim else [],
        }
    if task_type == "visit_history":
        factual_claims = [
            claim
            for claim in engine.claims
            if claim["normalized_subject"] == "protocol.visit_interval" and claim["claim_type"] == "factual"
        ]
        factual_claims.sort(key=lambda claim: claim.get("created_at", ""))
        return {
            "visit_history": [claim["normalized_object"] for claim in factual_claims],
            "supporting_sources": _claim_sources(factual_claims),
        }
    if task_type == "changed_source_eligibility":
        claims = engine.get_active_claims("protocol.exclusion_criteria")
        return {
            "changed_source": claims[0]["source_ids"][0] if claims else None,
            "supporting_sources": claims[0]["source_ids"] if claims else [],
        }
    if task_type == "current_eligibility":
        claims = engine.get_active_claims("protocol.exclusion_criteria")
        return {
            "current_exclusion": claims[0]["normalized_object"] if claims else None,
            "supporting_sources": _claim_sources(claims[:1]),
        }
    if task_type == "previous_eligibility":
        claim = engine.get_direct_predecessor_claim("protocol.exclusion_criteria")
        return {
            "previous_exclusion": claim["normalized_object"] if claim else None,
            "supporting_sources": claim["source_ids"] if claim else [],
        }
    if task_type == "eligibility_history":
        factual_claims = [
            claim
            for claim in engine.claims
            if claim["normalized_subject"] == "protocol.exclusion_criteria" and claim["claim_type"] == "factual"
        ]
        factual_claims.sort(key=lambda claim: claim.get("created_at", ""))
        return {
            "exclusion_history": [claim["normalized_object"] for claim in factual_claims],
            "supporting_sources": _claim_sources(factual_claims),
        }
    if task_type == "impact_sections_all":
        if mode in {"temporal_only", "no_impact"}:
            return {"impacted_sections": [], "supporting_sources": []}
        return {
            "impacted_sections": [row["section_id"] for row in impacts.get("impacted_sections", [])],
            "supporting_sources": [row["source_id"] for row in impacts.get("changed_sources", [])],
        }
    if task_type == "impact_sections_dose_only":
        if mode in {"temporal_only", "no_impact"}:
            return {"impacted_sections": [], "supporting_sources": []}
        return {
            "impacted_sections": [row["section_id"] for row in dose_impacts.get("impacted_sections", [])],
            "supporting_sources": [row["source_id"] for row in dose_impacts.get("changed_sources", [])],
        }
    if task_type == "governing_sources_all":
        if mode in {"temporal_only", "no_governance"}:
            return {"governing_sources": [], "supporting_sources": []}
        return {
            "governing_sources": [row["source_id"] for row in impacts.get("governing_sources", [])],
            "supporting_sources": [row["source_id"] for row in impacts.get("governing_sources", [])],
        }
    if task_type == "governing_sources_dose_only":
        if mode in {"temporal_only", "no_governance"}:
            return {"governing_sources": [], "supporting_sources": []}
        return {
            "governing_sources": [row["source_id"] for row in dose_impacts.get("governing_sources", [])],
            "supporting_sources": [row["source_id"] for row in dose_impacts.get("governing_sources", [])],
        }
    if task_type == "rule_answer":
        claim = _find_best_rule_claim(engine.claims, task.get("prompt", ""))
        return {
            "answer": claim["normalized_object"] if claim else None,
            "supporting_sources": claim.get("source_ids", []) if claim else [],
            "matched_claim_id": claim.get("claim_id") if claim else None,
            "_provenance": _deterministic_provenance("claim_ledger_lexical_retrieval"),
        }
    raise ValueError(f"Unsupported task type: {task_type}")


def _find_best_rule_claim(claims: List[Dict[str, Any]], question: str) -> Dict[str, Any] | None:
    candidates = [
        claim
        for claim in claims
        if claim["claim_status"] == "active"
        and claim["claim_type"] in {"requirement", "recommendation"}
    ]
    if not candidates:
        return None

    question_tokens = {
        token for token in _tokenize(question) if token not in _RULE_STOPWORDS
    }

    def score(claim: Dict[str, Any]) -> Tuple[int, int, str]:
        subject_text = str(claim.get("normalized_subject", "")).replace("_", " ").replace(".", " ")
        topic_text = " ".join(map(str, claim.get("topic_labels", [])))
        source_text = " ".join(map(str, claim.get("source_ids", []))).replace("_", " ")
        body_text = " ".join(
            [
                str(claim.get("claim_text", "")),
                str(claim.get("retrieval_summary", "")),
                str(claim.get("normalized_object", "")),
                topic_text,
                source_text,
            ]
        )
        subject_tokens = set(_tokenize(subject_text))
        body_tokens = set(_tokenize(body_text))
        weighted_overlap = 3 * len(question_tokens & subject_tokens) + len(question_tokens & body_tokens)
        phrase_bonus = sum(
            2
            for phrase in ("immediate hazard", "source data", "phase 1", "dose increase", "design change")
            if phrase in question.lower() and phrase in body_text.lower()
        )
        return weighted_overlap + phrase_bonus, len(question_tokens & body_tokens), claim.get("claim_id", "")

    ranked = sorted(candidates, key=score, reverse=True)
    best = ranked[0]
    return best if score(best)[0] > 0 else None


def _claim_sources(claims: List[Dict[str, Any]]) -> List[str]:
    sources: List[str] = []
    for claim in claims:
        for source_id in claim.get("source_ids", []):
            if source_id not in sources:
                sources.append(source_id)
    return sources


def _normalize_rag_payload(task_type: str, payload: Dict[str, Any], contexts: List[Dict[str, Any]]) -> Dict[str, Any]:
    if task_type in payload and isinstance(payload[task_type], dict):
        payload = payload[task_type]

    supporting_sources = payload.get("supporting_sources", [])
    if not isinstance(supporting_sources, list):
        supporting_sources = []

    normalized: Dict[str, Any] = {"supporting_sources": supporting_sources}
    if task_type == "current_fact":
        normalized["current_dose"] = payload.get("current_dose")
    elif task_type == "previous_fact":
        normalized["previous_dose"] = payload.get("previous_dose")
    elif task_type == "dose_history":
        normalized["dose_history"] = payload.get("dose_history", [])
    elif task_type == "changed_source":
        normalized["changed_source"] = payload.get("changed_source")
    elif task_type == "current_visit":
        normalized["current_visit"] = payload.get("current_visit")
    elif task_type == "previous_visit":
        normalized["previous_visit"] = payload.get("previous_visit")
    elif task_type == "visit_history":
        normalized["visit_history"] = payload.get("visit_history", [])
    elif task_type == "changed_source_visit":
        normalized["changed_source"] = payload.get("changed_source")
    elif task_type == "current_eligibility":
        normalized["current_exclusion"] = payload.get("current_exclusion")
    elif task_type == "previous_eligibility":
        normalized["previous_exclusion"] = payload.get("previous_exclusion")
    elif task_type == "eligibility_history":
        normalized["exclusion_history"] = payload.get("exclusion_history", [])
    elif task_type == "changed_source_eligibility":
        normalized["changed_source"] = payload.get("changed_source")
    elif task_type in {"impact_sections_all", "impact_sections_dose_only"}:
        normalized["impacted_sections"] = payload.get("impacted_sections", [])
    elif task_type in {"governing_sources_all", "governing_sources_dose_only"}:
        normalized["governing_sources"] = payload.get("governing_sources", [])
    elif task_type == "rule_answer":
        normalized["answer"] = payload.get("answer")
    else:
        return payload

    if not normalized.get("supporting_sources"):
        normalized["supporting_sources"] = _fallback_supporting_sources(contexts)
    return normalized


def _heuristic_rag_answer(task_type: str, contexts: List[Dict[str, Any]]) -> Dict[str, Any]:
    joined = "\n".join(chunk.get("text", "") for chunk in contexts)
    supporting_sources = _fallback_supporting_sources(contexts)
    if task_type == "current_fact":
        doses = _extract_ordered_doses(contexts)
        match = re.search(r"(\d+\s*mg once daily)", joined, flags=re.IGNORECASE)
        current = doses[-1] if doses else (match.group(1) if match else None)
        return {"current_dose": current, "supporting_sources": supporting_sources}
    if task_type == "previous_fact":
        doses = _extract_ordered_doses(contexts)
        return {
            "previous_dose": doses[-2] if len(doses) >= 2 else (doses[0] if doses else None),
            "supporting_sources": supporting_sources,
        }
    if task_type == "dose_history":
        return {"dose_history": _extract_ordered_doses(contexts), "supporting_sources": supporting_sources}
    if task_type == "changed_source":
        source_id = _latest_protocol_source(contexts) or (contexts[0]["source_id"] if contexts else None)
        return {"changed_source": source_id, "supporting_sources": supporting_sources}
    if task_type == "current_visit":
        intervals = _extract_ordered_visit_intervals(contexts)
        match = re.search(r"(\d+\s*days)", joined, flags=re.IGNORECASE)
        current = intervals[-1] if intervals else (match.group(1) if match else None)
        return {"current_visit": current, "supporting_sources": supporting_sources}
    if task_type == "previous_visit":
        intervals = _extract_ordered_visit_intervals(contexts)
        return {
            "previous_visit": intervals[-2] if len(intervals) >= 2 else (intervals[0] if intervals else None),
            "supporting_sources": supporting_sources,
        }
    if task_type == "visit_history":
        return {"visit_history": _extract_ordered_visit_intervals(contexts), "supporting_sources": supporting_sources}
    if task_type == "changed_source_visit":
        source_id = _latest_protocol_source(contexts) or (contexts[0]["source_id"] if contexts else None)
        return {"changed_source": source_id, "supporting_sources": supporting_sources}
    if task_type == "current_eligibility":
        exclusions = _extract_ordered_exclusion_lists(contexts)
        return {"current_exclusion": exclusions[-1] if exclusions else None, "supporting_sources": supporting_sources}
    if task_type == "previous_eligibility":
        exclusions = _extract_ordered_exclusion_lists(contexts)
        return {
            "previous_exclusion": exclusions[-2] if len(exclusions) >= 2 else (exclusions[0] if exclusions else None),
            "supporting_sources": supporting_sources,
        }
    if task_type == "eligibility_history":
        return {"exclusion_history": _extract_ordered_exclusion_lists(contexts), "supporting_sources": supporting_sources}
    if task_type == "changed_source_eligibility":
        source_id = _latest_protocol_source(contexts) or (contexts[0]["source_id"] if contexts else None)
        return {"changed_source": source_id, "supporting_sources": supporting_sources}
    if task_type in {"impact_sections_all", "impact_sections_dose_only"}:
        sections = sorted(set(re.findall(r"Section\s+(\d+\.\d+)", joined, flags=re.IGNORECASE)))
        return {"impacted_sections": sections, "supporting_sources": supporting_sources}
    if task_type in {"governing_sources_all", "governing_sources_dose_only"}:
        filtered = supporting_sources
        if task_type == "governing_sources_dose_only":
            filtered = [
                source_id
                for source_id in supporting_sources
                if source_id in {"fda_ind_protocol_amendments", "sop_dose_change_citation", "ema_gcp_qa"}
            ]
        return {"governing_sources": filtered[:3], "supporting_sources": supporting_sources}
    if task_type == "rule_answer":
        lowered = joined.lower()
        if "immediate hazard" in lowered:
            return {"answer": "implement immediately then notify FDA and IRB", "supporting_sources": supporting_sources}
        if "source data" in lowered and "crf" in lowered:
            return {"answer": "identify source data recorded directly into CRFs", "supporting_sources": supporting_sources}
        if "eligibility" in lowered and "source data" in lowered:
            return {"answer": "document individual eligibility criteria in source data", "supporting_sources": supporting_sources}
        if "study design" in lowered and "eligibility criteria" in lowered:
            return {"answer": "study design, eligibility criteria, and registry requirements", "supporting_sources": supporting_sources}
        if "toxicity" in lowered and "dose adjustment" in lowered:
            return {"answer": "toxicity monitoring, stopping rules, and dose adjustment rules", "supporting_sources": supporting_sources}
        if "protocol amendment" in lowered:
            return {"answer": "protocol amendment required", "supporting_sources": supporting_sources}
    return {"supporting_sources": supporting_sources}


def _fallback_supporting_sources(contexts: List[Dict[str, Any]]) -> List[str]:
    ranked_sources: List[str] = []
    for chunk in contexts:
        source_id = chunk.get("source_id")
        if source_id and source_id not in ranked_sources:
            ranked_sources.append(source_id)
    return ranked_sources


def run_temporal_proxy_method(task_type: str, contexts: List[Dict[str, Any]]) -> Dict[str, Any]:
    answer = _heuristic_rag_answer(task_type, contexts)
    answer["_provenance"] = _deterministic_provenance("version_aware_lexical_proxy")
    return answer


def _deterministic_provenance(backend: str) -> Dict[str, Any]:
    return {
        "backend": backend,
        "model": None,
        "cache_hit": False,
    }


def _protocol_version(source_id: str) -> int | None:
    if source_id == "protocol_v1":
        return 1
    match = re.search(r"protocol_amendment_v(\d+)", source_id)
    if match:
        return int(match.group(1))
    return None


def _select_protocol_versions(rows: List[Dict[str, Any]], mode: str, top_k: int) -> List[Dict[str, Any]]:
    grouped: Dict[int, List[Dict[str, Any]]] = {}
    for row in rows:
        version = _protocol_version(row.get("source_id", ""))
        if version is None:
            continue
        grouped.setdefault(version, []).append(row)

    versions = sorted(grouped)
    if not versions:
        return []

    if mode == "latest":
        selected_versions = [versions[-1]]
    elif mode == "previous":
        if len(versions) >= 2:
            selected_versions = [versions[-2], versions[-1]]
        else:
            selected_versions = [versions[-1]]
    else:
        selected_versions = versions

    ordered_rows: List[Dict[str, Any]] = []
    for version in selected_versions:
        version_rows = sorted(
            grouped[version],
            key=lambda row: (
                _dose_signal(row),
                _visit_signal(row),
                _eligibility_signal(row),
                row.get("section_index", 0),
            ),
            reverse=True,
        )
        ordered_rows.extend(version_rows)

    return _merge_unique(ordered_rows, top_k)


def _merge_unique(rows: List[Dict[str, Any]], top_k: int) -> List[Dict[str, Any]]:
    seen: set[Tuple[str, str, str]] = set()
    merged: List[Dict[str, Any]] = []
    for row in rows:
        key = (
            row.get("chunk_id", ""),
            row.get("source_id", ""),
            row.get("heading", ""),
        )
        if key in seen:
            continue
        seen.add(key)
        merged.append(row)
        if len(merged) >= top_k:
            break
    return merged


def _dose_signal(row: Dict[str, Any]) -> int:
    text = f"{row.get('heading', '')} {row.get('text', '')}".lower()
    return int("mg once daily" in text or "dosing" in text or "dose" in text)


def _visit_signal(row: Dict[str, Any]) -> int:
    text = f"{row.get('heading', '')} {row.get('text', '')}".lower()
    return int("visit" in text or "day" in text or "schedule" in text)


def _eligibility_signal(row: Dict[str, Any]) -> int:
    text = f"{row.get('heading', '')} {row.get('text', '')}".lower()
    return int("exclu" in text or "eligibility" in text)


def _governance_priority(row: Dict[str, Any]) -> int:
    source_id = row.get("source_id", "")
    if source_id == "sop_dose_change_citation":
        return 5
    if source_id == "fda_ind_protocol_amendments":
        return 4
    if source_id == "ema_gcp_qa":
        return 3
    if source_id == "fda_clinical_protocols":
        return 2
    return 1


def _rule_priority(row: Dict[str, Any]) -> int:
    source_id = row.get("source_id", "")
    if source_id in {"fda_ind_protocol_amendments", "ema_gcp_qa", "fda_clinical_protocols", "cdisc_home"}:
        return 5
    if source_id.startswith("protocol_"):
        return 1
    return 2


def _extract_ordered_doses(contexts: List[Dict[str, Any]]) -> List[str]:
    version_to_dose: Dict[int, str] = {}
    for row in contexts:
        version = _protocol_version(row.get("source_id", ""))
        if version is None:
            continue
        match = re.search(r"(\d+\s*mg once daily)", row.get("text", ""), flags=re.IGNORECASE)
        if match and version not in version_to_dose:
            version_to_dose[version] = match.group(1)
    return [version_to_dose[version] for version in sorted(version_to_dose)]


def _extract_ordered_visit_intervals(contexts: List[Dict[str, Any]]) -> List[str]:
    version_to_interval: Dict[int, str] = {}
    for row in contexts:
        version = _protocol_version(row.get("source_id", ""))
        if version is None:
            continue
        match = re.search(r"(\d+\s*days)", row.get("text", ""), flags=re.IGNORECASE)
        if match and version not in version_to_interval:
            version_to_interval[version] = match.group(1)
    return [version_to_interval[version] for version in sorted(version_to_interval)]


def _extract_ordered_exclusion_lists(contexts: List[Dict[str, Any]]) -> List[str]:
    version_to_exclusion: Dict[int, str] = {}
    for row in contexts:
        version = _protocol_version(row.get("source_id", ""))
        if version is None:
            continue
        match = re.search(
            r"subjects currently receiving ([a-z, ]+?) are excluded",
            row.get("text", ""),
            flags=re.IGNORECASE,
        )
        if match and version not in version_to_exclusion:
            drug_list = re.sub(r"\s+or\s+", ", ", match.group(1).strip())
            version_to_exclusion[version] = drug_list
    return [version_to_exclusion[version] for version in sorted(version_to_exclusion)]


def _latest_protocol_source(contexts: List[Dict[str, Any]]) -> str | None:
    ranked: List[Tuple[int, str]] = []
    for row in contexts:
        source_id = row.get("source_id", "")
        version = _protocol_version(source_id)
        if version is not None:
            ranked.append((version, source_id))
    if not ranked:
        return None
    ranked.sort()
    return ranked[-1][1]


def _cache_key(
    question: str,
    task_type: str,
    contexts: List[Dict[str, Any]],
    deployment_name: str,
    api_version: str,
) -> str:
    payload = json.dumps(
        {
            "cache_schema_version": CACHE_SCHEMA_VERSION,
            "question": question,
            "task_type": task_type,
            "contexts": contexts,
            "deployment": deployment_name,
            "api_version": api_version,
        },
        sort_keys=True,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _load_cached_answer(cache_key: str) -> Dict[str, Any] | None:
    if not EVAL_CACHE_PATH.exists():
        return None
    try:
        payload = json.loads(EVAL_CACHE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    entry = payload.get(cache_key)
    if not isinstance(entry, dict):
        return None
    if entry.get("cache_schema_version") != CACHE_SCHEMA_VERSION:
        return None
    if not isinstance(entry.get("answer"), dict) or not isinstance(entry.get("provenance"), dict):
        return None
    if entry["provenance"].get("backend") != "azure_openai":
        return None
    return entry


def _store_cached_answer(
    cache_key: str,
    answer: Dict[str, Any],
    provenance: Dict[str, Any],
) -> None:
    if EVAL_CACHE_PATH.exists():
        try:
            payload = json.loads(EVAL_CACHE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            payload = {}
    else:
        payload = {}
    payload[cache_key] = {
        "cache_schema_version": CACHE_SCHEMA_VERSION,
        "answer": answer,
        "provenance": provenance,
    }
    EVAL_CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    EVAL_CACHE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
