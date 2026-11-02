# A targeted timing challenge to the HP-triggered grower

Checked 2026-10-31T19:09:35.114445+00:00.

H1, no H loss on the twelve declared matching-model settings in both assignments: REFUTED. H scores 0W/0D/24L in the twenty-four games.

H is unchanged from the completed five-policy table. Each attacker privately models that same H policy from public observations. The six round/tier settings and both defensive orderings were fixed before execution. This directly challenges the scope of the earlier finite-table result; the attackers were not members of that table.

| Attack setting | H outcome | HP H:attacker | End round | Units bought |
|---|---|---|---:|---:|
| r3_tier2_df0 | L | 656:800 | 50 | 4 |
| r3_tier2_df1 | L | 656:800 | 50 | 4 |
| r3_tier3_df0 | L | 644:800 | 50 | 1 |
| r3_tier3_df1 | L | 644:800 | 50 | 1 |
| r4_tier3_df0 | L | 462:800 | 50 | 2 |
| r4_tier3_df1 | L | 462:800 | 50 | 2 |
| r4_tier4_df0 | L | 320:800 | 50 | 1 |
| r4_tier4_df1 | L | 320:800 | 50 | 1 |
| r5_tier3_df0 | L | 150:800 | 50 | 4 |
| r5_tier3_df1 | L | 150:800 | 50 | 4 |
| r5_tier4_df0 | L | 380:800 | 50 | 1 |
| r5_tier4_df1 | L | 380:800 | 50 | 1 |

Each row represents both assignments. 12 of twelve pairs have identical complete canonical histories. All 2400 external policy decisions are freshly regenerated; 1200 additional attacker regenerations verify the saved trace, exact target predictions and original incoming combat. No observation is mutated, no submitted action is rejected, and no bot or source error is recorded. Four prefix components passed before the full games.

Exact prediction is conditional on these reached histories and computations. It does not prove best-response optimality, and repeated deterministic histories are not independent random evidence. The actual attack count is reported even if the attacker declined a nonprofitable or unaffordable purchase. All results, timings, declarations and hashes are retained in verification/full_games.json.

Reproduce the six hp-handoff-forecaster manifests with run_data_forecasts, followed by audit_development_strict, replay_audit, audit_data_archives, check_fixed_game_histories and check_timing_forecaster_histories. The component checker is check_hp_forecast_components. The bounded commands and real timestamps are in runs/validation/hp-handoff-forecaster-001-pipeline.log. Use the supplied environment from the project root with disabled bytecode, research-local temporary files, a free assigned low-priority core and one numerical thread.
