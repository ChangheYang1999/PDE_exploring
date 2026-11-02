# Guard handoff timing against the v27 revision

Recorded: 2026-10-31T13:52:34.600463+00:00

Completed 28 of 28 declared conditions. Candidate outcomes: {'L': 18, 'W': 10}. Attempts: {'valid': 28}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 14; identical normalized histories: 14.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5TFU | guard_handoff_r10 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFU | guard_handoff_r11 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFU | guard_handoff_r12 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFU | guard_handoff_r13 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFU | guard_handoff_r14 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFU | guard_handoff_r15 | W, 520:195, 50 | W, 520:195, 50 |
| P5TFU | guard_handoff_r16 | W, 520:-1345, 16 | W, 520:-1345, 16 |
| P5TNU | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNU | guard_handoff_r11 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNU | guard_handoff_r12 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNU | guard_handoff_r13 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNU | guard_handoff_r14 | W, 660:55, 50 | W, 660:55, 50 |
| P5TNU | guard_handoff_r15 | W, 660:-1205, 15 | W, 660:-1205, 15 |
| P5TNU | guard_handoff_r16 | W, 660:-1345, 15 | W, 660:-1345, 15 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/v27-guard-timing-strict-001.json`, `bot_research/runs/validation/v27-guard-timing-replay-001.json`.
