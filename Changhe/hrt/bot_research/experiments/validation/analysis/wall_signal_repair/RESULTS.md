# Full-policy test of the defensive repair

Checked 2026-10-31T19:45:57.830536+00:00.

H1 L wins against J on the exact H-control history: CONFIRMED.
H2 L has a better outcome against J than against I: CONFIRMED.

Six new standard-start games follow the fixed pre-call clarification in PROOF.md. Six K20 games are explicitly reused old controls, selected after their losses and the one-round feasibility diagnosis. This is development evidence, not held-out validation.

| Opponent | K20 result, HP, round | L result, HP, round | First repair | Repairs |
|---|---|---|---:|---:|
| J | L, -40:656, 9 | W, 800:656, 50 | 7 | 5 |
| H | L, -40:656, 9 | W, 800:656, 50 | 7 | 5 |
| I | D, 752:752, 50 | D, 752:752, 50 | 8 | 1 |

Each row represents both assignments, whose full normalized histories are identical. All six new games pass strict accounting, original-engine replay, source/data checks, 600 fresh external decisions, and 300 extra attacker/forecast checks. The six prefix cases passed before full games. All old/new histories are equal before the first selected repair. There are no submitted rejections, bot errors, source drift or observation mutations.

The public selector chooses H, and its complete histories equal the fixed H controls. Forecast mismatches against I are retained in verification/full_games.json. A local damage reduction does not prove long-horizon optimality, and these three opponents do not certify a general best response. The policy uses public observations and its own private clone only; no installed best.py or pool D data is used.
