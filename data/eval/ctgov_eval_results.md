# Real-Data Evaluation: ClinicalTrials.gov Changed-Module Detection

Task: `ctgov_changed_modules` over **1902** real amendments.
Gold = registry-declared changed modules (non-circular, external).

| Method | Set-F1 | Precision | Recall | N |
| --- | --- | --- | --- | --- |
| Structured state comparison | 0.7798 | 1.0000 | 0.7693 | 1902 |
| Predict-all (naive) | 0.4345 | 0.2989 | 1.0000 | 1902 |

Notes:
- `Structured state comparison` deterministically compares the tracked before/after fields. It is a component-level transfer test, not the full claim-graph system.
- `LLM-over-text` is optional, fail-closed, and reported only when model provenance is present for every evaluated row.
- `Predict-all (naive)` always predicts every module (high recall, low precision).
- This is real, externally-labeled data, so no method saturates at 1.0; the registry marks module changes outside our extracted schema, which bounds recall for any content-based method.
