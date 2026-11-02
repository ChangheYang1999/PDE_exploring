# First wrapped heavy copy: zero-based roster indexing

## Statement and notation

Use the bundled rules: 250 ticks, an active ordered roster indexed starting at
zero, tier1 cost 15 and tier5 cost 650. An active entry of index k spawns at tick
k modulo 250. Let N be the number of active existing entries and let p new tier1
entries precede the first new tier5 entry. That tier5 entry has index N+p.
For an intended spawn at tick zero, the least nonnegative padding is
p = (-N) modulo 250.

The frozen fortress17 helper `wrap_bundles` instead computes
p_old = 250*(floor(N/250)+1)-N-1. Its first heavy entry consequently has index
249 modulo 250, not zero. On a positive-length route this copy cannot arrive
before tick 250. With N divisible by 250 the correct least padding is zero,
whereas the helper also skips that immediate wrap opportunity.

## Proof

The N existing entries have indices 0 through N-1. Appending p fillers assigns
them indices N through N+p-1, so the next entry has index N+p. Reducing this
index modulo 250 proves the first formula. Substituting the helper's expression
gives N+p_old = 250*(floor(N/250)+1)-1, whose remainder is 249. A newly spawned
copy does not move until the next tick. Its arrival tick on a route of length
L is 249+L, exceeding the final tick 249 when L is positive.

## Component counterexample to the sampled threat set

Let the defender use the full default fortress17 layout, with the nine layout
cells of greatest final splash adjacency occupied by splash turrets and all
other layout cells occupied by walls. Break adjacency ties by x then y.
The verification script records the resulting exact cells, route length L and
splash damage S. The construction only needs 560 <= S < 1500 and L > 49; these
are checked before any conclusion is reported.

Let the attacker have 200 active tier1 entries and 1400 gold. Let the defender
have no other turrets. The affordable purchase of fifty tier1 entries followed
by one tier5 costs 50*15+650 = 1400. Its new tier5 has index 250, spawns at zero
and arrives after L ticks with positive HP, dealing 140 base damage. Every
tier1 dies because S >= 560 > 20.

For the particular sampled threat set of fortress17, the verification script
checks every generated composition against the original combat implementation.
The assertion to be checked is that all of those compositions cause zero
base damage. This last finite check is implementation-dependent; the indexing
argument above does not assume it.

## Scope, dependencies and verification

This is a component-state counterexample, not a complete standard-start game
or a claim that a particular bot necessarily reaches this state. Exact state
parameters, legal construction actions, sampled compositions and original-engine
combat results are saved in `verification/evidence.json` and its named artifact.
Legal construction of the fixed map is checked from an empty map with sufficient
component-test gold. Reachability of the complete resource-and-roster state
from the standard initial state is not claimed.

Dependencies: the unmodified `td_game/combat.py` spawn and arrival rules, balanced
unit costs/HP/damage, and the explicitly hashed frozen fortress17 planner. No
formal proof or universal guarantee for a repaired sample is claimed.
