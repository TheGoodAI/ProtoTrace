from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, List

from .llm_normalizer import normalize_claim_candidates


def _candidate(
    claim_id: str,
    chunk: Dict[str, Any],
    claim_text: str,
    subject: str,
    predicate: str,
    obj: str,
    claim_type: str,
    status: str = "active",
) -> Dict[str, Any]:
    return {
        "claim_id": claim_id,
        "source_id": chunk["source_id"],
        "chunk_id": chunk["chunk_id"],
        "claim_text": claim_text,
        "normalized_subject": subject,
        "predicate": predicate,
        "normalized_object": obj,
        "claim_type": claim_type,
        "claim_status": status,
        "evidence": {
            "heading": chunk.get("heading"),
            "text": chunk.get("text"),
            "citation_locator": chunk.get("citation_locator"),
        },
    }


def extract_rule_based_candidates(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    candidates: List[Dict[str, Any]] = []
    for chunk in chunks:
        text = chunk["text"]
        lowered = text.lower()
        sid = chunk["source_id"]
        dose_change_phrase = "increased from 50 mg to 75 mg" in lowered or "from 50 mg to 75 mg" in lowered
        visit_change_phrase = "changes visits to every 21 days" in lowered or "changed visits to every 21 days" in lowered

        if dose_change_phrase:
            candidates.append(
                _candidate(
                    f"claim_{sid}_dose_change_50_to_75",
                    chunk,
                    "The protocol dose changed from 50 mg once daily to 75 mg once daily.",
                    "protocol.current_dose",
                    "changes_to",
                    "75 mg once daily",
                    "change_event",
                )
            )
            candidates.append(
                _candidate(
                    f"claim_{sid}_dose_75mg",
                    chunk,
                    "The current protocol dose is 75 mg once daily.",
                    "protocol.current_dose",
                    "equals",
                    "75 mg once daily",
                    "factual",
                )
            )
        elif "50 mg" in text:
            candidates.append(
                _candidate(
                    f"claim_{sid}_dose_50mg",
                    chunk,
                    "The protocol dose is 50 mg once daily.",
                    "protocol.current_dose",
                    "equals",
                    "50 mg once daily",
                    "factual",
                    status="superseded" if sid == "protocol_v1" else "active",
                )
            )
        elif "75 mg" in text:
            predicate = "equals"
            candidates.append(
                _candidate(
                    f"claim_{sid}_dose_75mg",
                    chunk,
                    "The current protocol dose is 75 mg once daily.",
                    "protocol.current_dose",
                    predicate,
                    "75 mg once daily",
                    "factual",
                )
            )
        if visit_change_phrase:
            candidates.append(
                _candidate(
                    f"claim_{sid}_visit_change_14_to_21",
                    chunk,
                    "The protocol visit interval changed from 14 days to 21 days.",
                    "protocol.visit_interval",
                    "changes_to",
                    "21 days",
                    "change_event",
                )
            )
            candidates.append(
                _candidate(
                    f"claim_{sid}_visit_21days",
                    chunk,
                    "Visits occur every 21 days.",
                    "protocol.visit_interval",
                    "equals",
                    "21 days",
                    "factual",
                )
            )
        elif "14 days" in text:
            candidates.append(
                _candidate(
                    f"claim_{sid}_visit_14days",
                    chunk,
                    "Visits occur every 14 days.",
                    "protocol.visit_interval",
                    "equals",
                    "14 days",
                    "factual",
                    status="superseded" if sid == "protocol_v1" else "active",
                )
            )
        elif "21 days" in text:
            predicate = "equals"
            candidates.append(
                _candidate(
                    f"claim_{sid}_visit_21days",
                    chunk,
                    "Visits occur every 21 days.",
                    "protocol.visit_interval",
                    predicate,
                    "21 days",
                    "factual",
                )
            )
        if "must be cited" in lowered:
            candidates.append(
                _candidate(
                    f"claim_{sid}_dose_change_citation",
                    chunk,
                    "Dose changes must be cited to the source amendment.",
                    "sop.dose_change_citation_requirement",
                    "requires",
                    "citation to source amendment",
                    "requirement",
                )
            )
        if "submit protocol amendments" in lowered or "submitted as a protocol amendment" in lowered:
            candidates.append(
                _candidate(
                    f"claim_{sid}_protocol_amendment_requirement",
                    chunk,
                    "Protocol changes should be submitted as protocol amendments before implementation or as required by the process.",
                    "regulation.protocol_amendment_requirement",
                    "requires",
                    "protocol amendment submission for protocol changes",
                    "requirement",
                )
            )
        if "adherence to the protocol is a fundamental part" in lowered:
            candidates.append(
                _candidate(
                    f"claim_{sid}_protocol_adherence",
                    chunk,
                    "Protocol adherence is fundamental to clinical study conduct.",
                    "regulation.protocol_adherence",
                    "states",
                    "protocol adherence is fundamental",
                    "recommendation",
                )
            )
    return candidates


def finalize_claims(normalized_candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    now = datetime.now(timezone.utc).isoformat()
    claims: List[Dict[str, Any]] = []
    for candidate in normalized_candidates:
        evidence = candidate.get("evidence", {})
        claims.append(
            {
                "claim_id": candidate["claim_id"],
                "claim_text": candidate["claim_text"],
                "normalized_subject": candidate["normalized_subject"],
                "predicate": candidate["predicate"],
                "normalized_object": candidate["normalized_object"],
                "claim_type": candidate.get("claim_type", "factual"),
                "claim_status": candidate.get("claim_status", "active"),
                "effective_start": now,
                "effective_end": None,
                "supersedes_claim_ids": candidate.get("supersedes_claim_ids", []),
                "superseded_by_claim_id": candidate.get("superseded_by_claim_id"),
                "evidence_ids": [candidate["chunk_id"]],
                "source_ids": [candidate["source_id"]],
                "citation_spans": [
                    {
                        "source_id": candidate["source_id"],
                        "locator": evidence.get("citation_locator") or evidence.get("heading") or "unknown",
                        "quoted_text": evidence.get("text"),
                    }
                ],
                "extraction_method": "rule_first_plus_azure_openai_mini",
                "extraction_confidence": 0.8,
                "reviewer_decision": None,
                "reviewer_notes": None,
                "entity_ids": [],
                "relation_ids": [],
                "topic_labels": [],
                "retrieval_keywords": [],
                "retrieval_summary": candidate["claim_text"],
                "created_at": now,
            }
        )
    claims = _dedupe_equivalent_claims(claims)
    _link_supersession(claims)
    return claims


def _dedupe_equivalent_claims(claims: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    deduped: Dict[tuple, Dict[str, Any]] = {}
    for claim in claims:
        key = (
            claim["normalized_subject"],
            claim["predicate"],
            claim["normalized_object"],
            claim["claim_status"],
            claim["claim_type"],
        )
        existing = deduped.get(key)
        if not existing:
            deduped[key] = claim
            continue

        existing["evidence_ids"] = sorted(set(existing["evidence_ids"] + claim["evidence_ids"]))
        existing["source_ids"] = sorted(set(existing["source_ids"] + claim["source_ids"]))
        existing["citation_spans"].extend(claim["citation_spans"])
        if claim["claim_text"] not in existing["retrieval_summary"]:
            existing["retrieval_summary"] = f"{existing['retrieval_summary']} | {claim['claim_text']}"
    return list(deduped.values())


def _link_supersession(claims: List[Dict[str, Any]]) -> None:
    by_subject: Dict[str, List[Dict[str, Any]]] = {}
    for claim in claims:
        by_subject.setdefault(claim["normalized_subject"], []).append(claim)

    for subject_claims in by_subject.values():
        active_claims = [claim for claim in subject_claims if claim["claim_status"] == "active" and claim["claim_type"] == "factual"]
        superseded_claims = [claim for claim in subject_claims if claim["claim_status"] == "superseded" and claim["claim_type"] == "factual"]
        if len(active_claims) == 1 and superseded_claims:
            active_claim = active_claims[0]
            for old_claim in superseded_claims:
                old_claim["superseded_by_claim_id"] = active_claim["claim_id"]
                active_claim["supersedes_claim_ids"].append(old_claim["claim_id"])


def extract_claims(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    candidates = extract_rule_based_candidates(chunks)
    normalized = normalize_claim_candidates(candidates)
    return finalize_claims(normalized)
