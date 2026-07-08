from __future__ import annotations

import re
from typing import Any, Dict, List

from .query_engine import GraphQueryEngine


def _contains_citation(text: str) -> bool:
    return bool(re.search(r"\[[^\]]+:[^\]]+\]", text))


def validate_draft(engine: GraphQueryEngine, draft: Dict[str, Any]) -> Dict[str, Any]:
    text = draft["text"]
    issues: List[Dict[str, Any]] = []

    active_dose = engine.get_active_claims("protocol.current_dose")
    superseded_dose = engine.get_superseded_claims("protocol.current_dose")
    active_visit = engine.get_active_claims("protocol.visit_interval")
    superseded_visit = engine.get_superseded_claims("protocol.visit_interval")

    if superseded_dose and superseded_dose[0]["normalized_object"] in text:
        issues.append(
            {
                "severity": "critical",
                "issue_type": "stale_fact",
                "message": f"Draft uses stale dose value {superseded_dose[0]['normalized_object']}.",
                "related_claim_ids": [superseded_dose[0]["claim_id"]],
            }
        )

    if active_dose and active_dose[0]["normalized_object"] not in text:
        issues.append(
            {
                "severity": "warning",
                "issue_type": "missing_current_fact",
                "message": f"Draft does not include the active dose value {active_dose[0]['normalized_object']}.",
                "related_claim_ids": [active_dose[0]["claim_id"]],
            }
        )

    if superseded_visit and superseded_visit[0]["normalized_object"] in text:
        issues.append(
            {
                "severity": "warning",
                "issue_type": "stale_fact",
                "message": f"Draft uses stale visit interval {superseded_visit[0]['normalized_object']}.",
                "related_claim_ids": [superseded_visit[0]["claim_id"]],
            }
        )

    if active_visit and active_visit[0]["normalized_object"] not in text:
        issues.append(
            {
                "severity": "warning",
                "issue_type": "missing_current_fact",
                "message": f"Draft does not include the active visit interval {active_visit[0]['normalized_object']}.",
                "related_claim_ids": [active_visit[0]["claim_id"]],
            }
        )

    if not _contains_citation(text):
        issues.append(
            {
                "severity": "critical",
                "issue_type": "missing_citation",
                "message": "Draft contains protocol facts without citations.",
                "related_claim_ids": [],
            }
        )

    return {
        "draft_id": draft["draft_id"],
        "issue_count": len(issues),
        "issues": issues,
        "status": "pass" if not issues else "fail",
    }
