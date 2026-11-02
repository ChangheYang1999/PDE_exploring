# Public first-roster selection: baselines

Checked 2026-10-31T15:53:42.884239+00:00.

REFUTED: the adaptive selector scores strictly more wins plus half draws than either fixed branch on this finite set. Counter outcomes: adaptive 16W/6D/2L; early 18W/0D/6L; growth 18W/6D/0L. The selected branch is early in2 games and growth in22 games.

Every table row represents both assignments. Outcome and HP below are from the target perspective, opposite to the counter totals above.

| Target | Mode | Selected branch | First-round tier1 count | Target outcome | HP target:counter | Final round |
|---|---|---|---:|---|---|---:|
| rush_t1 | adaptive | early | 6 | W | 80:-305 | 8 |
| rush_t1 | early | early | 6 | W | 80:-305 | 8 |
| rush_t1 | growth | growth | 6 | L | -40:650 | 8 |
| rush_t2 | adaptive | growth | 0 | L | -40:560 | 8 |
| rush_t2 | early | early | 0 | L | -260:248 | 9 |
| rush_t2 | growth | growth | 0 | L | -40:560 | 8 |
| rush_t3 | adaptive | growth | 0 | L | -40:462 | 8 |
| rush_t3 | early | early | 0 | L | -180:514 | 10 |
| rush_t3 | growth | growth | 0 | L | -40:462 | 8 |
| heavy_t4 | adaptive | growth | 0 | L | -40:800 | 8 |
| heavy_t4 | early | early | 0 | L | 80:680 | 50 |
| heavy_t4 | growth | growth | 0 | L | -40:800 | 8 |
| eco3_t1 | adaptive | growth | 0 | L | -40:800 | 8 |
| eco3_t1 | early | early | 0 | W | 420:-410 | 7 |
| eco3_t1 | growth | growth | 0 | L | -40:800 | 8 |
| eco5_t1 | adaptive | growth | 0 | L | -40:800 | 8 |
| eco5_t1 | early | early | 0 | L | 80:800 | 50 |
| eco5_t1 | growth | growth | 0 | L | -40:800 | 8 |
| eco5_t3 | adaptive | growth | 0 | D | -40:-526 | 8 |
| eco5_t3 | early | early | 0 | L | 80:696 | 50 |
| eco5_t3 | growth | growth | 0 | D | -40:-526 | 8 |
| eco6_t5 | adaptive | growth | 0 | D | -40:-40 | 8 |
| eco6_t5 | early | early | 0 | W | 440:-40 | 9 |
| eco6_t5 | growth | growth | 0 | D | -40:-40 | 8 |
| splash_t2 | adaptive | growth | 0 | L | -40:728 | 8 |
| splash_t2 | early | early | 0 | L | 80:764 | 50 |
| splash_t2 | growth | growth | 0 | L | -40:728 | 8 |
| splash3_t4 | adaptive | growth | 0 | L | -40:620 | 8 |
| splash3_t4 | early | early | 0 | L | 80:200 | 50 |
| splash3_t4 | growth | growth | 0 | L | -40:620 | 8 |
| gun_t3 | adaptive | growth | 0 | L | -40:540 | 8 |
| gun_t3 | early | early | 0 | L | 80:384 | 50 |
| gun_t3 | growth | growth | 0 | L | -40:540 | 8 |
| mixed5 | adaptive | growth | 0 | D | -40:-40 | 8 |
| mixed5 | early | early | 0 | L | 80:680 | 50 |
| mixed5 | growth | growth | 0 | D | -40:-40 | 8 |

All72 declared games pass strict accounting, unchanged-engine replay, immutable source/data verification, public-selection checks and fresh policy regeneration. There are1170 exactly reproduced decisions and312 locally filtered proposals. No invalid action or bot error is submitted. All36 normalized assignment pairs match, and all24 declared complete-history comparisons pass. The adaptive histories equal those of their selected forced branch. For the eight-target experiment the other16 comparisons reproduce the earlier guarded-strike policy exactly.

The feature and threshold were chosen from development histories, and all opponents here are known development policies. This is a finite matched comparison, not an estimate of a population win rate. Equality of repeated decisions was checked empirically because the growth branch and some targets retain wall-clock planner cutoffs. No improvement outside the stated set follows. The selector commits permanently after round1; it can be misled by an opponent that changes its later behavior. Pool C remains unused.

Reproduction: use eachselector-baselines manifest with run_data_development; run the strict, replay, summary, data and check_public_selector_histories audits; then compare_recorded_controls withselector-baselines-control-pairs-001.json. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

- `bot_research/experiments/validation/selector-baselines-a001.json`.
- `bot_research/runs/validation/selector-baselines-a001-strict.json`.
- `bot_research/runs/validation/selector-baselines-a001-replay.json`.
- `bot_research/runs/validation/selector-baselines-a001-summary.json`.
- `bot_research/runs/validation/selector-baselines-a001-data.json`.
- `bot_research/runs/validation/selector-baselines-a001-histories.json`.
- `bot_research/runs/validation/selector-baselines-a001-opening.json`.
- `bot_research/experiments/validation/selector-baselines-b001.json`.
- `bot_research/runs/validation/selector-baselines-b001-strict.json`.
- `bot_research/runs/validation/selector-baselines-b001-replay.json`.
- `bot_research/runs/validation/selector-baselines-b001-summary.json`.
- `bot_research/runs/validation/selector-baselines-b001-data.json`.
- `bot_research/runs/validation/selector-baselines-b001-histories.json`.
- `bot_research/runs/validation/selector-baselines-b001-opening.json`.
- `bot_research/experiments/validation/selector-baselines-c001.json`.
- `bot_research/runs/validation/selector-baselines-c001-strict.json`.
- `bot_research/runs/validation/selector-baselines-c001-replay.json`.
- `bot_research/runs/validation/selector-baselines-c001-summary.json`.
- `bot_research/runs/validation/selector-baselines-c001-data.json`.
- `bot_research/runs/validation/selector-baselines-c001-histories.json`.
- `bot_research/runs/validation/selector-baselines-c001-opening.json`.
- `bot_research/runs/validation/selector-baselines-controls-001.json`.
- `bot_research/experiments/validation/selector-baselines-control-pairs-001.json`.
