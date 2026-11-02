# Fixed walls do not repair transfer

Checked 2026-10-31T15:48:47.797451+00:00.

CONFIRMED: both fixed-wall interventions preserve the three nominee/best_v9e wins. REFUTED: either intervention repairs any of the five other transfer targets.

Every row represents both physical assignments. Outcome and HP are from the target perspective.

| Target | Counter mode | Outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
| P4TNUB | walls_none | L | 740:755 | 50 | 5 |
| P4TNUB | walls_stage_a | L | 740:755 | 50 | 5 |
| P4TNUB | walls_full | L | 740:755 | 50 | 5 |
| P5TNUBM | walls_none | L | 740:755 | 50 | 5 |
| P5TNUBM | walls_stage_a | L | 740:755 | 50 | 5 |
| P5TNUBM | walls_full | L | 740:755 | 50 | 5 |
| best_v9e | walls_none | L | 740:755 | 50 | 5 |
| best_v9e | walls_stage_a | L | 740:755 | 50 | 5 |
| best_v9e | walls_full | L | 740:755 | 50 | 5 |
| F36 | walls_none | W | 740:-75 | 15 | 5 |
| F36 | walls_stage_a | W | 740:-635 | 16 | 5 |
| F36 | walls_full | W | 740:-495 | 16 | 5 |
| F37 | walls_none | W | 740:-75 | 15 | 5 |
| F37 | walls_stage_a | W | 740:-635 | 16 | 5 |
| F37 | walls_full | W | 740:-495 | 16 | 5 |
| lead8 | walls_none | W | 500:240 | 50 | 5 |
| lead8 | walls_stage_a | W | 380:240 | 50 | 5 |
| lead8 | walls_full | W | 380:240 | 50 | 5 |
| E25RM | walls_none | W | 320:-9 | 14 | none |
| E25RM | walls_stage_a | W | 320:-9 | 14 | none |
| E25RM | walls_full | W | 320:-9 | 14 | none |
| E30 | walls_none | W | 320:-9 | 14 | none |
| E30 | walls_stage_a | W | 320:-9 | 14 | none |
| E30 | walls_full | W | 320:-9 | 14 | none |

Both wall settings lose to F36/F37 in round16, compared with round15 without walls. They reduce lead8's final HP from500 to380 but still lose380:240. The economy targets prevent the trigger entirely, so all three modes have the same outcome320:-9 at round14. The completed tables do not support a strength improvement from fixed walls.

All48 declared games pass strict accounting, original-engine replay, immutable source/data checks and fresh counter regeneration. All24 assignment pairs have identical normalized histories. Fresh instances reproduce 1556 decisions and record 576 locally filtered proposals; no invalid action is submitted and no bot error occurs. All16 control histories exactly match their earlier half-budget guarded-strike counterparts. Repetition verifies reproducibility and is not an independent sample.

The intervention leaves the opening and public HP trigger unchanged. The forecast still covers a finite set of pure-tier purchases and gives no general mixed-roster guarantee. Targets and the inherited growth policies with wall-clock search retain that limitation. These are development conditions on the standard empty start. Pool C is unused.

Reproduce the three wall-handoff manifests with run_data_development, then the strict, replay, data and fresh-history checks named by the recorded pipeline. Run from the project root using the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority. The control comparison is compare_recorded_controls with the declared16 pairs.

Audit inputs:

- `bot_research/experiments/validation/wall-handoff-a001.json`.
- `bot_research/runs/validation/wall-handoff-a001-strict.json`.
- `bot_research/runs/validation/wall-handoff-a001-replay.json`.
- `bot_research/runs/validation/wall-handoff-a001-summary.json`.
- `bot_research/runs/validation/wall-handoff-a001-data.json`.
- `bot_research/runs/validation/wall-handoff-a001-histories.json`.
- `bot_research/runs/validation/wall-handoff-a001-opening.json`.
- `bot_research/experiments/validation/wall-handoff-b001.json`.
- `bot_research/runs/validation/wall-handoff-b001-strict.json`.
- `bot_research/runs/validation/wall-handoff-b001-replay.json`.
- `bot_research/runs/validation/wall-handoff-b001-summary.json`.
- `bot_research/runs/validation/wall-handoff-b001-data.json`.
- `bot_research/runs/validation/wall-handoff-b001-histories.json`.
- `bot_research/runs/validation/wall-handoff-b001-opening.json`.
- `bot_research/experiments/validation/wall-handoff-c001.json`.
- `bot_research/runs/validation/wall-handoff-c001-strict.json`.
- `bot_research/runs/validation/wall-handoff-c001-replay.json`.
- `bot_research/runs/validation/wall-handoff-c001-summary.json`.
- `bot_research/runs/validation/wall-handoff-c001-data.json`.
- `bot_research/runs/validation/wall-handoff-c001-histories.json`.
- `bot_research/runs/validation/wall-handoff-c001-opening.json`.
- `bot_research/runs/validation/wall-handoff-controls-001.json`.
- `bot_research/experiments/validation/wall-handoff-control-pairs-001.json`.
