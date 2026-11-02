# One permanent splash guard on a grower's maze

## Exact statement and hypotheses

Use the unchanged balanced rules. Let W be a legal finite wall set and let c
be an unoccupied cell other than spawn or base such that W together with c
still leaves a route. Build a splash turret at c, retain all walls of W, and
make no further construction changes. Let P be the engine's resulting route,
including its initial spawn and final base cells. Suppose at least two cells
of P other than the base have Chebyshev distance exactly one from c.

Then no tier1 copy reaches this base while this map is unchanged, regardless
of how many tier1 entries are active, their ordering, or the presence of other
minion types. Copies that do not reach the relevant route cells by tick249 may
be cleared alive. The statement is about arrivals, not universal killing. It
does not protect against arbitrary stronger types or certify full-game victory.

## Complete argument

The legality hypothesis ensures that installing the turret leaves the selected
route available. A tier1 copy has20 HP and moves one route cell per tick. If a
copy were to reach the base during this round, it would previously occupy every
cell of P other than the base in order, beginning with the spawn cell on its
spawn tick. On each such tick, movement and arrival processing precede turret
fire. It has not yet arrived, so the splash attack is applied to it whenever
it is at one of the specified adjacent cells. The splash fires on every tick,
deals10 damage to every adjacent live copy, and has no target-capacity limit.
Other copies cannot absorb or divert that damage.

Before this putative arrival, the copy therefore receives at least two attacks,
for at least20 damage. It is removed no later than the second such attack and
cannot arrive, a contradiction. If the round ends first, the copy is cleared
without arrival. Full-HP respawning next round repeats exactly the same argument.

## Planned experiment and dependencies

For each selected grower layout, search legal currently unoccupied cells for
maximum splash exposure on the resulting shortest route. Store the selected
positions, paths and exposure in exact JSON and independently verify them with
original action application and combat. Delaying the guard until round3 or4
preserves more early factory purchases but allows earlier hits. Those hits, the
guard cost, the path change, enemy reactions, and attacks by stronger types all
remain empirical full-game considerations.

The dependencies are the bundled pathfinding, construction validation, tier1
HP/speed, splash area/cooldown/damage, and spawn/move/arrival/attack/cleanup order.
The argument is a specialization of the current-route immunity result, restated
here so the guard guarantee is standalone. No formal proof assistant is used.

## Tier2 corollary on the selected lead-opening guard

Under the same fixed-map hypotheses, replace the two adjacent route cells
by at least seven such cells. Then tier2 copies, whose configured HP is70,
also cannot arrive: a putative arriving copy must receive seven attacks of10,
and the identical nonpositive-HP contradiction applies. Tier1 still cannot
arrive. The checked lead_opening guard at(1,3) has exactly70 exposure; the
empty and cash_rank_1 guards have only50 and60. This corollary therefore
applies to the lead_opening guard, not to those other two guards. It concerns
combat after installation and does not certify earlier survival or immunity
to tier3 through tier5.
