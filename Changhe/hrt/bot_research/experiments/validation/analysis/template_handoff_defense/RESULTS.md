# Joint construction repairs the two fortress losses

Checked 2026-10-31T15:48:48.707098+00:00.

CONFIRMED: the joint wall/turret planner repairs the F36/F37 transfer losses while preserving the three nominee/best_v9e wins. REFUTED: this intervention beats all eight targets.

Every row represents both physical assignments. Outcome and HP are from the target perspective.

| Target | Counter mode | Outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
| P4TNUB | planner_free | L | 740:755 | 50 | 5 |
| P4TNUB | planner_template | L | 740:755 | 50 | 5 |
| P5TNUBM | planner_free | L | 740:755 | 50 | 5 |
| P5TNUBM | planner_template | L | 740:755 | 50 | 5 |
| best_v9e | planner_free | L | 740:755 | 50 | 5 |
| best_v9e | planner_template | L | 740:755 | 50 | 5 |
| F36 | planner_free | W | 740:-75 | 15 | 5 |
| F36 | planner_template | L | 740:765 | 50 | 5 |
| F37 | planner_free | W | 740:-75 | 15 | 5 |
| F37 | planner_template | L | 740:765 | 50 | 5 |
| lead8 | planner_free | W | 500:240 | 50 | 5 |
| lead8 | planner_template | W | 500:380 | 50 | 5 |
| E25RM | planner_free | W | 320:-9 | 14 | none |
| E25RM | planner_template | W | 320:-9 | 14 | none |
| E30 | planner_free | W | 320:-9 | 14 | none |
| E30 | planner_template | W | 320:-9 | 14 | none |

F36/F37 now lose740:765 at round50. The same targets beat the free planner740:-75 at round15. The joint planner still loses500:380 to lead8 at round50, while the free planner loses500:240. E25RM/E30 again prevent the trigger, so a post-trigger intervention cannot alter their320:-9 round14 wins. These matched complete-policy interventions establish the measured differences; they do not attribute them to one particular wall or turret.

All32 declared games pass strict accounting, original-engine replay, immutable source/data checks and fresh counter regeneration. All16 assignment pairs have identical normalized histories. Fresh instances reproduce 1172 decisions and record 384 locally filtered proposals; no invalid action is submitted and no bot error occurs. All16 control histories exactly match their earlier half-budget guarded-strike counterparts. Repetition verifies reproducibility and is not an independent sample.

The intervention leaves the opening and public HP trigger unchanged. The forecast still covers a finite set of pure-tier purchases and gives no general mixed-roster guarantee. Targets and the inherited growth policies with wall-clock search retain that limitation. These are development conditions on the standard empty start. Pool C is unused.

Reproduce the three template-handoff manifests with run_data_development, then the strict, replay, data and fresh-history checks named by the recorded pipeline. Run from the project root using the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority. The control comparison is compare_recorded_controls with the declared16 pairs.

Audit inputs:

- `bot_research/experiments/validation/template-handoff-a001.json`.
- `bot_research/runs/validation/template-handoff-a001-strict.json`.
- `bot_research/runs/validation/template-handoff-a001-replay.json`.
- `bot_research/runs/validation/template-handoff-a001-summary.json`.
- `bot_research/runs/validation/template-handoff-a001-data.json`.
- `bot_research/runs/validation/template-handoff-a001-histories.json`.
- `bot_research/runs/validation/template-handoff-a001-opening.json`.
- `bot_research/experiments/validation/template-handoff-b001.json`.
- `bot_research/runs/validation/template-handoff-b001-strict.json`.
- `bot_research/runs/validation/template-handoff-b001-replay.json`.
- `bot_research/runs/validation/template-handoff-b001-summary.json`.
- `bot_research/runs/validation/template-handoff-b001-data.json`.
- `bot_research/runs/validation/template-handoff-b001-histories.json`.
- `bot_research/runs/validation/template-handoff-b001-opening.json`.
- `bot_research/experiments/validation/template-handoff-c001.json`.
- `bot_research/runs/validation/template-handoff-c001-strict.json`.
- `bot_research/runs/validation/template-handoff-c001-replay.json`.
- `bot_research/runs/validation/template-handoff-c001-summary.json`.
- `bot_research/runs/validation/template-handoff-c001-data.json`.
- `bot_research/runs/validation/template-handoff-c001-histories.json`.
- `bot_research/runs/validation/template-handoff-c001-opening.json`.
- `bot_research/runs/validation/template-handoff-controls-001.json`.
- `bot_research/experiments/validation/template-handoff-control-pairs-001.json`.
