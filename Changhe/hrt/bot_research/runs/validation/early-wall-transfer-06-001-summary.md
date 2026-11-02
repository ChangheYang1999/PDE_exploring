# Early-wall policy development

Recorded: 2026-10-31T18:26:20.264219+00:00

Completed 14 of 14 declared conditions. Candidate outcomes: {'W': 8, 'L': 2, 'D': 4}. Attempts: {'valid': 14}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 7; identical normalized histories: 7.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| guard00 | E20 | W, 785:740, 50 | W, 785:740, 50 |
| guard00 | E27 | W, 785:740, 50 | W, 785:740, 50 |
| guard00 | E29 | W, 785:740, 50 | W, 785:740, 50 |
| guard00 | bait_guard_A | L, 365:380, 50 | L, 365:380, 50 |
| guard00 | bait_guard_B | W, 365:360, 50 | W, 365:360, 50 |
| guard00 | delegated_adaptive | D, 740:740, 50 | D, 740:740, 50 |
| guard00 | delegated_early | D, 740:740, 50 | D, 740:740, 50 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/early-wall-transfer-06-001-strict.json`, `bot_research/runs/validation/early-wall-transfer-06-001-replay.json`.
