# A one-way continuation after catalogue rejection

## Exact statement and hypotheses

Let C be the stateful catalogue controller described in
`../stateful_catalogue/PROOF.md`, with fixed parameters and a fixed initial
catalogue. Let F be another observation-only policy with a deterministic
constructor and private state. Define C_F as follows. While the catalogue
is nonempty, C_F performs C's normal prediction and elimination step. If
that step leaves a nonempty catalogue, it returns exactly C's actions.
When the catalogue first becomes empty, C_F creates a fresh F, passes the
current observation to it, and returns F's actions. On every subsequent
reached round it calls this same F once on the new observation. It never
reintroduces a rejected catalogue member or changes back to C's actions.
The initial elimination round may perform an unused defensive computation;
assume that computation has no external effect.

For any fixed deterministic opponent and fixed initial game state, C_F and
C have identical complete action and observation prefixes strictly before
the first empty-catalogue round in their coupled play. If the opponent is
a fixed member satisfying every hypothesis of the catalogue-retention
proof, the catalogue never becomes empty, and the complete game trajectories
of C_F and C are identical. This last claim includes ending round, HP,
accepted actions and outcome.

After a switch in round s, the continuation receives exactly the observation
sequence of the actual game from s onward, with its documented fresh private
state. It is called once on every reached round and never before s. This is
not a claim that its state equals a hypothetical F that played rounds 1
through s-1, or that its actions improve on C's fallback.

## Proof

Before the first decision, the two catalogue states and game states agree.
Suppose they agree before a round in which their common elimination step
retains at least one member. They call the same deterministic clones on
equal copied observations and obtain the same predictions, catalogue and
updated clone states. By construction C_F returns C's exact action list.
The opponent also receives equal observations and has equal private state,
so returns equal actions. The unchanged engine therefore produces equal
accepted actions, combat, income and next observations. Induction proves
the prefix assertion.

If the true opponent satisfies the catalogue-retention hypotheses, its
member is never removed. The switch condition is therefore false on every
reached round. Applying the preceding induction through termination proves
complete trajectory equality.

For a switch, F is constructed exactly when the first empty set is observed.
The current observation is passed to it once. The continuation reference
persists thereafter, and the round-order guard permits only the next round
on the same player assignment. Thus its kth call uses the actual observation
in round s+k-1 and the private state resulting from its preceding k-1 calls.
There are no further catalogue calls after rejection because no member
remains. The empty-set trace can be extended without evaluating any clone.
This proves the stated call and state protocol.

## Scope and dependencies

The prefix claim assumes deterministic controllers and an opponent without
external effects. The full-trajectory claim additionally assumes true fixed
catalogue membership. An outside policy can imitate a member for many rounds,
so the switch need not happen promptly or at all. A fresh continuation can
be unsuitable for the inherited buildings or current round. There is no
value, safety or recovery guarantee after a switch.

The implementation will use the frozen economy20 policy as F, with its
foreign-map re-planning and documented fresh-state semantics. Its constructor
and parameters will be recorded in the experiment declaration. A separate
component check will compare every continuation action with an independent
fresh F advanced on the same actual observations. An exact-parent comparison
will cover the nonempty-catalogue branch. Full-game paired comparisons are
separate empirical evidence.

Dependencies are the catalogue-retention proof, deterministic unchanged
engine transitions, and the one-way-switch argument in
`../falsification_fallback/PROOF.md`. No formal proof assistant is used.
This argument was written before the new continuation wrapper.
