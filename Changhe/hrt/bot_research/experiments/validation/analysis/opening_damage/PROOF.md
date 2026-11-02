# Maximum first-round damage against a map with no turrets

## Statement

Under the unchanged bundled balanced rules, start with 100 gold, no active
minions, and the standard 12 by 12 board. Suppose the opponent's legal first
submission builds no turrets and leaves a valid route. The maximum damage
that a first-round purchase can cause to that opponent in that round is 32.
It is attained by four tier1 copies and one tier2 copy, in any order.

This statement concerns immediate damage, not final-game strength, the cost
of defending one's own base, or an opponent that builds turrets in that round.

## Proof

The route selected by shortest_path is simple. A simple route on 144 board
cells has at most 143 steps. At most six minions can be purchased with 100
gold, because the cheapest costs 15. Their dense indices are zero through at
most five. Hence each spawns by tick five, traverses the route at speed one,
and arrives by tick 148, strictly before the 250-tick round ends. There are
no damaging buildings, so every purchased copy arrives alive.

Tier4 and tier5 cost more than 100 and cannot be purchased. If a tier3 is
purchased, its cost is 100, leaving no other purchases; its damage is 26.
Otherwise let x be the number of tier1 copies and y the number of tier2
copies. Their cost is 15x + 40y and their total damage is 5x + 12y.
Nonnegative integer y can only be zero, one or two. If y = 0, then x <= 6
and damage <= 30. If y = 1, then x <= 4 and damage <= 32. If y = 2,
then x <= 1 and damage <= 29. Buying anything other than minions only
reduces the available budget, so cannot improve this upper bound.

Taking x = 4 and y = 1 spends exactly 100 and gives damage 32. This proves
both the bound and its attainment. With no turrets, order cannot affect
survival, and the preceding spawn argument applies to every order.

## Dependencies and checks

The exact costs, damage, speeds, board dimensions and round length are read
from td_game/balanced.json. Arrival and spawn semantics are those of the
unchanged td_game/combat.py; path simplicity follows from BFS without revisits
in td_game/pathfinding.py. The computation listed in verification/evidence.json
independently enumerates all affordable ordered rosters and applies original
combat on the empty map and two legal wall layouts in both assignments.
It is supplementary to this informal proof. No formal proof assistant is used.
