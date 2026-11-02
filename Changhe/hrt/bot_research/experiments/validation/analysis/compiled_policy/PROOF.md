# Compiling one public game trajectory into a contingent policy

## Statement and hypotheses

Consider the unchanged deterministic engine and a recorded complete legal game
of R rounds. Let c(o) normalize a public observation o by putting the acting
player first, dropping the two player names, and retaining the round, complete
rules and all other player snapshot fields. For round r of the recorded game,
store the exact value s_r = c(o_r) and the acting player's complete ordered
legal action list a_r. Equality below means structural equality of these data,
not equality of a hash.

Define a policy C as follows. Until its first mismatch, if its round is r and
c(o) = s_r, it submits a fresh copy of a_r. At its first mismatch, or outside
rounds 1 through R, it switches permanently to a fixed fallback F. The fallback
receives the actual observation and maintains only its own legitimate state.

Assume the replay begins in the recorded initial state up to player exchange
and player renaming. Assume the opposing policy has the same initial private
state and is deterministic and equivariant under these exchanges and renamings.
Assume the engine's transitions are likewise equivariant. Then C never switches
before the recorded terminal round and the complete game agrees with the
recorded trajectory up to that exchange and renaming.

## Proof

At the first round, the initial-state hypothesis gives c(o) = s_1. Thus C
submits a_1. The opponent sees the corresponding recorded observation and has
the corresponding recorded private state; determinism and equivariance give
its recorded action list and next private state. The engine receives the same
ordered actions under the stated identification, hence gives the recorded next
state and outcome.

Inductively suppose the statement holds through round r-1 and the game has not
terminated. The acting player's observation is s_r after normalization, so C
has no mismatch and submits a_r. The opponent's observation and private state
still agree with their recorded values, so its next action and private-state
transition agree. The engine therefore yields the recorded round-r state and
outcome. This proves the statement through R, including its terminal outcome.

The engine's action application changes only the acting player's own state;
both combats and both income settlements finish before the terminal test.
These facts support exchange equivariance, as discussed separately in
../assignment_symmetry/PROOF.md. A policy that reads names or player numbers
strategically need not satisfy the policy hypothesis.

## Scope and limitations

The table contains public pre-decision observations and this policy's actions.
It contains no pending opponent submission. The policy need not evaluate or
import the opponent's source during a game. It consults only its own fixed
policy data and the received observation.

There is no guarantee against a different opponent: that opponent can choose
different hidden current actions before a mismatch becomes visible. The exact
state guard does not anticipate such a change. After a mismatch the conclusion
is only that C stops consulting the recorded plan for action selection and uses
F. A fallback can still be slow, illegal, or strategically poor unless checked
separately. On-trajectory legality follows from equality with the recorded own
state; fallback legality is a separate obligation.

The initial application compiles the measured round-ten attack against frozen
fortress15. It must be replayed with actual policy calls in both assignments;
replaying saved actions alone would not check the implementation of C. New
opponent tests are development conditions, not held-out final validation.

The argument is informal. Verification/evidence.json will identify the data,
implementation and completed checks; importing the table is not a proof of the
hypotheses or of strength outside the recorded trajectory.

The particular fortress15 implementation also has a wall-clock planning cutoff.
Consequently, the deterministic-opponent hypothesis is not asserted for every
future execution of that code. Matching fresh games establish only the observed
reproduction. If a timed decision changes, the compiled policy can encounter a
mismatch on the next round and use its fallback.
