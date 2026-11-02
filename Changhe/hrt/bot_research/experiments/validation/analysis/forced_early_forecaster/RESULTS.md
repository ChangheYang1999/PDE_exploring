# Forced early branch against matching public clones

Checked 2026-10-31T17:45:56.080536+00:00.

The paired repair claim is CONFIRMED: 14 old target losses become nonlosses, with 0 W/D/L regressions. The stricter no-target-loss claim is REFUTED.

From the target counter's perspective, adaptive mode scores 0W/2D/38L; forced early scores 6W/10D/24L. There are 14 improved conditions. All twenty timing configurations and both assignments are included. The attacker forecasts the corresponding mode in each experiment, so this comparison changes both the target's branch policy and the attacker's correct private model. It does not pretend that a stale forecast is an exact one.

Each cell gives target outcome, HP target:attacker, final round and first delegate round. None means the delegate was never called. Equal physical assignments share a cell.

| Attacker configuration | Adaptive target | Forced early target |
|---|---|---|
| clone_r3_tier2_df0 | L 656:800 r50, handoff None | L 704:740 r50, handoff 5 |
| clone_r3_tier2_df1 | L 656:800 r50, handoff None | L 704:740 r50, handoff 5 |
| clone_r3_tier3_df0 | L 644:800 r50, handoff None | W 748:740 r50, handoff 5 |
| clone_r3_tier3_df1 | L 644:800 r50, handoff None | W 748:740 r50, handoff 5 |
| clone_r4_tier3_df0 | L 514:800 r50, handoff None | W 748:740 r50, handoff 5 |
| clone_r4_tier3_df1 | L 514:800 r50, handoff None | D 800:800 r50, handoff None |
| clone_r4_tier4_df0 | L 440:800 r50, handoff None | D 740:740 r50, handoff 5 |
| clone_r4_tier4_df1 | L 440:800 r50, handoff None | D 800:800 r50, handoff None |
| clone_r5_tier3_df0 | L 306:800 r50, handoff None | L 748:800 r50, handoff 6 |
| clone_r5_tier3_df1 | L 306:800 r50, handoff None | L 748:800 r50, handoff 6 |
| clone_r5_tier4_df0 | L 500:800 r50, handoff None | L 740:800 r50, handoff 6 |
| clone_r5_tier4_df1 | L 500:800 r50, handoff None | L 740:800 r50, handoff 6 |
| clone_r6_tier4_df0 | L 80:800 r50, handoff None | L 740:800 r50, handoff 7 |
| clone_r6_tier4_df1 | L 80:800 r50, handoff None | L 740:800 r50, handoff 7 |
| clone_r7_tier4_df0 | L -100:520 r9, handoff None | L 620:660 r50, handoff 8 |
| clone_r7_tier4_df1 | L 440:800 r50, handoff None | L 740:800 r50, handoff 8 |
| clone_r7_tier5_df0 | L -40:520 r9, handoff None | D 660:660 r50, handoff 8 |
| clone_r7_tier5_df1 | D 800:800 r50, handoff None | D 800:800 r50, handoff None |
| clone_r8_tier5_df0 | L -40:520 r9, handoff None | L 660:800 r50, handoff 9 |
| clone_r8_tier5_df1 | L 240:800 r50, handoff None | L 660:800 r50, handoff 9 |

All eighty underlying games pass strict accounting, original-engine replay, registered-source/data checks and exact actual forecast diagnostics. Four component prefixes passed 32 reached rounds before the new game manifests. Fresh checks reproduce 2000 new target and 2000 new attacker decisions, plus 1754 corresponding adaptive target and attacker decisions. Every submitted action is legal, observations remain unchanged, and original incoming damage agrees with forecast residuals. Independent handoff reconstruction agrees in every reached round. All forty paired histories are exactly equal through round three after removing only the run identifier.

These are deterministic targeted development conditions, not independent samples or reserved final validation. The complete transition table, attack counts, handoff rounds and measured low-priority decision times are in verification/full_games.json. Exact reproduction on these histories does not establish load-independent behavior for planners with wall-clock cutoffs. This experiment does not modify the installed best bot.

Reproduce the five forced-early-forecaster manifests with run_data_forecasts and the audit sequence in their pipeline log. The comparison also needs the five adaptive Fortress 38 campaigns from delegated_forecaster version 002. Use the original project environment, disabled bytecode, the research temporary directory, fixed affinity, one numerical thread and low priority.
