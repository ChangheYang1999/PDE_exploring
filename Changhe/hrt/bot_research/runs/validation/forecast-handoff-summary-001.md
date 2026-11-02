# Forecast versus visible-only defense after a guarded opening

Recorded: 2026-10-31T14:36:29.181932+00:00

Completed 48 of 48 declared conditions. Candidate outcomes: {'L': 24, 'W': 24}. Attempts: {'valid': 48}.

Every valid attempt passes strict checks and full unchanged-engine replay; trajectory hashes are rechecked here.

Complete assignment pairs: 24; identical normalized histories: 24.

| Candidate | Opponent | Seat 0: outcome, HP, round | Seat 1: outcome, HP, round |
| --- | --- | --- | --- |
| P5TNUB | forecasttrue_r9 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUB | forecastfalse_r9 | W, 660:-3131, 24 | W, 660:-3131, 24 |
| P5TNUB | forecasttrue_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUB | forecastfalse_r10 | W, 660:-49, 14 | W, 660:-49, 14 |
| P5TNUcurrent | forecasttrue_r9 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUcurrent | forecastfalse_r9 | W, 660:-251, 14 | W, 660:-251, 14 |
| P5TNUcurrent | forecasttrue_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUcurrent | forecastfalse_r10 | W, 660:-225, 14 | W, 660:-225, 14 |
| P5TNUF3 | forecasttrue_r9 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUF3 | forecastfalse_r9 | W, 660:-251, 14 | W, 660:-251, 14 |
| P5TNUF3 | forecasttrue_r10 | L, 660:755, 50 | L, 660:755, 50 |
| P5TNUF3 | forecastfalse_r10 | W, 660:-345, 15 | W, 660:-345, 15 |
| F34 | forecasttrue_r9 | W, 240:-507, 15 | W, 240:-507, 15 |
| F34 | forecastfalse_r9 | W, 240:-27, 13 | W, 240:-27, 13 |
| F34 | forecasttrue_r10 | W, 100:-227, 15 | W, 100:-227, 15 |
| F34 | forecastfalse_r10 | W, 100:-357, 14 | W, 100:-357, 14 |
| E25RM | forecasttrue_r9 | W, 240:-12662, 40 | W, 240:-12662, 40 |
| E25RM | forecastfalse_r9 | W, 240:-38, 21 | W, 240:-38, 21 |
| E25RM | forecasttrue_r10 | L, -40:618, 10 | L, -40:618, 10 |
| E25RM | forecastfalse_r10 | L, -40:618, 10 | L, -40:618, 10 |
| rush_t1 | forecasttrue_r9 | L, -40:650, 8 | L, -40:650, 8 |
| rush_t1 | forecastfalse_r9 | L, -40:650, 8 | L, -40:650, 8 |
| rush_t1 | forecasttrue_r10 | L, -40:650, 8 | L, -40:650, 8 |
| rush_t1 | forecastfalse_r10 | L, -40:650, 8 | L, -40:650, 8 |

Exact stated development conditions. Assignment pairs and identical reruns are not independent samples. Timeouts are computational failures, never game losses.

Evidence: `bot_research/runs/validation/forecast-handoff-strict-001.json`, `bot_research/runs/validation/forecast-handoff-replay-001.json`.
