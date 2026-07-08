# Pilot Annotation Pools

Two independently annotated scenario pools for impact-section and governing-source
judgments, used to check the rule-based impact/governance logic against human gold.

## Annotator

Both pools were labeled by a single annotator with no role in building the system's
rules, blind to any system output. One annotator means no inter-annotator agreement
statistic is available. Do not describe this as "independent annotators" (plural) or
imply agreement statistics exist.

## Composition

- 50 scenarios per pool, across 8 amendment archetypes (dose, eligibility,
  visit-schedule, safety-monitoring, endpoint, informed-consent,
  discontinuation-criteria, drug-interaction), ~6-7 per archetype.
- 10-16 therapeutic areas per pool, so archetypes aren't tied to a single indication.
- Impacted-section choices come from one fixed 20-item section scheme; governing-reference
  choices come from one fixed 8-item reference pool — a constrained, comparable option set
  rather than free-inventing section numbers.
- Each scenario gives real prose for 8 candidate sections, not just section titles, so
  impact judgments require reading actual section content.
- Text is synthetic, modeled on public FDA/EMA/ICH protocol-amendment language and
  structure, not copied from any real trial.

**Known limitation**: within an archetype, all 6-7 scenarios' gold answers are identical
(same section set, same reference set) — surface details vary (dose values, area names)
but not the categorical correct answer. The effective independent sample size per pool is
**~8 (one per archetype)**, each replicated 6-7 times, not 50 independent judgments.

## Files

- `protocol_pool_v1.json` / `annotator_worksheet.md` / `gold_labels_v1.json` — pool 1.
- `heldout_pool_v1.json` / `heldout_annotator_worksheet.md` /
  `heldout_gold_labels_v1.json` — pool 2, non-overlapping with pool 1 (different study
  IDs, areas, phrasing).

## Why two pools

`src/kg_demo/pilot_rule_engine.py` implements deterministic impact/governance rules for
all 8 archetypes, reasoned from general ICH E6(R2)/FDA/EMA protocol-amendment principles.
Those rules were written without consulting pool 1's gold labels, and are scored against
pool 2 instead — a set neither the rule logic nor its scoring process had prior access to
— so the result is a genuine held-out check rather than a fit to already-seen labels.

Score pool 1 against a general LLM baseline: `python scripts/run_pilot_annotation_eval.py`.
Score pool 2 against the rule engine: `python scripts/run_heldout_eval.py`.
