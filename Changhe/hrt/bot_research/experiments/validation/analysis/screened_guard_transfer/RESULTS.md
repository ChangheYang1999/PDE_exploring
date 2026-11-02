# Screened-guard transfer

Completed 2026-10-31T20:32:04.962318+00:00.

H1, the guard wins both AS1C assignments: **REFUTED**. H2, the guard never worsens W/D/L relative to its matched control: **CONFIRMED**.

| Opponent | Guard, seat 0 | Control, seat 0 | Guard, seat 1 | Control, seat 1 |
| --- | --- | --- | --- | --- |
| AS1C | L 380:774 r50 | L 644:774 r50 | L 380:774 r50 | L 644:774 r50 |
| AS1 | L 380:774 r50 | L 644:774 r50 | L 380:774 r50 | L 644:774 r50 |
| best_v9f | L 740:800 r50 | L -4:800 r12 | L 740:800 r50 | L -4:800 r12 |
| Fortress41 | L 660:800 r50 | L -66:800 r11 | L 660:800 r50 | L -66:800 r11 |
| V29_g1 | L 560:800 r50 | L 490:800 r50 | L 560:800 r50 | L 490:800 r50 |
| V29_guard60 | D 800:800 r50 | L 774:800 r50 | D 800:800 r50 | L 774:800 r50 |

All 24 new games pass strict accounting, original-engine replay, source/archive checks and 2092 fresh policy calls. 12 of 12 assignment pairs have identical normalized histories.

The opponent set and both policies were fixed before these games. The guard was selected against best_v9e earlier; this transfer set consists of known development finalists and a newly proposed attack-budget variant. It does not estimate performance against an untouched opponent distribution. Final best.py and pool D are unchanged. The Fortress search includes a wall-clock cutoff, so exact reproduction here does not promise timing-invariant behavior on other runs.
