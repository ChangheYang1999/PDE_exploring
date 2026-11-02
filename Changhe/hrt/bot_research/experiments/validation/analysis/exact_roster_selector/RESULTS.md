# Exact-count selector repair

Checked 2026-10-31T16:01:01.269279+00:00.

CONFIRMED: the exact-count predicate repairs the rush_t1 loss and preserves the selected branch histories on the other nineteen development targets.

Counter outcomes: select_exact 32W/8D/0L.

Every row represents both physical assignments. The table gives target outcomes and target-first HP.

| Target | Counter | First-round tier1 | Selected branch | Target outcome | HP target:counter | Final round |
|---|---|---:|---|---|---|---:|
| P4TNUB | select_exact | 3 | early | L | 740:755 | 50 |
| P5TNUBM | select_exact | 3 | early | L | 740:755 | 50 |
| best_v9e | select_exact | 3 | early | L | 740:755 | 50 |
| F36 | select_exact | 2 | growth | L | 240:765 | 50 |
| F37 | select_exact | 2 | growth | L | 520:739 | 50 |
| lead8 | select_exact | 0 | growth | D | -40:-40 | 8 |
| E25RM | select_exact | 1 | growth | L | -40:618 | 10 |
| E30 | select_exact | 1 | growth | L | -40:618 | 10 |
| rush_t1 | select_exact | 6 | growth | L | -40:650 | 8 |
| rush_t2 | select_exact | 0 | growth | L | -40:560 | 8 |
| rush_t3 | select_exact | 0 | growth | L | -40:462 | 8 |
| heavy_t4 | select_exact | 0 | growth | L | -40:800 | 8 |
| eco3_t1 | select_exact | 0 | growth | L | -40:800 | 8 |
| eco5_t1 | select_exact | 0 | growth | L | -40:800 | 8 |
| eco5_t3 | select_exact | 0 | growth | D | -40:-526 | 8 |
| eco6_t5 | select_exact | 0 | growth | D | -40:-40 | 8 |
| splash_t2 | select_exact | 0 | growth | L | -40:728 | 8 |
| splash3_t4 | select_exact | 0 | growth | L | -40:620 | 8 |
| gun_t3 | select_exact | 0 | growth | L | -40:540 | 8 |
| mixed5 | select_exact | 0 | growth | D | -40:-40 | 8 |

The forty new games score32W/8D/0L. The old threshold selector scored30W/8D/2L across the same twenty targets. Fixed early play scored24W/0D/16L and fixed growth30W/8D/2L. Every new history matches its predeclared old forced-branch control exactly. Those controls are reused evidence, not forty further independent samples. The repair was chosen after observing the old rush_t1 failure.

All40 declared games pass strict accounting, original-engine replay, pinned source/data checks and fresh selector regeneration. All748 decisions reproduce exactly; the wrappers locally filter72 proposals, and no invalid action or bot error is submitted. All20 normalized seat pairs and40 complete-history controls match. These are development conditions. The growth planner retains a wall-clock cutoff, so exact repeatability is measured here rather than assumed for arbitrary machine load. Pool C remains unused.

Reproduction uses the declared manifests with run_data_development, the standard strict/replay/source/data audits, check_roster_selector_opening, check_roster_selector_histories and compare_recorded_controls. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

- `bot_research/experiments/validation/exact-selector-a001.json`.
- `bot_research/runs/validation/exact-selector-a001-strict.json`.
- `bot_research/runs/validation/exact-selector-a001-replay.json`.
- `bot_research/runs/validation/exact-selector-a001-summary.json`.
- `bot_research/runs/validation/exact-selector-a001-data.json`.
- `bot_research/runs/validation/exact-selector-a001-histories.json`.
- `bot_research/runs/validation/exact-selector-a001-opening.json`.
- `bot_research/experiments/validation/exact-selector-b001.json`.
- `bot_research/runs/validation/exact-selector-b001-strict.json`.
- `bot_research/runs/validation/exact-selector-b001-replay.json`.
- `bot_research/runs/validation/exact-selector-b001-summary.json`.
- `bot_research/runs/validation/exact-selector-b001-data.json`.
- `bot_research/runs/validation/exact-selector-b001-histories.json`.
- `bot_research/runs/validation/exact-selector-b001-opening.json`.
- `bot_research/experiments/validation/exact-selector-c001.json`.
- `bot_research/runs/validation/exact-selector-c001-strict.json`.
- `bot_research/runs/validation/exact-selector-c001-replay.json`.
- `bot_research/runs/validation/exact-selector-c001-summary.json`.
- `bot_research/runs/validation/exact-selector-c001-data.json`.
- `bot_research/runs/validation/exact-selector-c001-histories.json`.
- `bot_research/runs/validation/exact-selector-c001-opening.json`.
- `bot_research/runs/validation/exact-selector-controls-001.json`.
- `bot_research/experiments/validation/exact-selector-control-pairs-001.json`.
