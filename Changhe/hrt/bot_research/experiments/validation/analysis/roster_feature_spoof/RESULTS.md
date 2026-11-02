# Adversarial first-round roster changes

Checked 2026-10-31T16:05:24.034989+00:00.

CONFIRMED: a declared change of opening count makes a selector lose while its alternative fixed branch wins.

Counter outcomes: select_adaptive 2W/0D/6L; select_exact 4W/0D/4L; select_early 6W/0D/2L; select_growth 2W/0D/6L.

Every row represents both physical assignments. The table gives target outcomes and target-first HP.

| Target | Counter | First-round tier1 | Selected branch | Target outcome | HP target:counter | Final round |
|---|---|---:|---|---|---|---:|
| P5M_poke0 | select_adaptive | 0 | growth | W | 800:566 | 50 |
| P5M_poke0 | select_exact | 0 | growth | W | 800:566 | 50 |
| P5M_poke0 | select_early | 0 | early | L | 740:800 | 50 |
| P5M_poke0 | select_growth | 0 | growth | W | 800:566 | 50 |
| P5M_poke2 | select_adaptive | 2 | growth | W | 800:692 | 50 |
| P5M_poke2 | select_exact | 2 | growth | W | 800:692 | 50 |
| P5M_poke2 | select_early | 2 | early | L | 740:770 | 50 |
| P5M_poke2 | select_growth | 2 | growth | W | 800:692 | 50 |
| P5M_poke3 | select_adaptive | 3 | early | L | 740:755 | 50 |
| P5M_poke3 | select_exact | 3 | early | L | 740:755 | 50 |
| P5M_poke3 | select_early | 3 | early | L | 740:755 | 50 |
| P5M_poke3 | select_growth | 3 | growth | W | 800:755 | 50 |
| P5M_poke4 | select_adaptive | 4 | early | W | 740:-184 | 12 |
| P5M_poke4 | select_exact | 4 | growth | L | 660:740 | 50 |
| P5M_poke4 | select_early | 4 | early | W | 740:-184 | 12 |
| P5M_poke4 | select_growth | 4 | growth | L | 660:740 | 50 |

Qualifying controlled counterexamples: [{"alternative": "select_early", "alternative_hp_target_first": [740, 800], "hp_target_first": [800, 566], "selected": "growth", "selector": "select_adaptive", "target": "P5M_poke0"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 800], "hp_target_first": [800, 566], "selected": "growth", "selector": "select_exact", "target": "P5M_poke0"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 770], "hp_target_first": [800, 692], "selected": "growth", "selector": "select_adaptive", "target": "P5M_poke2"}, {"alternative": "select_early", "alternative_hp_target_first": [740, 770], "hp_target_first": [800, 692], "selected": "growth", "selector": "select_exact", "target": "P5M_poke2"}, {"alternative": "select_growth", "alternative_hp_target_first": [660, 740], "hp_target_first": [740, -184], "selected": "early", "selector": "select_adaptive", "target": "P5M_poke4"}]. Each adaptive history matches its selected forced branch, and all six count3 default-control histories reproduce the earlier nominee experiment. The opening changes also change income and damage; the claim is the measured complete-policy comparison, not a pure isolated effect of the displayed count.

All32 declared games pass strict accounting, original-engine replay, pinned source/data checks and fresh selector regeneration. All1448 decisions reproduce exactly; the wrappers locally filter168 proposals, and no invalid action or bot error is submitted. All16 normalized seat pairs and22 complete-history controls match. These are development conditions. The growth planner retains a wall-clock cutoff, so exact repeatability is measured here rather than assumed for arbitrary machine load. Pool C remains unused.

Reproduction uses the declared manifests with run_data_development, the standard strict/replay/source/data audits, check_roster_selector_opening, check_roster_selector_histories and compare_recorded_controls. Run from the project root with the supplied Python environment, bytecode disabled, bot_research/tmp, one thread, assigned affinity and low priority.

Audit inputs:

- `bot_research/experiments/validation/roster-spoof-001.json`.
- `bot_research/runs/validation/roster-spoof-001-strict.json`.
- `bot_research/runs/validation/roster-spoof-001-replay.json`.
- `bot_research/runs/validation/roster-spoof-001-summary.json`.
- `bot_research/runs/validation/roster-spoof-001-data.json`.
- `bot_research/runs/validation/roster-spoof-001-histories.json`.
- `bot_research/runs/validation/roster-spoof-001-opening.json`.
- `bot_research/runs/validation/roster-spoof-controls-001.json`.
- `bot_research/experiments/validation/roster-spoof-control-pairs-001.json`.
