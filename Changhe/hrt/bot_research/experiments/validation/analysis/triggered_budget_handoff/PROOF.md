# Public-HP-triggered budget defense

## Statement and hypotheses

Take the unchanged balanced engine and the fixed BudgetHandoff opening and defensive planner. Fix an earliest switch round L strictly after the declared heavy-strike round, and a nonnegative integer margin m. Let h_self and h_enemy be the two HP values in the decision observation. Stay with the opening until the first observed round r>=L with h_self>h_enemy+m, then permanently use the budget defender. If there is no such round, keep the opening for the whole game. The optional round5 tier4 purchase still precedes this switch test's eligible rounds.

The controller's switch depends only on public observations and its own one-way state. Its action list remains legal in the original engine. If its first switch is H, every action through the completed game is identical to the fixed-deadline BudgetHandoff(H) on the same observation history, with all other parameters equal. This is a conditional policy equivalence, not an assertion that the condition is met in every game.

The empirical hypothesis is that refusing to stop attacking while behind improves transfer of the earlier fixed handoff counter. The first matrix fixes L=6 and m=0, switches the round5 tier4 count between0 and1, and uses budget fractions1/2 and1. It tests P4TNUB, P5TNUBM, fortress36/37, best_v9e and lead8 in both seats, standard start. None of these targets or conditions is reserved pool C.

## Proof of the policy claims

The state is initially unswitched. At each decision the round and both HP values are present in the observation. Testing the two inequalities therefore uses no private information. The transition is one-way: after its first successful test the switch round is stored and never changed. Before transition, the opening branch is selected; after transition, the defensive branch is selected. The same owner-local validation and action-subsequence argument as in BudgetHandoff establishes legality, including any early heavy purchase and the later factories.

For conditional equivalence, use induction on decision rounds along a common observation history. Before H, both the triggered policy and the deadline-H policy select the opening, which receives the same observation and has been advanced the same number of times. At H and later they both select the budget planner with the same parameters and snapshot. Its finite hypothetical rosters, deterministic greedy search, action filtering and factory purchases agree. Thus their returned action lists agree. The observation-history assumption is satisfied for two whole games against the same deterministic opponent with the same initial state, as long as the trigger first fires at H: identical earlier actions produce identical engine states and opponent observations. A target's wall-time cutoff prevents an unconditional claim of whole-game equality under arbitrary machine load; recorded trajectories must still be compared.

## Limitations and dependencies

A positive HP lead is not a proof of future survival. The defender still covers only a finite set of pure-tier extensions, not all affordable mixtures. The switch can occur too early, its defense can waste income, or it can never occur. An already bought roster remains active according to the original lifetime rules; switching stops new attack purchases but does not remove earlier entries. Sources are BudgetHandoff, ScreenedGuardMaze, the frozen free_plan routine, original actions/engine/state/combat, and exact JSON layouts. Full original-engine games and separate fresh policy checks establish only their explicitly reported conditions.
