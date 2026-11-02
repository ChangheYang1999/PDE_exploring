# Disclosed handoff counters against frozen fortress v36

## Exact claim and hypotheses

This is a finite empirical transfer test, declared before its games. Its subject is the unchanged frozen fortress v36 with default parameters on the standard initial state of the bundled balanced engine. The five opponents are the already disclosed public-HP handoff at threshold round 8 and the forecast and visible-roster handoffs at rounds 9 and 10. Each condition is played in both physical assignments. The claim to test is that v36 wins every condition. A loss or draw refutes that claim; ten wins confirm it only for the ten recorded conditions.

The forecast counter retains its previously declared P5TNUB model. There is no premise that this model predicts v36, and no prediction guarantee is inferred. Both the counter and the target may use only their public observations and legitimate private state. A wall-clock stopping rule in the target is part of the measured runtime conditions.

## Notation and complete argument

For a condition c, let E(c) be the terminal result returned by the original engine after fresh policies are loaded, and let W(c) indicate that the winner is the target's physical seat. The tested conjunction is W(c) for all ten declared c. A full result row binds both specifications, source hashes, the standard start, the seat, the outcome, action errors, and the replay. Replaying the recorded submissions through a fresh original engine verifies that the log and terminal result agree. Independent strict accounting verifies that every declared condition appears exactly once and has neither errors nor rejected submissions. Source and data archive checks bind the executed inputs. Only after these checks pass does the measured conjunction have the stated finite meaning. Identical deterministic seat-swapped trajectories are a symmetry check, not independent random samples.

Comparison to the earlier fortress v34 campaign is descriptive: it concerns the entire v36 policy change. It cannot by itself identify the causal contribution of economy matching or race selection. Fresh counter shadows separately test that the recorded counter actions can be reproduced from the public histories, and report any clock-dependent or model-dependent discrepancies.

## Dependencies and scope

The observation boundary and handoff legality arguments are in ../hp_handoff/PROOF.md and ../forecast_handoff/PROOF.md. The current engine and the complete input closure are bound in ../../fortress36-handoff-001.json. This is a development test; it neither consumes the reserved final pool nor certifies global optimality, performance on other starts, exact prediction of v36, or load-independent behavior.
