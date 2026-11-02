# Public first-roster selection: targets

Checked 2026-10-31T15:53:42.497190+00:00.

CONFIRMED: the adaptive selector scores strictly more wins plus half draws than either fixed branch on this finite set. Counter outcomes: adaptive 14W/2D/0L; early 6W/0D/10L; growth 12W/2D/2L. The selected branch is early in6 games and growth in10 games.

Every table row represents both assignments. Outcome and HP below are from the target perspective, opposite to the counter totals above.

| Target | Mode | Selected branch | First-round tier1 count | Target outcome | HP target:counter | Final round |
|---|---|---|---:|---|---|---:|
| P4TNUB | adaptive | early | 3 | L | 740:755 | 50 |
| P4TNUB | early | early | 3 | L | 740:755 | 50 |
| P4TNUB | growth | growth | 3 | L | 520:755 | 50 |
| P5TNUBM | adaptive | early | 3 | L | 740:755 | 50 |
| P5TNUBM | early | early | 3 | L | 740:755 | 50 |
| P5TNUBM | growth | growth | 3 | W | 800:755 | 50 |
| best_v9e | adaptive | early | 3 | L | 740:755 | 50 |
| best_v9e | early | early | 3 | L | 740:755 | 50 |
| best_v9e | growth | growth | 3 | L | 520:755 | 50 |
| F36 | adaptive | growth | 2 | L | 240:765 | 50 |
| F36 | early | early | 2 | W | 740:-75 | 15 |
| F36 | growth | growth | 2 | L | 240:765 | 50 |
| F37 | adaptive | growth | 2 | L | 520:739 | 50 |
| F37 | early | early | 2 | W | 740:-75 | 15 |
| F37 | growth | growth | 2 | L | 520:739 | 50 |
| lead8 | adaptive | growth | 0 | D | -40:-40 | 8 |
| lead8 | early | early | 0 | W | 500:240 | 50 |
| lead8 | growth | growth | 0 | D | -40:-40 | 8 |
| E25RM | adaptive | growth | 1 | L | -40:618 | 10 |
| E25RM | early | early | 1 | W | 320:-9 | 14 |
| E25RM | growth | growth | 1 | L | -40:618 | 10 |
| E30 | adaptive | growth | 1 | L | -40:618 | 10 |
| E30 | early | early | 1 | W | 320:-9 | 14 |
| E30 | growth | growth | 1 | L | -40:618 | 10 |

All48 declared games pass strict accounting, unchanged-engine replay, immutable source/data verification, public-selection checks and fresh policy regeneration. There are1628 exactly reproduced decisions and264 locally filtered proposals. No invalid action or bot error is submitted. All24 normalized assignment pairs match, and all32 declared complete-history comparisons pass. The adaptive histories equal those of their selected forced branch. For the eight-target experiment the other16 comparisons reproduce the earlier guarded-strike policy exactly.

The feature and threshold were chosen from development histories, and all opponents here are known development policies. This is a finite matched comparison, not an estimate of a population win rate. Equality of repeated decisions was checked empirically because the growth branch and some targets retain wall-clock planner cutoffs. No improvement outside the stated set follows. The selector commits permanently after round1; it can be misled by an opponent that changes its later behavior. Pool C remains unused.

Reproduction: use eachpublic-selector manifest with run_data_development; run the strict, replay, summary, data and check_public_selector_histories audits; then compare_recorded_controls withpublic-selector-control-pairs-001.json. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

- `bot_research/experiments/validation/public-selector-a001.json`.
- `bot_research/runs/validation/public-selector-a001-strict.json`.
- `bot_research/runs/validation/public-selector-a001-replay.json`.
- `bot_research/runs/validation/public-selector-a001-summary.json`.
- `bot_research/runs/validation/public-selector-a001-data.json`.
- `bot_research/runs/validation/public-selector-a001-histories.json`.
- `bot_research/runs/validation/public-selector-a001-opening.json`.
- `bot_research/experiments/validation/public-selector-b001.json`.
- `bot_research/runs/validation/public-selector-b001-strict.json`.
- `bot_research/runs/validation/public-selector-b001-replay.json`.
- `bot_research/runs/validation/public-selector-b001-summary.json`.
- `bot_research/runs/validation/public-selector-b001-data.json`.
- `bot_research/runs/validation/public-selector-b001-histories.json`.
- `bot_research/runs/validation/public-selector-b001-opening.json`.
- `bot_research/experiments/validation/public-selector-c001.json`.
- `bot_research/runs/validation/public-selector-c001-strict.json`.
- `bot_research/runs/validation/public-selector-c001-replay.json`.
- `bot_research/runs/validation/public-selector-c001-summary.json`.
- `bot_research/runs/validation/public-selector-c001-data.json`.
- `bot_research/runs/validation/public-selector-c001-histories.json`.
- `bot_research/runs/validation/public-selector-c001-opening.json`.
- `bot_research/runs/validation/public-selector-controls-001.json`.
- `bot_research/experiments/validation/public-selector-control-pairs-001.json`.
