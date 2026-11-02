# Fixed-deadline controls for the no-strike HP trigger

## Exact comparison

Fix the unchanged balanced engine, standard start and exact target specifications P4TNUB, P5TNUBM and best_v9e. Use the already tested BudgetHandoff controller with strike_count=0, public-budget fraction 1/2, the unchanged screened opening, and deadline H=6 or H=8. Play both physical assignments. These twelve new conditions are development controls for the no-strike TriggeredBudgetHandoff with earliest switch L=6, margin zero and fraction 1/2. The trigger references are reused from the completed triggered-budget campaign; they are not new games.

The empirical hypothesis is that withholding the defensive handoff until an observed lead improves the no-strike policy against P4TNUB and best_v9e. The fixed-H8 setting is an equality control because both reference triggers actually switch at H=8. P5TNUBM is a negative transfer control because its reference trigger never fires. All outcomes, including draws and failures, must be reported.

## Proof obligations and argument

The public-only action legality argument is exactly the one in ../budget_handoff/PROOF.md. With zero strike count the constructor is still within its declared range and no extra heavy purchase is attempted. Removing the strike changes subsequent gold and possibly later target decisions; it is not treated as a local HP adjustment.

For a reference game in which the trigger first fires at H=8, the conditional equivalence proved in ../triggered_budget_handoff/PROOF.md predicts identical actions and complete trajectories for the fixed-H8 control, when both policies face the same deterministic target from the same standard start. The three target standard branches use no wall-clock cutoff, under the no-foreign-construction argument in ../forecast_standard_scope/PROOF.md and its v30 analogue. The source and recorded histories must still be checked. If the histories disagree, report the discrepancy instead of inferring equivalence from final HP.

The H6 and H8 controls differ only in the deadline parameter. Each comparison therefore measures that complete policy intervention for one fixed target and assignment. It cannot attribute any outcome change to a single purchase because all later observations and decisions may change. A victory at H8 does not prove the HP trigger is optimal or that every later handoff improves play. All exact reference histories and new control histories must pass original-engine replay and source/data checks.

## Scope and dependencies

Dependencies are the pinned declarations, original engine and balanced configuration, immutable counter source and exact JSON layouts, frozen imported planners, and exact target sources. The hypotheses concern twelve new games and six reused trigger games only. No held-out opponent or scenario is evaluated, and no pool C condition is used.
