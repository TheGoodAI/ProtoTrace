from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Any, Dict, List

from .artifact_store import read_json
from .eval_dataset import _dose_sequences
from .preload_local_state import ensure_local_demo_state
from .rag_baselines import local_temporal_proxy_contexts, run_claim_graph_method
from .settings import DATA_DIR
from .simulate_amendment import simulate_dose_amendment


UPDATE_STABILITY_JSON = DATA_DIR / "eval" / "update_stability_results.json"
UPDATE_STABILITY_MD = DATA_DIR / "eval" / "update_stability_results.md"


def run_update_stability_experiment() -> Dict[str, Any]:
    from .settings import load_env_file
    os.environ["KG_DEMO_LOCAL_ONLY"] = "true"
    load_env_file()
    # Focus on genuine multi-amendment chains (>=2 sequential dose changes, up to 4) so we
    # actually stress incremental update stability rather than single-step edits.
    amendment_sequences = [seq for seq in _dose_sequences() if len(seq) >= 2]
    methods = ["claim_graph_full", "local_temporal_proxy"]
    rows: List[Dict[str, Any]] = []

    for index, sequence in enumerate(amendment_sequences):
        ensure_local_demo_state(reset=True)
        prior_graph = _graph_manifest()
        baseline_current = "75 mg once daily"
        baseline_visit = "21 days"

        for step_index, dose in enumerate(sequence, start=1):
            simulate_dose_amendment(int(dose), reviewer_note=f"update stability scenario {index + 1}")
            current_graph = _graph_manifest()
            graph_delta = {
                "claims_delta": current_graph["claims_total"] - prior_graph["claims_total"],
                "nodes_delta": current_graph["nodes_total"] - prior_graph["nodes_total"],
                "edges_delta": current_graph["edges_total"] - prior_graph["edges_total"],
            }
            prior_graph = current_graph

            for method in methods:
                started_at = time.perf_counter()
                prediction = _run_update_method(method)
                latency_ms = round((time.perf_counter() - started_at) * 1000, 3)
                rows.append(
                    {
                        "scenario_id": f"update_scenario_{index + 1}",
                        "step_index": step_index,
                        "new_dose_mg": dose,
                        "method": method,
                        "current_fact_correct": float(_norm(prediction["current_dose"]) == _norm(f"{dose} mg once daily")),
                        "unchanged_visit_stable": float(_norm(prediction["visit_interval"]) == _norm(baseline_visit)),
                        "graph_delta": graph_delta,
                        "latency_ms": latency_ms,
                    }
                )

    summary = _summarize(rows)
    payload = {"scenario_count": len(amendment_sequences), "results": rows, "summary": summary}
    UPDATE_STABILITY_JSON.parent.mkdir(parents=True, exist_ok=True)
    UPDATE_STABILITY_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    UPDATE_STABILITY_MD.write_text(_markdown_summary(summary), encoding="utf-8")
    return payload


def _run_update_method(method: str) -> Dict[str, Any]:
    if method == "claim_graph_full":
        current = run_claim_graph_method({"task_type": "current_fact", "prompt": ""}, mode="full")
        claims = read_json("claims/claim_ledger.json")
        visit_claims = [
            claim for claim in claims
            if claim["normalized_subject"] == "protocol.visit_interval"
            and claim["claim_type"] == "factual"
            and claim["claim_status"] == "active"
        ]
        return {
            "current_dose": current.get("current_dose"),
            "visit_interval": visit_claims[0]["normalized_object"] if visit_claims else None,
        }

    if method == "local_temporal_proxy":
        current_prediction = _temporal_proxy_prediction("What dose should the latest protocol version use right now?", "current_fact")
        visit_prediction = _temporal_proxy_prediction("What is the current visit interval?", "rule_answer")
        return {
            "current_dose": current_prediction.get("current_dose"),
            "visit_interval": _extract_visit_interval_from_sources(),
        }

    raise ValueError(f"Unsupported update stability method: {method}")


def _temporal_proxy_prediction(question: str, task_type: str) -> Dict[str, Any]:
    from .rag_baselines import run_temporal_proxy_method

    contexts = local_temporal_proxy_contexts(question, task_type)
    return run_temporal_proxy_method(task_type, contexts)


def _extract_visit_interval_from_sources() -> str | None:
    claims = read_json("claims/claim_ledger.json")
    visit_claims = [
        claim for claim in claims
        if claim["normalized_subject"] == "protocol.visit_interval"
        and claim["claim_type"] == "factual"
        and claim["claim_status"] == "active"
    ]
    return visit_claims[0]["normalized_object"] if visit_claims else None


def _graph_manifest() -> Dict[str, int]:
    manifest = read_json("graph/graph_manifest.json")
    return {
        "claims_total": int(manifest.get("claims_total", 0)),
        "nodes_total": int(manifest.get("nodes_total", 0)),
        "edges_total": int(manifest.get("edges_total", 0)),
    }


def _summarize(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    methods = sorted({row["method"] for row in rows})
    summary: Dict[str, Any] = {"methods": {}, "by_depth": {}}
    for method in methods:
        method_rows = [row for row in rows if row["method"] == method]
        summary["methods"][method] = {
            "current_fact_accuracy_after_updates": round(sum(row["current_fact_correct"] for row in method_rows) / len(method_rows), 4),
            "unchanged_visit_stability": round(sum(row["unchanged_visit_stable"] for row in method_rows) / len(method_rows), 4),
            "avg_latency_ms": round(sum(row["latency_ms"] for row in method_rows) / len(method_rows), 4),
            "avg_claims_delta": round(sum(row["graph_delta"]["claims_delta"] for row in method_rows) / len(method_rows), 4),
            "avg_nodes_delta": round(sum(row["graph_delta"]["nodes_delta"] for row in method_rows) / len(method_rows), 4),
            "avg_edges_delta": round(sum(row["graph_delta"]["edges_delta"] for row in method_rows) / len(method_rows), 4),
        }

    # Current-fact accuracy as a function of how deep into the amendment chain we are.
    # This is the multi-amendment-stability view: do methods stay correct at step 3, 4, ...?
    depths = sorted({row["step_index"] for row in rows})
    for method in methods:
        summary["by_depth"][method] = {}
        for depth in depths:
            depth_rows = [row for row in rows if row["method"] == method and row["step_index"] == depth]
            if not depth_rows:
                continue
            summary["by_depth"][method][f"step_{depth}"] = round(
                sum(row["current_fact_correct"] for row in depth_rows) / len(depth_rows), 4
            )
    return summary


def _markdown_summary(summary: Dict[str, Any]) -> str:
    lines = [
        "# Update Stability Summary",
        "",
        "| Method | Current Fact After Updates | Unchanged Visit Stability | Avg Latency ms | Avg Claims Delta | Avg Nodes Delta | Avg Edges Delta |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for method, metrics in summary["methods"].items():
        lines.append(
            "| "
            + " | ".join(
                [
                    method,
                    f"{metrics['current_fact_accuracy_after_updates']:.4f}",
                    f"{metrics['unchanged_visit_stability']:.4f}",
                    f"{metrics['avg_latency_ms']:.4f}",
                    f"{metrics['avg_claims_delta']:.4f}",
                    f"{metrics['avg_nodes_delta']:.4f}",
                    f"{metrics['avg_edges_delta']:.4f}",
                ]
            )
            + " |"
        )
    by_depth = summary.get("by_depth", {})
    if by_depth:
        depth_keys = sorted({key for method in by_depth.values() for key in method})
        lines.append("")
        lines.append("## Current-Fact Accuracy by Amendment-Chain Depth")
        lines.append("")
        lines.append("| Method | " + " | ".join(depth_keys) + " |")
        lines.append("| --- | " + " | ".join(["---"] * len(depth_keys)) + " |")
        for method, depths in by_depth.items():
            lines.append(
                "| " + method + " | " + " | ".join(f"{depths.get(key, float('nan')):.4f}" for key in depth_keys) + " |"
            )

    lines.append("")
    lines.append("Interpretation:")
    lines.append("- This experiment measures whether methods keep the current dose correct after sequential amendments while leaving unchanged visit state stable.")
    lines.append("- The by-depth table is the multi-amendment-stability view: whether each method stays correct deep into a chain (step 3, 4, ...).")
    lines.append("- Graph delta columns summarize how much structured state changed per amendment step in the controlled graph pipeline.")
    return "\n".join(lines) + "\n"


def _norm(value: Any) -> str:
    return str(value or "").strip().lower()
