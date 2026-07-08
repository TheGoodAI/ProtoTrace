from __future__ import annotations

import json
import os
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List

from .eval_dataset import TEST_DATASET_PATH, build_eval_dataset
from .preload_local_state import ensure_local_demo_state
from .rag_baselines import (
    available_eval_methods,
    azure_search_contexts,
    azure_search_temporal_proxy_contexts,
    local_rag_contexts,
    local_temporal_proxy_contexts,
    run_claim_graph_method,
    run_temporal_proxy_method,
    synthesize_rag_answer,
)
from .settings import DATA_DIR, load_env_file
from .simulate_amendment import (
    simulate_dose_amendment,
    simulate_eligibility_amendment,
    simulate_visit_interval_amendment,
)


RESULTS_PATH = DATA_DIR / "eval" / "comparison_results.json"
PAPER_SUMMARY_PATH = DATA_DIR / "eval" / "paper_summary.json"
PAPER_SUMMARY_MD_PATH = DATA_DIR / "eval" / "paper_summary.md"
OBJECTIVE_SUMMARY_MD_PATH = DATA_DIR / "eval" / "objective_summary.md"

# Objective task types have gold that is mechanically determined by the amendment
# sequence (temporal facts) or is an externally-verifiable regulatory fact (rules).
# Scoring the system on these is NOT circular.
OBJECTIVE_TASK_TYPES = {
    "current_fact",
    "previous_fact",
    "dose_history",
    "changed_source",
    "rule_answer",
    "current_visit",
    "previous_visit",
    "visit_history",
    "changed_source_visit",
    "current_eligibility",
    "previous_eligibility",
    "eligibility_history",
    "changed_source_eligibility",
}
# Annotation-dependent task types require independent human gold (impacted sections,
# governing sources). The current gold for these mirrors the pipeline's own deterministic
# rules, so quantitative F1 on them is circular and is deferred to human annotation.
ANNOTATION_DEPENDENT_TASK_TYPES = {
    "impact_sections_all",
    "impact_sections_dose_only",
    "governing_sources_all",
    "governing_sources_dose_only",
}


def run_comparison(dataset_path: Path = TEST_DATASET_PATH) -> Dict[str, Any]:
    os.environ["KG_DEMO_LOCAL_ONLY"] = "true"
    # Load credentials so LLM retrieval baselines (local_rag_*, versionrag_style_*)
    # are discovered by available_eval_methods; without this only the deterministic
    # claim and proxy methods are run.
    load_env_file()
    if not dataset_path.exists():
        dataset_path.write_text(json.dumps(build_eval_dataset(), indent=2), encoding="utf-8")

    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
    scenarios_by_id = {scenario["scenario_id"]: scenario for scenario in dataset["scenarios"]}
    methods = available_eval_methods(_azure_search_ready())
    task_results: List[Dict[str, Any]] = []
    for task in dataset["tasks"]:
        scenario = scenarios_by_id.get(task["scenario_id"])
        ensure_local_demo_state(reset=True)
        if scenario:
            amendment_kind = scenario.get("amendment_kind", "dose")
            for value in scenario.get("amendment_sequence", []):
                if amendment_kind == "visit":
                    simulate_visit_interval_amendment(int(value), reviewer_note="evaluation scenario")
                elif amendment_kind == "eligibility":
                    simulate_eligibility_amendment(str(value), reviewer_note="evaluation scenario")
                else:
                    simulate_dose_amendment(int(value), reviewer_note="evaluation scenario")

        for method in methods:
            started_at = time.perf_counter()
            prediction = _run_single_method(method, task)
            wall_time_ms = round((time.perf_counter() - started_at) * 1000, 3)
            score = _score_task(task["task_type"], task["gold"], prediction, scenario, task.get("prompt", ""))
            provenance = prediction.get("_provenance", {})
            if provenance.get("backend") == "azure_openai":
                if not provenance.get("cache_hit") and provenance.get("model_latency_ms") is not None:
                    score["latency_ms"] = float(provenance["model_latency_ms"])
            else:
                score["latency_ms"] = wall_time_ms
            task_results.append(
                {
                    "task_id": task["task_id"],
                    "scenario_id": task["scenario_id"],
                    "task_type": task["task_type"],
                    "method": method["name"],
                    "method_family": method["family"],
                    "prompt": task["prompt"],
                    "gold": task["gold"],
                    "prediction": prediction,
                    "score": score,
                }
            )

    summary = _summarize_results(task_results)
    payload = {
        "dataset_id": dataset["dataset_id"],
        "task_count": len(dataset["tasks"]),
        "methods": [method["name"] for method in methods],
        "method_specs": methods,
        "results": task_results,
        "summary": summary,
        "paper_summary": _paper_summary(summary),
    }
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULTS_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    PAPER_SUMMARY_PATH.write_text(json.dumps(payload["paper_summary"], indent=2), encoding="utf-8")
    PAPER_SUMMARY_MD_PATH.write_text(_paper_summary_markdown(payload["paper_summary"]["table"]), encoding="utf-8")
    OBJECTIVE_SUMMARY_MD_PATH.write_text(_objective_summary_markdown(payload["paper_summary"]["table"]), encoding="utf-8")
    return payload


def _azure_search_ready() -> bool:
    return bool(
        os.environ.get("AZURE_SEARCH_API_KEY")
        and os.environ.get("AZURE_SEARCH_INDEX_NAME")
        and (os.environ.get("AZURE_SEARCH_ENDPOINT") or os.environ.get("AZURE_SEARCH_SERVICE_NAME"))
    )


def _run_single_method(method: Dict[str, str], task: Dict[str, Any]) -> Dict[str, Any]:
    if method["family"] == "claim_graph":
        return run_claim_graph_method(
            {
                "task_type": task["task_type"],
                "prompt": task.get("prompt", ""),
            },
            mode=method["mode"],
        )

    if method["family"] == "temporal_proxy":
        retriever = method["retriever"]
        if retriever == "local_temporal_proxy":
            contexts = local_temporal_proxy_contexts(task["prompt"], task["task_type"])
        elif retriever == "azure_search_temporal_proxy":
            contexts = azure_search_temporal_proxy_contexts(task["prompt"], task["task_type"])
        else:
            raise ValueError(f"Unsupported temporal proxy retriever: {retriever}")
        return run_temporal_proxy_method(task["task_type"], contexts)

    if method["family"] == "traditional_rag":
        retriever = method["retriever"]
        if retriever == "local":
            contexts = local_rag_contexts(task["prompt"])
        elif retriever == "local_temporal_proxy":
            contexts = local_temporal_proxy_contexts(task["prompt"], task["task_type"])
        elif retriever == "azure_search":
            contexts = azure_search_contexts(task["prompt"])
        elif retriever == "azure_search_temporal_proxy":
            contexts = azure_search_temporal_proxy_contexts(task["prompt"], task["task_type"])
        else:
            raise ValueError(f"Unsupported retriever: {retriever}")

        deployment_name = os.environ.get(method["deployment_env"])
        api_version = os.environ.get(method["api_version_env"])
        return synthesize_rag_answer(
            task["prompt"],
            task["task_type"],
            contexts,
            deployment_name=deployment_name,
            api_version=api_version,
        )

    raise ValueError(f"Unsupported method family: {method['family']}")


def _score_task(
    task_type: str,
    gold: Dict[str, Any],
    prediction: Dict[str, Any],
    scenario: Dict[str, Any] | None,
    prompt: str = "",
) -> Dict[str, Any]:
    score: Dict[str, Any] = {}

    if task_type == "current_fact":
        predicted = prediction.get("current_dose")
        score["exact_match"] = _binary_match(predicted, gold["current_dose"])
        score["wrong_version_rate"] = _wrong_version_rate(predicted, gold["current_dose"], scenario["gold"]["dose_history"])
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "previous_fact":
        predicted = prediction.get("previous_dose")
        score["exact_match"] = _binary_match(predicted, gold["previous_dose"])
        score["wrong_temporal_direction_rate"] = _wrong_direction_rate(
            predicted,
            gold["previous_dose"],
            scenario["gold"]["current_dose"],
        )
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "dose_history":
        pred = prediction.get("dose_history", [])
        score["exact_match"] = 1.0 if list(map(_normalize_text, pred)) == list(map(_normalize_text, gold["dose_history"])) else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "changed_source":
        score["exact_match"] = 1.0 if prediction.get("changed_source") == gold["changed_source"] else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "current_visit":
        predicted = prediction.get("current_visit")
        score["exact_match"] = _binary_match(predicted, gold["current_visit"])
        score["wrong_version_rate"] = _wrong_version_rate(predicted, gold["current_visit"], scenario["gold"]["visit_history"])
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "previous_visit":
        predicted = prediction.get("previous_visit")
        score["exact_match"] = _binary_match(predicted, gold["previous_visit"])
        score["wrong_temporal_direction_rate"] = _wrong_direction_rate(
            predicted,
            gold["previous_visit"],
            scenario["gold"]["current_visit"],
        )
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "visit_history":
        pred = prediction.get("visit_history", [])
        score["exact_match"] = 1.0 if list(map(_normalize_text, pred)) == list(map(_normalize_text, gold["visit_history"])) else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "changed_source_visit":
        score["exact_match"] = 1.0 if prediction.get("changed_source") == gold["changed_source"] else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "current_eligibility":
        predicted = prediction.get("current_exclusion")
        score["exact_match"] = _binary_match(predicted, gold["current_exclusion"])
        score["wrong_version_rate"] = _wrong_version_rate(predicted, gold["current_exclusion"], scenario["gold"]["exclusion_history"])
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "previous_eligibility":
        predicted = prediction.get("previous_exclusion")
        score["exact_match"] = _binary_match(predicted, gold["previous_exclusion"])
        score["wrong_temporal_direction_rate"] = _wrong_direction_rate(
            predicted,
            gold["previous_exclusion"],
            scenario["gold"]["current_exclusion"],
        )
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "eligibility_history":
        pred = prediction.get("exclusion_history", [])
        score["exact_match"] = 1.0 if list(map(_normalize_text, pred)) == list(map(_normalize_text, gold["exclusion_history"])) else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "changed_source_eligibility":
        score["exact_match"] = 1.0 if prediction.get("changed_source") == gold["changed_source"] else 0.0
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type in {"impact_sections_all", "impact_sections_dose_only"}:
        score["set_f1"] = _set_f1(gold["impacted_sections"], prediction.get("impacted_sections", []))
        return score

    if task_type in {"governing_sources_all", "governing_sources_dose_only"}:
        score["set_f1"] = _set_f1(gold["governing_sources"], prediction.get("governing_sources", []))
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    if task_type == "rule_answer":
        score["exact_match"] = _contains_match(prediction.get("answer"), gold["answer"])
        score["citation_source_f1"] = _set_f1(gold.get("supporting_sources", []), prediction.get("supporting_sources", []))
        return score

    raise ValueError(f"Unsupported task type: {task_type}")


def _binary_match(predicted: Any, gold: Any) -> float:
    return 1.0 if _normalize_text(predicted) == _normalize_text(gold) else 0.0


def _contains_match(predicted: Any, gold: Any) -> float:
    pred = _normalize_text(predicted)
    gold_norm = _normalize_text(gold)
    if not pred or not gold_norm:
        return 0.0
    if pred == gold_norm:
        return 1.0
    return 1.0 if (gold_norm in pred or pred in gold_norm) else 0.0


def _wrong_version_rate(predicted: Any, current_gold: str, history: List[str]) -> float:
    normalized_prediction = _normalize_text(predicted)
    normalized_current = _normalize_text(current_gold)
    normalized_history = [_normalize_text(item) for item in history]
    if not normalized_prediction or normalized_prediction == normalized_current:
        return 0.0
    return 1.0 if normalized_prediction in normalized_history else 0.0


def _wrong_direction_rate(predicted: Any, previous_gold: str, current_gold: str) -> float:
    normalized_prediction = _normalize_text(predicted)
    if not normalized_prediction or normalized_prediction == _normalize_text(previous_gold):
        return 0.0
    return 1.0 if normalized_prediction == _normalize_text(current_gold) else 0.0


def _set_f1(gold: List[str], pred: List[str]) -> float:
    gold_set = set(gold)
    pred_set = set(pred)
    if not gold_set and not pred_set:
        return 1.0
    if not gold_set or not pred_set:
        return 0.0
    precision = len(gold_set & pred_set) / len(pred_set)
    recall = len(gold_set & pred_set) / len(gold_set)
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)


def _normalize_text(value: Any) -> str:
    return str(value or "").strip().lower()


def _summarize_results(task_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    metrics: Dict[str, Dict[str, List[float]]] = defaultdict(lambda: defaultdict(list))
    by_task_type: Dict[str, Dict[str, Dict[str, List[float]]]] = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))

    for row in task_results:
        method = row["method"]
        task_type = row["task_type"]
        for metric_name, metric_value in row["score"].items():
            if not isinstance(metric_value, (int, float)):
                continue
            metrics[method][metric_name].append(metric_value)
            by_task_type[task_type][method][metric_name].append(metric_value)

    summary = {"overall": {}, "by_task_type": {}}
    for method, method_metrics in metrics.items():
        summary["overall"][method] = {
            metric_name: round(sum(values) / len(values), 4)
            for metric_name, values in method_metrics.items()
        }

    for task_type, methods in by_task_type.items():
        summary["by_task_type"][task_type] = {}
        for method, method_metrics in methods.items():
            summary["by_task_type"][task_type][method] = {
                metric_name: round(sum(values) / len(values), 4)
                for metric_name, values in method_metrics.items()
            }

    return summary


def _paper_summary(summary: Dict[str, Any]) -> Dict[str, Any]:
    overall = summary["overall"]
    by_task = summary["by_task_type"]
    table: Dict[str, Dict[str, float]] = {}
    for method, method_summary in overall.items():
        table[method] = {
            "current_fact_accuracy": by_task.get("current_fact", {}).get(method, {}).get("exact_match", 0.0),
            "wrong_version_rate": by_task.get("current_fact", {}).get(method, {}).get("wrong_version_rate", 0.0),
            "previous_fact_accuracy": by_task.get("previous_fact", {}).get(method, {}).get("exact_match", 0.0),
            "dose_history_accuracy": by_task.get("dose_history", {}).get(method, {}).get("exact_match", 0.0),
            "visit_history_accuracy": by_task.get("visit_history", {}).get(method, {}).get("exact_match", 0.0),
            "eligibility_history_accuracy": by_task.get("eligibility_history", {}).get(method, {}).get("exact_match", 0.0),
            "rule_accuracy": by_task.get("rule_answer", {}).get(method, {}).get("exact_match", 0.0),
            "citation_source_f1": method_summary.get("citation_source_f1", 0.0),
            "impact_section_f1": _average_present(
                [
                    by_task.get("impact_sections_all", {}).get(method, {}).get("set_f1"),
                    by_task.get("impact_sections_dose_only", {}).get(method, {}).get("set_f1"),
                ]
            ),
            "governing_source_f1": _average_present(
                [
                    by_task.get("governing_sources_all", {}).get(method, {}).get("set_f1"),
                    by_task.get("governing_sources_dose_only", {}).get(method, {}).get("set_f1"),
                ]
            ),
            "avg_latency_ms": method_summary.get("latency_ms", 0.0),
        }
    return {
        "table": table,
        "objective_task_types": sorted(OBJECTIVE_TASK_TYPES),
        "annotation_dependent_task_types": sorted(ANNOTATION_DEPENDENT_TASK_TYPES),
        "annotation_note": (
            "impact_section_f1 and governing_source_f1 are computed against pipeline-derived "
            "gold and are reported here only as a capability check, not as an independent "
            "quantitative result. Treat them as requiring human-annotated gold before any "
            "comparative claim. Objective metrics (current/previous/dose-history/changed-source/"
            "rule) have mechanically- or externally-verifiable gold and are non-circular."
        ),
    }


def _objective_summary_markdown(table: Dict[str, Dict[str, float]]) -> str:
    """Objective-only table: excludes the annotation-dependent impact/governance F1
    columns whose gold is currently circular (pipeline-derived)."""
    headers = [
        "Method",
        "Current Fact",
        "Wrong Version",
        "Previous Fact",
        "Dose History",
        "Visit History",
        "Eligibility History",
        "Rule Acc",
        "Citation F1",
        "Latency ms",
    ]
    lines = [
        "# Objective-Task Evaluation Summary (non-circular gold)",
        "",
        "Impact-section and governing-source F1 are intentionally excluded: their current",
        "gold mirrors the pipeline's own deterministic rules and requires independent human",
        "annotation before any comparative claim can be made.",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for method, metrics in table.items():
        lines.append(
            "| "
            + " | ".join(
                [
                    method,
                    _fmt(metrics["current_fact_accuracy"]),
                    _fmt(metrics["wrong_version_rate"]),
                    _fmt(metrics["previous_fact_accuracy"]),
                    _fmt(metrics["dose_history_accuracy"]),
                    _fmt(metrics["visit_history_accuracy"]),
                    _fmt(metrics["eligibility_history_accuracy"]),
                    _fmt(metrics["rule_accuracy"]),
                    _fmt(metrics["citation_source_f1"]),
                    _fmt(metrics["avg_latency_ms"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _average_present(values: List[float | None]) -> float:
    present = [value for value in values if value is not None]
    if not present:
        return 0.0
    return round(sum(present) / len(present), 4)


def _paper_summary_markdown(table: Dict[str, Dict[str, float]]) -> str:
    headers = [
        "Method",
        "Current Fact",
        "Wrong Version",
        "Previous Fact",
        "Dose History",
        "Visit History",
        "Eligibility History",
        "Rule Acc",
        "Citation F1",
        "Impact F1",
        "Governance F1",
        "Latency ms",
    ]
    lines = [
        "# Evaluation Summary",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for method, metrics in table.items():
        lines.append(
            "| "
            + " | ".join(
                [
                    method,
                    _fmt(metrics["current_fact_accuracy"]),
                    _fmt(metrics["wrong_version_rate"]),
                    _fmt(metrics["previous_fact_accuracy"]),
                    _fmt(metrics["dose_history_accuracy"]),
                    _fmt(metrics["visit_history_accuracy"]),
                    _fmt(metrics["eligibility_history_accuracy"]),
                    _fmt(metrics["rule_accuracy"]),
                    _fmt(metrics["citation_source_f1"]),
                    _fmt(metrics["impact_section_f1"]),
                    _fmt(metrics["governing_source_f1"]),
                    _fmt(metrics["avg_latency_ms"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def _fmt(value: float) -> str:
    return f"{value:.4f}" if isinstance(value, float) else str(value)

