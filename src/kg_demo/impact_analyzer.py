from __future__ import annotations

from typing import Any, Dict, List

from .artifact_store import read_json
from .document_store import document_index


def analyze_protocol_impacts() -> Dict[str, Any]:
    claims: List[Dict[str, Any]] = read_json("claims/claim_ledger.json")
    docs = document_index()
    active_factual = [
        claim for claim in claims
        if claim["claim_status"] == "active" and claim["claim_type"] == "factual"
    ]
    active_changes = [
        claim for claim in claims
        if claim["claim_status"] == "active" and claim["claim_type"] == "change_event"
    ]

    impacted_sections: List[Dict[str, Any]] = []
    graph_effects: List[str] = []
    rationale: List[str] = []
    governing_sources: List[Dict[str, Any]] = []
    changed_sources: List[Dict[str, Any]] = []

    for claim in active_changes:
        subject = claim["normalized_subject"]
        obj = claim["normalized_object"]
        changed_sources.extend(_source_entries_for_claim(claim, docs, role="changed_source"))

        if subject == "protocol.current_dose":
            governing_sources.extend(
                _governing_sources(
                    claims,
                    docs,
                    subjects=[
                        "regulation.protocol_amendment_requirement",
                        "sop.dose_change_citation_requirement",
                    ],
                )
            )
            impacted_sections.extend(
                [
                    {
                        "section_id": "6.2",
                        "section_title": "Dosing and Administration",
                        "impact_reason": f"Primary dosing instruction must reflect {obj}.",
                        "severity": "critical",
                        "governing_policy": "current dose fact + amendment submission + citation requirement",
                    },
                    {
                        "section_id": "11.3",
                        "section_title": "Dose Modifications and Discontinuation",
                        "impact_reason": "Dose change may require revision of adjustment and discontinuation rules.",
                        "severity": "high",
                        "governing_policy": "dose modification logic should remain consistent with the amended dose",
                    },
                    {
                        "section_id": "11.4",
                        "section_title": "Safety Monitoring Plan",
                        "impact_reason": "Higher or altered dose may affect monitoring cadence and safety checks.",
                        "severity": "medium",
                        "governing_policy": "monitoring obligations must reflect the amended dose exposure",
                    },
                    {
                        "section_id": "11.1",
                        "section_title": "Assessment Schedule and Procedures",
                        "impact_reason": "Dose changes can require assessment timing or procedure updates.",
                        "severity": "medium",
                        "governing_policy": "procedures must stay consistent with the current dose and amendment state",
                    },
                ]
            )
            graph_effects.extend(
                [
                    "Add a new active dose claim node.",
                    "Supersede the prior active dose claim node.",
                    "Update protocol_main HAS_CURRENT_VALUE to the new dose value node.",
                    "Attach the new amendment source node and SUPPORTS / AMENDS edges.",
                    "Attach IMPACTS edges from the dose-change claim to affected protocol sections.",
                ]
            )
            rationale.append(f"Dose change detected: current active dose is now {obj}.")

        if subject == "protocol.visit_interval":
            governing_sources.extend(
                _governing_sources(
                    claims,
                    docs,
                    subjects=[
                        "regulation.protocol_amendment_requirement",
                        "regulation.protocol_adherence",
                    ],
                )
            )
            impacted_sections.extend(
                [
                    {
                        "section_id": "7.1",
                        "section_title": "Visit Schedule",
                        "impact_reason": f"Visit timing must reflect {obj}.",
                        "severity": "critical",
                        "governing_policy": "visit schedule must align with the amended interval",
                    },
                    {
                        "section_id": "11.1",
                        "section_title": "Assessment Schedule and Procedures",
                        "impact_reason": "Visit timing changes affect procedure and assessment timing.",
                        "severity": "high",
                        "governing_policy": "procedures must align with the current visit interval",
                    },
                    {
                        "section_id": "11.5",
                        "section_title": "Efficacy Assessments and Endpoint Measurement",
                        "impact_reason": "Assessment windows may need alignment with new visit interval.",
                        "severity": "medium",
                        "governing_policy": "endpoint timing should remain synchronized with visit timing",
                    },
                ]
            )
            graph_effects.extend(
                [
                    "Add a new active visit-interval claim node.",
                    "Supersede the prior visit-interval claim node.",
                    "Update protocol_main HAS_CURRENT_VALUE for the visit interval value node.",
                    "Attach IMPACTS edges from the visit-change claim to affected protocol sections.",
                ]
            )
            rationale.append(f"Visit schedule change detected: current active visit interval is now {obj}.")

    if not impacted_sections:
        rationale.append("No active change-event claims were found, so no downstream protocol impacts were inferred.")

    deduped_sections = _dedupe_sections(impacted_sections)
    deduped_graph_effects = list(dict.fromkeys(graph_effects))
    current_state = {
        "active_factual_claims": [
            {
                "claim_id": claim["claim_id"],
                "subject": claim["normalized_subject"],
                "object": claim["normalized_object"],
            }
            for claim in active_factual
        ],
        "active_change_claims": [
            {
                "claim_id": claim["claim_id"],
                "subject": claim["normalized_subject"],
                "object": claim["normalized_object"],
            }
            for claim in active_changes
        ],
    }

    return {
        "summary": _build_summary(deduped_sections, rationale),
        "impacted_sections": deduped_sections,
        "graph_effects": deduped_graph_effects,
        "rationale": rationale,
        "governing_sources": _dedupe_source_entries(governing_sources),
        "changed_sources": _dedupe_source_entries(changed_sources),
        "current_state": current_state,
    }


def analyze_protocol_impacts_for_subject(subject_filter: str) -> Dict[str, Any]:
    payload = analyze_protocol_impacts()
    if subject_filter == "protocol.current_dose":
        keep_sections = {"6.2", "11.3", "11.4", "11.1"}
        keep_changed_claims = {
            claim["claim_id"]
            for claim in payload["current_state"].get("active_change_claims", [])
            if claim["subject"] == "protocol.current_dose"
        }
        payload["impacted_sections"] = [
            section for section in payload["impacted_sections"] if section["section_id"] in keep_sections
        ]
        payload["changed_sources"] = [
            source for source in payload["changed_sources"] if source["claim_id"] in keep_changed_claims
        ]
        payload["governing_sources"] = [
            source
            for source in payload["governing_sources"]
            if source["source_id"] in {"fda_ind_protocol_amendments", "sop_dose_change_citation"}
        ]
        return payload
    return payload


def _dedupe_sections(sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    deduped: Dict[str, Dict[str, Any]] = {}
    severity_order = {"critical": 3, "high": 2, "medium": 1, "low": 0}
    for section in sections:
        key = section["section_id"]
        existing = deduped.get(key)
        if not existing or severity_order[section["severity"]] > severity_order[existing["severity"]]:
            deduped[key] = section
    return sorted(deduped.values(), key=lambda item: item["section_id"])


def _build_summary(sections: List[Dict[str, Any]], rationale: List[str]) -> str:
    if not sections:
        return "No downstream protocol impacts detected from the current active changes."
    critical_count = sum(1 for section in sections if section["severity"] == "critical")
    return (
        f"{len(sections)} protocol sections are impacted by the current amendment state, "
        f"including {critical_count} critical sections. "
        + " ".join(rationale[:2])
    )


def _governing_sources(
    claims: List[Dict[str, Any]],
    docs: Dict[str, Dict[str, Any]],
    subjects: List[str],
) -> List[Dict[str, Any]]:
    selected = [
        claim
        for claim in claims
        if claim["claim_status"] == "active" and claim["normalized_subject"] in subjects
    ]
    rows: List[Dict[str, Any]] = []
    for claim in selected:
        rows.extend(_source_entries_for_claim(claim, docs, role="governing_source"))
    return rows


def _source_entries_for_claim(
    claim: Dict[str, Any],
    docs: Dict[str, Dict[str, Any]],
    role: str,
) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    for source_id in claim.get("source_ids", []):
        doc = docs.get(source_id, {})
        rows.append(
            {
                "role": role,
                "source_id": source_id,
                "title": doc.get("title") or doc.get("label") or source_id,
                "authority": doc.get("family") or "Unknown",
                "kind": doc.get("kind") or "document",
                "claim_id": claim["claim_id"],
                "reason": claim.get("retrieval_summary") or claim["claim_text"],
            }
        )
    return rows


def _dedupe_source_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    deduped: Dict[str, Dict[str, Any]] = {}
    for entry in entries:
        key = f"{entry['role']}::{entry['source_id']}::{entry['claim_id']}"
        deduped[key] = entry
    return list(deduped.values())
