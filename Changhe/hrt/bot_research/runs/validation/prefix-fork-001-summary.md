# Indistinguishable public-prefix challenge

Recorded: 2026-10-31T16:39:45.116534+00:00

Completed 12 of 12 declared conditions. Candidate outcomes: {'L': 6, 'W': 6}. Attempts: {'valid': 12}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 6; identical normalized histories: 6.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| baseline | route_adaptive | L, 740:800, 50 | L, 740:800, 50 |
| baseline | route_early | L, 740:800, 50 | L, 740:800, 50 |
| baseline | route_growth | W, 800:566, 50 | W, 800:566, 50 |
| flood | route_adaptive | W, 420:-495, 7 | W, 420:-495, 7 |
| flood | route_early | W, 420:-495, 7 | W, 420:-495, 7 |
| flood | route_growth | L, -40:800, 8 | L, -40:800, 8 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/prefix-fork-001-strict.json`, `bot_research/runs/validation/prefix-fork-001-replay.json`.
