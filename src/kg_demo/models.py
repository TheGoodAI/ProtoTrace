from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class ClaimStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    SUPERSEDED = "superseded"
    DISPUTED = "disputed"
    REJECTED = "rejected"


class ValidationSeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class CitationSpan(BaseModel):
    source_id: str
    locator: str
    quoted_text: Optional[str] = None


class SourceDocument(BaseModel):
    source_id: str
    family: str
    title: str
    url: Optional[str] = None
    source_type: str
    version_label: Optional[str] = None
    effective_date: Optional[str] = None
    retrieved_at: datetime = Field(default_factory=datetime.utcnow)


class EvidenceChunk(BaseModel):
    evidence_id: str
    source_id: str
    chunk_text: str
    section_label: Optional[str] = None
    citation_label: Optional[str] = None
    keywords: List[str] = Field(default_factory=list)


class TemporalClaim(BaseModel):
    claim_id: str
    claim_text: str
    normalized_subject: str
    predicate: str
    normalized_object: str
    claim_status: ClaimStatus
    effective_start: Optional[str] = None
    effective_end: Optional[str] = None
    supersedes_claim_ids: List[str] = Field(default_factory=list)
    superseded_by_claim_id: Optional[str] = None
    evidence_ids: List[str] = Field(default_factory=list)
    source_ids: List[str] = Field(default_factory=list)
    citation_spans: List[CitationSpan] = Field(default_factory=list)
    topic_labels: List[str] = Field(default_factory=list)
    reviewer_decision: Optional[str] = None
    reviewer_notes: Optional[str] = None


class ValidationIssue(BaseModel):
    issue_id: str
    severity: ValidationSeverity
    issue_type: str
    message: str
    related_claim_ids: List[str] = Field(default_factory=list)
    evidence_ids: List[str] = Field(default_factory=list)
