# Indistinguishable public-prefix challenge

Recorded: 2026-10-31T16:44:03.135235+00:00

Completed 8 of 8 declared conditions. Candidate outcomes: {'L': 6, 'W': 2}. Attempts: {'valid': 8}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 4; identical normalized histories: 4.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| baseline | emergency_damage | L, 740:800, 50 | L, 740:800, 50 |
| baseline | emergency_none | L, 740:800, 50 | L, 740:800, 50 |
| flood | emergency_damage | L, 80:715, 50 | L, 80:715, 50 |
| flood | emergency_none | W, 420:-495, 7 | W, 420:-495, 7 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/emergency-prefix-001-strict.json`, `bot_research/runs/validation/emergency-prefix-001-replay.json`.
