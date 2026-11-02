# Defense and economy ablations against H10 and H12

Recorded: 2026-10-31T14:18:04.966282+00:00

Completed 40 of 40 declared conditions. Candidate outcomes: {'L': 20, 'W': 20}. Attempts: {'valid': 40}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 20; identical normalized histories: 20.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| passive_until_4 | guard_handoff_r10 | L, 520:755, 50 | L, 520:755, 50 |
| passive_until_4 | guard_handoff_r12 | W, 520:-775, 20 | W, 520:-775, 20 |
| passive_until_6 | guard_handoff_r10 | L, 520:651, 50 | L, 520:651, 50 |
| passive_until_6 | guard_handoff_r12 | W, 520:-51, 11 | W, 520:-51, 11 |
| passive_until_7 | guard_handoff_r10 | L, 100:469, 50 | L, 100:469, 50 |
| passive_until_7 | guard_handoff_r12 | W, 100:-285, 11 | W, 100:-285, 11 |
| fortress_n_null | guard_handoff_r10 | L, 660:729, 50 | L, 660:729, 50 |
| fortress_n_null | guard_handoff_r12 | W, 660:417, 50 | W, 660:417, 50 |
| fortress_n_2 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| fortress_n_2 | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| fortress_n_8 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| fortress_n_8 | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| fortress_k_1 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| fortress_k_1 | guard_handoff_r12 | W, 660:391, 50 | W, 660:391, 50 |
| big_partial_false | guard_handoff_r10 | L, 520:573, 50 | L, 520:573, 50 |
| big_partial_false | guard_handoff_r12 | W, 520:27, 50 | W, 520:27, 50 |
| spec_share_0.8 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| spec_share_0.8 | guard_handoff_r12 | W, 660:453, 50 | W, 660:453, 50 |
| spec_share_1.0 | guard_handoff_r10 | L, 660:755, 50 | L, 660:755, 50 |
| spec_share_1.0 | guard_handoff_r12 | W, 660:453, 50 | W, 660:453, 50 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/h10-defense-spending-strict-001.json`, `bot_research/runs/validation/h10-defense-spending-replay-001.json`.
