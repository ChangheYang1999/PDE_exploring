# A pure-tier maximum need not bound affordable damage

## Statement and exact hypotheses

Use the bundled balanced rules and one static combat on the empty 12 by 12
map except for a splash turret at (1,1). The spawn is (0,0), the base is
(11,11), and the engine's breadth-first neighbor order is right, down, left,
up. There are 250 ticks. The attacker's active roster begins with exactly
225 tier1 entries in purchase order, and it may append purchases costing at
most 3000 gold. All those entries are active in the evaluated round.

Among purchases consisting of a single tier, with no artificial count cap,
the largest resulting base damage is 636. A mixed purchase costing 2970 gold
causes 792 base damage. Thus maximizing over pure-tier purchases does not
produce an upper bound on the damage of all affordable purchases.

This statement concerns a fixed, legal combat input and a purchase budget.
It is not a claim that any particular bot reaches this position, nor a claim
of globally optimal mixed damage.

## Notation and rule values

The tier costs are (15,40,100,260,650), HP values are (20,70,180,560,1500),
and base damages are (5,12,26,60,140), in tier1 through tier5 order. A splash
costs 60 and deals 10 damage at each adjacent route cell, including diagonals.
The k-th active entry spawns at tick k modulo 250. A copy can arrive only if
its spawn tick plus route length is at most 249.

## Proof

The turret does not block the engine's chosen route: the route runs right
along row 0 to column 11, then down column 11 to the base. It has length 22.
Exactly three attackable route cells are adjacent to (1,1): (0,0), (1,0),
and (2,0). Consequently the pure-splash damage per copy is 30. By the
[pure-splash arrival criterion](../splash_threshold/PROOF.md), every tier1
copy dies and every copy of tier2 or higher survives if its spawn phase is
at most 227.

The 225 pre-existing tier1 copies deal zero damage. New entries start at
phase 225, leaving three useful phases before the 22 unusable phases
228 through 249. Appending as many copies of one fixed tier as the budget
permits gives the following exact counts:

| Purchased tier | Affordable copies | Arriving copies | Base damage |
| --- | ---: | ---: | ---: |
| tier1 | 200 | 0 | 0 |
| tier2 | 75 | 3 + 50 = 53 | 636 |
| tier3 | 30 | 3 + 5 = 8 | 208 |
| tier4 | 11 | 3 | 180 |
| tier5 | 4 | 3 | 420 |

For any fixed tier, appending fewer copies gives a prefix of the same spawn
sequence. On this map the additional copies cannot hurt earlier copies:
splash is independent of roster density and there are no guns. Damage is
therefore nondecreasing in the appended count. The table covers the optimum
for each pure tier, including all smaller affordable counts. Its largest
entry is 636.

Instead append three tier2 copies, then 22 tier1 copies, then 63 tier2 copies.
The initial three tier2 copies occupy phases 225 through 227. The tier1
copies fill phases 228 through 249. The final 63 tier2 copies occupy phases
0 through 62 after wrapping. All 66 tier2 copies arrive and deal
66 times 12 = 792 damage. The tier1 copies deal zero. The purchase costs
66 times 40 + 22 times 15 = 2970, which is at most 3000. Since 792 exceeds
636, the asserted upper-bound interpretation is false.

## Dependencies, evidence, and scope

The argument uses only the explicit catalog values, the bundled route rule,
and the pure-splash arrival criterion. The unchanged engine reproduction is
registered in verification/evidence.json, along with the exact JSON input.
The proof does not depend on trusting a planning simulator. No machine-checked
formalization or universal optimality result is claimed.
