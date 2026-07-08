from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .artifact_store import read_json


@dataclass
class QueryResult:
    question_type: str
    answer: str
    claims: List[Dict[str, Any]]
    citations: List[Dict[str, Any]]


class GraphQueryEngine:
    def __init__(self) -> None:
        self.claims: List[Dict[str, Any]] = read_json("claims/claim_ledger.json")
        self.nodes: List[Dict[str, Any]] = read_json("graph/nodes.json")
        self.edges: List[Dict[str, Any]] = read_json("graph/edges.json")
        self.chunks: List[Dict[str, Any]] = read_json("chunks/all_chunks.json")
        self.chunk_by_id = {chunk["chunk_id"]: chunk for chunk in self.chunks}
        self.claim_by_id = {claim["claim_id"]: claim for claim in self.claims}

    def get_active_claims(self, subject: str) -> List[Dict[str, Any]]:
        claims = [
            claim
            for claim in self.claims
            if claim["normalized_subject"] == subject
            and claim["claim_status"] == "active"
            and claim["claim_type"] == "factual"
        ]
        claims.sort(
            key=lambda claim: claim.get("created_at", ""),
            reverse=True,
        )
        return claims

    def get_superseded_claims(self, subject: str) -> List[Dict[str, Any]]:
        claims = [
            claim
            for claim in self.claims
            if claim["normalized_subject"] == subject
            and claim["claim_status"] == "superseded"
            and claim["claim_type"] == "factual"
        ]
        claims.sort(key=lambda claim: claim.get("created_at", ""), reverse=True)
        return claims

    def get_direct_predecessor_claim(self, subject: str) -> Optional[Dict[str, Any]]:
        active_claims = self.get_active_claims(subject)
        if not active_claims:
            return None

        active_claim = active_claims[0]
        predecessor_ids = active_claim.get("supersedes_claim_ids", [])
        factual_predecessors = [
            self.claim_by_id[claim_id]
            for claim_id in predecessor_ids
            if claim_id in self.claim_by_id
            and self.claim_by_id[claim_id]["claim_type"] == "factual"
            and self.claim_by_id[claim_id]["normalized_subject"] == subject
        ]
        if factual_predecessors:
            factual_predecessors.sort(key=lambda claim: claim.get("created_at", ""), reverse=True)
            return factual_predecessors[0]

        superseded_claims = self.get_superseded_claims(subject)
        return superseded_claims[0] if superseded_claims else None

    def get_change_claims(self, subject: str) -> List[Dict[str, Any]]:
        return [
            claim
            for claim in self.claims
            if claim["normalized_subject"] == subject and claim["claim_type"] == "change_event"
        ]

    def claim_citations(self, claim: Dict[str, Any]) -> List[Dict[str, Any]]:
        citations: List[Dict[str, Any]] = []
        for evidence_id in claim.get("evidence_ids", []):
            chunk = self.chunk_by_id.get(evidence_id)
            if not chunk:
                continue
            citations.append(
                {
                    "source_id": chunk["source_id"],
                    "heading": chunk.get("heading"),
                    "chunk_id": evidence_id,
                    "quoted_text": chunk.get("text"),
                }
            )
        return citations

    def answer_current_dose(self) -> QueryResult:
        claims = self.get_active_claims("protocol.current_dose")
        if not claims:
            return QueryResult("current_dose", "No active dose claim found.", [], [])
        claim = claims[0]
        answer = f"The current dose is {claim['normalized_object']}."
        return QueryResult("current_dose", answer, [claim], self.claim_citations(claim))

    def answer_current_visit_interval(self) -> QueryResult:
        claims = self.get_active_claims("protocol.visit_interval")
        if not claims:
            return QueryResult("current_visit_interval", "No active visit interval claim found.", [], [])
        claim = claims[0]
        answer = f"The current visit interval is {claim['normalized_object']}."
        return QueryResult("current_visit_interval", answer, [claim], self.claim_citations(claim))

    def answer_what_changed(self) -> QueryResult:
        active_dose = self.get_active_claims("protocol.current_dose")
        old_dose = [claim for claim in [self.get_direct_predecessor_claim("protocol.current_dose")] if claim]
        change_dose = self.get_change_claims("protocol.current_dose")
        active_visit = self.get_active_claims("protocol.visit_interval")
        old_visit = [claim for claim in [self.get_direct_predecessor_claim("protocol.visit_interval")] if claim]
        change_visit = self.get_change_claims("protocol.visit_interval")

        parts: List[str] = []
        selected_claims: List[Dict[str, Any]] = []

        if old_dose and active_dose:
            parts.append(f"Dose changed from {old_dose[0]['normalized_object']} to {active_dose[0]['normalized_object']}.")
            selected_claims.extend([old_dose[0], active_dose[0]])
        elif change_dose:
            parts.append(f"Dose changed to {change_dose[0]['normalized_object']}.")
            selected_claims.extend(change_dose[:1])

        if old_visit and active_visit:
            parts.append(f"Visit interval changed from {old_visit[0]['normalized_object']} to {active_visit[0]['normalized_object']}.")
            selected_claims.extend([old_visit[0], active_visit[0]])
        elif change_visit:
            parts.append(f"Visit interval changed to {change_visit[0]['normalized_object']}.")
            selected_claims.extend(change_visit[:1])

        citations: List[Dict[str, Any]] = []
        seen = set()
        for claim in selected_claims:
            for citation in self.claim_citations(claim):
                key = citation["chunk_id"]
                if key not in seen:
                    seen.add(key)
                    citations.append(citation)

        return QueryResult("what_changed", " ".join(parts) if parts else "No changes found.", selected_claims, citations)

    def get_requirement_claims(self) -> List[Dict[str, Any]]:
        return [claim for claim in self.claims if claim["claim_type"] in {"requirement", "recommendation"}]
