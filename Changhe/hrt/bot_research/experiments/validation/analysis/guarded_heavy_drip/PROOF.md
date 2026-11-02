# Affordability of a guarded two-purchase heavy schedule

## Statement, notation and hypotheses

Use the bundled balanced rules and an empty starting map with100 gold.
Assume the player stays alive through round9 and its sole round1 tier1 copy
arrives at the enemy base in round1. No further arrivals are required.
Build gun1 at(10,1), buy that tier1 and two factories in round1. Buy
3,5,9,15 factories in rounds2,3,4,5. Buy nothing in round6. Buy one tier5
in each of rounds7 and8. Build gun2 at(10,2) in round9.

Every scheduled action is legal and affordable. At the end of rounds1..9,
the player's gold is at least72,109,181,308,540,1072,954,836,1288 respectively.
These are lower bounds, not claimed exact full-game balances. The statement
does not assert survival, successful later attacks, or victory.

## Proof

Both gun cells are off the unchanged22-edge right-first route. Removing
those cells leaves the selected shortest route available and creates no
earlier route in the fixed search order. The cells are distinct and not
endpoints. Thus construction remains legal and the route income stays22.
Factories cost20 and pay15 each in the round bought. Gun1 costs30, tier1
costs15, tier5 costs650, and gun2 costs80. The first-round purchases cost85,
leaving15. The two factories and the route pay52, and the hypothesized first
hit pays5. This gives72 at the first round end.

Ignore every later hit bounty, which is nonnegative. The cumulative factory
counts after rounds1..5 are2,5,10,19,34. Sequential subtraction of purchase
costs and addition of22 plus15 per factory gives

- round2:72-60+97=109;
- round3:109-100+172=181;
- round4:181-180+307=308;
- round5:308-300+532=540;
- round6:540+532=1072;
- round7:1072-650+532=954;
- round8:954-650+532=836;
- round9:836-80+532=1288.

Every pre-income remainder is nonnegative. Extra bounties can only increase
the balances, and incoming attacks do not remove factories or gold. The
survival hypothesis permits each round to occur. This proves legality,
affordability and the stated lower bounds.

The first-hit hypothesis matters: deleting its5 bounty makes the nominal
round4 factory bill exceed the corresponding lower balance by4. The
implementation filters unaffordable actions on a private public-state copy,
so it remains a valid policy when that hypothesis fails, but then need not
follow the full schedule.

## Dependencies and verification

Dependencies are the bundled action costs, income rule, construction and
pathfinding. The exact schedule and lower bounds are in
bots/counters/data/heavy_drip_001.json, relative to bot_research. The checker
uses the original engine in both assignments. Its opponent allows the first
hit and installs gun1 in round2, eliminating further tier1 arrivals. It
checks legal actions, unchanged observations and the lower bounds through9.
No formal proof assistant is claimed. Full-game transfer is tested separately.
