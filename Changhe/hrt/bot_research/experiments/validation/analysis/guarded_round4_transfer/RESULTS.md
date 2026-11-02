# Guarded-strike transfer is limited

Checked 2026-10-31T15:39:47.425291+00:00.

CONFIRMED: both guarded round-four settings beat best_v9e by 15 HP in both assignments. REFUTED: either fixed setting also beats the five other declared targets.

Each row represents both assignments, with outcome and HP from the target perspective.

| Target | Counter | Target outcome | HP target:counter | Final round | Handoff |
|---|---|---|---|---:|---:|
| F36 | earlygun1_budget1of2 | W | 740:-75 | 15 | 5 |
| F36 | earlygun1_budget1of1 | W | 740:-67 | 25 | 5 |
| F37 | earlygun1_budget1of2 | W | 740:-75 | 15 | 5 |
| F37 | earlygun1_budget1of1 | W | 740:-67 | 25 | 5 |
| best_v9e | earlygun1_budget1of2 | L | 740:755 | 50 | 5 |
| best_v9e | earlygun1_budget1of1 | L | 740:755 | 50 | 5 |
| lead8 | earlygun1_budget1of2 | W | 500:240 | 50 | 5 |
| lead8 | earlygun1_budget1of1 | W | 500:-40 | 9 | 5 |
| E25RM | earlygun1_budget1of2 | W | 320:-9 | 14 | none |
| E25RM | earlygun1_budget1of1 | W | 320:-9 | 14 | none |
| E30 | earlygun1_budget1of2 | W | 320:-9 | 14 | none |
| E30 | earlygun1_budget1of1 | W | 320:-9 | 14 | none |

The early strike preserves its 755:740 win against the installed best_v9e, whose exact source is pinned in the declaration. It also gains an early lead against F36 and F37, but their later attacks defeat the budget defender. The two fortress versions have the same complete recorded outcomes here. Both economy targets stop the early strike and later win320:-9 in round14; the public lead trigger never fires. Against lead8 it does fire, but the defense later leaks. Using the whole public budget is not uniformly better than using half: against lead8 it dies in round9, whereas the half-budget policy survives to round50 but still loses.

All24 games pass strict accounting, original-engine replay, source/data archive checks and fresh counter regeneration. All12 assignment pairs have identical normalized histories. The checker reproduces 590 decisions, verifies all public triggers and records 288 locally filtered proposals. No invalid action is submitted and no bot error occurs. The fortress planners retain wall-clock limits; these agreements do not prove load independence.

These are the six named transfer targets, without retuning between them. The original two nominee wins remain valid but do not establish general dominance. Player swaps are reproducibility controls, not independent samples. Pool C remains unused.

Reproduce guarded-transfer-a001/b001/c001 with run_data_development and the strict, replay, data and check_guarded_round4_histories audits. Run from the project root with .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

- `bot_research/runs/validation/guarded-transfer-a001-strict.json`.
- `bot_research/runs/validation/guarded-transfer-a001-replay.json`.
- `bot_research/runs/validation/guarded-transfer-a001-summary.json`.
- `bot_research/runs/validation/guarded-transfer-a001-data.json`.
- `bot_research/runs/validation/guarded-transfer-a001-histories.json`.
- `bot_research/runs/validation/guarded-transfer-a001-opening.json`.
- `bot_research/experiments/validation/guarded-transfer-a001.json`.
- `bot_research/runs/validation/guarded-transfer-b001-strict.json`.
- `bot_research/runs/validation/guarded-transfer-b001-replay.json`.
- `bot_research/runs/validation/guarded-transfer-b001-summary.json`.
- `bot_research/runs/validation/guarded-transfer-b001-data.json`.
- `bot_research/runs/validation/guarded-transfer-b001-histories.json`.
- `bot_research/runs/validation/guarded-transfer-b001-opening.json`.
- `bot_research/experiments/validation/guarded-transfer-b001.json`.
- `bot_research/runs/validation/guarded-transfer-c001-strict.json`.
- `bot_research/runs/validation/guarded-transfer-c001-replay.json`.
- `bot_research/runs/validation/guarded-transfer-c001-summary.json`.
- `bot_research/runs/validation/guarded-transfer-c001-data.json`.
- `bot_research/runs/validation/guarded-transfer-c001-histories.json`.
- `bot_research/runs/validation/guarded-transfer-c001-opening.json`.
- `bot_research/experiments/validation/guarded-transfer-c001.json`.
