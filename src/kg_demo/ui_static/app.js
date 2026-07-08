const state = {
  documents: [],
  claims: [],
  systemEvents: [],
  graphManifest: {},
  graph: { nodes: [], edges: [] },
  graphDelta: null,
};

async function api(path, options = {}) {
  const response = await fetch(path, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!response.ok) {
    let message = `Request failed: ${response.status}`;
    try {
      const body = await response.json();
      if (body && body.error) message = body.error;
    } catch (_parseError) {
      // response body wasn't JSON; keep the generic status message
    }
    throw new Error(message);
  }
  return response.json();
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function setStatus(text, tone = "ready") {
  const chip = document.getElementById("statusChip");
  chip.textContent = text;
  chip.className = `chip tone-${tone}`;
}

function setBusy(busy) {
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.disabled = busy;
  });
}

function markActiveAction(action) {
  document.querySelectorAll("[data-action]").forEach((button) => {
    button.classList.toggle("active", button.dataset.action === action);
  });
}

function renderDocuments() {
  const root = document.getElementById("documentList");
  root.innerHTML = state.documents.map((doc) => `
    <div class="document-item">
      <strong>${escapeHtml(doc.title)}</strong>
      <div class="document-meta">${escapeHtml(doc.family || "Unknown")} &middot; ${escapeHtml(doc.kind || "document")}</div>
    </div>
  `).join("");
}

function claimStatusClass(claim) {
  if (claim.claim_status === "superseded") return "status-superseded";
  return "status-active";
}

function renderLedger() {
  const root = document.getElementById("ledgerList");
  document.getElementById("ledgerStats").textContent = `${state.claims.length} claims`;
  root.innerHTML = state.claims.map((claim) => `
    <div class="ledger-item ${claim.claim_status === "superseded" ? "item-superseded" : ""}">
      <strong>${escapeHtml(claim.claim_text)}</strong>
      <div class="claim-meta">${escapeHtml(claim.normalized_subject)} &middot; ${escapeHtml(claim.normalized_object)}</div>
      <span class="claim-status ${claimStatusClass(claim)}">${escapeHtml(claim.claim_status)}</span>
    </div>
  `).join("");
}

function renderSystemEvents() {
  const root = document.getElementById("systemEvents");
  if (!state.systemEvents.length) {
    root.classList.add("placeholder");
    root.textContent = "System events will appear here.";
    return;
  }
  root.classList.remove("placeholder");
  root.innerHTML = state.systemEvents.slice().reverse().map((event) => `
    <div class="event-item">
      <strong>${escapeHtml(event.claim_id || event.action || "event")}</strong>
      <div class="event-meta">${escapeHtml(event.reviewer || "system")} &middot; ${escapeHtml(event.reviewed_at || event.created_at || "")}</div>
      <div>${escapeHtml(event.notes || event.message || "")}</div>
    </div>
  `).join("");
}

function renderAnswer(title, body, tone = "Ready", toneClass = "ready") {
  setStatus(tone, toneClass);
  const summary = document.getElementById("answerSummary");
  summary.classList.remove("placeholder");
  summary.innerHTML = `
    <div class="panel-heading">${escapeHtml(title)}</div>
    <div style="margin-top:8px; font-size:0.98rem; line-height:1.55;">${escapeHtml(body)}</div>
  `;
}

function renderValidationBanner(report) {
  const banner = document.getElementById("validationBanner");
  if (!report || !report.issues || !report.issues.length) {
    banner.classList.add("hidden");
    banner.innerHTML = "";
    return;
  }
  banner.classList.remove("hidden");
  banner.innerHTML = report.issues.map((issue) => `
    <div class="validation-issue">
      <span class="severity-dot ${issue.severity === "critical" ? "bad" : "warn"}"></span>
      <div><strong>${escapeHtml(issue.issue_type)}</strong>: ${escapeHtml(issue.message)}</div>
    </div>
  `).join("");
}

function renderCitations(citations = []) {
  const root = document.getElementById("citationTray");
  if (!citations.length) {
    root.classList.add("empty");
    root.textContent = "Citations will appear here.";
    return;
  }
  root.classList.remove("empty");
  root.innerHTML = citations.map((citation) => `
    <div class="citation-item">
      <strong>${escapeHtml(citation.source_id)}</strong>
      <div class="mini-meta">${escapeHtml(citation.heading || citation.locator || "")}</div>
      <div>${escapeHtml(citation.quoted_text || "")}</div>
    </div>
  `).join("");
}

function renderProtocolPreview(text) {
  const root = document.getElementById("protocolPreview");
  root.classList.toggle("placeholder", !text);
  root.textContent = text || "No generated protocol text yet.";
}

function renderChangeSummary(text) {
  const root = document.getElementById("changeSummary");
  root.classList.toggle("placeholder", !text);
  root.textContent = text || "Graph and protocol changes will appear here after a simulated amendment.";
}

function renderImpactPanel(payload) {
  const root = document.getElementById("impactPanel");
  if (!payload) {
    root.classList.add("placeholder");
    root.textContent = "Impact analysis will appear here.";
    return;
  }
  root.classList.remove("placeholder");
  const sections = (payload.impacted_sections || []).map((section) => `
    <div class="event-item" style="margin-top:10px;">
      <strong>${escapeHtml(section.section_id)} ${escapeHtml(section.section_title)}</strong>
      <div class="event-meta">${escapeHtml(section.severity)} impact</div>
      <div>${escapeHtml(section.impact_reason)}</div>
      <div class="mini-meta" style="margin-top:6px;">${escapeHtml(section.governing_policy || "")}</div>
    </div>
  `).join("");
  const graphEffects = (payload.graph_effects || []).map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  root.innerHTML = `
    <div class="panel-heading">Impact analysis</div>
    <div style="margin-top:8px;">${escapeHtml(payload.summary || "")}</div>
    ${sections}
    ${graphEffects ? `<div class="panel-heading" style="margin-top:12px;">Graph effects</div><ul style="margin:8px 0 0; padding-left:18px;">${graphEffects}</ul>` : ""}
  `;
}

function renderGovernancePanel(payload) {
  const root = document.getElementById("governancePanel");
  if (!payload) {
    root.classList.add("placeholder");
    root.textContent = "Governing and changed sources will appear here.";
    return;
  }
  root.classList.remove("placeholder");
  const governing = (payload.governing_sources || []).map((source) => `
    <div class="event-item" style="margin-top:10px;">
      <strong>${escapeHtml(source.title)}</strong>
      <div class="event-meta">${escapeHtml(source.authority)} &middot; governing source</div>
      <div>${escapeHtml(source.reason)}</div>
    </div>
  `).join("");
  const changed = (payload.changed_sources || []).map((source) => `
    <div class="event-item" style="margin-top:10px;">
      <strong>${escapeHtml(source.title)}</strong>
      <div class="event-meta">${escapeHtml(source.authority)} &middot; changed source</div>
      <div>${escapeHtml(source.reason)}</div>
    </div>
  `).join("");
  root.innerHTML = `
    <div class="panel-heading">Governing sources</div>
    ${governing || "<div class='mini-meta' style='margin-top:8px;'>No governing sources surfaced yet.</div>"}
    <div class="panel-heading" style="margin-top:12px;">Changed sources</div>
    ${changed || "<div class='mini-meta' style='margin-top:8px;'>No changed sources surfaced yet.</div>"}
  `;
}

function renderGraphStats() {
  const manifest = state.graphManifest || {};
  document.getElementById("graphStats").textContent = `${manifest.nodes_total || 0} nodes &middot; ${manifest.edges_total || 0} edges`.replaceAll("&middot;", "·");
}

function classifyNode(node) {
  if (node.node_type === "Claim") return "node-claim";
  if (["SourceDocument", "Organization", "SOP"].includes(node.node_type)) return "node-doc";
  if (["Dose", "VisitInterval", "PolicyRequirement", "RegulatoryConcept", "Entity", "ProtocolSection"].includes(node.node_type)) return "node-entity";
  return "node-container";
}

const GRAPH_LANES = [
  { title: "Sources", types: ["SourceDocument", "Organization", "SOP", "RegulatoryFramework"] },
  { title: "Protocol + Amendments", types: ["Protocol", "Amendment"] },
  { title: "Claims", types: ["Claim"] },
  { title: "Values", types: ["Dose", "VisitInterval", "Entity", "RegulatoryConcept"] },
  { title: "Sections + Policies", types: ["ProtocolSection", "PolicyRequirement"] },
];

const EDGE_STYLES = {
  HAS_CURRENT_VALUE: { color: "#3556e0", width: 2.6, dash: "", label: "current value" },
  SUPERSEDES: { color: "#d97706", width: 2.2, dash: "6 4", label: "supersedes" },
  SUPERSEDED_BY: { color: "#d97706", width: 2.2, dash: "6 4", label: "supersedes" },
  IMPACTS: { color: "#0e9f6e", width: 2.2, dash: "", label: "impacts" },
  GOVERNS: { color: "#7c3aed", width: 1.8, dash: "", label: "governs" },
  GOVERNED_BY: { color: "#7c3aed", width: 1.8, dash: "", label: "governs" },
  AMENDS: { color: "#101828", width: 2.2, dash: "", label: "amends" },
  DEFAULT: { color: "#c2cddd", width: 1.5, dash: "", label: "other link" },
};

function edgeStyle(edgeType) {
  return EDGE_STYLES[edgeType] || EDGE_STYLES.DEFAULT;
}

function laneIndex(node) {
  const index = GRAPH_LANES.findIndex((lane) => lane.types.includes(node.node_type));
  return index === -1 ? 3 : index;
}

function compactLabel(label, limit = 24) {
  const text = String(label || "");
  return text.length > limit ? `${text.slice(0, limit - 1)}…` : text;
}

function renderGraphLegend(usedEdgeTypes, shownNodeCount, totalNodeCount) {
  const root = document.getElementById("graphLegend");
  const seen = new Set();
  const edgeItems = [...usedEdgeTypes]
    .map((type) => edgeStyle(type))
    .filter((style) => (seen.has(style.label) ? false : seen.add(style.label)))
    .map((style) => `
      <span class="legend-item">
        <span class="legend-line ${style.dash ? "dashed" : ""}" style="border-color:${style.color};"></span>
        ${escapeHtml(style.label)}
      </span>
    `)
    .join("");
  const truncationNote = totalNodeCount > shownNodeCount
    ? `<span class="legend-item mini-meta">showing ${shownNodeCount} of ${totalNodeCount} nodes (most relevant to current state)</span>`
    : "";
  root.innerHTML = `
    ${edgeItems}
    <span class="legend-item"><span class="legend-swatch" style="border-color:#3556e0; border-width:2px;"></span> new after amendment</span>
    <span class="legend-item"><span class="legend-swatch" style="border-color:#d97706; border-width:2px; border-style:dashed;"></span> superseded</span>
    ${truncationNote}
  `;
}

function renderGraph() {
  const svg = document.getElementById("graphCanvas");
  const nodes = state.graph.nodes || [];
  const edges = state.graph.edges || [];

  const preferredIds = new Set([
    "protocol_main",
    ...state.claims
      .filter((claim) => claim.normalized_subject === "protocol.current_dose" || claim.normalized_subject === "protocol.visit_interval")
      .slice(-10)
      .map((claim) => `claim_${claim.claim_id}`),
  ]);

  const selectedNodes = nodes.filter((node) =>
    preferredIds.has(node.node_id) ||
    node.node_id.startsWith("dose_") ||
    node.node_id.startsWith("visit_interval_") ||
    node.node_id.startsWith("doc_protocol_") ||
    node.node_id.startsWith("amendment_") ||
    node.node_id.startsWith("section_") ||
    node.node_id.startsWith("policy_")
  ).slice(0, 22);

  const selectedIds = new Set(selectedNodes.map((node) => node.node_id));
  const selectedEdges = edges.filter((edge) => selectedIds.has(edge.source) && selectedIds.has(edge.target)).slice(0, 36);

  const newNodeIds = new Set((state.graphDelta?.added_nodes || []).map((node) => node.node_id));
  const supersededNodeIds = new Set(state.graphDelta?.superseded_node_ids || []);
  const impactNodeIds = new Set(
    selectedEdges
      .filter((edge) => edge.edge_type === "IMPACTS")
      .map((edge) => edge.target)
  );

  const nodeW = 168;
  const nodeH = 62;
  const laneW = 192;
  const rowH = 84;
  const topPad = 40;

  const laneRows = GRAPH_LANES.map(() => 0);
  const positions = new Map();
  selectedNodes.forEach((node) => {
    const lane = laneIndex(node);
    const row = laneRows[lane];
    laneRows[lane] += 1;
    positions.set(node.node_id, {
      x: 16 + lane * laneW,
      y: topPad + row * rowH,
    });
  });

  const maxRows = Math.max(1, ...laneRows);
  const height = Math.max(300, topPad + maxRows * rowH + 12);
  svg.setAttribute("viewBox", `0 0 980 ${height}`);

  const laneLabels = GRAPH_LANES.map((lane, index) => (
    laneRows[index]
      ? `<text x="${16 + index * laneW}" y="22" class="lane-label">${escapeHtml(lane.title)}</text>`
      : ""
  )).join("");

  const usedEdgeTypes = new Set(selectedEdges.map((edge) => edge.edge_type));
  const markerDefs = [...new Set([...usedEdgeTypes].map((type) => edgeStyle(type).color))]
    .map((color) => `
      <marker id="arrow-${color.replace("#", "")}" viewBox="0 0 10 10" refX="9" refY="5"
              markerWidth="6.5" markerHeight="6.5" orient="auto-start-reverse">
        <path d="M 0 1 L 9 5 L 0 9 z" fill="${color}"></path>
      </marker>
    `)
    .join("");

  const edgeSvg = selectedEdges.map((edge) => {
    const a = positions.get(edge.source);
    const b = positions.get(edge.target);
    if (!a || !b) return "";
    const style = edgeStyle(edge.edge_type);
    const leftToRight = a.x <= b.x;
    const x1 = leftToRight ? a.x + nodeW : a.x;
    const x2 = leftToRight ? b.x : b.x + nodeW;
    const y1 = a.y + nodeH / 2;
    const y2 = b.y + nodeH / 2;
    const bend = Math.max(30, Math.abs(x2 - x1) * 0.45);
    const c1 = leftToRight ? x1 + bend : x1 - bend;
    const c2 = leftToRight ? x2 - bend : x2 + bend;
    return `
      <path d="M ${x1} ${y1} C ${c1} ${y1}, ${c2} ${y2}, ${x2} ${y2}"
            fill="none" stroke="${style.color}" stroke-width="${style.width}"
            ${style.dash ? `stroke-dasharray="${style.dash}"` : ""}
            marker-end="url(#arrow-${style.color.replace("#", "")})" opacity="0.9">
        <title>${escapeHtml(edge.edge_type)}</title>
      </path>
    `;
  }).join("");

  const nodeSvg = selectedNodes.map((node) => {
    const pos = positions.get(node.node_id);
    const highlightClass = newNodeIds.has(node.node_id)
      ? "node-new"
      : supersededNodeIds.has(node.node_id)
        ? "node-superseded"
        : impactNodeIds.has(node.node_id)
          ? "node-impact"
          : "";
    const label = String(node.label || "");
    let line1 = label;
    let line2 = "";
    if (label.length > 24) {
      const breakAt = label.lastIndexOf(" ", 24);
      const split = breakAt > 10 ? breakAt : 24;
      line1 = label.slice(0, split);
      line2 = compactLabel(label.slice(split).trimStart(), 24);
    }
    return `
      <g class="graph-node ${classifyNode(node)} ${highlightClass}">
        <title>${escapeHtml(node.node_type)}: ${escapeHtml(node.label)}</title>
        <rect x="${pos.x}" y="${pos.y}" width="${nodeW}" height="${nodeH}" rx="12"></rect>
        <text x="${pos.x + 12}" y="${pos.y + 19}" class="node-type">${escapeHtml(compactLabel(node.node_type, 20))}</text>
        <text x="${pos.x + 12}" y="${pos.y + 36}" class="node-label">${escapeHtml(line1)}</text>
        ${line2 ? `<text x="${pos.x + 12}" y="${pos.y + 51}" class="node-label">${escapeHtml(line2)}</text>` : ""}
      </g>
    `;
  }).join("");

  svg.innerHTML = `
    <defs>${markerDefs}</defs>
    ${laneLabels}
    ${edgeSvg}
    ${nodeSvg}
  `;

  renderGraphLegend(usedEdgeTypes, selectedNodes.length, nodes.length);
}

async function refreshState() {
  const [bootstrapPayload, graphPayload] = await Promise.all([
    api("/api/bootstrap"),
    api("/api/state/graph"),
  ]);
  state.documents = bootstrapPayload.documents || [];
  state.claims = bootstrapPayload.claims || [];
  state.systemEvents = bootstrapPayload.system_events || bootstrapPayload.approval_events || [];
  state.graphManifest = bootstrapPayload.graph_manifest || {};
  state.graph = graphPayload || { nodes: [], edges: [] };
  document.getElementById("draftInput").value = (bootstrapPayload.demo_flawed_draft || {}).text || "";
  renderDocuments();
  renderLedger();
  renderSystemEvents();
  renderGraphStats();
  renderGraph();
  renderImpactPanel(null);
  renderGovernancePanel(null);
}

async function runAction(action) {
  const draftInput = document.getElementById("draftInput").value;
  setStatus("Working…", "working");

  if (action === "current-dose") {
    const payload = await api("/api/actions/current-dose", { method: "POST" });
    renderAnswer("Current fact", payload.answer, "Current Fact", "good");
    renderCitations(payload.citations);
    renderValidationBanner(null);
    renderProtocolPreview("");
    return;
  }

  if (action === "what-changed") {
    const payload = await api("/api/actions/what-changed", { method: "POST" });
    renderAnswer("What changed", payload.answer, "Change Summary", "good");
    renderCitations(payload.citations);
    renderValidationBanner(null);
    renderChangeSummary(payload.answer);
    return;
  }

  if (action === "draft") {
    const payload = await api("/api/actions/draft", { method: "POST" });
    document.getElementById("draftInput").value = payload.text;
    renderAnswer("Generated draft", "Updated protocol text drafted from the active claim state.", "Drafted", "good");
    renderCitations(payload.citations);
    renderValidationBanner(null);
    renderProtocolPreview(payload.text);
    return;
  }

  if (action === "validate") {
    const payload = await api("/api/actions/validate", {
      method: "POST",
      body: JSON.stringify({ text: draftInput, draft_id: "ui_validation_draft" }),
    });
    const passed = payload.status === "pass";
    renderAnswer("Validation", `${payload.issue_count} issue(s) found.`, passed ? "Pass" : "Review", passed ? "good" : "warn");
    renderValidationBanner(payload);
    renderCitations([]);
    return;
  }

  if (action === "impact-map") {
    const payload = await api("/api/actions/impact-map", { method: "POST" });
    renderAnswer("Impact analysis", payload.summary, "Impact Map", "good");
    renderImpactPanel(payload);
    renderGovernancePanel(payload);
    renderValidationBanner(null);
    renderCitations([]);
    return;
  }

  if (action === "current-dose-now") {
    const payload = await api("/api/actions/current-dose-now", { method: "POST" });
    renderAnswer("Updated current fact", payload.answer, "Updated", "good");
    renderCitations(payload.citations);
    renderValidationBanner(null);
    return;
  }

  if (action === "simulate-amendment") {
    const newDoseValue = Number(document.getElementById("newDoseInput").value || "100");
    const payload = await api("/api/actions/simulate-amendment", {
      method: "POST",
      body: JSON.stringify({
        new_dose_mg: newDoseValue,
        note: `Simulated new amendment from UI for ${newDoseValue} mg once daily.`,
      }),
    });
    state.graphDelta = payload.graph_delta;
    renderAnswer("New amendment created", `Dose changed to ${payload.new_dose}. Prior active claim was superseded.`, "Graph Updated", "good");
    renderProtocolPreview(payload.generated_protocol_text);
    renderChangeSummary(`Created ${payload.new_source_id}. New claim ${payload.new_claim_id}.`);
    const delta = document.getElementById("graphDelta");
    delta.classList.remove("placeholder");
    delta.innerHTML = `
      Added ${payload.graph_delta.added_nodes.length} node(s) and ${payload.graph_delta.added_edges.length} edge(s).
      <div class="mini-meta">Superseded claim nodes: ${payload.graph_delta.superseded_node_ids.length}</div>
      <div class="mini-meta">New totals: ${payload.graph_delta.new_nodes_total} nodes · ${payload.graph_delta.new_edges_total} edges</div>
    `;
    renderValidationBanner(null);
    renderCitations([]);
    await refreshState();
    state.graphDelta = payload.graph_delta;
    renderGraph();
    const impactPayload = await api("/api/actions/impact-map", { method: "POST" });
    renderImpactPanel(impactPayload);
    renderGovernancePanel(impactPayload);
    return;
  }

  if (action === "reset-demo") {
    const payload = await api("/api/actions/reset-demo", { method: "POST" });
    state.graphDelta = null;
    await refreshState();
    renderAnswer("Demo reset", payload.message, "Reset", "ready");
    renderProtocolPreview("");
    renderChangeSummary("");
    const delta = document.getElementById("graphDelta");
    delta.classList.add("placeholder");
    delta.textContent = "New graph changes will be shown after each amendment.";
    renderValidationBanner(null);
    renderCitations([]);
    return;
  }
}

let actionInFlight = false;

document.querySelectorAll("[data-action]").forEach((button) => {
  button.addEventListener("click", async () => {
    if (actionInFlight) return;
    actionInFlight = true;
    setBusy(true);
    markActiveAction(button.dataset.action);
    try {
      await runAction(button.dataset.action);
    } catch (error) {
      renderAnswer("Action Error", error.message, "Error", "bad");
    } finally {
      actionInFlight = false;
      setBusy(false);
    }
  });
});

setStatus("Loading…", "working");
refreshState()
  .then(async () => {
    renderAnswer("Ready", "Test current fact retrieval, temporal change handling, drafting, validation, impact analysis, or create a new amendment.", "Ready", "ready");
    // Optional auto-run for demos and screenshot capture, e.g. /?auto=impact-map or
    // /?auto=simulate-amendment,current-dose-now (comma-separated, run in order).
    const auto = new URLSearchParams(window.location.search).get("auto");
    if (auto) {
      for (const action of auto.split(",")) {
        markActiveAction(action);
        await runAction(action.trim());
      }
    }
  })
  .catch((error) => {
    renderAnswer("Bootstrap Error", error.message, "Error", "bad");
  });
