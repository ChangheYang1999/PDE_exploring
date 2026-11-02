# Guarded growth followed by a frozen defender

Recorded: 2026-10-31T13:37:37.776041+00:00

Completed 24 of 24 declared conditions. Candidate outcomes: {'L': 10, 'W': 14}. Attempts: {'valid': 24}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 12; identical normalized histories: 12.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5TF | guard_handoff_r12 | L, 520:755, 50 | L, 520:755, 50 |
| P5TF | guard_handoff_r16 | L, 520:755, 50 | L, 520:755, 50 |
| P5TF | guard_handoff_r19 | L, 520:755, 50 | L, 520:755, 50 |
| P5TF | guard_handoff_r22 | L, 520:755, 50 | L, 520:755, 50 |
| P5Tcurrent | guard_handoff_r12 | W, 520:-775, 20 | W, 520:-775, 20 |
| P5Tcurrent | guard_handoff_r16 | W, 520:-103, 13 | W, 520:-103, 13 |
| P5Tcurrent | guard_handoff_r19 | W, 520:-103, 13 | W, 520:-103, 13 |
| P5Tcurrent | guard_handoff_r22 | W, 520:-103, 13 | W, 520:-103, 13 |
| P5TFullResponse | guard_handoff_r12 | L, 520:755, 50 | L, 520:755, 50 |
| P5TFullResponse | guard_handoff_r16 | W, 520:-1345, 16 | W, 520:-1345, 16 |
| P5TFullResponse | guard_handoff_r19 | W, 520:-1345, 16 | W, 520:-1345, 16 |
| P5TFullResponse | guard_handoff_r22 | W, 520:-1345, 16 | W, 520:-1345, 16 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/guard-handoff-strict-001.json`, `bot_research/runs/validation/guard-handoff-replay-001.json`.
