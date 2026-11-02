# Failure-count ablation against guarded handoffs

Recorded: 2026-10-31T13:52:21.893060+00:00

Completed 16 of 16 declared conditions. Candidate outcomes: {'L': 4, 'W': 12}. Attempts: {'valid': 16}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 8; identical normalized histories: 8.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5TNUF3 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUF3 | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| P5TNUF3 | guard_handoff_r14 | W, 660:-103, 12 | W, 660:-103, 12 |
| P5TNUF3 | guard_handoff_r16 | W, 660:-103, 12 | W, 660:-103, 12 |
| P5TNUF4 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUF4 | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| P5TNUF4 | guard_handoff_r14 | W, 660:-103, 12 | W, 660:-103, 12 |
| P5TNUF4 | guard_handoff_r16 | W, 660:-103, 12 | W, 660:-103, 12 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/v27-failure-limit-strict-001.json`, `bot_research/runs/validation/v27-failure-limit-replay-001.json`.
