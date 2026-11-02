# Later purchases behind the same public wall signal

Checked 2026-10-31T19:38:32.390121+00:00.

H1, at least one setting beats J on the exact H-response history: REFUTED.
H2, at least one such setting has a strictly better outcome against J than against I: REFUTED.

All four attackers use the same twenty-wall first move and the same private H model. Only the declared purchase round and tier differ. The settings were selected from earlier successful attacks on wall-free H, after the nineteen-wall tier2 attack had lost its six games. This is targeted development, with no claim that the grid was sampled at random.

| Setting | Opponent | Attacker result | HP attacker:opponent | End round | Units bought | Forecast mismatch count |
|---|---|---|---|---:|---:|---:|
| r3_tier3 | J | L | -40:670 | 9 | 1 | 0 |
| r3_tier3 | H | L | -40:670 | 9 | 1 | 0 |
| r3_tier3 | I | L | 752:774 | 50 | 1 | 47 |
| r4_tier3 | J | L | -40:410 | 8 | 3 | 0 |
| r4_tier3 | H | L | -40:410 | 8 | 3 | 0 |
| r4_tier3 | I | L | 704:722 | 50 | 3 | 48 |
| r4_tier4 | J | L | -40:560 | 9 | 1 | 0 |
| r4_tier4 | H | L | -40:560 | 9 | 1 | 0 |
| r4_tier4 | I | L | 704:740 | 50 | 1 | 48 |
| r5_tier4 | J | L | -40:320 | 8 | 2 | 0 |
| r5_tier4 | H | L | -40:320 | 8 | 2 | 0 |
| r5_tier4 | I | W | 752:740 | 50 | 1 | 47 |

Every displayed row represents both physical assignments, with identical normalized histories. All 24 full games pass strict accounting, original-engine replay, archived-source and data checks, 1072 fresh external decisions and 536 additional attacker/forecast checks. The 24 prefix cases passed first. There were no submitted rejections, bot errors, source drift or mutated observations.

Every J history exactly matches the corresponding H history. The private H forecasts agree against both targets; mismatches against I are retained. This confirms the selected response but does not by itself establish an exploit. The same attacker against I is the control for attributing an outcome difference to that response choice.

Winning settings against J: none. Settings whose outcome against J exceeds their outcome against I: none.

The results cover this declared grid only. A refuted hypothesis leaves other signal designs and purchase schedules open. The inherited branch proof assumes the observed common first move and correctly advanced private state; wall-clock-dependent choices outside the checked histories are not covered. Neither these policies nor their outcomes are used in pool D. Full timings, sources and commands are retained in the four manifests, verification/full_games.json and runs/validation/wall-signal-delayed-001-pipeline.log.
