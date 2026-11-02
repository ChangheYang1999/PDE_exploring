# Guarded screened-roster policy results

Completed 2026-10-31T20:18:14.720025+00:00.

H1 (a guarded continuation wins both seats): **CONFIRMED**. H2 (every final HP margin is nondecreasing): **REFUTED**.

Six new games and six explicitly reused controls. Every new game passes strict accounting, full original-engine replay, source/archive checks and fresh reproduction of both policies (304actual calls). All three new assignment pairs agree exactly. All six paired old/new checks preserve the round1-5 history and actual target round6 action; the guard changes own round6HP from774 to800 while keeping target HP774.

| Continuation | Guarded result | Guarded HP | Round | Control result | Control HP | Round |
| --- | --- | --- | --- | --- | --- | --- |
| original | L | -1000:774 | 14 | L | -240:774 | 12 |
| fortress38 | W | 800:774 | 50 | D | 774:774 | 50 |
| economy20 | L | -320:774 | 12 | L | -486:774 | 13 |

Both seats agree on every table entry. The construction was selected from the prior component search and tested against a known fixed candidate. Later effects include map geometry, path income, HP and policy responses. No held-out or unrestricted-strength claim is made. The source-level Fortress38 wall-clock cutoff remains a limitation beyond the exactly reproduced calls.

See PROOF.md and verification/full_check.json for hypotheses, exact inputs, actions and paired comparisons.
