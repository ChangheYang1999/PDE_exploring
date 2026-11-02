# A public opening selector with a common prefix

## Statement and hypotheses

Consider the unchanged deterministic engine, a fixed initial state, and a
fixed opposing policy whose private state is deterministic and whose decisions
depend only on its observations and its own state. Let A and B be two
policies whose decisions after round1 depend only on their current public
observation and fixed parameters. Suppose A and B submit the same action list
in round1. Define C to submit this common list in round1. At round2, C chooses
A or B using any deterministic function of its round2 observation and retains
that choice for the rest of the game.

Then the complete trajectory of C against this opposing policy is exactly
the trajectory of the chosen arm against the same opposing policy, from the
same initial state and with the same player assignment. Trajectory means
submitted actions, accepted actions, observations, combat results and outcome.
The claim applies separately to each initial state for which the common-prefix
hypothesis holds. It gives no win guarantee and no identification guarantee.

## Notation and argument

Write s_r for the engine state just before round r and z_r for the opponent's
private state. The initial values are equal in the selector game and either
arm's game. In round1 the selector and both arms submit the same list by
hypothesis. The opponent sees the same observation and starts in the same
private state, so its submitted list and its next private state are also the
same. Deterministic engine transition therefore gives identical s_2 and z_2.

Let D be the arm selected by C from this common round2 observation. At round2,
C and D submit the same list because D needs no unrecorded history or private
state. Again the opponent receives the same observation in the same private
state, so the resulting engine and opponent states agree. Repeat this argument
at each later reached round. The finite game ends with the same outcome. This
is induction on the round number and includes simultaneous hidden submissions:
neither policy has observed the opponent's pending round2 actions.

The proof would fail for a stateful arm whose necessary round1 state had not
been advanced. It would also fail for an opponent using unrecorded randomness,
wall-clock branches with different outcomes, process-global interactions, or
information outside the stipulated observation interface. Recorded equality
is therefore checked separately from this conditional argument.

## Concrete selector and scope

Arm A is MazeGrower on the empty layout, growth through6, one tier1 bought in
round2, then all affordable tier5 after growth. Arm B is StagedGuardMaze on the
same layout, growth through6, no bait, with splash guards in rounds4 and6,
then the same tier5 rule. Their round1 list on the standard start is five
factory purchases. Both arms reconstruct local state from each observation;
neither maintains an action history. The selector chooses A if the opponent's
round2 public roster is exactly three tier1 entries all bought in round1;
otherwise it chooses B. It resets on round1 when reused for another game.

The choice rule was selected after inspecting the opening counts and counter
outcomes of seven development policies. It is not a held-out result or a proof
of strategy identification. In particular, changing an opponent's first-round
roster can switch arms even when its later policy remains almost unchanged.
A predeclared stress test measures that fragility. No reserve-pool information
is used.

## Dependencies and evidence

The argument uses the engine's deterministic observation/transition contract
and the implementations of maze_grower.py and staged_guard_maze.py. Source
hashes, first-round equality checks, input-immutability checks and original
engine runs are recorded in verification/. There is no machine-checked proof.
The full-game hypothesis and its empirical verdict are separate from this
conditional trajectory theorem.
