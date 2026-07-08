from __future__ import annotations

import copy
from datetime import datetime, timezone
from typing import Any, Dict, List

from .artifact_store import read_json, write_json
from .chunker import chunk_documents
from .demo_docs import build_demo_documents
from .document_store import invalidate_document_cache, load_local_normalized_documents
from .graph_export import build_evidence_manifest, export_graph


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def simulate_dose_amendment(new_dose_mg: int, reviewer_note: str | None = None) -> Dict[str, Any]:
    claims: List[Dict[str, Any]] = read_json("claims/claim_ledger.json")
    demo_docs: List[Dict[str, Any]] = read_json("normalized/demo_documents.json")
    prior_nodes: List[Dict[str, Any]] = read_json("graph/nodes.json")
    prior_edges: List[Dict[str, Any]] = read_json("graph/edges.json")
    prior_events: List[Dict[str, Any]] = read_json("claims/approval_events.json")

    protocol_docs = [doc for doc in demo_docs if doc["source_id"].startswith("protocol_")]
    amendment_number = len([doc for doc in protocol_docs if "amendment" in doc["source_id"]]) + 2
    source_id = f"protocol_amendment_v{amendment_number}"
    created_at = _now()

    old_active_dose_claims = [
        claim for claim in claims
        if claim["normalized_subject"] == "protocol.current_dose"
        and claim["claim_status"] == "active"
        and claim["claim_type"] == "factual"
    ]
    prior_claim_ids = [claim["claim_id"] for claim in old_active_dose_claims]

    for claim in old_active_dose_claims:
        claim["claim_status"] = "superseded"
        claim["superseded_by_claim_id"] = f"claim_{source_id}_dose_{new_dose_mg}mg"

    new_document = {
        "source_id": source_id,
        "family": "DEMO",
        "label": f"Protocol Amendment Version {amendment_number}",
        "kind": "amendment",
        "seed_url": None,
        "resolved_url": None,
        "retrieved_at": created_at,
        "retrieved_via": "ui_simulated_demo",
        "title": f"Protocol Amendment Version {amendment_number}",
        "text": f"Section 6.2 Dosing and Administration. Dose will be increased to {new_dose_mg} mg once daily.",
        "sections": [
            {
                "heading": "Section 6.2 Dosing and Administration",
                "text": f"Dose will be increased to {new_dose_mg} mg once daily.",
            }
        ],
        "citation_spans": [
            {
                "locator": "section 6.2",
                "quoted_text": f"Dose will be increased to {new_dose_mg} mg once daily.",
            }
        ],
    }
    demo_docs.append(new_document)

    all_docs = load_local_normalized_documents() + demo_docs
    chunks = chunk_documents(all_docs)
    new_chunk = next(chunk for chunk in chunks if chunk["source_id"] == source_id)

    new_claim = {
        "claim_id": f"claim_{source_id}_dose_{new_dose_mg}mg",
        "claim_text": f"The current protocol dose is {new_dose_mg} mg once daily.",
        "normalized_subject": "protocol.current_dose",
        "predicate": "equals",
        "normalized_object": f"{new_dose_mg} mg once daily",
        "claim_type": "factual",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": prior_claim_ids,
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 6.2 Dosing and Administration",
                "quoted_text": f"Dose will be increased to {new_dose_mg} mg once daily.",
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["dosing", "amendment"],
        "retrieval_keywords": ["current dose", "dose change", f"{new_dose_mg} mg"],
        "retrieval_summary": f"Current dose updated to {new_dose_mg} mg once daily.",
        "created_at": created_at,
    }

    new_change_claim = {
        "claim_id": f"claim_{source_id}_dose_change_to_{new_dose_mg}mg",
        "claim_text": f"The protocol dose changed to {new_dose_mg} mg once daily.",
        "normalized_subject": "protocol.current_dose",
        "predicate": "changes_to",
        "normalized_object": f"{new_dose_mg} mg once daily",
        "claim_type": "change_event",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": [],
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 6.2 Dosing and Administration",
                "quoted_text": f"Dose will be increased to {new_dose_mg} mg once daily.",
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["dosing", "amendment"],
        "retrieval_keywords": ["dose change", f"{new_dose_mg} mg"],
        "retrieval_summary": f"Dose changed to {new_dose_mg} mg once daily.",
        "created_at": created_at,
    }

    updated_claims = claims + [new_change_claim, new_claim]
    graph = export_graph(updated_claims)
    evidence_manifest = build_evidence_manifest(chunks)
    system_event = {
        "event_id": f"event_{source_id}_{created_at}",
        "action": "simulate_amendment",
        "reviewer": "demo_system",
        "message": f"Created {source_id} with a new active dose of {new_dose_mg} mg once daily.",
        "notes": reviewer_note or "Simulated amendment from the demo UI.",
        "created_at": created_at,
    }

    write_json("normalized/demo_documents.json", demo_docs)
    write_json("chunks/all_chunks.json", chunks)
    write_json("chunks/evidence_manifest.json", evidence_manifest)
    write_json("claims/claim_ledger.json", updated_claims)
    write_json("claims/approval_events.json", prior_events + [system_event])
    write_json("graph/nodes.json", graph["nodes"])
    write_json("graph/edges.json", graph["edges"])
    write_json(
        "graph/graph_manifest.json",
        {
            "nodes_total": len(graph["nodes"]),
            "edges_total": len(graph["edges"]),
            "claims_total": len(updated_claims),
            "chunks_total": len(chunks),
            "outputs": {
                "nodes": "graph/nodes.json",
                "edges": "graph/edges.json",
                "evidence_manifest": "chunks/evidence_manifest.json",
            },
        },
    )
    invalidate_document_cache()

    previous_dose = old_active_dose_claims[0]["normalized_object"] if old_active_dose_claims else "unknown"
    prior_node_ids = {node["node_id"] for node in prior_nodes}
    prior_edge_ids = {edge["edge_id"] for edge in prior_edges}
    added_nodes = [node for node in graph["nodes"] if node["node_id"] not in prior_node_ids]
    added_edges = [edge for edge in graph["edges"] if edge["edge_id"] not in prior_edge_ids]
    superseded_node_ids = [f"claim_{claim_id}" for claim_id in prior_claim_ids]
    updated_current_edges = [
        edge
        for edge in added_edges
        if edge["edge_type"] == "HAS_CURRENT_VALUE" and edge["source"] == "protocol_main"
    ]
    generated_protocol_text = (
        f"Section 6.2 Dosing and Administration. Subjects will receive {new_dose_mg} mg once daily under the latest amendment. "
        f"Previous current dose {previous_dose} is superseded by amendment {amendment_number}."
    )

    return {
        "new_source_id": source_id,
        "new_claim_id": new_claim["claim_id"],
        "new_dose": new_claim["normalized_object"],
        "superseded_claim_ids": prior_claim_ids,
        "claims_total": len(updated_claims),
        "generated_protocol_text": generated_protocol_text,
        "system_event": system_event,
        "graph_delta": {
            "added_nodes": added_nodes,
            "added_edges": added_edges,
            "superseded_node_ids": superseded_node_ids,
            "updated_current_edges": updated_current_edges,
            "new_nodes_total": len(graph["nodes"]),
            "new_edges_total": len(graph["edges"]),
        },
    }


def simulate_visit_interval_amendment(new_interval_days: int, reviewer_note: str | None = None) -> Dict[str, Any]:
    claims: List[Dict[str, Any]] = read_json("claims/claim_ledger.json")
    demo_docs: List[Dict[str, Any]] = read_json("normalized/demo_documents.json")
    prior_nodes: List[Dict[str, Any]] = read_json("graph/nodes.json")
    prior_edges: List[Dict[str, Any]] = read_json("graph/edges.json")
    prior_events: List[Dict[str, Any]] = read_json("claims/approval_events.json")

    protocol_docs = [doc for doc in demo_docs if doc["source_id"].startswith("protocol_")]
    amendment_number = len([doc for doc in protocol_docs if "amendment" in doc["source_id"]]) + 2
    source_id = f"protocol_amendment_v{amendment_number}"
    created_at = _now()

    old_active_visit_claims = [
        claim for claim in claims
        if claim["normalized_subject"] == "protocol.visit_interval"
        and claim["claim_status"] == "active"
        and claim["claim_type"] == "factual"
    ]
    prior_claim_ids = [claim["claim_id"] for claim in old_active_visit_claims]

    for claim in old_active_visit_claims:
        claim["claim_status"] = "superseded"
        claim["superseded_by_claim_id"] = f"claim_{source_id}_visit_{new_interval_days}days"

    new_document = {
        "source_id": source_id,
        "family": "DEMO",
        "label": f"Protocol Amendment Version {amendment_number}",
        "kind": "amendment",
        "seed_url": None,
        "resolved_url": None,
        "retrieved_at": created_at,
        "retrieved_via": "ui_simulated_demo",
        "title": f"Protocol Amendment Version {amendment_number}",
        "text": f"Section 7.1 Visit Schedule. Subjects will attend visits every {new_interval_days} days.",
        "sections": [
            {
                "heading": "Section 7.1 Visit Schedule",
                "text": f"Subjects will attend visits every {new_interval_days} days.",
            }
        ],
        "citation_spans": [
            {
                "locator": "section 7.1",
                "quoted_text": f"Subjects will attend visits every {new_interval_days} days.",
            }
        ],
    }
    demo_docs.append(new_document)

    all_docs = load_local_normalized_documents() + demo_docs
    chunks = chunk_documents(all_docs)
    new_chunk = next(chunk for chunk in chunks if chunk["source_id"] == source_id)

    new_claim = {
        "claim_id": f"claim_{source_id}_visit_{new_interval_days}days",
        "claim_text": f"Visits occur every {new_interval_days} days.",
        "normalized_subject": "protocol.visit_interval",
        "predicate": "equals",
        "normalized_object": f"{new_interval_days} days",
        "claim_type": "factual",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": prior_claim_ids,
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 7.1 Visit Schedule",
                "quoted_text": f"Subjects will attend visits every {new_interval_days} days.",
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["visit_schedule", "amendment"],
        "retrieval_keywords": ["visit interval", "visit schedule change", f"{new_interval_days} days"],
        "retrieval_summary": f"Visit interval updated to every {new_interval_days} days.",
        "created_at": created_at,
    }

    new_change_claim = {
        "claim_id": f"claim_{source_id}_visit_change_to_{new_interval_days}days",
        "claim_text": f"The protocol visit interval changed to every {new_interval_days} days.",
        "normalized_subject": "protocol.visit_interval",
        "predicate": "changes_to",
        "normalized_object": f"{new_interval_days} days",
        "claim_type": "change_event",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": [],
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 7.1 Visit Schedule",
                "quoted_text": f"Subjects will attend visits every {new_interval_days} days.",
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["visit_schedule", "amendment"],
        "retrieval_keywords": ["visit schedule change", f"{new_interval_days} days"],
        "retrieval_summary": f"Visit interval changed to every {new_interval_days} days.",
        "created_at": created_at,
    }

    updated_claims = claims + [new_change_claim, new_claim]
    graph = export_graph(updated_claims)
    evidence_manifest = build_evidence_manifest(chunks)
    system_event = {
        "event_id": f"event_{source_id}_{created_at}",
        "action": "simulate_amendment",
        "reviewer": "demo_system",
        "message": f"Created {source_id} with a new active visit interval of every {new_interval_days} days.",
        "notes": reviewer_note or "Simulated amendment from the demo UI.",
        "created_at": created_at,
    }

    write_json("normalized/demo_documents.json", demo_docs)
    write_json("chunks/all_chunks.json", chunks)
    write_json("chunks/evidence_manifest.json", evidence_manifest)
    write_json("claims/claim_ledger.json", updated_claims)
    write_json("claims/approval_events.json", prior_events + [system_event])
    write_json("graph/nodes.json", graph["nodes"])
    write_json("graph/edges.json", graph["edges"])
    write_json(
        "graph/graph_manifest.json",
        {
            "nodes_total": len(graph["nodes"]),
            "edges_total": len(graph["edges"]),
            "claims_total": len(updated_claims),
            "chunks_total": len(chunks),
            "outputs": {
                "nodes": "graph/nodes.json",
                "edges": "graph/edges.json",
                "evidence_manifest": "chunks/evidence_manifest.json",
            },
        },
    )
    invalidate_document_cache()

    previous_interval = old_active_visit_claims[0]["normalized_object"] if old_active_visit_claims else "unknown"
    prior_node_ids = {node["node_id"] for node in prior_nodes}
    prior_edge_ids = {edge["edge_id"] for edge in prior_edges}
    added_nodes = [node for node in graph["nodes"] if node["node_id"] not in prior_node_ids]
    added_edges = [edge for edge in graph["edges"] if edge["edge_id"] not in prior_edge_ids]
    superseded_node_ids = [f"claim_{claim_id}" for claim_id in prior_claim_ids]
    updated_current_edges = [
        edge
        for edge in added_edges
        if edge["edge_type"] == "HAS_CURRENT_VALUE" and edge["source"] == "protocol_main"
    ]
    generated_protocol_text = (
        f"Section 7.1 Visit Schedule. Subjects will attend visits every {new_interval_days} days under the latest amendment. "
        f"Previous visit interval {previous_interval} is superseded by amendment {amendment_number}."
    )

    return {
        "new_source_id": source_id,
        "new_claim_id": new_claim["claim_id"],
        "new_value": new_claim["normalized_object"],
        "superseded_claim_ids": prior_claim_ids,
        "claims_total": len(updated_claims),
        "generated_protocol_text": generated_protocol_text,
        "system_event": system_event,
        "graph_delta": {
            "added_nodes": added_nodes,
            "added_edges": added_edges,
            "superseded_node_ids": superseded_node_ids,
            "updated_current_edges": updated_current_edges,
            "new_nodes_total": len(graph["nodes"]),
            "new_edges_total": len(graph["edges"]),
        },
    }


def simulate_eligibility_amendment(new_excluded_drug: str, reviewer_note: str | None = None) -> Dict[str, Any]:
    """Add one concomitant-medication exclusion to the eligibility criteria.

    Unlike dose/visit amendments, which replace a scalar value, this amendment type
    accumulates: each step appends a drug name to a growing exclusion list, giving the
    benchmark a third, structurally distinct amendment semantics (cumulative-list growth
    rather than value replacement).
    """
    claims: List[Dict[str, Any]] = read_json("claims/claim_ledger.json")
    demo_docs: List[Dict[str, Any]] = read_json("normalized/demo_documents.json")
    prior_nodes: List[Dict[str, Any]] = read_json("graph/nodes.json")
    prior_edges: List[Dict[str, Any]] = read_json("graph/edges.json")
    prior_events: List[Dict[str, Any]] = read_json("claims/approval_events.json")

    protocol_docs = [doc for doc in demo_docs if doc["source_id"].startswith("protocol_")]
    amendment_number = len([doc for doc in protocol_docs if "amendment" in doc["source_id"]]) + 2
    source_id = f"protocol_amendment_v{amendment_number}"
    created_at = _now()

    old_active_exclusion_claims = [
        claim for claim in claims
        if claim["normalized_subject"] == "protocol.exclusion_criteria"
        and claim["claim_status"] == "active"
        and claim["claim_type"] == "factual"
    ]
    prior_claim_ids = [claim["claim_id"] for claim in old_active_exclusion_claims]
    previous_list = old_active_exclusion_claims[0]["normalized_object"] if old_active_exclusion_claims else ""
    excluded_drugs = [d.strip() for d in previous_list.split(",") if d.strip()] + [new_excluded_drug]
    new_list = ", ".join(excluded_drugs)
    slug = new_excluded_drug.lower().replace(" ", "_")

    for claim in old_active_exclusion_claims:
        claim["claim_status"] = "superseded"
        claim["superseded_by_claim_id"] = f"claim_{source_id}_exclusion_{slug}"

    section_text = f"Exclusion criteria updated: subjects currently receiving {new_list} are excluded."
    new_document = {
        "source_id": source_id,
        "family": "DEMO",
        "label": f"Protocol Amendment Version {amendment_number}",
        "kind": "amendment",
        "seed_url": None,
        "resolved_url": None,
        "retrieved_at": created_at,
        "retrieved_via": "ui_simulated_demo",
        "title": f"Protocol Amendment Version {amendment_number}",
        "text": f"Section 5.2 Eligibility Criteria. {section_text}",
        "sections": [
            {
                "heading": "Section 5.2 Eligibility Criteria",
                "text": section_text,
            }
        ],
        "citation_spans": [
            {
                "locator": "section 5.2",
                "quoted_text": section_text,
            }
        ],
    }
    demo_docs.append(new_document)

    all_docs = load_local_normalized_documents() + demo_docs
    chunks = chunk_documents(all_docs)
    new_chunk = next(chunk for chunk in chunks if chunk["source_id"] == source_id)

    new_claim = {
        "claim_id": f"claim_{source_id}_exclusion_{slug}",
        "claim_text": f"The current exclusion criteria are {new_list}.",
        "normalized_subject": "protocol.exclusion_criteria",
        "predicate": "equals",
        "normalized_object": new_list,
        "claim_type": "factual",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": prior_claim_ids,
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 5.2 Eligibility Criteria",
                "quoted_text": section_text,
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["eligibility", "amendment"],
        "retrieval_keywords": ["exclusion criteria", "eligibility change", new_excluded_drug],
        "retrieval_summary": f"Exclusion criteria updated to {new_list}.",
        "created_at": created_at,
    }

    new_change_claim = {
        "claim_id": f"claim_{source_id}_exclusion_change_{slug}",
        "claim_text": f"The exclusion criteria changed from {previous_list} to {new_list}.",
        "normalized_subject": "protocol.exclusion_criteria",
        "predicate": "changes_to",
        "normalized_object": new_list,
        "claim_type": "change_event",
        "claim_status": "active",
        "effective_start": created_at,
        "effective_end": None,
        "supersedes_claim_ids": [],
        "superseded_by_claim_id": None,
        "evidence_ids": [new_chunk["chunk_id"]],
        "source_ids": [source_id],
        "citation_spans": [
            {
                "source_id": source_id,
                "locator": "Section 5.2 Eligibility Criteria",
                "quoted_text": section_text,
            }
        ],
        "extraction_method": "ui_simulated_amendment",
        "extraction_confidence": 0.95,
        "reviewer_decision": None,
        "reviewer_notes": reviewer_note,
        "entity_ids": [],
        "relation_ids": [],
        "topic_labels": ["eligibility", "amendment"],
        "retrieval_keywords": ["exclusion criteria change", new_excluded_drug],
        "retrieval_summary": f"Exclusion criteria changed to {new_list}.",
        "created_at": created_at,
    }

    updated_claims = claims + [new_change_claim, new_claim]
    graph = export_graph(updated_claims)
    evidence_manifest = build_evidence_manifest(chunks)
    system_event = {
        "event_id": f"event_{source_id}_{created_at}",
        "action": "simulate_amendment",
        "reviewer": "demo_system",
        "message": f"Created {source_id} adding {new_excluded_drug} to the exclusion criteria.",
        "notes": reviewer_note or "Simulated amendment from the demo UI.",
        "created_at": created_at,
    }

    write_json("normalized/demo_documents.json", demo_docs)
    write_json("chunks/all_chunks.json", chunks)
    write_json("chunks/evidence_manifest.json", evidence_manifest)
    write_json("claims/claim_ledger.json", updated_claims)
    write_json("claims/approval_events.json", prior_events + [system_event])
    write_json("graph/nodes.json", graph["nodes"])
    write_json("graph/edges.json", graph["edges"])
    write_json(
        "graph/graph_manifest.json",
        {
            "nodes_total": len(graph["nodes"]),
            "edges_total": len(graph["edges"]),
            "claims_total": len(updated_claims),
            "chunks_total": len(chunks),
            "outputs": {
                "nodes": "graph/nodes.json",
                "edges": "graph/edges.json",
                "evidence_manifest": "chunks/evidence_manifest.json",
            },
        },
    )
    invalidate_document_cache()

    prior_node_ids = {node["node_id"] for node in prior_nodes}
    prior_edge_ids = {edge["edge_id"] for edge in prior_edges}
    added_nodes = [node for node in graph["nodes"] if node["node_id"] not in prior_node_ids]
    added_edges = [edge for edge in graph["edges"] if edge["edge_id"] not in prior_edge_ids]
    superseded_node_ids = [f"claim_{claim_id}" for claim_id in prior_claim_ids]
    updated_current_edges = [
        edge
        for edge in added_edges
        if edge["edge_type"] == "HAS_CURRENT_VALUE" and edge["source"] == "protocol_main"
    ]
    generated_protocol_text = (
        f"Section 5.2 Eligibility Criteria. {section_text} "
        f"Previous exclusion criteria {previous_list or 'none'} superseded by amendment {amendment_number}."
    )

    return {
        "new_source_id": source_id,
        "new_claim_id": new_claim["claim_id"],
        "new_value": new_claim["normalized_object"],
        "superseded_claim_ids": prior_claim_ids,
        "claims_total": len(updated_claims),
        "generated_protocol_text": generated_protocol_text,
        "system_event": system_event,
        "graph_delta": {
            "added_nodes": added_nodes,
            "added_edges": added_edges,
            "superseded_node_ids": superseded_node_ids,
            "updated_current_edges": updated_current_edges,
            "new_nodes_total": len(graph["nodes"]),
            "new_edges_total": len(graph["edges"]),
        },
    }
