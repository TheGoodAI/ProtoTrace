from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List


def build_demo_documents() -> List[Dict[str, Any]]:
    retrieved_at = datetime.now(timezone.utc).isoformat()
    return [
        {
            "source_id": "protocol_v1",
            "family": "DEMO",
            "label": "Protocol Version 1",
            "kind": "protocol",
            "seed_url": None,
            "resolved_url": None,
            "retrieved_at": retrieved_at,
            "retrieved_via": "synthetic_demo",
            "title": "Protocol Version 1",
            "text": (
                "Section 6.2 Dosing and Administration. Subjects will receive 50 mg once daily. "
                "Section 7.1 Visit Schedule. Subjects will attend visits every 14 days. "
                "Section 5.2 Eligibility Criteria. Subjects currently receiving fluvoxamine are excluded."
            ),
            "sections": [
                {
                    "heading": "Section 6.2 Dosing and Administration",
                    "text": "Subjects will receive 50 mg once daily.",
                },
                {
                    "heading": "Section 7.1 Visit Schedule",
                    "text": "Subjects will attend visits every 14 days.",
                },
                {
                    "heading": "Section 5.2 Eligibility Criteria",
                    "text": "Subjects currently receiving fluvoxamine are excluded.",
                },
            ],
            "citation_spans": [
                {
                    "locator": "section 6.2",
                    "quoted_text": "Subjects will receive 50 mg once daily.",
                }
            ],
        },
        {
            "source_id": "protocol_amendment_v2",
            "family": "DEMO",
            "label": "Protocol Amendment Version 2",
            "kind": "amendment",
            "seed_url": None,
            "resolved_url": None,
            "retrieved_at": retrieved_at,
            "retrieved_via": "synthetic_demo",
            "title": "Protocol Amendment Version 2",
            "text": (
                "Section 6.2 Dosing and Administration. Dose will be increased from 50 mg to 75 mg once daily. "
                "Section 7.1 Visit Schedule. Subjects will attend visits every 21 days. "
                "Section 5.2 Eligibility Criteria. Exclusion criteria updated: subjects currently receiving "
                "fluvoxamine or ciprofloxacin are excluded."
            ),
            "sections": [
                {
                    "heading": "Section 6.2 Dosing and Administration",
                    "text": "Dose will be increased from 50 mg to 75 mg once daily.",
                },
                {
                    "heading": "Section 7.1 Visit Schedule",
                    "text": "Subjects will attend visits every 21 days.",
                },
                {
                    "heading": "Section 5.2 Eligibility Criteria",
                    "text": (
                        "Exclusion criteria updated: subjects currently receiving fluvoxamine or "
                        "ciprofloxacin are excluded."
                    ),
                },
            ],
            "citation_spans": [
                {
                    "locator": "section 6.2",
                    "quoted_text": "Dose will be increased from 50 mg to 75 mg once daily.",
                }
            ],
        },
        {
            "source_id": "sop_dose_change_citation",
            "family": "DEMO",
            "label": "SOP Dose Change Citation Requirement",
            "kind": "sop",
            "seed_url": None,
            "resolved_url": None,
            "retrieved_at": retrieved_at,
            "retrieved_via": "synthetic_demo",
            "title": "SOP Dose Change Citation Requirement",
            "text": (
                "Any dose change in a protocol or protocol amendment must be cited to the source amendment in the final drafting output."
            ),
            "sections": [
                {
                    "heading": "Dose Change Citation Policy",
                    "text": "Any dose change in a protocol or protocol amendment must be cited to the source amendment in the final drafting output.",
                }
            ],
            "citation_spans": [
                {
                    "locator": "policy 1",
                    "quoted_text": "Any dose change in a protocol or protocol amendment must be cited to the source amendment in the final drafting output.",
                }
            ],
        },
        {
            "source_id": "visit_schedule_table",
            "family": "DEMO",
            "label": "Visit Schedule Table",
            "kind": "table",
            "seed_url": None,
            "resolved_url": None,
            "retrieved_at": retrieved_at,
            "retrieved_via": "synthetic_demo",
            "title": "Visit Schedule Table",
            "text": "Visit schedule table: v1 shows visits every 14 days. Amendment v2 changes visits to every 21 days.",
            "sections": [
                {
                    "heading": "Visit Schedule Changes",
                    "text": "v1 shows visits every 14 days. Amendment v2 changes visits to every 21 days.",
                }
            ],
            "citation_spans": [
                {
                    "locator": "row 1",
                    "quoted_text": "Amendment v2 changes visits to every 21 days.",
                }
            ],
        },
    ]
