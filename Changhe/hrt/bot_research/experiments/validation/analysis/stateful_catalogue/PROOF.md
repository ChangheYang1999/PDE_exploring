# Monotone identification of a stateful public policy

## Statement and notation

Fix the unchanged bundled rules, a standard start, and a finite catalogue H
of deterministic policies with known initial private states and parameters.
The actual opponent is one fixed member h of H. Each policy's action list and
next private state depend only on its current private state and public
observation. No external randomness, clock cutoff, mutable file, process
identity or shared opponent object affects a decision. Assume every predicted
action is legal and every model call completes.

At the start of round 1 initialize one independent clone for every member.
Keep an active set A, initially H. In each reached round, call each active
clone exactly once on a private copy of the opponent's actual public
observation, preserving that clone's private state between calls. Apply its
predicted actions to a private copy of the opponent's public player state.
Record the signature consisting of its factory count, ordered building types
and coordinates, and ordered types of the minions bought in that round.

At the next reached round, before making any new predictions, delete every
member whose recorded signature differs from the observed opponent signature
for the previous round. Deleted members are never reintroduced. Then h is
never deleted. Every prediction made by h's clone is exact. If A becomes the
singleton {h}, the observer knows the actual current action list before
submitting its own action list, by evaluating that independent clone.

This claim concerns public computation. It gives neither hidden-action access
nor a guarantee of sufficient gold to answer the predicted action list.

## Proof

Both sides receive the same two public snapshots, rules and round number.
Changing only the player index therefore reconstructs the opponent's input.
Before round 1, h is active and its clone has the same private state as h.

Assume h is active before a reached round r and its clone has the same private
state as the actual opponent. The two receive equal inputs. Determinism gives
equal actions and equal next private states. Each action affects only the
acting player's own state; interleaving the observer's actions cannot change
the opponent's accepted construction or purchases. Applying the equal action
lists to equal copied public player states therefore gives equal signatures.

Combat and income do not change the factory count or ordered building list.
Minions bought in round r have the configured twelve-round lifetime and
survive cleanup of round r. Their ordered types can therefore be read from
the next observation by selecting roster entries whose bought_round is r.
The recorded signature of h equals this observed signature. If another round
is reached, h is retained. Its clone's next private state still agrees with
h's state. This proves the induction step, including equality of private
states and exact prediction. The induction holds on every reached round.
A terminal round needs no subsequent signature check.

If only h remains, its exact action list is the unique catalogue prediction.
The observer's own response can change the next public state, but the next
induction step uses that resulting state, rather than a predicted future
state. Thus adaptive observer actions do not invalidate the argument.

## Scope and failure cases

Distinct policies can produce equal signatures, including when their action
lists use different interleavings of factories and construction. Equal
signatures do not prove equal policies or private states. The procedure need
not identify a singleton, even over the whole game. It can delete all members
against a policy outside the catalogue, a switching policy, a different
initial private state, or a policy whose clock cutoff changes its output.
A subsequent visible-state fallback is an explicit heuristic and is outside
the theorem. Resetting a deleted clone at a later round does not satisfy the
hypotheses.

The bounded construction and attack searches performed after prediction are
also heuristics. A nonempty active set does not itself imply that a chosen
construction protects against all its forecasts. Their residual damage must
be measured separately. No strength, convergence or universal dominance
claim follows from this proof.

## Dependencies and implementation evidence

The argument uses the bundled action isolation, observation, roster cleanup
and construction persistence rules, established in the rules audit. It
combines the purchase-signature argument in model_identification/PROOF.md
with the clone induction in stateful_forecast/PROOF.md, removing the earlier
restriction to state-free or directly reconstructed private state.

The intended implementation is bots/counters/stateful_catalogue.py. Component
checks will compare each true clone's actions with a separate actual policy,
verify signature deletion and legal actions on the unchanged engine, and
exercise empty-catalogue fallback. Evidence is registered in verification/.
This informal argument was written before implementation. No machine-checked
proof is claimed.
