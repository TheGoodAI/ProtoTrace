# Update Stability Summary

| Method | Current Fact After Updates | Unchanged Visit Stability | Avg Latency ms | Avg Claims Delta | Avg Nodes Delta | Avg Edges Delta |
| --- | --- | --- | --- | --- | --- | --- |
| claim_graph_full | 1.0000 | 1.0000 | 6.4603 | 2.0000 | 3.9825 | 12.9825 |
| local_temporal_proxy | 1.0000 | 1.0000 | 3.1915 | 2.0000 | 3.9825 | 12.9825 |

## Current-Fact Accuracy by Amendment-Chain Depth

| Method | step_1 | step_2 | step_3 | step_4 |
| --- | --- | --- | --- | --- |
| claim_graph_full | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| local_temporal_proxy | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

Interpretation:
- This experiment measures whether methods keep the current dose correct after sequential amendments while leaving unchanged visit state stable.
- The by-depth table is the multi-amendment-stability view: whether each method stays correct deep into a chain (step 3, 4, ...).
- Graph delta columns summarize how much structured state changed per amendment step in the controlled graph pipeline.
