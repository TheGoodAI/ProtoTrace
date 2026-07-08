from __future__ import annotations

from typing import Any, Dict


def gold_demo_assets() -> Dict[str, Any]:
    return {
        "tasks": {
            "D1": {
                "question": "What is the current dose?",
                "expected_answer_contains": ["75 mg once daily"],
                "expected_claim_subject": "protocol.current_dose",
            },
            "D2": {
                "question": "What changed from v1 to v2?",
                "expected_answer_contains": ["50 mg once daily", "75 mg once daily", "14 days", "21 days"],
            },
            "D3": {
                "question": "Draft the dosing section for the updated protocol.",
                "expected_answer_contains": ["75 mg once daily", "21 days", "["],
            },
            "D4": {
                "question": "Validate this draft for stale or unsupported claims.",
                "expected_issue_types": ["stale_fact", "missing_citation"],
            },
        }
    }

