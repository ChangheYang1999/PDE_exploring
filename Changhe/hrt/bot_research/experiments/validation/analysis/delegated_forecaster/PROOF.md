# A public-clone adversary for the adaptive counter

Written 2026-10-31T17:09:51.786417+00:00, before component or full-game experiments.

## Exact questions

The adaptive route counter now has a stronger defensive continuation, frozen Fortress 38. Test whether a legal public-clone timing adversary can defeat it. Compare the same adversary family against the emergency-template continuation. A success is an original-engine win by at least one declared adversary setting in both physical assignments, with exactly matching public predictions and no illegal actions or errors. The claim remains open until the complete grid is checked. Absence of a win in the finite grid does not prove unexploitable play.

Use the existing StatefulPublicTiming policy, with a private model factory DelegatedRouteSelector and parameters delegate='fortress38' or delegate='template' matching the actual target. Set attack_share=1 and count_cap=200. Cross defense_first in {false,true} with attack-round/tier pairs (3,tier2), (3,tier3), (4,tier3), (4,tier4), (5,tier3), (5,tier4), (6,tier4), (7,tier4), (7,tier5), (8,tier5). Leave all remaining timing-policy parameters at their defaults. There are twenty adversaries per target and two physical assignments, eighty games. The attack is attempted only if it has positive predicted gain. This is targeted development, not held-out validation.

## Informal information-use proof

The private model and real target start from the same factory parameters and initial state. Before each reached standard-game round, the forecaster copies the public observation and changes only its player index to the target's index. The other fields are shared public data. It calls its private target instance exactly once, retaining legitimate private state for the next round. It never accesses the real instance, pending submissions or live engine state.

Conditional on identical deterministic policy transitions, the two target states and actions agree by induction. They agree initially. Equal private states and equal observations give equal actions and next states. The next public state may depend on the adversary's own action, but it is observed afresh and supplied equally to both instances; advance knowledge of that state is not needed. This is the argument in stateful_forecast/PROOF.md. The target imports teammate planners that may use wall-clock cutoffs, so this experiment does not assert that the determinism hypothesis holds under every possible load. Instead it must check every actual predicted action against the original recorded target submission and regenerate both policies on the reached observations.

An exact prediction permits a correct one-round simulation, but does not imply that a winning attack or affordable defense exists. The finite attack schedule, single-tier attack package, factory cap and heuristic defensive planner restrict this adversary. Forecast correctness, component combat agreement and full-game wins are separate claims.

## Components, dependencies and verification

Before declaring full games, run eight original-engine prefixes through round eight: both target continuations, both physical assignments, and timing configurations (round4,tier3,defense_first=false) and (round7,tier5,defense_first=true). Check both observations remain unchanged, the forecaster calls its model exactly once per round, predicted actions equal independently computed target actions, all actions are legal, and original incoming damage equals the forecast residual. Stop a prefix if the engine terminates; report its actual length.

After components pass, pin all transitive source and three exact layout/guard JSON dependencies, the component receipt and this proof in the full-game manifests. Evaluate every declared condition. Use strict accounting, original-engine replay, source/data archive checks, exact forecast diagnostics, fresh regeneration of the adversary and adaptive target, and independent handoff reconstruction. Retain failures as failures, not outcomes. Report W/D/L, HP, rounds, actual purchase counts, prediction mismatches and runtime. The comparison does not modify the installed best bot or its reserved evaluation.
