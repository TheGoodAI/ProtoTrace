from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple

from .artifact_store import read_json, write_json


def load_claim_ledger() -> List[Dict[str, Any]]:
    return read_json("claims/claim_ledger.json")


def approve_claim(
    claim_id: str,
    reviewer: str,
    notes: str,
    ledger_blob: str = "claims/claim_ledger.json",
) -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    claims = read_json(ledger_blob)
    updated_claims = deepcopy(claims)
    approved_claim: Dict[str, Any] | None = None
    reviewed_at = datetime.now(timezone.utc).isoformat()

    for claim in updated_claims:
        if claim["claim_id"] != claim_id:
            continue
        claim["reviewer_decision"] = "approved"
        claim["reviewer_notes"] = notes
        claim["reviewed_by"] = reviewer
        claim["reviewed_at"] = reviewed_at
        approved_claim = claim
        break

    if approved_claim is None:
        raise ValueError(f"Claim {claim_id} not found in ledger.")

    approval_event = {
        "event_id": f"approval_{claim_id}_{reviewed_at}",
        "claim_id": claim_id,
        "action": "approve",
        "reviewer": reviewer,
        "notes": notes,
        "reviewed_at": reviewed_at,
    }

    write_json("claims/claim_ledger.json", updated_claims)

    try:
        history = read_json("claims/approval_events.json")
        if not isinstance(history, list):
            history = []
    except Exception:  # noqa: BLE001
        history = []
    history.append(approval_event)
    write_json("claims/approval_events.json", history)

    manifest = {
        "last_reviewed_at": reviewed_at,
        "approved_claim_id": claim_id,
        "reviewer": reviewer,
        "ledger_blob": "claims/claim_ledger.json",
        "approval_events_blob": "claims/approval_events.json",
    }
    write_json("claims/review_manifest.json", manifest)
    return updated_claims, approval_event
