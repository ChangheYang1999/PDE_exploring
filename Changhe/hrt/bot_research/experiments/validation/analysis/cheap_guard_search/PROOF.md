# Finite cheap-extension search on the two-splash guard map

## Exact statement and hypotheses

Use the unchanged balanced engine, a funded round6 own state with exactly
splashes at (10,1) and (1,0), and no other buildings. Let C be the cells of
the 12 by12 board other than those two occupied cells, spawn (0,0), and
base (11,11). Consider an extension containing at most one new turret,
at most one new wall, and no other actions. A turret is one of gun1, gun2,
gun3 or splash. Every chosen cell is distinct. Fix the three component
rosters: three tier1 plus three tier3; three tier1 plus six tier3; and
three tier1 plus one tier4. Every entry is active in round6.

The finite algorithm below returns a minimum-cost zero-damage extension
for each roster among these extensions, if any exists. It also returns
the maximum splash exposure among legal single-splash additions. A
reported minimum is limited to this class, not all legal construction.
The fixture has sufficient gold for every extension; no claim about a
real opening's ability to pay follows from the minimum.

## Argument

Enumerate no turret or every pair (turret type, cell) from the stated
finite catalog. Independently enumerate no wall or every cell in C. Drop
pairs whose two cells coincide. This lists every allowed extension:
the turret and wall are uniquely specified by type and cell, or absence.
For each extension, reconstruct the funded fixture and call the original
apply_action sequentially on turret then wall. Reject any unaccepted
list. There is no omitted legal ordering. For two distinct constructions,
occupancy and cost conditions are order-independent. If the final map
has a spawn-to-base path, removing one obstacle leaves a path, so every
intermediate construction is also path-legal. The initial funding covers
the combined cost. Thus a legal wall-first extension is legal turret-first.

Compute the shortest route with the original pathfinder and simulate the
stated active entries with the original combat function. The resulting
base damage is exactly the fixture's damage under the engine rules.
For each roster, retain the least total cost among candidates with zero
damage, breaking equal-cost ties by a declared lexicographic action key.
Exhaustive enumeration and this comparison prove the conditional
minimum claim. If no candidate has zero damage, report absence in this
class instead of claiming no legal defense exists.

For a single additional splash, compute exposure as ten times the number
of (pre-arrival path cell, splash) pairs at Chebyshev distance exactly
one. This is the current splash damage rule. Taking the maximum over all
accepted single-splash cells is exhaustive for that class. The exposure
bound and direct component simulations are separate checks. Other maps,
larger extensions, changed routes, inactive or additional rosters, and
full-game performance are outside the result.

## Verification and empirical scope

Keep the exact winning constructions and complete enumeration counts in
JSON. Check each retained construction again on the original engine in
an independent verifier, including its cost, route and component damage.
The minimum additionally depends on reviewing or repeating the exhaustive
enumerator; replaying the retained constructions alone proves feasibility,
not optimality. No formal prover is claimed. This is a development search
prompted by the cost of the early guard extensions, not a held-out test.
