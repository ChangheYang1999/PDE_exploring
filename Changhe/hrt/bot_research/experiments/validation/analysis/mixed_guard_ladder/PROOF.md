# A finite search for a porous guard that stops one tier3

## Claim and hypotheses

Fix the bundled balanced rules and the first two or three splash cells in
the previously checked empty-map staged guard. Enumerate a finite list of
extensions: one gun of any configured gun type, or two distinct gun1 cells.
All added cells must be legal in their given construction order, preserving
an original shortest path. Suppose an extension passes the following tests
on the unchanged original combat implementation: one tier3 causes zero
arrivals; sixty tier3 cause positive damage; and at sixty copies each, tier3
ranks among the top two current-map damage-per-cost choices from tier3,
tier4 and tier5. Then that extension has exactly these tested properties on
the stated map and homogeneous rosters. It does not follow that the extension
wins a game or that its future mixed-roster behavior has the same ranking.

## Argument

The finite enumeration uses every unoccupied grid cell except spawn and
base for each allowed gun type, with pairs ordered lexicographically to
avoid repetitions of the same two gun1 buildings. Each candidate starts
from a fresh copied defender and uses the original apply_action in sequence.
Rejected actions discard the candidate. The original shortest_path supplies
the path used by original simulate_map. For each test, the attacking roster
has exactly the stated count of new active entries of one type. No inference
from pure-splash exposure is used for gun damage. Requiring zero hits for
one tier3, positive measured damage for sixty, and the stated exact rational
rank is precisely the conjunction in the claim. Comparing integer products
avoids rounding in the rank test. This proves soundness of every reported
witness, conditional on the specified executable game contract. Search
completeness is only over this finite extension family, not arbitrary maps.

A component defender has enough synthetic gold to test geometric legality.
The real bot must separately check affordability against its own public
snapshot. Full games, both assignments, measure the causal strategic effect.
All cells, costs, combat results and exact source hashes are stored in JSON.
These checks do not constitute a proof-assistant formalization.

## Development hypothesis

A gun can stop one predicted tier3 while still letting many through, unlike
the previous five-splash upgrade that stopped all tier3. Keeping tier3 among
the top two large-roster choices may keep the response-aware attack rule
from considering tier5. Try adding the chosen extension at round9 or10 to
the existing growth6, guards4/6 schedule. The outcome is open until full
unchanged-engine games. This is outcome-informed counter development.
