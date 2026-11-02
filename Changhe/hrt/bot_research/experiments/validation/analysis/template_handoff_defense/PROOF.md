# Joint wall and turret planning after the public lead trigger

## Exact intervention and hypothesis

The baseline is GuardedRound4Trigger with one round-four tier4, a corner gun1, earliest public lead trigger in round5, and a forecast using half the opponent's public gold. Its opening, trigger, forecast and factory policy remain fixed. The free mode immediately delegates to that baseline. The template mode replaces only the defensive planner after the trigger with frozen-v7 plan_defense, allowing guns and requesting its best affordable partial answer. Unlike free_plan, this planner considers wall prefixes together with splash placement, including route-changing cells. It is not an exhaustive map search.

The empirical hypothesis is that joint construction repairs some transfer losses without losing the measured nominee wins. Neither the planner nor the forecast proves that hypothesis. A forecast includes the current active roster and that roster followed by a homogeneous purchase in each tier. It excludes mixed purchases, and the capped budget forecast need not contain the actual purchase. A zero-leak result on those scenarios does not imply universal defense.

## Public observation and legality argument

Before the first round at or after lead_from in which own HP exceeds opponent HP plus the declared margin, return exactly the inherited opening decisions. Thus the opening actions, state and trigger time match the baseline against the same opponent under equal observations. Once triggered, retain the trigger round forever. Compute the active opponent roster from the public snapshot using the original roster lifetime rule. For each tier compute min(max_new, floor(floor(opponent_gold*numerator/denominator)/tier_cost)) and append that many copies after the visible roster. These operations use only public observations and declared constants.

Give a deep copy of the observation, available own gold and these scenarios to plan_defense. Reconstruct the owner state from the original public snapshot. Validate each proposed action sequentially with the unchanged apply_action, recording only accepted actions and retaining the updated local owner state. Before round48, buy up to max_factories additional affordable factories. Each factory is again validated and a rejection is an error. No post-trigger minion purchase is proposed. Induction on the accepted prefix proves that each submitted action is legal in the actual owner state: both start identically and apply the same local transition. The opponent's simultaneous actions do not modify that owner state. Copies and local reconstruction leave the supplied observation unchanged.

The free mode immediately invokes the original policy and introduces no gameplay state change. It therefore has exactly the old complete history against the same opponent, conditional on deterministic opponent decisions and equal observations. This is checked directly rather than presumed for wall-clock-limited opponents.

## Evaluation and scope

Declare 32 standard-start games before running them: eight named development targets, free and template planners, and both player assignments. Check all eight-round prefixes for legal actions, immutable observations and the trigger invariant. Keep full original-engine histories, strict outcome accounting and frozen source/data archives. Reconstruct every counter decision on the recorded original-engine observations and compare the returned action lists. Compare the free controls with the earlier half-budget guarded-strike histories. Report all declared conditions and any errors, including failures or regressions. Swapped deterministic assignments are reproducibility controls, not independent random samples. Pool C and its scenarios remain unused.
