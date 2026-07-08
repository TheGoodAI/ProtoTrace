from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .models import TemporalClaim, ValidationIssue


@dataclass
class DemoAnswer:
    answer_text: str
    supporting_claims: List[TemporalClaim] = field(default_factory=list)
    validation_issues: List[ValidationIssue] = field(default_factory=list)


class TemporalClaimPipeline:
    """
    Minimal orchestration shell for the demo system.

    This is intentionally lightweight for now:
    - ingest sources into normalized documents;
    - extract evidence and claims;
    - answer using active claims first;
    - validate drafts against the active ledger.
    """

    def __init__(self) -> None:
        self.claims: List[TemporalClaim] = []

    def load_claims(self, claims: List[TemporalClaim]) -> None:
        self.claims = claims

    def get_active_claims(self, subject: str) -> List[TemporalClaim]:
        return [
            claim
            for claim in self.claims
            if claim.normalized_subject == subject and claim.claim_status.value == "active"
        ]

    def answer_current_fact(self, subject: str) -> DemoAnswer:
        active_claims = self.get_active_claims(subject)
        if not active_claims:
            return DemoAnswer(answer_text="No active claim found for the requested subject.")

        answer_text = active_claims[0].claim_text
        return DemoAnswer(answer_text=answer_text, supporting_claims=active_claims)
