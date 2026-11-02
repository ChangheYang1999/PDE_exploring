# An affordable guard for the round-four heavy strike

## Statement and hypotheses

Use the unchanged balanced game. On a decision observation with an empty own map and gold 291, a gun1 at (10,1) and one tier4 cost 30+260=290 and are jointly legal, leaving one gold. The resulting own map stops an incoming active roster of at most three tier1 entries, with no other incoming entries. This claim applies in any round in which those entries are active, not only in round 1, because combat copies are recreated at full HP with dense active-entry indices every round.

The empirical hypothesis is that adding this cheap guard to the round-four heavy-strike counter preserves an HP lead and yields a full-game win against both P4TNUB and P5TNUBM. Compare the same fixed timing R=4, earliest handoff L=5, and public-budget fractions 1/2 and 1, with the gun enabled or disabled. Both physical assignments and all outcomes must be reported. The disabled variant is an exact controller control for the already measured unguarded timing.

## Proof of the component

The right-first shortest route on the empty map follows the top row to (11,0), then the right column to (11,11). The gun cell (10,1) is neither on that route nor an endpoint, so the route remains available and shortest. Its range 2.5 covers exactly path indices 8 through 14. An active tier1 copy has 20 HP, and a gun1 shot deals 8, so three shots kill it. With n<=3 consecutive dense active indices, copy k spawns at tick k. The frontmost-target rule assigns shots 8,9,10 to copy zero, 11,12,13 to copy one, and 14,15,16 to copy two, omitting absent copies. These shots lie in each copy's seven-tick coverage interval and precede its base arrival. Thus all incoming copies die. This is the same complete argument as ../corner_guard/PROOF.md, applied to the active roster in round four. Own factories and own offensive purchases do not alter this geometry or incoming combat.

The cost sum 290 is at most the hypothesized 291 gold. The tier4 purchase changes only the own attacking roster, not the own map. Therefore both actions can be accepted before any later proposals. A 60-gold splash could not accompany the same strike under that budget; the cheaper gun is the proposed intervention.

## Controller construction and scope

The guarded controller first obtains the unchanged TriggeredBudgetHandoff proposal. On the declared strike round only, it submits the fixed gun proposal before that proposal and rechecks the entire list sequentially using the original owner-local validator. It omits actions made unaffordable by the gun. It updates its diagnostic map residuals from the accepted list, not from the parent proposal. On other rounds it returns the parent result exactly. No observation is mutated, and the parent opening is a function of observations, so no hidden state is borrowed from the opponent or engine.

The returned list is legal by induction on its accepted prefix: the copied owner state equals the state reached by the same accepted actions in the engine, and each next action is added only after validation succeeds. The HP handoff still depends solely on public observations. Full-game strength is not proved by the component; future attacks may require stronger defense, and paying 30 gold can change future income. Source, exact guard data and configuration are pinned before the comparison. No reserved conditions are used.
