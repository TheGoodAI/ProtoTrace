from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .settings import DATA_DIR


EVAL_DIR = DATA_DIR / "eval"
TEST_DATASET_PATH = EVAL_DIR / "test_dataset.json"


def build_eval_dataset() -> Dict[str, Any]:
    dose_sequences: List[List[int]] = _dose_sequences()
    visit_sequences: List[List[int]] = _visit_sequences()
    scenarios: List[Dict[str, Any]] = []
    tasks: List[Dict[str, Any]] = []

    for index, sequence in enumerate(dose_sequences):
        scenario_id = f"scenario_{index + 1}"
        history = [50, 75] + sequence
        source_history = ["protocol_v1", "protocol_amendment_v2"] + [
            f"protocol_amendment_v{version}"
            for version in range(3, 3 + len(sequence))
        ]
        current_dose = f"{history[-1]} mg once daily"
        previous_dose = f"{history[-2]} mg once daily"
        changed_source = source_history[-1]
        scenario = {
            "scenario_id": scenario_id,
            "amendment_kind": "dose",
            "label": "Baseline amendment v2" if not sequence else f"Sequential amendments to {' -> '.join(map(str, sequence))} mg",
            "reset_before_run": True,
            "amendment_sequence": sequence,
            "gold": {
                "current_dose": current_dose,
                "previous_dose": previous_dose,
                "dose_history": [f"{dose} mg once daily" for dose in history],
                "source_history": source_history,
                "changed_source": changed_source,
                "impacted_sections_all": ["6.2", "7.1", "11.1", "11.3", "11.4", "11.5"],
                "impacted_sections_dose_only": ["6.2", "11.1", "11.3", "11.4"],
                "governing_sources_all": [
                    "fda_ind_protocol_amendments",
                    "sop_dose_change_citation",
                    "ema_gcp_qa",
                ],
                "governing_sources_dose_only": [
                    "fda_ind_protocol_amendments",
                    "sop_dose_change_citation",
                ],
            },
        }
        scenarios.append(scenario)
        tasks.extend(_scenario_tasks(index + 1, scenario))

    visit_offset = len(dose_sequences)
    for index, sequence in enumerate(visit_sequences):
        scenario_id = f"scenario_{visit_offset + index + 1}"
        history = [14, 21] + sequence
        source_history = ["protocol_v1", "protocol_amendment_v2"] + [
            f"protocol_amendment_v{version}"
            for version in range(3, 3 + len(sequence))
        ]
        current_visit = f"{history[-1]} days"
        previous_visit = f"{history[-2]} days"
        changed_source = source_history[-1]
        scenario = {
            "scenario_id": scenario_id,
            "amendment_kind": "visit",
            "label": "Baseline visit amendment v2" if not sequence else f"Sequential visit-interval amendments to {' -> '.join(map(str, sequence))} days",
            "reset_before_run": True,
            "amendment_sequence": sequence,
            "gold": {
                "current_visit": current_visit,
                "previous_visit": previous_visit,
                "visit_history": [f"{days} days" for days in history],
                "source_history": source_history,
                "changed_source": changed_source,
            },
        }
        scenarios.append(scenario)
        tasks.extend(_scenario_tasks(visit_offset + index + 1, scenario))

    eligibility_offset = len(dose_sequences) + len(visit_sequences)
    for index, sequence in enumerate(_eligibility_sequences()):
        scenario_id = f"scenario_{eligibility_offset + index + 1}"
        excluded = ["fluvoxamine", "ciprofloxacin"] + sequence
        history = [", ".join(excluded[: i + 1]) for i in range(len(excluded))]
        source_history = ["protocol_v1", "protocol_amendment_v2"] + [
            f"protocol_amendment_v{version}"
            for version in range(3, 3 + len(sequence))
        ]
        current_exclusion = history[-1]
        previous_exclusion = history[-2]
        changed_source = source_history[-1]
        scenario = {
            "scenario_id": scenario_id,
            "amendment_kind": "eligibility",
            "label": "Baseline eligibility amendment v2" if not sequence else f"Sequential eligibility amendments adding {' -> '.join(sequence)}",
            "reset_before_run": True,
            "amendment_sequence": sequence,
            "gold": {
                "current_exclusion": current_exclusion,
                "previous_exclusion": previous_exclusion,
                "exclusion_history": history,
                "source_history": source_history,
                "changed_source": changed_source,
            },
        }
        scenarios.append(scenario)
        tasks.extend(_scenario_tasks(eligibility_offset + index + 1, scenario))

    tasks.extend(_regulatory_tasks())

    return {
        "dataset_id": "temporal_claim_centered_protocol_eval_v4_large_hybrid",
        "description": (
            "Large hybrid benchmark combining adversarial multi-amendment scenarios (dose, "
            "visit-interval, and eligibility-criterion amendment types) with internet-derived "
            "FDA, EMA, and CDISC governance tasks."
        ),
        "scenario_count": len(scenarios),
        "task_count": len(tasks),
        "scenarios": scenarios,
        "tasks": tasks,
        "source_basis": [
            "FDA IND protocol amendments",
            "FDA clinical protocols",
            "EMA GCP Q&A",
            "CDISC foundational standards / PRM",
        ],
    }


def write_eval_dataset(path: Path = TEST_DATASET_PATH) -> Path:
    payload = build_eval_dataset()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return path


def _dose_sequences() -> List[List[int]]:
    return [
        [],
        [80],
        [85],
        [90],
        [95],
        [100],
        [105],
        [110],
        [115],
        [120],
        [80, 95],
        [80, 110],
        [95, 85],
        [110, 90],
        [130, 140],
        [150, 140],
        [95, 85, 115],
        [150, 140, 160],
        [88, 104, 92],
        [82, 96, 108],
        [100, 90, 105],
        [75, 85, 95],
        [85, 100, 120],
        [90, 110, 100],
        [100, 120, 140],
        [130, 120, 125],
        [145, 130, 150],
        [70, 85, 100, 110],
        [80, 100, 95, 115],
        [90, 105, 120, 135],
    ]


def _visit_sequences() -> List[List[int]]:
    return [
        [],
        [28],
        [35],
        [42],
        [49],
        [56],
        [21, 28],
        [28, 35],
        [35, 21],
        [42, 28],
        [21, 28, 35],
        [28, 42, 35],
        [14, 28, 35, 21],
    ]


def _eligibility_sequences() -> List[List[str]]:
    return [
        [],
        ["enoxacin"],
        ["carbamazepine"],
        ["itraconazole"],
        ["ketoconazole"],
        ["rifampin"],
        ["enoxacin", "carbamazepine"],
        ["itraconazole", "ketoconazole"],
        ["rifampin", "phenytoin"],
        ["enoxacin", "carbamazepine", "itraconazole"],
        ["ritonavir", "tacrolimus", "warfarin"],
        ["clopidogrel", "methotrexate", "phenobarbital", "rifampin"],
    ]


def _scenario_tasks(index: int, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    if scenario["amendment_kind"] == "visit":
        return _visit_scenario_tasks(index, scenario)
    if scenario["amendment_kind"] == "eligibility":
        return _eligibility_scenario_tasks(index, scenario)
    return _dose_scenario_tasks(index, scenario)


def _visit_scenario_tasks(index: int, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    prefix = f"S{index}"
    gold = scenario["gold"]
    source_history = gold["source_history"]
    changed_source = gold["changed_source"]
    return [
        {
            "task_id": f"{prefix}_current_visit",
            "scenario_id": scenario["scenario_id"],
            "task_type": "current_visit",
            "prompt": "What visit interval should the latest protocol version use right now?",
            "gold": {"current_visit": gold["current_visit"], "supporting_sources": [changed_source]},
        },
        {
            "task_id": f"{prefix}_previous_visit",
            "scenario_id": scenario["scenario_id"],
            "task_type": "previous_visit",
            "prompt": "Immediately before the latest amendment, what visit interval was active?",
            "gold": {"previous_visit": gold["previous_visit"], "supporting_sources": [source_history[-2]]},
        },
        {
            "task_id": f"{prefix}_visit_history",
            "scenario_id": scenario["scenario_id"],
            "task_type": "visit_history",
            "prompt": "List the visit-interval history in temporal order from the original protocol through the latest amendment.",
            "gold": {"visit_history": gold["visit_history"], "supporting_sources": source_history},
        },
        {
            "task_id": f"{prefix}_changed_source_visit",
            "scenario_id": scenario["scenario_id"],
            "task_type": "changed_source_visit",
            "prompt": "Which amendment source introduced the latest active visit interval?",
            "gold": {"changed_source": changed_source, "supporting_sources": [changed_source]},
        },
    ]


def _eligibility_scenario_tasks(index: int, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    prefix = f"S{index}"
    gold = scenario["gold"]
    source_history = gold["source_history"]
    changed_source = gold["changed_source"]
    return [
        {
            "task_id": f"{prefix}_current_eligibility",
            "scenario_id": scenario["scenario_id"],
            "task_type": "current_eligibility",
            "prompt": "Which concomitant medications are currently excluded under the latest protocol version?",
            "gold": {"current_exclusion": gold["current_exclusion"], "supporting_sources": [changed_source]},
        },
        {
            "task_id": f"{prefix}_previous_eligibility",
            "scenario_id": scenario["scenario_id"],
            "task_type": "previous_eligibility",
            "prompt": "Immediately before the latest amendment, which concomitant medications were excluded?",
            "gold": {"previous_exclusion": gold["previous_exclusion"], "supporting_sources": [source_history[-2]]},
        },
        {
            "task_id": f"{prefix}_eligibility_history",
            "scenario_id": scenario["scenario_id"],
            "task_type": "eligibility_history",
            "prompt": "List the exclusion-criteria history in temporal order from the original protocol through the latest amendment.",
            "gold": {"exclusion_history": gold["exclusion_history"], "supporting_sources": source_history},
        },
        {
            "task_id": f"{prefix}_changed_source_eligibility",
            "scenario_id": scenario["scenario_id"],
            "task_type": "changed_source_eligibility",
            "prompt": "Which amendment source introduced the latest active exclusion criteria?",
            "gold": {"changed_source": changed_source, "supporting_sources": [changed_source]},
        },
    ]


def _dose_scenario_tasks(index: int, scenario: Dict[str, Any]) -> List[Dict[str, Any]]:
    prefix = f"S{index}"
    gold = scenario["gold"]
    source_history = gold["source_history"]
    changed_source = gold["changed_source"]
    return [
        {
            "task_id": f"{prefix}_current_fact",
            "scenario_id": scenario["scenario_id"],
            "task_type": "current_fact",
            "prompt": "What dose should the latest protocol version use right now?",
            "gold": {"current_dose": gold["current_dose"], "supporting_sources": [changed_source]},
        },
        {
            "task_id": f"{prefix}_previous_fact",
            "scenario_id": scenario["scenario_id"],
            "task_type": "previous_fact",
            "prompt": "Immediately before the latest amendment, what dose was active?",
            "gold": {"previous_dose": gold["previous_dose"], "supporting_sources": [source_history[-2]]},
        },
        {
            "task_id": f"{prefix}_dose_history",
            "scenario_id": scenario["scenario_id"],
            "task_type": "dose_history",
            "prompt": "List the dose history in temporal order from the original protocol through the latest amendment.",
            "gold": {"dose_history": gold["dose_history"], "supporting_sources": source_history},
        },
        {
            "task_id": f"{prefix}_changed_source",
            "scenario_id": scenario["scenario_id"],
            "task_type": "changed_source",
            "prompt": "Which amendment source introduced the latest active dose?",
            "gold": {"changed_source": changed_source, "supporting_sources": [changed_source]},
        },
        {
            "task_id": f"{prefix}_impact_sections_all",
            "scenario_id": scenario["scenario_id"],
            "task_type": "impact_sections_all",
            "prompt": "Which downstream protocol sections should be reviewed after the current amendment state?",
            "gold": {"impacted_sections": gold["impacted_sections_all"]},
        },
        {
            "task_id": f"{prefix}_impact_sections_dose_only",
            "scenario_id": scenario["scenario_id"],
            "task_type": "impact_sections_dose_only",
            "prompt": "Ignoring visit timing effects, which sections are impacted specifically by the latest dose amendment?",
            "gold": {"impacted_sections": gold["impacted_sections_dose_only"]},
        },
        {
            "task_id": f"{prefix}_governing_sources_all",
            "scenario_id": scenario["scenario_id"],
            "task_type": "governing_sources_all",
            "prompt": "Which authoritative sources govern the current protocol update overall?",
            "gold": {"governing_sources": gold["governing_sources_all"], "supporting_sources": gold["governing_sources_all"]},
        },
        {
            "task_id": f"{prefix}_governing_sources_dose_only",
            "scenario_id": scenario["scenario_id"],
            "task_type": "governing_sources_dose_only",
            "prompt": "For the latest dose update specifically, which authoritative sources govern the change?",
            "gold": {"governing_sources": gold["governing_sources_dose_only"], "supporting_sources": gold["governing_sources_dose_only"]},
        },
    ]


def _regulatory_tasks() -> List[Dict[str, Any]]:
    return [
        {
            "task_id": "R1_dose_increase_requires_amendment",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "Under FDA IND protocol amendment guidance, if the dose is increased beyond the current protocol, what is the required action?",
            "gold": {
                "answer": "protocol amendment required",
                "supporting_sources": ["fda_ind_protocol_amendments"],
            },
        },
        {
            "task_id": "R2_design_change_requires_amendment",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "Under FDA IND protocol amendment guidance, what is required for a significant protocol design change such as adding or removing a control group?",
            "gold": {
                "answer": "protocol amendment required",
                "supporting_sources": ["fda_ind_protocol_amendments"],
            },
        },
        {
            "task_id": "R3_safety_monitoring_change_requires_amendment",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "If a protocol adds or removes a safety monitoring test intended to detect side effects, what does FDA IND amendment guidance require?",
            "gold": {
                "answer": "protocol amendment required",
                "supporting_sources": ["fda_ind_protocol_amendments"],
            },
        },
        {
            "task_id": "R4_immediate_hazard_exception",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "If a protocol change is needed to eliminate an apparent immediate hazard to subjects, what action is allowed before formal amendment review is complete?",
            "gold": {
                "answer": "implement immediately then notify FDA and IRB",
                "supporting_sources": ["fda_ind_protocol_amendments"],
            },
        },
        {
            "task_id": "R5_source_data_identification",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "According to EMA GCP Q&A, what should the protocol identify about data recorded directly into CRFs?",
            "gold": {
                "answer": "identify source data recorded directly into CRFs",
                "supporting_sources": ["ema_gcp_qa"],
            },
        },
        {
            "task_id": "R6_eligibility_documentation",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "According to EMA GCP Q&A, where should adherence to individual inclusion and exclusion criteria be documented?",
            "gold": {
                "answer": "document individual eligibility criteria in source data",
                "supporting_sources": ["ema_gcp_qa"],
            },
        },
        {
            "task_id": "R7_cdisc_prm_scope",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "What does the CDISC Protocol Representation Model focus on?",
            "gold": {
                "answer": "study design, eligibility criteria, and registry requirements",
                "supporting_sources": ["cdisc_home"],
            },
        },
        {
            "task_id": "R8_phase1_safety_detail",
            "scenario_id": "regulatory_static",
            "task_type": "rule_answer",
            "prompt": "According to FDA clinical protocol guidance, what safety-critical elements should a Phase 1 protocol specify in detail?",
            "gold": {
                "answer": "toxicity monitoring, stopping rules, and dose adjustment rules",
                "supporting_sources": ["fda_clinical_protocols"],
            },
        },
    ]
