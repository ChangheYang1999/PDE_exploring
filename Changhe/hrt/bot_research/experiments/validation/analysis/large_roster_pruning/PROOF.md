# A large roster can still admit a cheap gun defense

## Exact statement and scope

This is a finite computational counterexample to the assertion that guns need
not be considered against a roster with more than 120 entries. It concerns the
bundled balanced rules and frozen fortress v18's defensive component, not a
full game reachable from the standard start by its default policy.

Let the defender's blocked cells be the default full 59-cell fortress layout.
They comprise rows y = 1, 3, 5, 7, except respectively x = 11, 0, 11, 0, and
five vertical pillars: x = 1, 5, 9 at y = 8, 9, 10, and x = 3, 7 at
 y = 9, 10, 11. Put splash turrets at
(1,1), (10,1), (1,3), (1,5), (10,5), (1,10), (3,9), (5,10), (7,9).
All other blocked cells are walls. The defender has 1,000 gold. The attacker
has 1,400 gold and 200 active tier1 entries, in purchase order. All entries
are active for the round under consideration. The construction sequence and
complete initial observation are in the linked JSON fixture.

The frozen v18 threat sampler returns 13 compositions, including the 200
visible entries followed by 50 tier1 and one tier5. The latter purchase costs
50 times 15 plus 650 = 1,400. The v18 planner with budget 1,000 returns two
splashes costing 120, and this legal purchase still causes 140 base damage.
Alternatively, adding gun3 turrets at (10,8) and (11,8) costs 400, is legal,
and stops all 13 sampled compositions, including that purchase.

This statement does not assert that these two guns stop every affordable
ordered purchase, nor that 400 is the minimum cost over all legal defenses.

## Argument and finite verification

The default blocked layout has a route of length 78. The nine splashes give
610 total damage to each copy that traverses the route. With 200 existing
entries, the 50 cheap additions occupy indices 200 through 249; the tier5
occupies index 250 and therefore spawns at tick zero. Its route would finish
at tick 78, before the 250-tick round ends. It survives the splash-only map,
so the unmodified engine records one hit of 140 damage. The corrected sampler
includes this exact composition.

`check_roster_wrap_repair.py` reconstructs the fixture with the unmodified
Engine and applies every construction and purchase through apply_action,
requiring acceptance. It calls the frozen v18 sampler and planner, applies the
returned defense, and passes the resulting states to the original simulate_map.
The saved result records the two splash actions and the remaining 140 damage.

`search_wrap_defense.py` independently reconstructs the same fixture. It
checks all six initially legal gun3 locations and all fifteen pairs. For
each accepted pair, it recomputes the route and executes original simulate_map
on independent copies of the attacker and defender. For every pair that stops
the specified wrapped tier5 attack, it repeats this test for each of the 13
sampled compositions. Six pairs stop every sampled composition; the two
coordinates in the statement are the first such pair. Each damage result is
zero. The total cost is twice 200, and the accepted construction preserves a
route of length 78. Thus this is a concrete affordable gun response to a
sampled threat that the returned defense fails to stop.

The source explains the omission: the gun pass is skipped whenever any
sampled composition has more than GUN_PASS_MAX_ENTITIES = 120 entries.
That shortcut does not distinguish cheap entries already killed by splash
from the few surviving heavy entries that guns could stop. The fixture
refutes a universal justification for that pruning rule; it does not quantify
how often the shortcut matters in normal games.

## Direct-helper follow-up

A separate check calls the unchanged v18 `_gun_pass` helper directly on the
same observation, with all 13 sampled compositions, a 1,000-gold budget,
and no deadline. It finds gun3 turrets at (10,8) and (10,9), costing 400.
Original-engine checks confirm zero damage for every sampled composition.
The published `plan_defense` still returns the two splashes and leaks 140.
Thus the effective response is available to the existing gun-search routine
in this fixture, rather than only to the exhaustive pair search. This does
not establish that removing the cutoff is affordable or sufficient in other
states. The script and result are included in the evidence manifest.

## Dependencies and evidence

Dependencies are the unchanged balanced configuration, action validation,
path selection and combat code, plus the exact frozen v18 sampler and planner.
The zero-based wrapping calculation is proved in ../roster_wrap/PROOF.md.
`verification/evidence.json` records the fixture, implementations and result
hashes. This is a checked finite computation with an informal argument, not a
machine-checked proof. No engine code was edited or replaced.
