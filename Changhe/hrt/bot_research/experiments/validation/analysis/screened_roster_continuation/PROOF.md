# An omitted roster order and its complete-policy continuation

Declared before any new full-policy execution on 2026-10-31. Exact declaration time and source hashes are recorded in screened-roster-continuation-001.json.

## Objects, hypotheses and scope

The rules are the unchanged bundled balanced configuration and original Engine. B is frozen best_v9e. C02 is the retained standard-start opponent with four splash towers, growth through round9, roster (tier5,tier2), and attacks in rounds congruent to1 modulo5. All policies receive only their normal public observation.

For continuation c in {original, fortress38, economy20} and order o in {(tier2,tier2,tier3), (tier2,tier3,tier2), (tier3,tier2,tier2)}, define Q(c,o) as follows. In rounds1 through5 use exactly C02. In round6 purchase o in its stated order, with no other purchases. From round7 use C02, frozen Fortress38 with its default parameters, or frozen Economy20 with the parameters in the implementation, according to c. A purchase is submitted only when the entire package is affordable. Both assignments against B are included, giving18 declared full games. The reference C02 histories are already selected development evidence; this experiment is not a holdout.

The preceding exhaustive audit found that in the retained C02 round6 state all five sampled rosters do zero damage, while (tier2,tier2,tier3), costing180 of190gold, deals26. The unchanged original-engine witness also shows the other base takes26, leaving774:774. This one-round fact does not imply a complete-policy win.

## Shared-prefix proposition and argument

Suppose B's decisions are deterministic on the encountered observations and each Q follows the policy above. Then for fixed player assignment every Q(c,o) has exactly the same actions, states and results through round5. Its round6 B action is also the same for every c and o. Proof: all policies start from the same state. Before round6 their action function is C02. Induct on completed rounds using the deterministic engine transition. The observations before round6 consequently agree. B sees no pending opponent action, so its round6 action agrees as well. This proof is conditional on actual deterministic decision behavior; fresh-call checks and complete-prefix comparisons verify the condition on these finite histories.

For the three round6 orders, the multiset, cost and number of bought minions coincide. Holding the pre-round state and B action fixed therefore makes the ordering the only intervened purchase property. A difference in this round's damage establishes an order effect. Future outcomes may differ through changed public states, changed B actions, and the chosen continuation; they cannot be attributed to ordering without this qualification.

## Predeclared empirical questions

H1: at least one Q(c,(tier2,tier2,tier3)) wins against B in both assignments. H2: for every continuation c, that screened ordering ends with a strictly larger own-minus-enemy HP difference than each of the other two orderings. These are separate questions; engine winner, not HP sign, determines H1. Both hypotheses are OPEN before execution. Every win, draw, loss, timeout, invalid action, source mismatch and policy-reproduction difference is retained.

## Verification and dependencies

Freeze all policy, runner, replay and checker sources before calls. Each game runs in a fresh process. Verify strict condition accounting, original-engine complete replay, archive hashes, both fresh factory policies on every retained observation, and common prefixes plus round6 orders. Report18 games as nine paired deterministic conditions, not18 independent random samples. The three-second cutoff inherited by Fortress38 remains a source-level reproducibility limitation even if fresh calls agree. No proof assistant or general best-response guarantee is claimed. The selected installed best.py is never edited or used for these games; pool D remains unplayed until its fixed gate.

Dependencies: analysis/affordable_roster_coverage/PROOF.md and RESULTS.md; the declaration's exact source and witness hashes; the original engine. All full-game conclusions depend on the retained verification receipts, not on private-simulator predictions.
