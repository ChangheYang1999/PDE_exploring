# The route-preserving defender has a splash ceiling

## Exact statement

Use the unchanged balanced 12 by 12 game, with spawn (0,0), base (11,11), right/down/left/up breadth-first tie order, and the initial gun1 at (10,1). Let P be the route along the top row to (11,0), then down the right column to the base. Starting from this map, repeatedly add buildings only on cells outside the current returned route. Then the route remains P, with length 22. With the initial gun fixed, the total full-route splash exposure is at most 560 HP, regardless of how many of the other cells receive turrets. This is a bound on splash exposure, not on combined gun damage.

The bound is attained by putting a splash on every off-route cell adjacent to an attackable cell of P, except the initial gun cell. On that particular map, one tier5, or any dense active roster of 1 through 228 tier5 entries, all survive the defenses and reach the base. Other placements of additional guns are not covered by this last claim.

The inherited free_plan used by BudgetHandoff satisfies the off-current-route restriction. Therefore, when a guarded round-four handoff starts with only this gun, later actions of that defender cannot increase its route length or exceed the splash ceiling. This does not by itself prove that the defender must lose a full game.

## Proof of route invariance

The specified FIFO breadth-first search with fixed neighbor order returns a shortest path whose move sequence is lexicographically least among shortest paths. To see this, order each breadth-first layer by the first move sequence that discovers its cells. Expanding the layer in that order, and each cell's neighbors in the fixed order, visits all length-one extensions in lexicographic order; duplicate discoveries retain the first sequence. Induction on layers gives the assertion for the base's first discovery and its parent chain.

Delete any set of vertices outside the returned path P. P remains available. No new path is introduced, so the shortest length cannot decrease and no new lexicographically earlier shortest path can appear. Since P is still available, the length also cannot increase. Thus the same path is returned. Applying this argument after each building proves invariance. Factories and minion purchases change no map cell.

The initial gun is outside the empty-map route P, so the same argument establishes the initial route as well. The planner explicitly excludes all cells on its current route at every turret proposal and never proposes walls. The returned legal proposals therefore meet the induction hypothesis.

## Exact exposure count

An arriving copy occupies every path cell except the base once before arrival. The only off-route cells adjacent in the splash Chebyshev metric to these attackable cells lie in row y=1, x=0 through 10, and column x=10, y=2 through 11. The intersection cell (10,1) is occupied by the fixed gun and cannot also be a splash.

For row y=1, cell x=0 has two attackable neighbors and x=1 through 9 have three each, totaling 29. For column x=10, y=2 through 9 each have three, y=10 has two because the base is not attacked, and y=11 has one, totaling 27. Thus available splash adjacency is at most 29+27=56. Every adjacency deals 10, so the exposure is at most 560. All coefficients are nonnegative. Filling exactly these twenty available cells with splashes attains the bound, and their off-route positions preserve legality and P.

## Tier5 check on the maximizing splash map

The fixed gun1 covers only seven path positions, 8 through 14. It fires at most one 8-HP shot per tick, and any individual copy spends at most seven attack ticks in range. Thus each copy takes at most 56 gun damage, even if it receives every possible shot. Its splash exposure is 560, so its total damage is at most 616, strictly below tier5 HP 1500. Every copy survives. For a dense roster of n<=228 active entries, copy k spawns at tick k, with 0<=k<=227, and arrives at k+22<=249. Each therefore deals the configured 140 base damage. The total is 140n. This says nothing about maps that replace some of these splashes by additional guns.

## Verification and scope

A separate checker enumerates the contributing cells, verifies all actions on the original owner state, checks the unchanged engine route after each addition, computes the adjacency total in two orders, and runs original combat for the stated single-copy and dense-roster cases. Exact configuration and source hashes are pinned in the receipt. A wall-building counter will intentionally violate the off-route-addition premise, so this ceiling need not apply to it. All strength claims require full-game evidence.
