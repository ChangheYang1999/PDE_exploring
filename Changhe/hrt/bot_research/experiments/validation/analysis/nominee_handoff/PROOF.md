# Transfer of the disclosed handoff counters to two early-defense repairs

## Statement and hypotheses

The test fixes two candidate specifications, P4TNUB and P5TNUBM, and five
already disclosed opponent specifications: the HP-lead trigger from round8
with deadline12; forecast defense from round9 or10; and the visible-roster
control at each of those deadlines. Every condition starts from the
standard balanced initial state and runs in both physical assignments.
The manifest fixes all20 conditions and their input source/data hashes
before any of these matches. Strength assertions are limited to their
original-engine outcomes. No win-rate population or universal dominance
claim is made.

## Verification argument and dependencies

Legality and public-information access of the HP trigger are justified in
hp_handoff/PROOF.md; forecast_handoff/PROOF.md and the correction in
forecast_standard_scope/PROOF.md justify the forecast counter's information
boundary. Here its model remains P5TNUB for both repaired targets, so
exact forecasting is not presumed. Their different histories can produce
model disagreements, which must be retained when checking fresh calls.

For each condition, a fresh process obtains each policy's submissions from
its observation and passes them to the unchanged engine. A completed result
supports the finite outcome claim only after its source hashes, action
acceptance and recorded winner are checked. Replaying every submitted joint
action in a fresh engine verifies the recorded history and winner. Comparing
normalized histories across assignments tests equality on these records;
it does not turn the assignments into independent random samples.

The two forecast/control comparisons at a fixed candidate and deadline
are complete-policy interventions. Their later states need not match and
no one-round causal effect is asserted. A win by a repaired target refutes
that particular old counter's transfer, while a loss supplies a specific
counterexample to superiority over the whole disclosed pool. Neither
outcome proves general improvement or regression. Full-game strength is
empirical and remains open until the declared games and checks finish.

Dependencies are the declared sources, bundled engine/configuration,
original action replay, the existing HP and forecast counter proofs, and
the published target parameters. Pool C is not used.
