# Early-wall guard against matching timing attackers

Checked 2026-10-31T18:50:36.237826+00:00.

The no-loss claim is REFUTED. The stricter paired improvement claim over the forced-early target is CONFIRMED: 16 improved settings and assignments, 0 regressions. The fixed guard scores 6W/26D/8L; the adaptive delegated target scored 0W/2D/38L, and its forced-early version 6W/10D/24L.

This table includes all twenty timing configurations and both assignments. Each attacker predicts the actual target policy through a private public-state model. Replacing the target therefore also replaces the attacker's model. These are comparisons against a matching-model adversary family, not an ablation against one unchanged opposing policy. The earlier round-three/tier2/defense-first=false draw is repeated in two explicitly labeled control games; the other nineteen settings were new for this fixed guard when declared.

Cells give target outcome, target:attacker HP, ending round, and the total number of attacker roster purchases recorded in its trace. An attacker can decline an unprofitable purchase. A draw with zero purchases does not independently demonstrate survival of the nominal attack.

| Configuration | Adaptive delegate | Forced early delegate | Early-wall guard00 |
|---|---|---|---|
| clone_r3_tier2_df0 | L 656:800 r50; buys 4 | L 704:740 r50; buys 4 | D 800:800 r50; buys 0 |
| clone_r3_tier2_df1 | L 656:800 r50; buys 4 | L 704:740 r50; buys 4 | D 800:800 r50; buys 0 |
| clone_r3_tier3_df0 | L 644:800 r50; buys 1 | W 748:740 r50; buys 1 | W 748:740 r50; buys 1 |
| clone_r3_tier3_df1 | L 644:800 r50; buys 1 | W 748:740 r50; buys 1 | W 748:740 r50; buys 1 |
| clone_r4_tier3_df0 | L 514:800 r50; buys 2 | W 748:740 r50; buys 2 | W 748:740 r50; buys 2 |
| clone_r4_tier3_df1 | L 514:800 r50; buys 2 | D 800:800 r50; buys 0 | D 800:800 r50; buys 0 |
| clone_r4_tier4_df0 | L 440:800 r50; buys 1 | D 740:740 r50; buys 1 | D 740:740 r50; buys 1 |
| clone_r4_tier4_df1 | L 440:800 r50; buys 1 | D 800:800 r50; buys 0 | D 800:800 r50; buys 0 |
| clone_r5_tier3_df0 | L 306:800 r50; buys 4 | L 748:800 r50; buys 2 | L 748:800 r50; buys 2 |
| clone_r5_tier3_df1 | L 306:800 r50; buys 4 | L 748:800 r50; buys 2 | L 748:800 r50; buys 2 |
| clone_r5_tier4_df0 | L 500:800 r50; buys 1 | L 740:800 r50; buys 1 | L 740:800 r50; buys 1 |
| clone_r5_tier4_df1 | L 500:800 r50; buys 1 | L 740:800 r50; buys 1 | L 740:800 r50; buys 1 |
| clone_r6_tier4_df0 | L 80:800 r50; buys 3 | L 740:800 r50; buys 1 | D 800:800 r50; buys 0 |
| clone_r6_tier4_df1 | L 80:800 r50; buys 3 | L 740:800 r50; buys 1 | D 800:800 r50; buys 0 |
| clone_r7_tier4_df0 | L -100:520 r9; buys 5 | L 620:660 r50; buys 3 | D 800:800 r50; buys 0 |
| clone_r7_tier4_df1 | L 440:800 r50; buys 2 | L 740:800 r50; buys 1 | D 800:800 r50; buys 0 |
| clone_r7_tier5_df0 | L -40:520 r9; buys 2 | D 660:660 r50; buys 1 | D 800:800 r50; buys 0 |
| clone_r7_tier5_df1 | D 800:800 r50; buys 0 | D 800:800 r50; buys 0 | D 800:800 r50; buys 0 |
| clone_r8_tier5_df0 | L -40:520 r9; buys 3 | L 660:800 r50; buys 1 | D 800:800 r50; buys 0 |
| clone_r8_tier5_df1 | L 240:800 r50; buys 2 | L 660:800 r50; buys 1 | D 800:800 r50; buys 0 |

All forty new games pass strict accounting, original-engine replay, registered source/data checks, and complete fresh reconstruction of both policies. The new checks reproduce 4000 policy calls and independently verify 2000 attacker predictions and incoming combat results. The guard filters 0 proposed actions before submission; the engine rejects none, and there are no bot errors. All eight predeclared component prefixes pass. Both earlier draw controls reproduce exactly. 20 of twenty assignment pairs have identical normalized complete histories.

The controls are eighty previously audited games. They do not add eighty new executions here. This is targeted development evidence selected after earlier counterexamples, not reserved final validation. It establishes only the finite table and its recorded execution behavior. It does not prove global optimality or load-independent behavior for wall-clock-limited planning.

Full per-game source/result references, attack rounds, outcome transitions and measured decision times are in verification/full_games.json. Reproduce the five manifests listed in early-wall-forecaster-campaigns-001.json using run_data_forecasts, audit_development_strict, replay_audit, audit_data_archives, check_early_wall_histories and check_timing_forecaster_histories. The bounded pipeline log records exact commands. Use the original environment from the project root with disabled bytecode, the research temporary directory, one assigned low-priority core and one numerical thread.
