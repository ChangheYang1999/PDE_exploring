# Exact affordable-roster coverage on retained early states

## Objects and hypotheses

Fix the final best_v9e candidate, SHA256 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87, the bundled balanced rules and the 24 standard-start histories in reserved-C-best-v9e-001. Pool C was used for selection. This is a post-selection component diagnosis, not new held-out evidence.

For each retained history consider every reached round from 2 through 6 whose opponent has at most 250 gold before submissions. The opponent's entire available gold is the purchase budget; it is not truncated to 250. Retain the candidate's original complete action list in that round. Let R be the opponent's active roster before new purchases, in its original order. Let Q(g) contain every finite ordered purchase list with total catalog cost at most the opponent's gold g, including the empty list. Let S(g) be the lists returned by the frozen v7 planner's affordable_bundles at budget g, with the empty list added only if the planner returns no list.

For q in Q(g), let d(q) be the candidate's incoming base damage when the unchanged Engine executes the retained candidate list against exactly the new minion purchases q, from the original pre-round state. Define M as the maximum of d(q) over Q(g), and m as its maximum over S(g). The two finite hypotheses, declared before these interventions, are:

- H1: M = m at every eligible retained state. The sampled lists attain the exact worst damage.
- H2: at every eligible state with m = 0, M = 0. Stopping the sampled lists suffices for these particular states.

Both hypotheses are OPEN until all declared states are checked. A counterexample refutes the corresponding universal finite statement. Failure to find a counterexample confirms it only for the enumerated states. A result with no eligible states or no zero-sample states must be reported as vacuous, not as substantive coverage.

## Why the enumeration is complete

All catalog costs are positive integers. Generate the empty list, then for each affordable type t append t and recurse with the budget decreased by its cost. Recursion terminates because every appended entry decreases the remaining budget by at least 15. Every generated list is affordable by induction on its length. Conversely every nonempty affordable list has a unique first type t, followed by a list affordable with the remaining budget; induction on length shows that it appears in that branch. The empty list appears once, and distinct branches have distinct first types. Thus the generator enumerates Q(g) exactly once.

At g = 250 there are 2166 lists under the bundled costs. This count bounds the per-state work; smaller budgets are enumerated with their exact value. Each list is submitted to the original Engine after copying the original pre-round Engine state. No combat formula or planning simulator is used to decide M or m. A compact compressed record retains every tested list, its cost and incoming damage. The ordinary retained game is also independently replayed in full, so every pre-round state is tied to its retained original history.

## Scope of a fixed-round witness

Deleting the opponent's other purchases leaves its new minion subsequence legal: buildings and factories have positive costs and cannot add spending money during submission. Conversely any q in Q(g) is a legal purchase-only submission. Opponent construction changes only the opponent's map, while incoming damage on the candidate's map depends on that map, the opponent's active roster R followed by q, and the combat rules. The Engine finishes both combats before settlement, including when a base is destroyed. Outgoing candidate damage, opponent map changes and hit income therefore cannot change the candidate's incoming damage in this round. The fixed-round maximum M consequently covers every legal opponent action list at this state when the candidate action list is fixed.

This is not a bound against a candidate that changes its own list, and it supplies no guarantee for the next round. The intervention may alter future gold, roster and HP. It is not a complete counter-policy or a new W/D/L result. A full-game strength claim would require a separately declared and evaluated legal policy.

## Verification and dependencies

The declaration pins this statement, the checker, its source closure, balanced configuration, the parent candidate hash, the retained jobs, results and replays, and the completed identity-audit receipt. Every case verifies the pins before and after execution. Each generated submission must be accepted in full. The sampled lists must lie in Q(g). Candidate observations and both player assignments are inherited from the original retained histories; no candidate or opponent policy is called in this diagnosis.

For each eligible state, retain counts, both maxima, a deterministic maximizing witness, all enumeration rows in compressed form, and a full original-engine replay of each reported sample-bound counterexample. Keep every failure or timeout. The summary reports all declared jobs, every eligible state, counts by player assignment, and both hypotheses separately. The finite argument above depends on original-engine execution and the exhaustive recursion; it is not a formal theorem-prover proof of the implementation.
