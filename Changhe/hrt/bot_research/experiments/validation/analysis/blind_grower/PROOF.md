# Removing the unused forecast from a grower

## Statement and hypotheses

Use the bundled standard rules, with rounds numbered from 1 through at most
50. Let F be ForecastGrower in bots/counters/forecast_grower.py, with
its first defensive round strictly greater than 50. Let B be FeatureBluff
in bots/counters/feature_bluff.py, with turret_x=0, turret_y=11 and
turret_kind="gun1". Give F and B the same nonnegative turret_round,
growth_rounds, factory_cap and purchase_cap, and the same valid minion tier.
The defaults for the two caps are 2000 and 1000, respectively.

Suppose every forecast call by F terminates without an exception. Suppose
it does not mutate F's supplied observation or affect any action, combat
or opposing-policy output through external state. The clone may keep its
own private state and pure memoization caches. If F and B receive the same
legal observation, their returned action lists agree.

Consequently, against the same deterministic opposing policy with equal
initial private state, F and B produce equal full public trajectories from
the same standard initial state. This conclusion is about returned actions
and game records, excluding policy-private traces and computation times.
It does not assert that either policy wins.

## Proof

F computes a forecast on a deep copy of the public observation. Under the
hypotheses this succeeds and does not change the observation used below.
F and B next reconstruct equal private copies of their own player state
and parse the same rules. Thus their gold, factory counts and buildings
agree before proposing any action.

On the common turret round, both propose the same gun1 at (0,11). Both call
the same original apply_action function. If the proposal is accepted they
append it; if rejected neither appends it and neither player copy changes.
Their player copies and action prefixes therefore still agree.

The defensive branch of F is never reached, since the current round is
at most 50 and its first defensive round is greater than 50. The predicted
actions and predicted enemy state are not read by any later purchase step.

In a growth round, both compute the minimum of the remaining factory cap
and the integer number of factories affordable with current gold. They
append that many buy_factory actions. Each is legal: the cost is fixed
and positive, the precomputed count fits the current gold, and the
original rules impose no other factory-purchase restriction. Hence F's
exception branch and B's early-break branch are both unreachable.

In every later round, both compute the minimum of purchase_cap and the
number of copies of the common tier affordable with current gold. They
append that many buy_minion actions in the same order. The tier is valid,
each cost is fixed and positive, and the count is affordable. The original
rules impose no additional cap on these purchases, so every call succeeds.
Thus the complete returned action lists agree in both cases. F's later
trace append does not change its returned list.

For the trajectory claim, the observations initially agree. Equal returned
actions and equal opposing-policy state give equal actions on both sides.
The deterministic engine then gives equal next public states. Inducting
through every reached round proves equal histories and termination.

## Dependencies and scope

Dependencies are the two named policy sources, forecast_timing.predict,
visible_search.player_from_snapshot, and the original action, configuration
and engine modules. Forecast correctness is not required: its result is
unused here. Forecast termination, legality and absence of external effects
are required. An erroneous predicted action can make F fail even though B
continues, so no unconditional equivalence is claimed.

This argument does not cover defense beginning in round 50 or earlier,
changed gun placement, different purchase caps, or a timed opponent whose
choices can depend on the extra forecast computation. It is an informal
source-level proof. No proof assistant was used.
