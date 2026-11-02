# Sticky-attack and fortress-gun ablations on three fixed opponents

Recorded: 2026-10-31T13:12:18.688134+00:00

Completed 24 of 24 declared conditions. Candidate outcomes: {'W': 20, 'L': 4}. Attempts: {'valid': 24}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 12; identical normalized histories: 12.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5 | fixed_heavy_drip | W, 375:-1348, 35 | W, 375:-1348, 35 |
| P5 | empty_g6_s4_6 | L, 520:755, 50 | L, 520:755, 50 |
| P5 | forecast_t5_r8 | W, 800:785, 50 | W, 800:785, 50 |
| P5noFG | fixed_heavy_drip | W, 375:-1348, 35 | W, 375:-1348, 35 |
| P5noFG | empty_g6_s4_6 | W, 520:-25, 12 | W, 520:-25, 12 |
| P5noFG | forecast_t5_r8 | L, 660:785, 50 | L, 660:785, 50 |
| P5twoFailures | fixed_heavy_drip | W, 375:-348, 16 | W, 375:-348, 16 |
| P5twoFailures | empty_g6_s4_6 | W, 520:-233, 13 | W, 520:-233, 13 |
| P5twoFailures | forecast_t5_r8 | W, 800:785, 50 | W, 800:785, 50 |
| P5current | fixed_heavy_drip | W, 375:-348, 16 | W, 375:-348, 16 |
| P5current | empty_g6_s4_6 | W, 520:-233, 13 | W, 520:-233, 13 |
| P5current | forecast_t5_r8 | W, 800:785, 50 | W, 800:785, 50 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/sticky-attack-ablation-strict-001.json`, `bot_research/runs/validation/sticky-attack-ablation-replay-001.json`.
