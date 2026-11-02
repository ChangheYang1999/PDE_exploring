# Minimum number of pure-splash additions on the original guarded map

## Exact statement and hypotheses

Fix the bundled balanced configuration, round6, a funded defender with only
splashes at(10,1) and(1,0), and the original shortest-path tie order. Allow
only additional splashes at distinct unoccupied cells. No wall, gun,
removal, relocation or future construction is allowed in this component.
For each legal resulting map let P be its chosen shortest route, including
spawn and base, and let

    S = sum of splash damage over all adjacent splash/pre-base-route-cell pairs.

Adjacency means Chebyshev distance exactly one. Then no tier3 copy can
arrive alive if S is at least the configured tier3 HP. Conversely, if
S is smaller, the roster consisting of one active tier3 entry arrives
alive in this round. Thus S at least the tier3 HP is necessary and sufficient
for excluding all tier3 arrivals on this fixed pure-splash map.

Enumerating every zero-, one- and two-splash extension gives the exact
maximum S for each such cardinality. The first cardinality whose maximum
reaches tier3 HP is the minimum in these cardinalities. If none reaches it
but an explicitly verified three-splash witness does, the minimum over
all finite pure-splash extensions is three. The computation must determine
which case holds; this statement does not assume its numerical result.

## Complete argument

The original pathfinder returns a simple path: a cell acquires one parent
on its first visit. Hence P contains at most144 cells. The round contains
250 ticks, so an entry born at tick0 has enough time to reach the base.
On its birth tick it stays on the spawn cell; on each later tick it moves
to the next cell. Arrival is resolved before attacks on the base cell.
A surviving copy therefore occupies each pre-base path cell exactly once
for purposes of turret attacks.

Every splash attacks every adjacent live copy on every tick, independent
of other copies. Splash damage sums before deaths are removed. A copy
which could survive through the route would receive exactly S damage.
If S reaches its initial HP, it must die by the last damaging pre-base
cell and cannot arrive. Late spawning can only prevent an arrival by the
tick cutoff; it cannot enable one with insufficient HP. This proves the
sufficiency assertion for every finite roster and every copy.

If S is smaller than tier3 HP, each prefix damage total is at most S,
so a single tier3 born at tick0 stays alive at every pre-base cell. The
simple-path length bound gives arrival strictly before the tick cutoff.
This proves necessity for excluding every possible tier3 arrival. The
argument is specific to a map with no guns; it is not a converse to the
general splash-immunity sufficiency theorem.

Every allowed extension of size k is a k-element subset of the board's
available cells. Enumerating combinations in a fixed order lists each
once. Original apply_action filters illegal lists. For distinct splashes,
if the final map has a route then all prefixes have a route, since they
have fewer blocked cells; sufficient funding covers every prefix. Thus
this ordering omits no legal set. Computing S on each original route and
taking the maximum proves the finite maximum claim. Exhausting all smaller
cardinalities and checking one successful next-cardinality witness proves
the minimum number of additions. At the fixed splash price, that also
gives the minimum construction cost within this restricted class.

## Dependencies and verification

Dependencies are the original balanced configuration, action rejection,
pathfinder, combat tick order and spawn schedule. Record exact candidates,
legality, exposures, witnesses and input hashes in JSON. Independently
reconstruct every candidate and check the single-tier3 implication with
original combat. A large JSON result is data until checked. No formal
proof assistant or global minimum across other turret types is claimed.
No conclusion about a full game's optimal spending follows.
