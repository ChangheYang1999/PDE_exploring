# A public-HP trigger for a one-way defensive handoff

## Statement, hypotheses and notation

Fix the bundled balanced engine. At each reached round r, let h be the
controller's publicly observed base HP and q the opponent's publicly observed
base HP. Fix a deadline D in 1..50, an optional lead threshold L in 1..50,
a margin m >= 0, an optional panic threshold P >= 0 and a first panic round
J in 1..50. Define the trigger by the disjunction

    r >= D,
    L is enabled and r >= L and h > q + m,
    P is enabled and r >= J and h <= P.

A controller starts in opening mode. On the first reached observation
satisfying the trigger it permanently enters defender mode. The opening
is the fixed ScreenedGuardMaze with guards in rounds4 and6 and, if that
round is reached before the switch, its round9 gun extension. The defender
is one fresh frozen F34 instance, initialized once at controller creation
with attack=none and round1_poke=0. It is not called before the switch.

Each selected delegate receives a deep copy of the current observation.
For its returned finite list, reconstruct the acting player's observed
state and apply the original apply_action sequentially. Retain exactly
accepted actions. Assume the delegated call terminates and returns a finite
list. The bundled engine rejects actions without changing the acting state,
and all allowed actions affect only that player's state.

Then: (1) the switch is one-way and depends only on public observations;
(2) every returned action is legal sequentially from the observed own state;
(3) the supplied observation is unchanged by the wrapper and its delegate;
(4) when L and P are disabled and D=10, the output equals GuardHandoff(H=10)
on every common public history, conditional on identical delegate outputs
and legal opening outputs.

## Proof

Before each call, the stored mode is either opening or defender. The only
assignment changing it sets defender when the displayed trigger is true.
There is no assignment back to opening. The trigger reads only r,h,q and
fixed parameters, so it cannot read the hidden current-round submission.
Both delegates receive only a copy of the public observation, and their own
state evolves only on their respective calls. These facts prove (1).

Initially the private reconstructed state equals the acting player's state
in the observation. Induct over the delegate's proposed list. If an action
is accepted, the original transition updates this private state and the
action is appended. If rejected, the bundled rejection semantics leave the
state unchanged and the action is omitted. Therefore after each prefix the
private state equals the state produced by submitting the retained prefix.
Every retained action was accepted at exactly that state. This proves (2).
A delegate can mutate only its deep copy; reconstruction and transitions
also operate on private objects. The wrapper itself writes only its stored
mode, trace and newly allocated objects. This proves (3).

For (4), no trigger can fire before round10, and the deadline fires there.
Thus the same delegate receives the same observation sequence as in the
fixed H10 wrapper, including its fresh defender's first call in round10.
Inductively, identical delegate outputs give identical proposed lists.
Legal opening lists survive the added filter unchanged; defender lists use
the same filter as GuardHandoff. Hence the returned lists agree. A shared
wall-clock cutoff can violate the identical-output hypothesis, so the
statement is deliberately conditional rather than a determinism claim.

## Dependencies, implementation and empirical scope

Dependencies are td_game/actions.py (validate before mutation), the public
observation contract, ScreenedGuardMaze, GuardHandoff and frozen F34. The
implementation will be bots/counters/hp_handoff.py. Evidence is kept in
verification/ beside this proof. No proof-assistant formalization is claimed.

Conjecture: abandoning the open growth phase after taking a public HP lead
can preserve its successful timing attacks, while a low-HP trigger avoids
some early-rush losses. Compare fixed deadlines8,9,10, a lead-from8 rule with
deadline12, a panic600 rule with deadline12, and their combination. The
newest lead candidate and seven disclosed strong/simple target families
will be compared in both seats. These are counter-informed development
conditions. The trigger cannot predict an unseen strike. No winning claim
or superiority over fixed H10 follows from the proof.
