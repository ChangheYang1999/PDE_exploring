# Five-policy paired development comparison

Recorded: 2026-10-31T11:43:24.784292+00:00

Completed 20 of 20 declared conditions. Candidate outcomes: {'W': 10, 'L': 10}. Attempts: {'valid': 20}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 10; identical normalized histories: 10.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| best_v9b | economy21 | W, 795:785, 50 | W, 795:785, 50 |
| best_v9b | fortress32 | W, 790:785, 50 | W, 790:785, 50 |
| best_v9b | guard_t1 | L, 795:800, 50 | L, 795:800, 50 |
| best_v9b | adaptive_weight4 | L, 765:800, 50 | L, 765:800, 50 |
| economy21 | fortress32 | L, 778:795, 50 | L, 778:795, 50 |
| economy21 | guard_t1 | W, 768:-1337, 21 | W, 768:-1337, 21 |
| economy21 | adaptive_weight4 | L, 768:800, 50 | L, 768:800, 50 |
| fortress32 | guard_t1 | L, 735:788, 50 | L, 735:788, 50 |
| fortress32 | adaptive_weight4 | W, 344:-2297, 39 | W, 344:-2297, 39 |
| guard_t1 | adaptive_weight4 | W, 795:783, 50 | W, 795:783, 50 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/current-policy-game-strict-001.json`, `bot_research/runs/validation/current-policy-game-replay-001.json`.
