# Exact public forecasting through a known legal opening

## Statement and hypotheses

Use the bundled engine and a fixed player index s. Let P be a deterministic
policy with known initial private state. Its only inputs are its own private
state and the public observation. Let O be a known deterministic opening
function of the public observation. O returns either a legal action list or
None. Define the composed policy W as follows: compute O on a private copy
of the observation, invoke P exactly once on the observation in every round,
and return O's list when present or P's list otherwise. Neither call fails.
The returned opening list need not equal P's discarded list.

A forecaster holds a distinct W with the same P and O parameters and initial
state. It calls that instance exactly once each round, from round 1, with a
copy of the actual public observation for player s. Then its forecast equals
W's actual submitted actions in every reached round, and the two copies of
P have equal private state after each call. This covers both symmetric and
asymmetric openings when O uses the actual player index in the same way.

## Proof

Initially the two copies of P have equal private state. Assume they still
do before round r. Both calls to O receive equal observations, so either both
return None or they return equal action lists. Both copies of P also receive
equal observations and equal private states. Determinism gives equal proposed
actions and next private states. The selection rule therefore returns equal
submitted actions. It also preserves equality of P's state, regardless of
whether those proposed actions were discarded. This proves the induction
step. In the next round the forecaster copies the actual public observation;
it does not assume that the discarded action list changed the game. Induction
from round 1 proves the statement.

## Dependencies and scope

This specializes the proof in analysis/stateful_forecast/PROOF.md to a known
composition. It uses the engine's shared public observations. It does not
assume that a target starting after the opening has the same state as a target
called during the opening. Those are different evaluation protocols.

The implementation in bots/counters/prefixed_v4.py follows the call-through
protocol of harness/match.py's TimedBot: the opening is computed before the
underlying call, and the underlying call still occurs in opening rounds.
Unlike that adapter, it does not suppress underlying exceptions. Successful
checked games have no such exceptions. Openings come from the unmodified
harness/scenarios.py; both the model and actual target use the same function.
A bounded component check must verify call counts, exact forecasts, accepted
actions and agreement with the adapter before full-game claims are made.

This result proves conditional forecast exactness, not strength or scenario
robustness. The composed policy is a known-development-opening policy, not a
claim that a general bot can infer an arbitrary unseen opening. No hidden
opponent state, pending submission, live engine instance or call stack is read.
No proof assistant or modified engine is used.
