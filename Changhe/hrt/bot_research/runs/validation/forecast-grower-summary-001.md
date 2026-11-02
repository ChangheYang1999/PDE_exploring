# Forecast-defended growth against adaptive Lead10

Audit summary: 2026-10-31T07:35:03.827049+00:00.

All 16 declared conditions won. The eight reversed-seat pairs have identical normalized complete trajectories. Every completed game passes strict legality/source checks and a full unchanged-engine replay. The two original 120-second timeouts remain in the record; separate 300-second retries completed both conditions. Timeouts are not losses or additional independent games.

| Off-route gun round; first defense round | HP, counter first | End round |
| --- | --- | --- |
| turret0_defend1 | 800:-320 | 10 |
| turret0_defend4 | 755:380 | 50 |
| turret0_defend6 | 725:380 | 50 |
| turret0_defend8 | 645:380 | 50 |
| turret2_defend1 | 800:-40 | 10 |
| turret2_defend4 | 755:520 | 50 |
| turret2_defend6 | 725:-40 | 9 |
| turret2_defend8 | 695:-320 | 9 |

All 476 recorded full-action forecasts were exact. Candidate decision time totaled 389.689 seconds, with a 4.992-second maximum call. Selected match time totaled 791.072 seconds; replay took 32.243 seconds. These shared-machine timings are descriptive.

The policy buys factories through round6, then spends on tier5 waves. Its optional gun1 at (0,11) is placed in round2. Defense uses the exact public-history clone from the stated first defense round. The result confirms these declared counters beat this fixed adaptive setting; it does not isolate whether exact forecasting, defensive spending, or the opening gun is necessary. A no-defense ablation is declared separately after these results.

Evidence: forecast-grower-strict-001.json, forecast-grower-forecast-audit-001.json, forecast-grower-replay-audit-001.json and the companion summary JSON. All paths are relative to this directory.
