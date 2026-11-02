# Improvement by exact rollout against a fixed policy

## Statement and hypotheses

Consider a finite-horizon deterministic two-player game. Let t be the current
round, s the state, A(t,s) the nonempty set of legal actions for our player,
and b(t,s) a fixed deterministic opponent action. The next state is
F(t,s,a,b(t,s)). States that terminate early are treated as absorbing. Terminal
utility U takes values in a totally ordered set, for example the lexicographic
triple (win/draw/loss value, HP difference, own HP).

Fix a legal deterministic continuation policy a0(t,s). Its value V0(t,s) is
the terminal utility obtained by following a0 against b. At any state, let a
finite candidate set C(t,s) contain a0(t,s). For every candidate a, evaluate
exactly the terminal utility Q0(t,s,a) of taking a now and using a0 afterward.
Choose any action maximizing Q0 over C. It is also permitted to use a0 without
search at some states. Call the resulting policy g.

Then g's terminal utility from every initial state is at least that of a0,
against the fixed opponent b. This does not say that g is optimal among all
policies or robust to an opponent other than b.

## Proof

Work backward from the terminal horizon. At a terminal state the two policies
have the same value U. Suppose Vg(t+1,s') is at least V0(t+1,s') for every
possible next state s'. At state (t,s), write a = g(t,s) and
s' = F(t,s,a,b(t,s)). Determinism and the induction hypothesis give

Vg(t,s) = Vg(t+1,s') >= V0(t+1,s') = Q0(t,s,a).

If search is used, maximality and a0(t,s) in C(t,s) imply
Q0(t,s,a) >= Q0(t,s,a0(t,s)) = V0(t,s).
If search is not used, the same inequality is equality because a = a0(t,s).
Thus Vg(t,s) >= V0(t,s). Backward induction proves the claim at every round.
The argument uses only transitivity of the utility order, so it applies to
lexicographic utility as well as scalar utility.

Along a realized trajectory, the baseline-completion value predicted after
the selected action cannot decrease at the next search. That next search
again includes the baseline action. Therefore successive selected rollout
values, up to terminal settlement, form a nondecreasing sequence.

## Application to this experiment

`bots/counters/forecast_rollout.py` uses a private copy of the archived,
stateless Planner v3 as b. It reconstructs a separate original Engine from
the public observation. Its baseline a0 buys no new attackers, defends against
the private model's current purchase, adds splash immunity from round 14, and
invests remaining gold before round 48. The no-purchase action is always a
candidate. Other candidates buy a bounded pure-tier batch before the same
defense and investment rules. They are filtered by immediate damage, which
may limit strength but does not invalidate baseline inclusion.

Rollouts run to terminal settlement or an equivalent absorbing HP state:
both maps have per-copy splash at least the largest catalog HP, and all the
opponent Planner's template wall cells are already occupied. The baseline
adds no more attackers; both defensive builders leave an already immune map
unchanged. The Planner's attack search cannot damage an immune map. Hence
neither HP changes in that continuation, so settlement utility is already
known. For the splash argument, see [the threshold proof](../splash_threshold/PROOF.md).

The public observation omits the next unused roster ID. Reconstructing it
from current entries may rename future IDs after an empty roster. For the
policies here IDs are irrelevant: purchases append distinct active IDs,
spawn order follows list order, and expiration removes exactly the entries
whose expiration round has passed. An injective renaming of current IDs
therefore preserves combat, gold, HP and subsequent decisions. This argument
would not cover a policy that branches on the numeric ID values.

The theorem applies to exact forecasts of that frozen opponent and to exact
continuations. Forecast errors, a different opponent, a truncated rollout
with a heuristic terminal score, or removing the baseline action fall
outside its hypotheses. The saved matches check these conditions only on
their realized trajectories; they are not a machine-checked proof of the
implementation.

## Dependencies and evidence

Dependencies are finite backward induction, the ordered-utility definition,
and the separately stated splash threshold result. Original-engine
reconstruction checks and match evidence are registered in
verification/evidence.json. No formal theorem-prover source or global
optimality certificate is claimed.
