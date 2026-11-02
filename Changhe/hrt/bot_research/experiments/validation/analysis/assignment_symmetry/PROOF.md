# Player-assignment symmetry

## Statement and scope

Use the unchanged bundled engine and balanced configuration. Consider two policies A and B with private state initialized identically whenever that policy is instantiated. Assume:

1. A policy reads only its own observation and its private state. It does not inspect wall time, process identity, shared module state, a mutable external file, or the other policy's private state.
2. Renaming player identifiers 0 and 1 in an observation and swapping the two player snapshots does not change the actions returned by the same policy. The policy uses `observation['player']` only to locate itself and its opponent. Its private-state update has the same invariance.
3. A policy's random choices, if any, are fixed as a policy-specific stream that is preserved when the policy changes player assignment.
4. The two runs begin in the standard symmetric engine state and use the same policies, configuration, and random streams.

Then the run with A as player 0 and B as player 1 is obtained from the run with B as player 0 and A as player 1 by swapping the player-indexed states and winner. Per-policy action results agree after excluding the global action-order annotation. Round counts agree, and each named policy has the same HP, gold, buildings, roster, and action outcomes in both runs. Wall-clock runtimes and textual names need not agree.

## Notation

Let S be a settled engine state, including both player states, current round, and result. Let tau(S) exchange the two player states and replace a non-null winner w by 1-w. Apply tau to observations and player-indexed event lists in the same way. Null winners remain null. The global `order` number attached to an action is not part of the claimed event symmetry: swapping player priority can change it.

Let a and b be the two submitted action lists. Let F(S,a,b) be the next settled state produced by one call to `Engine.play_round`, ignoring physical runtime.

## Argument

The standard initial state is invariant under tau except for names. The names do not affect the engine rules.

In any state S, the observation for A in the first run becomes A's observation in the swapped run after applying tau. By the policy hypotheses, A returns the same action list and makes the same private-state update in both runs; likewise for B. The adapter makes private deep copies before invoking either policy, so permitted observation mutations cannot affect the other policy's input.

Each build, minion purchase, or factory purchase changes only the submitting player's gold, buildings, or roster. Its legality depends only on that player's state and the common configuration. Consequently, interleaving the two players' actions in the opposite order leaves each player's accepted and rejected action subsequence unchanged. No legal action in the current catalog reads the opponent's gold or map.

The combat routine on one map reads the attacker's roster, the defender's buildings, the common configuration, and the defender's route. It changes only that defender's HP and returns combat totals. It does not use either base's current HP to choose spawns or attacks. The engine settles both maps before determining a terminal result. Hence reversing the order in which the two map computations are performed only swaps their outputs, even if a base has already reached nonpositive HP during the first computation.

Income, roster expiration, and snapshot production are playerwise calculations from those action and combat results. Winner determination is symmetric: exactly one destroyed base loses, two destroyed bases draw, and at the round limit the higher-HP base wins with equal HP drawing. Therefore

F(tau(S),b,a) = tau(F(S,a,b)).

Induction over rounds proves the statement, including the first terminal round.

## Dependencies and verification evidence

The argument depends on `td_bots/protocol.py`, `td_game/actions.py`, `td_game/combat.py`, and `td_game/engine.py` as bundled at the initial inventory. The source hashes are recorded in `runs/validation/integrity-start.json` relative to the research directory.

The 144 ordered matches in `runs/validation/archetype-round-robin-001.jsonl` provide a finite check for the initial 12 private-state, identifier-invariant policies. This check cannot establish the theorem for arbitrary policy code.

## Exclusions

A policy that seeds randomness with the player identifier, shares module state with its opponent, or branches on names violates the hypotheses. Scripted asymmetric openings also violate the symmetric-start hypothesis. Both assignments remain useful tests because they can reveal precisely these implementation asymmetries. Repeating identical deterministic conditions does not add independent evidence about strategic strength.
