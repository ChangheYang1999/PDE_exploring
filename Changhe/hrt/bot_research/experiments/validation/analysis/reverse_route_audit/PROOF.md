# Independent backward-distance check of every wall score

Written 2026-10-31T20:41:34.020171+00:00, before implementing the checker.

## Exact assertion

Keep the selected C02 round-six state and all 14,901,218 wall-set records of screened_guard_minimum unchanged. For each recorded set, recompute the exposure score with a backward-distance algorithm. H1 is equality of all scores, including no-path results, with the original forward-parent enumeration. Every set, invalid or valid, is checked. No second large score table is needed: the checker reads the pinned original bytes, retains mismatch details if any, and records counts and score histograms. This is a verification extension, with no new game or policy call.

## Why the independently computed path is the engine path

The grid is an undirected unweighted graph of unblocked cells. Run breadth-first search from the base to assign each reachable vertex its graph distance d to the base. If the spawn is unreachable, there is no path. Otherwise, from the spawn choose at each step the first neighbor in the engine order right, down, left, up whose distance is one smaller. Distances strictly decrease to zero, so the resulting path is simple and shortest.

Among all shortest paths, this rule gives the lexicographically first sequence of direction indices. Every shortest path from a vertex must start with an edge to distance d-1. Choosing the first such edge minimizes the first symbol, and applying the same argument recursively minimizes the remaining suffix. Thus the backward-distance greedy path is the least direction word among shortest paths.

The engine's forward FIFO breadth-first search discovers vertices in increasing distance. Within each distance it visits them in the order of their least shortest direction word: the induction step processes parents in that order and neighbors in direction order. Dropping a later duplicate discovery cannot remove the least word for its endpoint. Every prefix of a shortest path is itself shortest to its endpoint, so the first discovered base path is the least shortest direction word. This is exactly the backward-distance greedy path. Summing the same splash weights over every path cell except the base therefore gives the same score; both methods return no path in the same disconnected cases.

## Implementation and checks

The new native checker uses a distance array filled from the base and greedily traverses distances from the spawn. It does not import or call the forward-parent enumerator. It reads and validates each five-byte record's padding, distinct valid wall cells and score range. The prior audited domain/order/count certificate supplies exhaustive set coverage. The new checker compares every score, counts per cardinality, invalid paths and a full score histogram. Per-shard outputs and hashes preserve exactly what was checked.

A separate Python version of the backward method compares full paths with the unchanged original shortest_path on all 11,097 retained original-router cases, including the parent's maximum witnesses. The complete native score comparison and these full-path component checks must both pass. All input, source and executable hashes are declared before execution. Compiler identity and actual durations are retained. A mismatch refutes H1 and is not discarded.

## Scope

Combined with the parent domain certificate, this independently verifies every score used in the minimum-five-wall result. It still depends on ordinary executable semantics, compilation and the proved routing correspondence; it is not a proof-assistant or verified-compiler result. It does not strengthen the minimum claim beyond the parent's fixed state, attack, opposing action and wall-only budget. Final candidate bytes and reserved D remain unchanged.
