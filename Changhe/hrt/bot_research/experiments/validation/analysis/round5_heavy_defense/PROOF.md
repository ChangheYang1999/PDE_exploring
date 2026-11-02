# One-building responses on the reached round-five map

## Statement and hypotheses

Fix the target's post-construction map in the strike_count=1, target_side=0 component of runs/validation/early-heavy-opening-001.json. Use the unchanged balanced configuration and round 5. Keep all existing buildings, permit either no addition or one legal wall or standard turret, and evaluate one tier4 active entry born at tick 0. The fixture is independently funded for the geometric search. Its funds are not claimed to be the target's post-submission budget.

The finite search returns a minimum-cost member of this restricted class that both stops the single tier4 and retains pure-splash exposure at least the tier3 HP threshold. It does not optimize over multiple additions, relocation, all affordable mixed rosters, or the full game. Existence and numerical cost are open until the search and check finish.

## Notation and proof

For a legal map M let P(M) be the engine's deterministically chosen shortest route. Let S(M) be the sum of splash damage over all non-base route cells adjacent in Chebyshev distance exactly one to each splash. Existing guns are absent in the fixture. Any added gun does not alter the definition of S.

The candidate set consists of the unchanged map and every pair (building type, board cell), with type ranging over a wall and the four standard turrets. This enumerates every allowed addition by definition. Apply the original action validator to a fresh copy of the funded fixture for every proposal. Rejecting proposals that it rejects leaves exactly the legal candidates. Compute the new route, S, and original simulate_map result for one active tier4. Retain precisely those with zero base damage and S at least the configured tier3 HP. If this set is nonempty, choosing its minimum by (cost, a fixed lexical key) attains the restricted minimum, because every allowed candidate has been enumerated.

The original-combat calculation establishes the single-tier4 condition. The separate S threshold prevents any standard copy of HP at most tier3 HP from arriving on that fixed map, even in the presence of a gun, by the splash-threshold argument. These two facts do not establish immunity against a mixed roster containing both a tier4 and other entries; gun targeting can change.

A second component check reconstructs the four-round common prefix on the unchanged Engine. At round 5 it removes enough proposed factory purchases to pay for the chosen addition, inserts that building, and submits the resulting legal list against the recorded counter actions. This is a legal one-round counterfactual if every action is accepted, and its observed HP is a component result only. The search's independently funded state alone would not prove affordability.

## Dependencies and scope

The source component, original actions, pathfinding and combat modules, and ../splash_threshold/PROOF.md are dependencies. Exact fixture inputs and numerical outputs are JSON, registered by hash in the search/check receipts. This is an informal finite-enumeration proof supplemented by executable checks. No Lean proof or full-policy improvement is claimed.
