"""Score the pilot rule engine (all 8 archetypes) against held-out human gold.

Requires data/pilot_annotation/heldout_gold_labels_v1.json to exist -- i.e., the
annotator has labeled heldout_annotator_worksheet.md and it has been transcribed to
the same schema as gold_labels_v1.json (scenario_id -> impacted_sections,
governing_sources).

Usage: python scripts/run_heldout_eval.py
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from kg_demo.pilot_rule_engine import analyze_pilot_scenario  # noqa: E402

POOL_PATH = ROOT / "data" / "pilot_annotation" / "heldout_pool_v1.json"
GOLD_PATH = ROOT / "data" / "pilot_annotation" / "heldout_gold_labels_v1.json"
OUT_JSON = ROOT / "data" / "eval" / "heldout_rule_engine_results.json"
OUT_MD = ROOT / "data" / "eval" / "heldout_rule_engine_results.md"


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
    if not GOLD_PATH.exists():
        raise SystemExit(
            f"{GOLD_PATH} does not exist yet. Have the annotator label "
            "heldout_annotator_worksheet.md, transcribe it to this path, then re-run."
        )
    pool = json.loads(POOL_PATH.read_text(encoding="utf-8"))
    gold = json.loads(GOLD_PATH.read_text(encoding="utf-8"))

    per_scenario = []
    for scenario in pool["scenarios"]:
        sid = scenario["scenario_id"]
        if sid not in gold:
            continue
        pred = analyze_pilot_scenario(scenario["archetype"])
        gold_sections = gold[sid]["impacted_sections"]
        gold_gov = gold[sid]["governing_sources"]

        p1, r1, f1_1 = prf1(pred["impacted_sections"], gold_sections)
        p2, r2, f1_2 = prf1(pred["governing_sources"], gold_gov)

        per_scenario.append(
            {
                "scenario_id": sid,
                "archetype": scenario["archetype"],
                "impact_sections": {"pred": pred["impacted_sections"], "gold": gold_sections, "precision": p1, "recall": r1, "f1": f1_1},
                "governing_sources": {"pred": pred["governing_sources"], "gold": gold_gov, "precision": p2, "recall": r2, "f1": f1_2},
            }
        )
        print(f"{sid} ({scenario['archetype']}): impact F1={f1_1:.2f}  governance F1={f1_2:.2f}")

    def macro(field, metric):
        vals = [row[field][metric] for row in per_scenario]
        return sum(vals) / len(vals) if vals else 0.0

    summary = {
        "n": len(per_scenario),
        "annotator": "single independent annotator (faculty advisor), no IAA, held-out pool",
        "rule_engine": "pilot_rule_engine (8/8 archetypes, authored without consulting original 50-scenario gold)",
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

    OUT_JSON.write_text(json.dumps({"summary": summary, "per_scenario": per_scenario}, indent=2), encoding="utf-8")
    md_lines = [
        "# Pilot Rule Engine (8/8 archetypes) vs. Held-Out Independent Gold (n={})".format(len(per_scenario)),
        "",
        "| Task | Precision | Recall | F1 |",
        "|---|---|---|---|",
        f"| impact_sections | {summary['impact_sections_macro']['precision']:.3f} | {summary['impact_sections_macro']['recall']:.3f} | {summary['impact_sections_macro']['f1']:.3f} |",
        f"| governing_sources | {summary['governing_sources_macro']['precision']:.3f} | {summary['governing_sources_macro']['recall']:.3f} | {summary['governing_sources_macro']['f1']:.3f} |",
    ]
    OUT_MD.write_text("\n".join(md_lines), encoding="utf-8")
    print()
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
