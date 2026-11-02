# A guarded opening followed by forecast-specific defense

## Statement and hypotheses

Fix the unchanged balanced engine and a controller invoked once per reached
round, starting at round 1. It owns one independent public-policy model M.
In every round, including its opening phase, the controller gives M a deep
copy of the current public observation with the player index exchanged.
M is advanced exactly once and its proposed actions are applied to a private
reconstruction of the opponent's observed state. Assume these calls terminate
and all model proposals are legal on that reconstructed state.

Fix a deadline D in 1..50 and an optional first lead round L in 1..50. The
controller permanently leaves its ScreenedGuardMaze opening on the first
round r satisfying r >= D, or r >= L and its observed HP exceeds the
opponent's observed HP. Before this switch it follows the opening. Afterward
it uses a bounded free-cell turret planner against either the privately
forecast active roster or the currently visible active roster, as selected
by a fixed flag. It buys no new minions after the switch. It spends the
remaining gold on a bounded number of factories through round 47.

Every proposed action is filtered sequentially by the original apply_action
on a private reconstruction of the controller's own observed state. Rejected
proposals are omitted. Assume the delegated opening and bounded planner
terminate and return finite lists. Then every returned action is legal, the
input observation is unchanged, and all decisions use only public observations
and the controller's own legitimate state.

If M additionally has the same initial state and deterministic transition
function as the actual opponent, with no clock, external state, randomness
or differing call sequence affecting either, its forecast roster is exact.
If original combat on the controller's final constructed map and this roster
has no arrivals, the controller takes no base damage in that round. Neither
legality nor model synchronization implies affordability of such a defense,
or that the bounded planner finds it, or that the controller wins the match.

## Proof

The only mode-changing assignment sets the switch flag to true. Its predicate
reads the public round and HP values. Every model input is a newly allocated
copy, and the reconstructed opponent state is private. The model's own state
changes only through those once-per-round calls. No pending real submission
or live opponent object is read. The opening, planner and original action
filter likewise receive only copies or reconstructed states. Thus the input
observation is unchanged and the information boundary holds.

For sequential legality, initially the private own state equals the observed
state. By induction over proposed actions, its state after a processed prefix
is exactly the state obtained by submitting the retained actions. An accepted
action updates that state and is appended. A rejected action leaves the state
unchanged and is omitted. Therefore the next retained action is accepted from
the state that will precede it in the actual submission. Opposing actions do
not alter this player's action legality under the bundled rules. This proves
legality of the complete returned list, including the factory tail.

For exact forecasting, induct on reached rounds. The clone and actual target
start in equal private states, receive equal observations and use the same
deterministic transition. Their submissions and next private states therefore
agree. The next observation is read from the actual public history, so no
assumption about hypothetical intervening play is needed. Applying the equal
submission to the observed opponent state gives the actual active roster.
Construction and purchases affect only the acting player. Thus original
combat on that roster and the controller's actual final map is the same
incoming combat used in the stated no-arrival condition. Zero arrivals mean
zero incoming base damage. This is a one-round conditional statement.

## Scope, dependencies and experiment

This result depends on the public observation contract, original action
rejection semantics, roster activation and combat rules, and the synchronized
model argument in ../stateful_forecast/PROOF.md. Implementation is
bots/counters/forecast_handoff.py. No proof-assistant formalization is claimed.
The current v28 model invokes a planner with a wall-clock cutoff, so the exact
forecast theorem does not apply unconditionally. Per-round prediction agreement
must be measured, and any discrepancy retained.

Hypothesis: after the guarded grower takes an HP lead, defending only against
the target's next predicted purchase can retain a vulnerable-looking map. A
current-map attacker might repeatedly spend gold on attacks that are answered
in the same round. A visible-roster-only version, identical until the switch,
is a causal comparison. These are development counters selected after H10;
none of their conditions belongs to reserved pool C. A better final HP margin
alone does not demonstrate repeated wasted attacks: that mechanism needs a
round-by-round trace of predictions, actual purchases and incoming damage.
