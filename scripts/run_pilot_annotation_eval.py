"""Score the LLM-over-text baseline against the n=50 pilot annotation gold
(data/pilot_annotation/gold_labels_v1.json), labeled by an independent human
annotator (faculty advisor), not the system's author.

This does NOT use the claim-graph rule engine (kg_demo.impact_analyzer), which only
covers dose/visit-interval archetypes. It uses the general LLM-over-text baseline
(synthesize_rag_answer) so all 8 archetypes in the pilot pool get a real prediction.

Usage: python scripts/run_pilot_annotation_eval.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kg_demo.rag_baselines import synthesize_rag_answer  # noqa: E402

POOL_PATH = ROOT / "data" / "pilot_annotation" / "protocol_pool_v1.json"
GOLD_PATH = ROOT / "data" / "pilot_annotation" / "gold_labels_v1.json"
OUT_JSON = ROOT / "data" / "eval" / "pilot_llm_baseline_results.json"
OUT_MD = ROOT / "data" / "eval" / "pilot_llm_baseline_results.md"

REF_SLUG = {
    "21 CFR 312.30": "fda_21cfr312_30",
    "21 CFR 312.32": "fda_21cfr312_32",
    "EMA GCP Q&A Section 3": "ema_gcpqa_s3",
    "EMA GCP Q&A Section 5": "ema_gcpqa_s5",
    "ICH E6(R2) Section 4.5": "ich_e6r2_s4_5",
    "SOP-DoseChange-01": "sop_dosechange_01",
    "SOP-SafetyMonitoring-02": "sop_safetymonitoring_02",
    "SOP-Eligibility-03": "sop_eligibility_03",
}


def build_contexts(scenario):
    contexts = [
        {"source_id": "previous_protocol", "title": "Previous protocol text", "heading": "Previous", "text": scenario["previous_protocol_text"]},
        {"source_id": "amendment", "title": "Amendment text", "heading": "Amendment", "text": scenario["amendment_text"]},
    ]
    for code, txt in scenario["context_sections"].items():
        contexts.append({"source_id": code, "title": f"Section {code}", "heading": code, "text": txt})
    for citation, slug in REF_SLUG.items():
        topic = next((r["topic"] for r in scenario["candidate_governing_refs"] if r["citation"] == citation), "")
        authority = next((r["authority"] for r in scenario["candidate_governing_refs"] if r["citation"] == citation), "")
        contexts.append({"source_id": slug, "title": citation, "heading": authority, "text": f"{authority} {citation}: {topic}"})
    return contexts


def prf1(pred, gold):
    pred_set, gold_set = set(pred), set(gold)
    if not pred_set and not gold_set:
        return 1.0, 1.0, 1.0
    tp = len(pred_set & gold_set)
    precision = tp / len(pred_set) if pred_set else 0.0
    recall = tp / len(gold_set) if gold_set else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0
    return precision, recall, f1


def main():
    pool = json.loads(POOL_PATH.read_text(encoding="utf-8"))
    gold = json.loads(GOLD_PATH.read_text(encoding="utf-8"))

    per_scenario = []
    provenance_models = set()

    for scenario in pool["scenarios"]:
        sid = scenario["scenario_id"]
        if sid not in gold:
            continue
        contexts = build_contexts(scenario)
        question_impact = (
            f"Given the amendment to Protocol {scenario['study_id']}, which downstream protocol "
            f"sections should be reviewed? Amendment: {scenario['amendment_text']}"
        )
        question_gov = (
            f"Given the amendment to Protocol {scenario['study_id']}, which governing regulatory/SOP "
            f"references apply? Amendment: {scenario['amendment_text']}"
        )

        impact_answer = synthesize_rag_answer(question_impact, "impact_sections_all", contexts)
        gov_answer = synthesize_rag_answer(question_gov, "governing_sources_all", contexts)

        provenance_models.add(impact_answer.get("_provenance", {}).get("model"))
        provenance_models.add(gov_answer.get("_provenance", {}).get("model"))

        pred_sections = impact_answer.get("impacted_sections", [])
        pred_gov = gov_answer.get("governing_sources", [])

        gold_sections = gold[sid]["impacted_sections"]
        gold_gov = gold[sid]["governing_sources"]

        p1, r1, f1_1 = prf1(pred_sections, gold_sections)
        p2, r2, f1_2 = prf1(pred_gov, gold_gov)

        per_scenario.append(
            {
                "scenario_id": sid,
                "archetype": scenario["archetype"],
                "impact_sections": {"pred": pred_sections, "gold": gold_sections, "precision": p1, "recall": r1, "f1": f1_1},
                "governing_sources": {"pred": pred_gov, "gold": gold_gov, "precision": p2, "recall": r2, "f1": f1_2},
                "impact_provenance": impact_answer.get("_provenance"),
                "governance_provenance": gov_answer.get("_provenance"),
            }
        )
        print(f"{sid} ({scenario['archetype']}): impact F1={f1_1:.2f}  governance F1={f1_2:.2f}")

    def macro(field, metric):
        vals = [row[field][metric] for row in per_scenario]
        return sum(vals) / len(vals) if vals else 0.0

    summary = {
        "n": len(per_scenario),
        "annotator": "single independent annotator (faculty advisor), no IAA",
        "baseline": "llm_over_text",
        "models_used": sorted(m for m in provenance_models if m),
        "impact_sections_macro": {
            "precision": macro("impact_sections", "precision"),
            "recall": macro("impact_sections", "recall"),
            "f1": macro("impact_sections", "f1"),
        },
        "governing_sources_macro": {
            "precision": macro("governing_sources", "precision"),
            "recall": macro("governing_sources", "recall"),
            "f1": macro("governing_sources", "f1"),
        },
    }

    payload = {"summary": summary, "per_scenario": per_scenario}
    OUT_JSON.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    md_lines = [
        "# Pilot LLM-over-text Baseline vs. Independent Human Gold (n=50)",
        "",
        f"Annotator: {summary['annotator']}",
        f"Models used: {', '.join(summary['models_used'])}",
        "",
        "| Task | Precision | Recall | F1 |",
        "|---|---|---|---|",
        f"| impact_sections_all | {summary['impact_sections_macro']['precision']:.3f} | {summary['impact_sections_macro']['recall']:.3f} | {summary['impact_sections_macro']['f1']:.3f} |",
        f"| governing_sources_all | {summary['governing_sources_macro']['precision']:.3f} | {summary['governing_sources_macro']['recall']:.3f} | {summary['governing_sources_macro']['f1']:.3f} |",
        "",
        "Macro-averaged over n=50 scenarios, single independent annotator, no inter-annotator agreement computed.",
    ]
    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")

    print()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
