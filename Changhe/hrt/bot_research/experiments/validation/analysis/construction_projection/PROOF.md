# Construction can be exact when a stateful action forecast is wrong

## Statement and hypotheses

Consider the fixed Lead10 source in
`bot_research/bots/counters/snapshots/lead_ten_001.py`, with SHA256
`2c3f4f7ec4698e24299801f8cc2fc0cd07bd7d9b6ccece1db8bd627273ce3eec`.
Use planner="v7" and foreign_planner=None. Fix all other policy parameters.
Assume the imported planning and simulation functions return the same output
on equal inputs; caches may save work but must not alter those outputs.

Let two terminating calls receive equal public observations. Their policy
instances have equal parameters and layout, and differ only in the valid
private fields pending and failed. Let C(A) denote the ordered subsequence
of action list A containing build_wall and build_turret actions. Then their
returned lists A and B satisfy C(A)=C(B).

In particular, a fresh clone predicts this construction subsequence exactly
for the stated policy, even when it predicts an incorrect full action list.
The observer must supply the same current public observation as the actual
policy. The conclusion does not assert equality across different histories
or observations.

## Proof

The initial pending check reads public opponent HP and may increment failed.
It then sets pending to None. It does not change the observation, parameters,
layout, initial gold variable, or initially empty returned-action list.

Both calls next plan the layout walls on equal inputs. By the deterministic
helper hypothesis, their wall lists and remaining gold agree. The derived
observation with these buildings therefore agrees as well.

In round 1, the guard or poke branch uses only the common parameters,
remaining gold, layout and observation. It produces equal actions. Its final
factory step contains no construction, proving the claim in this case.

In every later round, mandatory defense, speculative insurance, the large-
threat fallback, the low-tier poke condition and the optional late wall
placement use only the common observation, common parameters and previously
chosen construction. None reads pending or failed. Inducting through this
finite sequence of steps, their action lists, remaining gold and derived
observations agree until the attack step.

The attack step is the first step that reads failed to choose current or
robust attack mode. It may return different minion purchases and may set
pending differently. It appends only buy_minion actions. The only later
step appends buy_factory actions. Neither step appends, removes or modifies
any earlier build_wall or build_turret action. Thus the ordered construction
subsequences of the final lists agree.

## Dependencies and scope

This is a source-level informal argument about the stated snapshot and
helper determinism, not a machine-checked theorem. The v7 planner has no
wall-clock cutoff in its defense entry point. This statement does not cover
Lead13's persistent fortress flag, a different planner with time-dependent
output, mutable external files, or parameter changes during a call.

The result does not make the fresh full-action model exact. Wrong predicted
minion purchases can change the observer's defensive spending. Those changed
actions can then change later public observations, construction and outcomes.
Nor does exact construction alone guarantee that a chosen attack is legal,
profitable, survivable or winning. Full-action correctness under retained
private state has a separate proof in ../stateful_forecast/PROOF.md.

The neighboring verification directory will register the recorded-game
projection audit. That audit checks an explicit finite set of calls; it is
supplementary evidence for the argument, not proof of its universal scope.
