# Exact income of a fixed-wall grower

## Statement and hypotheses

Use the bundled balanced rules on the standard empty 12 by 12 board. Let W
be a fixed set of C distinct cells, containing neither spawn nor base, whose
removal leaves a route. Suppose C is at most100. A policy builds one wall in
every cell of W in round one, then buys as many factories as it can afford in
each round through a fixed growth horizon h. It makes no other purchases,
never hits the enemy base, has no factory cap that binds, and survives through
round h. Write L for the number of edges in the engine's shortest route after
W is built. Let F_r and G_r be its factory count and gold after the income of
round r.

Then all the wall purchases are legal in any order, and

    F_1 = floor((100-C)/20),
    G_1 = 100-C-20 F_1 + L + 15 F_1.

For 2 <= r <= h, putting k_r = floor(G_(r-1)/20),

    F_r = F_(r-1) + k_r,
    G_r = G_(r-1) - 20 k_r + L + 15 F_r.

The total gold available at the start of round h+1 is exactly G_h. Therefore
these recurrences rank such fixed-wall policies by that cash balance without
simulating combat. They do not rank full-game win rate, damage, surviving HP,
or policies with base-hit bounties or further construction.

## Proof

The final wall set leaves a route. Every proper prefix removes fewer cells,
so that same final route remains available after each prefix. Distinctness and
the endpoint exclusion satisfy the remaining geometric action checks. Each
wall costs one gold, so the initial100 pays for all C. The remaining100-C buys
exactly floor((100-C)/20) factories at20 gold each. No further construction
changes the route. Round-one income is L gold from the route and15 per owned
factory; the no-hit hypothesis excludes any bounty. This gives G_1.

Assume the formulas have computed the state after round r-1. No action can
change that gold before round r's submission. Exactly floor(G_(r-1)/20)
factories are affordable, and the nonbinding cap allows all of them. Subtract
their cost, add them to F_(r-1), and add the same route income L and15 gold for
every factory, including the newly purchased ones. This gives both recurrences.
Induction proves the stated values through h. Combat can change HP but cannot
change this player's gold except through its own base-hit income; that income
is zero by hypothesis. Survival makes every considered round well defined.

## Use and verification scope

The proposed counter builds one of a finite set of searched wall maps, then
uses the existing grower schedule with optional round-two tier1/tier2 bait and
later tier5 purchases. The recurrence is used only for the no-bait, no-hit
component check and for selecting an initial map. The original engine must
verify every imported coordinate, route length, affordable purchase and income
value. Full games must independently establish strength, including the effects
of bait, bounties, enemy response and possible early death.

Layouts will be stored in exact JSON rather than repeated numeral lists in
source. Their bytes must be pinned by the policy and every experiment manifest.
A finite search provides candidates, never a claim of a globally optimal maze.
No Lean or other formal proof assistant is used. Dependencies are the unchanged
balanced configuration, actions.py, pathfinding.py and engine.py.
