# Guarded counters against the v26 revision

Recorded: 2026-10-31T13:44:20.143022+00:00

Completed 24 of 24 declared conditions. Candidate outcomes: {'W': 12, 'L': 12}. Attempts: {'valid': 24}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 12; identical normalized histories: 12.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5TN | empty_g6_s4_6 | W, 660:-207, 12 | W, 660:-207, 12 |
| P5TN | g6_screened_r9 | L, 660:755, 50 | L, 660:755, 50 |
| P5TN | guard_handoff_r12 | L, 660:755, 50 | L, 660:755, 50 |
| P5TN | guard_handoff_r16 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNR | empty_g6_s4_6 | W, 660:-207, 12 | W, 660:-207, 12 |
| P5TNR | g6_screened_r9 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNR | guard_handoff_r12 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNR | guard_handoff_r16 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNcurrent | empty_g6_s4_6 | W, 660:-207, 12 | W, 660:-207, 12 |
| P5TNcurrent | g6_screened_r9 | W, 660:-103, 12 | W, 660:-103, 12 |
| P5TNcurrent | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| P5TNcurrent | guard_handoff_r16 | W, 660:-103, 12 | W, 660:-103, 12 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/v26-guard-transfer-strict-001.json`, `bot_research/runs/validation/v26-guard-transfer-replay-001.json`.
