# Why the purchase order changes the round-six outcome

## Exact claim and scope

Fix the original C02 round-six pre-action state and best_v9e's recorded round-six submission from affordable-roster-coverage-001. Submit each of the three distinct orders of the multiset {tier2, tier2, tier3} as the opponent's complete action list. Prior original-engine experiments established incoming best_v9e damage of 26 for (tier2, tier2, tier3), and zero for the other two orders. This analysis explains those known outcomes; it does not present them as new strength observations or prospectively discovered wins.

The descriptive claim is that the original gun target sequence and accumulated damage explain the different fate of the tier3. Verification must account for every copy's HP change at every tick, confirm arrivals precede turret damage, and reproduce the full original-engine round outcome. It also checks that all three cases have the same target route and buildings, equal attack cost, and no old active attacking roster. No policy is called, and no complete new game is run.

## Argument behind the trace

With three new active entries and no old ones, dense active-entry indexing spawns the purchased entries at ticks zero, one and two in purchase order. Every older live copy advances by one path cell per tick. At a tick, copies reaching the base are removed before turrets choose targets. Each gun chooses one in-range survivor with the greatest path index, keeping spawn order at a tie. Every gun chooses from the same pre-damage survivor list. Its damage is added to that copy; the combined damage is subtracted only after all choices. Splash damage applies independently to each adjacent survivor.

Consequently one cannot infer a heavy copy's fate from the multiset of purchases alone. Earlier copies can receive gun volleys that would otherwise hit it. The trace uses the unmodified combat_tick to advance the state. An independent observer computes the target and damage assignments from the pre-damage positions, then compares their sum with every actual HP change. Induction over the 250 ticks, starting with no combat copies, identifies the complete copy history. Summing arrivals and deaths yields the map combat totals, which must equal those produced by a separate Engine.play_round call on the same legal submissions.

The trace is a finite source-guided explanation, not a theorem that putting a heavy copy last is always strongest. Different routes, gun ranges, active rosters or later modulo spawn phases can reverse the effect. The selected five-wall defense and full-policy continuation are separate results. They are required for the later complete-game win; an attack-only one-round leak is insufficient.

## Dependencies and evidence

Pin the original witness, balanced configuration, engine/combat/actions/pathfinding sources, checker and this statement before tracing. Retain exact per-tick JSON, all three original-engine round witnesses and a receipt comparing every copy and aggregate total. Input hashes must agree before and after execution. The unchanged candidate and reserved pool D are not called or edited.
