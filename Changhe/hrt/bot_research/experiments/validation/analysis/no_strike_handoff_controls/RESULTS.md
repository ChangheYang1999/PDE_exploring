# Matched no-strike handoff controls

Checked 2026-10-31T15:34:32.411106+00:00.

CONFIRMED: delaying the fixed no-strike handoff from round 6 to round 8 converts losses into wins against P4TNUB and best_v9e. The H8 controls reproduce their HP-triggered reference histories exactly.

Each row represents both physical assignments. Outcomes and HP are from the target perspective. The budget fraction is one-half in every row, and no extra tier4 is bought.

| Target | Counter | Target outcome | HP target:counter | Final round |
|---|---|---|---|---:|
| P4TNUB | nostrike_handoff6_half | W | 800:755 | 50 |
| P4TNUB | nostrike_handoff8_half | L | 660:755 | 50 |
| P5TNUBM | nostrike_handoff6_half | W | 800:755 | 50 |
| P5TNUBM | nostrike_handoff8_half | W | 800:755 | 50 |
| best_v9e | nostrike_handoff6_half | W | 800:755 | 50 |
| best_v9e | nostrike_handoff8_half | L | 660:755 | 50 |

The round-6 and round-8 controls differ only in their handoff deadline. Both lose against P5TNUBM. Against P4TNUB and best_v9e, the earlier defensive policy keeps both players alive but leaves the counter behind 755:800. Continuing its opening until round 8 lets it gain a 755:660 lead that the later defensive policy preserves. This is evidence for the complete deadline intervention under these fixed opponents, not a claim that every two-round delay is beneficial.

The previously audited trigger policy first switches at round 8 against P4TNUB and best_v9e. Its complete normalized trajectory equals the matching fixed-H8 control in all four target-assignment comparisons. Against P5TNUBM the trigger never fires and loses by round 13; its two histories differ from the H8 controls, which lose by the HP comparison at round 50. Thus the trigger does not strictly improve every target's survival or outcome. It is also not needed to obtain the two wins when H8 is known in advance.

All twelve new games pass strict accounting, original-engine replay and source/data checks. Six assignment pairs match exactly, and 600 fresh controller calls reproduce every action without observation mutation, invalid actions or locally filtered proposals. Six earlier trigger games are reused only for the reference comparison; they are not counted as new games. The comparison checks complete actions and states after player/name normalization. No reserved conditions are used.

Reproduce the no-strike-controls manifest through run_data_development and its strict, replay, data and check_budget_handoff_histories checks, then compare_recorded_controls with no-strike-controls-pairs-001.json. Use the project root, .venv/bin/python -B, bytecode disabled, bot_research/tmp, one thread, low priority and assigned affinity.

Audit inputs:

- `bot_research/runs/validation/no-strike-controls-001-strict.json`.
- `bot_research/runs/validation/no-strike-controls-001-replay.json`.
- `bot_research/runs/validation/no-strike-controls-001-summary.json`.
- `bot_research/runs/validation/no-strike-controls-001-data.json`.
- `bot_research/runs/validation/no-strike-controls-001-histories.json`.
- `bot_research/runs/validation/no-strike-controls-comparison-001.json`.
- `bot_research/experiments/validation/no-strike-controls-pairs-001.json`.
- `bot_research/experiments/validation/no-strike-controls-001.json`.
- `bot_research/experiments/validation/analysis/triggered_budget_handoff/verification/full_games.json`.
