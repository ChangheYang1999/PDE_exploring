# Bait and guard schedules transfer across defenders

Checked 2026-10-31T17:52:29.268585+00:00.

Fortress41 margin reproduction: CONFIRMED. Transfer to at least one of best_v9e, V33C and the adaptive delegated counter: CONFIRMED. All 24 declared conditions are included.

Cells give defender outcome, defender:attacker HP and ending round. Equal physical assignments share a cell; differences are explicit.

| Defender | Schedule A | Schedule B |
|---|---|---|
| fortress41 | L 505:780 r50 | L 505:765 r50 |
| best_v9e | L 85:734 r50 | L 505:755 r50 |
| V33C | L 505:674 r50 | L 505:703 r50 |
| P5TNUBM | L 505:674 r50 | L 505:703 r50 |
| delegated_adaptive | W 350:-40 r8 | W 350:-40 r8 |
| delegated_early | L 350:380 r50 | W 350:296 r50 |

All 2064 freshly regenerated decisions across both policies agree with the recorded action lists. Original-engine replay, complete source/data archives, observation immutability and action legality checks pass. 12 of 12 assignment pairs have identical complete canonical histories. These pairs are reproducibility checks, not independent random samples.

The schedules were proposed in the defense lane and are used here unchanged. Both send three tier1 copies in round two, add guard turrets, buy three tier5 copies in round eight and then construct a splash defense. This test measures transfer of that concrete schedule. It does not show that bait causes each individual defender failure; the full receipt records damage rounds for further diagnosis.

Fortress41 was a known design target. The other five defender specifications were declared here before testing, but all are development targets and none belongs to the reserved validation pool. Teammate planners may use wall-clock limits, so exact repeat agreement is an observed property of these executions.

Reproduce the six bait-guard-transfer manifests with run_data_development, followed by audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories. The complete bounded commands are in runs/validation/bait-guard-transfer-001-pipeline.log. Use the existing Python, disabled bytecode, research temporary directory, assigned affinity, low priority and one numerical thread.
