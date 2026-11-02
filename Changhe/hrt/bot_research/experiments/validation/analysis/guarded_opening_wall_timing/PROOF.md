# Earlier walls for a defended heavy-strike opening

Written 2026-10-31T17:48:03.055636+00:00, before enumeration.

## Statement and scope

The previous finite search found no feasible round-three construction on its twelve wall layouts that both stops four fresh tier2 copies and retains a round-four tier4 purchase. This new claim allows the complete wall layout to be built in round one or round two. Each of the first two rounds spends all remaining cash on factories. The opponent buys five then four factories. In round three the defender adds one or two turrets, chosen from gun1, gun2 and splash, and again buys all affordable factories. The finite existence claim is that at least one such plan takes zero damage from four newly bought tier2 copies and has at least 260 gold at its round-four decision. This is a component claim, not a full-game strength claim.

## Exact budget and legality argument

For any nonterminal round without friendly minions, let G be cash before construction, c its cost, F the existing factory count, f=floor((G-c)/20) the new factories and L the final route length. The next cash is G-c-20f+15(F+f)+L = G-c-5f+15F+L. This follows from the original action cost and income settlement. No friendly roster means no outgoing hit bounty. Incoming base damage does not change income. Starting with G=100,F=0 and the empty map, apply this recurrence twice, constructing the fixed wall layout only in its selected round. Original-engine fixtures verify these two rounds, their legality and the resulting G3,F3. The third-round cash is G4=G3-t-5f3+15F3+L3 for turret cost t and f3=floor((G3-t)/20). Require G4>=260.

All wall cells and turret cells must be distinct and avoid the endpoints; the final blocked set must admit a route. Every prefix has fewer blocked cells and therefore also admits a route. The selected witnesses are nevertheless submitted as complete action lists through the original engine. A zero-damage third round ensures survival for the specified component.

## Finite verification and witness selection

Import all twelve wall layouts from counters/data/maze_layouts_001.json. For each wall round in {1,2}, enumerate every available turret cell and unordered pair, and every type assignment from the three affordable types. A gun3 exceeds the observed third-round cash for these openings and is outside the stated family regardless. Filter construction affordability and G4>=260, then simulate every retained map with the original combat function against four tier2 copies with dense indices 0..3, purchased in round three. Single-target guns are not replaced by coverage estimates.

Rank successful plans by most total factories after round three, then greatest G4, then lowest total wall-plus-turret cost, then wall round, layout identifier and serialized turret list. Retain the first eight distinct (wall round, layout) witnesses in that ranking. Recheck those witnesses through the original engine in round three, verify G4 and the legality of buying a tier4 at decision four, and record sixteen additional original-combat components: tiers1..4 crossed with counts1,2,4,8. These extra components are descriptive, not a claim of arbitrary-roster safety.

The search receipt pins its code, this statement, exact JSON and original rule dependencies. A negative search refutes only this finite family. A positive search proves existence only under these exact openings; deployment and a correctly updated public-clone opponent require separate full-game tests.
