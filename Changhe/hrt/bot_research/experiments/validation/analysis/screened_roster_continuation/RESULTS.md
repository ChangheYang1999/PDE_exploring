# Screened roster continuation results

Completed 2026-10-31T20:15:49.830727+00:00.

H1 (a screened complete policy wins both seats): **REFUTED**. H2 (screened order strictly improves final HP margin for every continuation): **REFUTED**.

All18 games completed with zero failed or invalid attempts. Strict accounting, original-engine replay, source archives and 900 fresh policy calls pass. All nine assignment pairs have identical normalized histories. Every round1-5 history and every target round6 action is identical across the18 games and matches the original selected C02 witness.

Round6 always leaves the counter at774HP. The target is at774HP after the screened order and800HP after either control ordering. The equal-cost order intervention therefore has the predicted immediate effect.

| Continuation | Order | Counter outcome | Final HP | Round |
| --- | --- | --- | --- | --- |
| original | screen | L | -240:774 | 12 |
| original | middle | L | -266:800 | 12 |
| original | front | L | -266:800 | 12 |
| fortress38 | screen | D | 774:774 | 50 |
| fortress38 | middle | L | 774:800 | 50 |
| fortress38 | front | L | 774:800 | 50 |
| economy20 | screen | L | -486:774 | 13 |
| economy20 | middle | L | -206:800 | 13 |
| economy20 | front | L | -206:800 | 13 |

Both seats agree on every table entry. Later outcomes include the opponent response and continuation behavior; the one-round ordering effect alone does not determine the winner. These are selected development tests, and no terminal D condition was used. The frozen Fortress38 planner retains a wall-clock cutoff even though all fresh calls reproduced in this finite check.

See PROOF.md, the exact manifests and verification/full_check.json for scope, inputs and comparisons.
