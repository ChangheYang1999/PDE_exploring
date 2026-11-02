# Minimum wall cost for the selected round-six defense

## Exact statement to check

Fix the original C02 round6 state, the opposing frozen best_v9e action and the attack purchases (tier2,tier2,tier3) from affordable-roster-coverage-001. The defender has four splash towers at (10,1), (1,0), (1,1), (1,2), no walls, and10gold left after the180gold attack. A wall costs1 and deals no damage. No turret or factory can be bought with the remainder. A five-wall package is already checked by the original Engine to stop all incoming damage.

H1: no legal set of at most four additional walls stops the incoming tier3, so five is the minimum additional defensive cost for this fixed state and fixed attack. OPEN before exhaustive execution. This is not a minimum over different openings, different rosters, demolition, or a different opposing action. If a smaller successful set is found, retain it and refute H1.

## Reduction to deterministic grid routing

Let P be the original shortest_path result after adding a wall set W. Legal sets exclude the four existing tower cells, spawn and base, and must leave a path. Every legal final set can be built in any order: an intermediate obstacle set is a subset of the final one, hence preserves at least the final path, and every prefix costs no more than the affordable final set. Conversely every legal sequence gives such a set.

Write w(v) for the number of the four splash towers at Chebyshev distance1 from grid cell v. Define S(W)=10 times the sum of w(v) over all cells of P except its final base cell. The current attacking roster consists of three tier1 entries and one tier3 entry, which spawn at ticks0,1,2,3. Every valid shortest path is simple and has at most140 cells before additional walls, so all surviving copies reach the base before tick250. The source combat order attacks new copies at spawn, then at each later non-base cell, and resolves base arrival before tower attacks. Every splash hits every in-range copy each such tick, without target competition. Consequently a tier3 is stopped exactly when S(W) is at least180. This also stops every tier1, whose HP is20. Thus zero incoming damage is equivalent to S(W)>=180 on this fixed state.

This reduction is checked against the actual source and original-engine witnesses. The reported count is a count of wall sets, not games or independent strength samples.

## Exhaustive enumeration and routing correspondence

There are138 available cells, so enumerate all subsets of cardinality0,1,2,3,4. The declared count is the sum of their binomial coefficients. Each nonempty set belongs to the shard given by its first available-cell index modulo3. Each shard enumerates cardinalities in increasing order and sorted cell tuples lexicographically, with no repeated cell. The three shard domains are disjoint. A strict ordering check within each shard plus per-cardinality counts equal to the binomial coefficients certifies that the retained records cover every set once.

The native enumerator is an optimization of original shortest_path. Map (x,y) to12*y+x. Both implementations start with spawn visited, pop cells FIFO, and discover valid unvisited neighbors in the same order: right, down, left, up. Inducting over queue pops shows equal queues and parent maps. Hence they return the same path or both return no path. The native loop sums the precomputed w over the parent chain beginning at the parent of the base; this is exactly P without the base.

Retain one compact record per set, the native source and executable hashes, compiler identity, per-shard counts and maxima. An independent Python audit checks record ordering, shard membership, counts and maxima; it calls the original Python router for every set of size at most2, every9973rd retained record, and each reported maximum witness. It checks maximum witnesses and the existing five-wall witness through the original Engine. The source correspondence argument, exhaustive domain checks and cross-implementation tests together support the finite result; there is no proof-assistant or verified-compiler claim.

## Evidence and limitations

Declare hashes before native enumeration. Every shard runs on an assigned low-priority CPU with no parallel children. Original-engine checks use the supplied Python environment. The verification folder records all results, counts, timings and failures. An interrupted enumeration or mismatch leaves H1 OPEN. A complete maximum below180 for every cardinality0 through4, together with the legal successful five-wall witness, establishes H1 under the stated source correspondence. A maximum at least180 supplies a smaller witness and refutes H1.

Dependencies: the unchanged balanced rules, actions, pathfinding and combat code; the exact six-round witness; screened_roster_wall_guard/verification/full_check.json; the native source and Python checker in this result's sources and validation tooling. No new policy calls, complete strength games or pool D conditions are involved.
