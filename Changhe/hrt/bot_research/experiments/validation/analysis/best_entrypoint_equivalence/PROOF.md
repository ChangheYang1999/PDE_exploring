# Fresh-process equivalence of the published bot entry points

## Statement and hypotheses

Fix the complete source closure recorded for a completed game and the current bundled engine. The candidate is the default policy exposed by both module:decide and module:@make. For every recorded public observation, independently regenerate the direct and factory actions from fresh instances that have received exactly their own preceding observations. The finite claim is that both action lists equal the recorded candidate list, are legal, and leave the supplied observation unchanged.

## Argument and method

A new interpreter handles each game. It imports the direct function and separately constructs the factory policy. The engine starts from its authoritative default initial state. At a prescribed opening round, use the registered candidate prefix actions and call neither policy, matching the independent continuation harness. At every later round, pass separate deep copies of the reconstructed public observation to the two policies. Compare both returned lists with the recorded actions and with each other, check legality on separate owner-local states, and replay both recorded players' actions through the unmodified Engine. Require exact recorded states and terminal outcome at every step.

Induction over rounds establishes the reconstructed observation history. Separate policy instances, fresh interpreters and the explicit skipped-prefix rule establish the intended private-state history. Equality is a finite computational result, not a proof for arbitrary observations or machine loads. Wall-clock planning may cause a genuine disagreement; such differences are retained and make the check fail instead of being silently replayed away.

## Dependencies and scope

The checker verifies result, replay, job, freeze and current source hashes, and records its own source closure. A bounded parent keeps every per-game receipt or timeout and permits resumable disjoint shards. Repeating a policy on a recorded history adds no strength sample. This check establishes entry-point and recorded-policy consistency only; it does not validate all possible actions or prove optimality. The separate engine replay and campaign accounting remain required.
