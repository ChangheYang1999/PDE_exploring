# One-way fallback after model falsification

## Exact statement and notation

Consider the finite-policy identifier in the separate model-identification
result. At each round it maintains a nonempty set of deterministic opponent
models. It predicts each surviving model's current action on the actual
public observation and stores the resulting purchase signature. At the next
round it retains exactly the models whose stored signatures agree with the
observed signature. Let I be its own decision rule, including any fixed
first-round action override.

Define W to use the same rule I while at least one stored signature agrees.
Immediately before the first call for which none agrees, W permanently
switches to a second, observation-based policy F. It also switches if a prior
call left no functioning model. The switch is one-way, and W never calls I
again after it switches.

Suppose the actual opponent is a fixed member of the initial catalogue; its
predicted signatures are exact on every history reached by W; reconstructing
public state is sufficient for those predictions; and model evaluation does
not raise an exception. Then W never switches and produces exactly the same
own actions and game trajectory as I from the same initial state.

Without the membership and exactness hypotheses, no trajectory or strength
claim follows. Regardless of the opponent, after a switch W makes zero
catalogue evaluations and exactly one call to F per subsequent decision.
This bounds the number of policy calls, not the time or memory used by F.

## Proof

Initially W and I have the same models, internal state and actual observation.
The actual model is in that set. Their first actions and saved predictions
therefore agree, including the first-round override.

Assume the trajectories and identifier states agree through round r, and the
actual model is still retained. By exactness, its saved purchase signature
agrees with the signature observed at round r+1. Thus the wrapper's switching
condition is false. The ordinary identifier retains this model by the
model-identification lemma. W calls I on the same observation and state, so
the actions, saved signatures and next game state again agree. Induction over
the finite game proves the first assertion.

For the second assertion, once W sets its fallback flag, the definition of
its decision rule sends every later observation directly to F and does not
call I. This gives the stated policy-call count. It does not bound the cost
of that call, and it does not prove that F can recover from the buildings or
spending chosen before the switch.

## Dependencies, scope and verification

Dependencies: finite induction and the exact purchase-signature identification
lemma in ../model_identification/PROOF.md. A wall-clock-limited replica need
not satisfy exactness, and an out-of-catalogue opponent may continue to match
some signature for many rounds. Fallback therefore does not certify that a
retained model is the true opponent.

Implementation: bots/counters/falsification_fallback.py. Evaluation evidence
will be listed in verification/evidence.json. This is an informal proof of
the stated controller property; no machine-checked formalization is claimed.
