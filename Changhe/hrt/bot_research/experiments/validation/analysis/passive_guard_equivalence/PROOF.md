# Threshold and relevance changes leave the guarded-heavy trajectories unchanged

## Exact statement and hypotheses

Fix the unchanged bundled engine and experiments/lead/v24.py. All planning
subroutines are assumed deterministic on their arguments. Let Q(B,M) be its
Insurer with passive_until=5, passive_bait=B and poke_reactive=M; every other
parameter is the same. Here B is any nonnegative integer and M is either
"turret" or "turret_only". Use identical initial states, player assignments
and a fixed deterministic opposing policy with identical initial private state.

Suppose that, along the Q(40,"turret") trajectory, the opponent has no active
roster entry bought in round2 or later in any decision observation of rounds1
through5. Also suppose that no reached observation in the whole game contains
an opposing entry bought in round2 or later whose configured HP is at most70.
Then every Q(B,M) produces the same submitted actions and complete game
trajectory as Q(40,"turret"). This is a statement about this exact program and
these observation hypotheses, not an equivalence on arbitrary opponents.

## Proof

The two differing parameters are read only in _passive and _reactive.
Initialization stores them but initializes all other private state identically.
The foreign-policy construction uses fixed E20_PARAMS and neither parameter.

In a decision observation with round at most5, the cost sum in _passive is
zero by the first hypothesis. If an opponent turret is present, the function
returns false before testing B. Otherwise it compares0 <= B, which is true
for every permitted B. After round5, the common passive_until=5 makes the
function return false before reading the cost sum or B. Thus all policies
obtain the same passive predicate on every stipulated observation.

The roster test in _reactive is false by the second hypothesis. For both
permitted values of M, the return value is therefore exactly whether an
opponent turret is present. In particular, changing from "turret" to
"turret_only" removes only a disjunct already false on these observations.

Induct on reached rounds. The initial engine and relevant private state agree.
Given agreement before a round, the observations agree, both predicates agree,
and all other executable branches read equal state and parameter values.
Deterministic planning returns identical plans. The policies therefore submit
the same actions and update every relevant private field identically. The
opponent also receives the same observation in the same private state and
submits the same actions. The engine reaches the same next state. The two
roster hypotheses continue to hold because this is the same baseline trajectory.
This induction includes the terminal round and proves the conclusion.

## Application and limits

The no-bait staged grower with growth through at least round5 buys no minion
before round6 and subsequently buys only tier5, whose configured HP is1500.
The fixed heavy-drip schedule buys one tier1 in round1 and later only tier5.
Both satisfy the hypotheses on every reached observation. Their turret
placements, factory counts and economic responses need not be equal to each
other; the claim compares parameter variants against one fixed opponent at a
time. Consequently raising the bait threshold or selecting turret-only
relevance cannot repair P5's recorded staged-guard loss in this exact family.

Verification runs fresh policy instances on observations reconstructed by the
original engine from the two already validated baseline replays, both seats.
Each shadow policy must submit the entire recorded baseline action list on
every reached round, while retaining its own legitimate private state. These
checks reuse existing game trajectories; they are not additional independent
strength samples. Source hashes, predicate-use locations and comparison evidence
are in verification/. There is no machine-checked formalization.
