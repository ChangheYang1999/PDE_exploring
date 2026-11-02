# A covering turret that cannot kill any standard copy

Written: 2026-10-31T11:41:28.646116+00:00

## Exact statement and hypotheses

Use the bundled balanced catalogue, its 12 by 12 board, spawn (0,0), base
(11,11), and its fixed pathfinder. The defender has exactly one gun1, at
(0,2) or at (9,11), and no other building. Its map remains fixed during combat.
The ordered active attacker roster may contain any finite number of standard
tier1 through tier5 entries, including repeated modulo-spawn phases.

For either position the gun covers at least one nonterminal cell of the
selected route, so the positive-route-coverage feature is true. Nevertheless
it cannot kill any copy. The base arrivals, their ticks and total base damage
are identical to combat on the empty map with the same roster and tick limit.
This is not equality of damaged-copy HP records or of the purchase economics.

## Notation and complete argument

The empty-map selected route P first visits (x,0) for x=0,...,11 and then
(11,y) for y=1,...,11. Both proposed gun cells lie outside P. Removing a cell
outside the selected shortest path cannot introduce a lexicographically prior
shortest path or remove P; the fixed neighbor order therefore keeps P. It is
also enough to inspect the breadth-first pathfinder directly for these two
finite maps, as the component checker will do.

A gun1 has range 2.5 and damage 8, firing at most once each tick. For the gun
at (0,2), exactly the two route cells (0,0) and (1,0) are in range: their squared
distances are 4 and 5, while the next cell has squared distance 8. The right
column is farther away. For (9,11), exactly (11,10) and (11,11) are in range,
with squared distances 5 and 4. The latter cell is the base; arrivals are
removed before guns attack. Thus there is only one attackable route cell.

Every standard copy has speed one, advances one route cell per tick after its
birth tick, and visits each such cell at most once. A particular copy therefore
receives at most two shots in the first map and at most one in the second,
even if the gun always prioritizes it. The respective upper bounds are 16 and
8 damage. The least standard starting HP is 20, and this is the only weapon.
No copy can die. This bound is independent of the roster order, simultaneous
spawns, target contention, and the gun's particular tie-breaking choices.

No deaths occur on the empty map either. Spawn ticks agree because the ordered
active roster is unchanged, and movement and arrival removal do not depend on
other copies or on damaged HP while positive. With the same route every copy
therefore has the same arrival tick in both simulations, or fails to arrive
before the same finite tick limit in both. Equal arriving types imply equal
base damage. Positive coverage follows from the explicit nonterminal cells
above, proving the statement.

## Dependencies and scope

The argument uses td_game/pathfinding.py, td_game/combat.py, and the balanced
catalogue. It refines the distinction between coverage and effective defense
from ../single_copy_exposure/PROOF.md. Construction changes, a second weapon,
a different catalogue, or changes to copy speed are excluded. Buying a gun
still costs 30 gold and changes public observations, so full-game equality and
full-game strength do not follow.

The empirical hypothesis is that changing the old off-route bluff gun from
(0,11) to either weak covering position can still trigger an expensive joint
insurance branch in the lead's proposed relevance-filtered policy. A separate
snapshot and both relevance settings will be compared with otherwise identical
parameters, against all three positions and both assignments. The theorem
alone neither proves the branch is costly nor proves a win. All full games
must use the unchanged engine; no formal proof assistant is used.
