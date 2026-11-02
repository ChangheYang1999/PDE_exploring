# Three purchases, two different outcomes

At one reached round-six state, best_v9e's five sampled attack rosters all predict zero incoming damage. The opponent has190gold. Buying two tier2 units followed by one tier3 costs180gold and deals26damage. Buying the same three units in either other order deals none. This is a counterexample to treating the sampled maximum as a guarantee over every affordable roster. It comes from a selected development state, not the reserved final test.

The [exhaustive roster audit](../affordable_roster_coverage/RESULTS.md) tried all361 affordable ordered lists at this state. Only `(tier2, tier2, tier3)` caused damage. The sample already included `(tier3, tier2, tier2)` and `(tier2, tier3, tier2)`, along with three other lists. The omitted order matters because the engine preserves purchase order when it schedules active entries.

![The same five-gun map beside the tier3 HP traces for all three purchase orders. The last-bought tier3 reaches the base with12HP; the other two orders die.](figures/purchase-order-v2.png)

## Follow the gun targets

There are no older active attacking entries at this state. The three new copies spawn at ticks0,1,2 in purchase order. A copy moves one route cell per later tick. The route takes44steps. A surviving tier3 bought last therefore reaches the base at tick46.

Each of the defender's five gun1 turrets deals8damage per shot. A gun chooses the in-range copy furthest along the route. All guns select before damage and deaths are resolved, so overlapping guns can commit their shots to the same copy. The first two tier2 copies can receive shots that would otherwise hit the tier3 behind them. This is target competition, even though every copy moves at the same speed.

The [complete tick trace](verification/full_check.json) gives the following totals. Damage includes the fatal volley, so a dead copy can have negative final HP.

| Purchase order | Tier3 damage received | Tier3 final HP | Tier3 fate | Base damage |
| --- | --- | --- | --- | --- |
| tier2, tier2, tier3 |168|12|Arrives at tick46|26|
| tier2, tier3, tier2 |192|-12|Dies at tick42|0|
| tier3, tier2, tier2 |184|-4|Dies at tick37|0|

The last-bought tier3 receives21 gun shots. The other orders receive24 and23 respectively. In the successful order, both tier2 copies die after receiving72damage each, at ticks16 and29. The tier3 does not need to avoid all fire; avoiding enough shots to keep12HP is sufficient. Once it reaches the base, arrival resolves before turret attacks. A final shot at the base cannot save the defender.

The trace advances the original combat routine through all250ticks for each order. A separate observer reconstructs each gun's chosen target and checks every copy's HP change. The aggregate arrivals, deaths and base damage agree with separate original-engine round executions. The three cases have identical defending buildings and routes. This checks the explanation directly rather than inferring it from the final score. It does not establish that putting the heaviest unit last is always best.

## A local leak still needs a complete strategy

An attack-only intervention leaves both bases at774HP: the target also returns one tier3. The [five-wall guard](../screened_roster_wall_guard/PROOF.md) spends5of the remaining10gold to route that copy past enough splash damage. On the fixed return attack it changes the attacker's HP to800 while preserving the target's774. The [wall enumeration](../screened_guard_minimum/RESULTS.md) checks all14,901,218sets of at most four added walls and finds no cheaper successful wall set under these fixed-state restrictions. Its source correspondence argument and original-engine witnesses are part of that finite computational result; it is not a proof-assistant certificate.

The continuation then decides whether the26HP lead survives. Following the attack and guard with frozen Fortress38 wins800:774 at round50 in both assignments. The same attack and Fortress38 continuation without the guard draws774:774. The original C02 continuation and the economy20 continuation still lose with the guard. All six new games, their six reused controls and304 fresh policy decisions are retained in the [complete-policy comparison](../screened_roster_guarded_policy/RESULTS.md).

The [transfer experiment](../screened_guard_transfer/RESULTS.md) limits the conclusion further. Against six other fixed development opponents, the guarded policy has two draws and ten losses. AS1C, the full-attack-budget variant of best_v9e with catch-up share0.5, wins774:380 in both assignments. It concedes the same round-six hit but sends two tier5 copies at round10 and another at round11. On the two selected loss states, giving the greedy free planner the exact next roster reduces the first hit from280 to140 and leaves the second at140. That [diagnosis](../screened_forecast_defense/RESULTS.md) uses recorded future actions only for a fixed-state intervention, not as information available to a playing bot.

The mechanism is exact on the stated round-six state. The guarded full policy is a verified counter to one frozen candidate. The transfer failures show why these are different claims.
