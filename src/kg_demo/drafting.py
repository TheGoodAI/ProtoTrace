from __future__ import annotations

from typing import Any, Dict, List

from .query_engine import GraphQueryEngine


def format_citation(citation: Dict[str, Any]) -> str:
    source_id = citation.get("source_id", "unknown_source")
    heading = citation.get("heading") or "section"
    return f"[{source_id}: {heading}]"


def draft_dosing_section(engine: GraphQueryEngine) -> Dict[str, Any]:
    dose = engine.answer_current_dose()
    visit = engine.answer_current_visit_interval()
    requirements = engine.get_requirement_claims()

    citations = dose.citations + visit.citations
    citation_text = " ".join(format_citation(citation) for citation in citations[:4])

    text = (
        f"Section 6.2 Dosing and Administration. Subjects will receive {dose.claims[0]['normalized_object']} "
        f"under the amended protocol. Section 7.1 Visit Schedule. Subjects will attend visits every "
        f"{visit.claims[0]['normalized_object']}. {citation_text}"
    )

    return {
        "draft_id": "draft_dosing_section_v1",
        "text": text,
        "supporting_claim_ids": [claim["claim_id"] for claim in dose.claims + visit.claims + requirements],
        "citations": citations,
    }


def flawed_dosing_draft() -> Dict[str, Any]:
    return {
        "draft_id": "draft_dosing_section_flawed",
        "text": (
            "Section 6.2 Dosing and Administration. Subjects will receive 50 mg once daily. "
            "Section 7.1 Visit Schedule. Subjects will attend visits every 21 days."
        ),
    }
