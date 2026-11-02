# A turret with no combat effect on the empty-map route

## Statement and scope

Use the unchanged bundled balanced rules: a 12 by 12 board, spawn (0,0), base (11,11), and gun1 range 2.5. Start with an empty own map. Suppose the only building ever placed on that map is one gun1 at (0,11). Every combat round has the same selected route as the empty map, and this gun deals zero damage to every attacking roster, regardless of roster order, size, or purchase round.

This is a statement about combat and geometry only. The purchase still costs 30 gold and changes the public building list and turret count. It can therefore affect future economic decisions and an adapting opponent's decisions. No full-game strength claim follows.

## Notation

Let P be the selected empty-map route, including spawn and base. Let d squared denote squared Euclidean distance. A gun may target a copy only when the copy is on a path cell at distance at most its range. Arrivals are removed before turret targeting.

## Argument

The engine's fixed neighbor order selects the route along the top row from (0,0) to (11,0), then down the last column to (11,11). The new occupied cell (0,11) is not on this route. The route remains legal and has the minimum possible length of 22 moves. Removing a cell outside the selected path cannot create an earlier shortest path or remove this path, so the deterministic route selection remains unchanged. Alternatively, the original pathfinder equality is checked directly in the accompanying finite computation.

For a top-row cell (x,0), its squared distance from (0,11) is x squared plus 121, at least 121. For a last-column cell (11,y), the distance squared is 121 plus (y minus 11) squared, also at least 121. Both bounds exceed gun1's squared range, 6.25. Thus every possible path position is outside the gun's range. Target selection always finds no target, so the gun adds no damage in any tick. This does not depend on which copies occupy those positions. The map does not change afterwards, proving the claim for every round.

## Public-policy implication

Economy13's source sets a permanent flag after observing a positive opponent turret count. It activates its no-turret case only when this flag is false and the round is at least `none_from`. Therefore a gun bought in round one disables that case from round two onward; a gun bought in round three disables it from round four onward. Current-round enemy actions remain hidden, so the effect cannot occur earlier through this flag.

This implication follows from the flag condition, not from any measured match outcome. Whether changing the branch compensates for spending 30 gold is an empirical question.

## Dependencies and verification

Authoritative sources are `td_game/pathfinding.py`, `td_game/combat.py`, and `td_game/balanced.json`. Policy sources are `bot_research/bots/counters/feature_bluff.py` and `bot_research/bots/economy/frozen/v13/econ13.py`.

`bot_research/experiments/validation/check_feature_bluff.py` checks unchanged path selection, the exact distance inequality, legal actions and observation immutability in ten eight-round runs on the original engine. It also checks equality with eco6_t5 for the no-turret control on 16 observations. Evidence is `bot_research/runs/validation/feature-bluff-check-001.json`. The evidence records source hashes; `verification/checksums.sha256` also binds this proof and checker to those inputs. No proof-assistant verification is claimed.
