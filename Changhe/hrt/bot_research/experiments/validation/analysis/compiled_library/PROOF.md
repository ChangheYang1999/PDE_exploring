# A compatible library of public game trajectories

## Statement, notation and hypotheses

A plan is a finite sequence of pairs (s_r, a_r), indexed by rounds starting
at one. Here s_r is the complete public observation normalized by putting the
acting player first and deleting only the player names; a_r is its complete
ordered action list. Each plan comes from a complete legal recorded game.
The normalization and engine assumptions are those of
../compiled_policy/PROOF.md.

Two plans conflict if there is a round r at which all their observations and
actions before r are equal, their round-r observations are equal, but their
round-r actions differ. If observations first differ, the plans do not conflict,
regardless of later coincidences. Ending one plan before another also causes
no conflict. A library is compatible when no pair of its plans conflicts.

The library policy starts with all plans active. At round r it removes every
active plan whose round-r observation is absent or differs from the actual
normalized observation. If none remain, it permanently uses a fixed fallback.
Otherwise it submits the common action of the remaining plans. Returned action
lists are copies, so the caller cannot mutate the stored library.

For each plan in a compatible library, suppose a fresh game starts at that
plan's initial state up to names and player exchange and faces the same
opponent policy with the same initial private state. Suppose the opponent is
deterministic and equivariant under these exchanges and renamings. Then the
library policy reproduces that plan's complete game and never falls back.

## Proof

Any two plans still active in round r have matched the same actual normalized
observations in every round through r. If previous submitted actions were
common to all then-active plans, the two plans also have equal prior actions.
Compatibility therefore implies equal round-r actions. At round one the prior
history is empty. Induction proves that the policy's common-action choice is
well-defined in every round before fallback.

Fix the particular recorded plan in the statement. It is initially active.
Suppose the fresh trajectory agrees with this plan through round r-1. The
actual round-r observation is its stored observation, so the plan remains
active. The common submitted action equals its stored action. The opponent's
observation and private state also agree with the recorded ones; determinism
and equivariance give the recorded opposing action and next private state.
The unchanged deterministic engine therefore gives the recorded next state.
Induction reaches the recorded terminal round without eliminating this plan
or entering fallback.

## Selecting a compatible sublibrary

Construct a finite graph with one vertex per plan and an edge for every
conflicting pair. A vertex subset is a compatible library exactly when it
contains no edge. Exhaustive enumeration of all subsets therefore finds a
maximum-cardinality compatible library: test every subset and retain a largest
edge-free one, with a declared deterministic tie break. This is a finite search
statement, not a claim that the selected library is strategically optimal.
Two plans with identical normalized trajectories can remain separate vertices;
they do not provide distinct behavioral evidence.

## Scope and verification

Only fixed own policy data and actual public observations are used at runtime.
No current hidden opposing action is read. Compatibility concerns the recorded
histories; a different opponent can deviate while still sharing a prefix.
Fallback then occurs only after a public mismatch and gives no recovery or
strength guarantee. Wall-clock-limited opponents do not meet an unconditional
determinism hypothesis. Fresh reproductions against them remain empirical.

The source games, exact conflict graph, selected subset, source hashes, fresh
policy games, guard checks and replay checks will be listed in
verification/evidence.json. This argument precedes implementation. No formal
machine-checked proof is claimed.

## Initial-observation obstruction

If two recorded plans have the same initial normalized observation and different
first action lists, a deterministic observation-only policy with one fixed
initial private state cannot reproduce both. It must output one action list on
that shared input. This excludes simultaneous trajectory reproduction only;
it does not show that one policy cannot win both games using another trajectory.
