from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Tuple


@dataclass
class GraphNode:
    node_id: str
    node_type: str
    label: str
    properties: Dict[str, Any]


@dataclass
class GraphEdge:
    edge_id: str
    edge_type: str
    source: str
    target: str
    properties: Dict[str, Any]


def _doc_node_id(source_id: str) -> str:
    return f"doc_{source_id}"


def _claim_node_id(claim_id: str) -> str:
    return f"claim_{claim_id}"


def _entity_node(subject: str, obj: str) -> Tuple[str, str, str]:
    if subject == "protocol.current_dose":
        match = re.search(r"(\d+)\s*mg", obj)
        if match:
            dose = match.group(1)
            return (f"dose_{dose}mg_once_daily", "Dose", f"Dose {dose} mg once daily")
    if subject == "protocol.visit_interval":
        match = re.search(r"(\d+)\s*days?", obj)
        if match:
            days = match.group(1)
            return (f"visit_interval_{days}_days", "VisitInterval", f"Visit every {days} days")
    if subject == "sop.dose_change_citation_requirement":
        return ("policy_dose_change_citation", "PolicyRequirement", "Dose change must cite amendment")
    if subject == "regulation.protocol_amendment_requirement":
        return ("policy_protocol_amendment_submission", "PolicyRequirement", "Protocol changes require amendment submission")
    if subject == "regulation.protocol_adherence":
        return ("concept_protocol_adherence", "RegulatoryConcept", "Protocol adherence")
    return (f"entity_{subject.replace('.', '_')}", "Entity", subject)


def _container_node_for_subject(subject: str) -> Tuple[str, str, str] | None:
    if subject.startswith("protocol."):
        return ("protocol_main", "Protocol", "Main protocol")
    if subject.startswith("sop."):
        return ("sop_policy", "SOP", "Protocol drafting SOP")
    if subject.startswith("regulation."):
        return ("regulatory_framework", "RegulatoryFramework", "Regulatory framework")
    return None


def _document_label(source_id: str) -> str:
    return source_id.replace("_", " ").title()


def _source_org_node(source_id: str) -> Tuple[str, str, str] | None:
    mapping = {
        "fda": ("org_fda", "Organization", "FDA"),
        "ich": ("org_ich", "Organization", "ICH"),
        "ema": ("org_ema", "Organization", "EMA"),
        "ecfr": ("org_ecfr", "Organization", "eCFR"),
        "cdisc": ("org_cdisc", "Organization", "CDISC"),
    }
    for prefix, node in mapping.items():
        if source_id.startswith(prefix):
            return node
    return None


def _impact_sections_for_claim(claim: Dict[str, Any]) -> List[Tuple[str, str, str]]:
    subject = claim["normalized_subject"]
    if claim["claim_type"] != "change_event":
        return []
    if subject == "protocol.current_dose":
        return [
            ("section_6_2", "ProtocolSection", "6.2 Dosing and Administration"),
            ("section_11_3", "ProtocolSection", "11.3 Dose Modifications and Discontinuation"),
            ("section_11_4", "ProtocolSection", "11.4 Safety Monitoring Plan"),
            ("section_11_1", "ProtocolSection", "11.1 Assessment Schedule and Procedures"),
        ]
    if subject == "protocol.visit_interval":
        return [
            ("section_7_1", "ProtocolSection", "7.1 Visit Schedule"),
            ("section_11_1", "ProtocolSection", "11.1 Assessment Schedule and Procedures"),
            ("section_11_5", "ProtocolSection", "11.5 Efficacy Assessments and Endpoint Measurement"),
        ]
    return []


def export_graph(claims: Iterable[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    nodes: Dict[str, GraphNode] = {}
    edges: Dict[str, GraphEdge] = {}
    claim_list = list(claims)

    def ensure_node(node_id: str, node_type: str, label: str, properties: Dict[str, Any] | None = None) -> None:
        if node_id not in nodes:
            nodes[node_id] = GraphNode(
                node_id=node_id,
                node_type=node_type,
                label=label,
                properties=properties or {},
            )

    def ensure_edge(edge_type: str, source: str, target: str, properties: Dict[str, Any] | None = None) -> None:
        edge_id = f"{edge_type}:{source}:{target}"
        if edge_id not in edges:
            edges[edge_id] = GraphEdge(
                edge_id=edge_id,
                edge_type=edge_type,
                source=source,
                target=target,
                properties=properties or {},
            )

    for claim in claim_list:
        claim_node = _claim_node_id(claim["claim_id"])
        ensure_node(
            claim_node,
            "Claim",
            claim["claim_text"],
            {
                "claim_status": claim["claim_status"],
                "claim_type": claim["claim_type"],
                "normalized_subject": claim["normalized_subject"],
                "predicate": claim["predicate"],
                "normalized_object": claim["normalized_object"],
            },
        )

        for source_id in claim.get("source_ids", []):
            doc_node = _doc_node_id(source_id)
            ensure_node(doc_node, "SourceDocument", _document_label(source_id), {"source_id": source_id})
            ensure_edge("SUPPORTED_BY", claim_node, doc_node)

            org_node = _source_org_node(source_id)
            if org_node:
                ensure_node(org_node[0], org_node[1], org_node[2], {})
                ensure_edge("ISSUED_BY", doc_node, org_node[0])

        entity_id, entity_type, entity_label = _entity_node(claim["normalized_subject"], claim["normalized_object"])
        ensure_node(
            entity_id,
            entity_type,
            entity_label,
            {"normalized_subject": claim["normalized_subject"], "value": claim["normalized_object"]},
        )
        ensure_edge("ABOUT", claim_node, entity_id)

        container = _container_node_for_subject(claim["normalized_subject"])
        if container:
            ensure_node(container[0], container[1], container[2], {})
            ensure_edge("FOR", claim_node, container[0])

        for superseded_id in claim.get("supersedes_claim_ids", []):
            ensure_edge("SUPERSEDES", claim_node, _claim_node_id(superseded_id))

        superseded_by = claim.get("superseded_by_claim_id")
        if superseded_by:
            ensure_edge("SUPERSEDED_BY", claim_node, _claim_node_id(superseded_by))

        if claim["claim_status"] == "active" and container:
            ensure_edge("HAS_CURRENT_VALUE", container[0], entity_id)

        if claim["normalized_subject"] == "protocol.current_dose":
            ensure_node("amendment_v2", "Amendment", "Protocol amendment v2", {})
            if "protocol_amendment_v2" in claim.get("source_ids", []):
                ensure_edge("AMENDS", "amendment_v2", "protocol_main")
        if claim["normalized_subject"] == "protocol.visit_interval":
            ensure_node("amendment_v2", "Amendment", "Protocol amendment v2", {})
        if claim["normalized_subject"].startswith("regulation.") or claim["normalized_subject"].startswith("sop."):
            if container:
                ensure_edge("GOVERNS", entity_id, "protocol_main")

    active_governance_nodes: List[str] = []
    for claim in claim_list:
        if claim["claim_status"] != "active":
            continue
        subject = claim["normalized_subject"]
        if subject.startswith("regulation.") or subject.startswith("sop."):
            entity_id, _, _ = _entity_node(subject, claim["normalized_object"])
            active_governance_nodes.append(entity_id)

    unique_governance_nodes = list(dict.fromkeys(active_governance_nodes))
    for claim in claim_list:
        if claim["claim_status"] != "active" or claim["claim_type"] != "change_event":
            continue
        claim_node = _claim_node_id(claim["claim_id"])
        for section_id, section_type, section_label in _impact_sections_for_claim(claim):
            ensure_node(section_id, section_type, section_label, {"subject": claim["normalized_subject"]})
            ensure_edge("IMPACTS", claim_node, section_id)
            for governance_node in unique_governance_nodes:
                ensure_edge("GOVERNED_BY", section_id, governance_node)

    return {
        "nodes": [node.__dict__ for node in nodes.values()],
        "edges": [edge.__dict__ for edge in edges.values()],
    }


def build_evidence_manifest(chunks: Iterable[Dict[str, Any]]) -> Dict[str, Any]:
    chunk_rows = []
    source_index: Dict[str, int] = {}
    for chunk in chunks:
        source_id = chunk["source_id"]
        source_index[source_id] = source_index.get(source_id, 0) + 1
        chunk_rows.append(
            {
                "chunk_id": chunk["chunk_id"],
                "source_id": source_id,
                "family": chunk.get("family"),
                "heading": chunk.get("heading"),
                "citation_locator": chunk.get("citation_locator"),
            }
        )
    return {
        "total_chunks": len(chunk_rows),
        "sources": [{"source_id": source_id, "chunk_count": count} for source_id, count in sorted(source_index.items())],
        "chunks": chunk_rows,
    }
