# Objective-Task Evaluation Summary (non-circular gold)

Impact-section and governing-source F1 are intentionally excluded: their current
gold mirrors the pipeline's own deterministic rules and requires independent human
annotation before any comparative claim can be made.

| Method | Current Fact | Wrong Version | Previous Fact | Dose History | Visit History | Eligibility History | Rule Acc | Citation F1 | Latency ms |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claim_graph_full | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9863 | 6.7551 |
| claim_temporal_only | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7779 | 3.6998 |
| claim_no_governance | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.7779 | 3.4634 |
| claim_no_impact | 1.0000 | 0.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9863 | 3.5965 |
| local_temporal_proxy | 1.0000 | 0.0000 | 0.9667 | 0.0000 | 1.0000 | 1.0000 | 0.1250 | 0.6270 | 1.4034 |
| local_rag_gpt4o | 1.0000 | 0.0000 | 1.0000 | 0.8667 | 0.0000 | 0.0000 | 0.0000 | 0.8742 | 1616.9937 |
| versionrag_style_gpt4o | 1.0000 | 0.0000 | 0.9000 | 0.9667 | 0.0000 | 0.0000 | 0.0000 | 0.8728 | 1882.6806 |
