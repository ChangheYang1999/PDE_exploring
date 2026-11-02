# Delayed switches cannot be rejected before they become observable

## Statement and hypotheses

Fix the unchanged deterministic bundled engine, standard initial state, and
one deterministic observing policy Q whose decisions use only its public
observation and private state. Let P be a deterministic public policy with a
fixed initial private state. For an integer k >= 2, define S as follows. In
rounds strictly before k it advances a private instance of P exactly once on
its actual public observation and submits P's actions. In round k it advances
P once but may submit another legal list. After k it follows any specified
observation-based continuation. All calls complete and there are no effects
from a clock, external randomness, shared policy state or mutable files.

Compare the match Q versus S with Q versus P, using the same player assignment.
If a round r <= k is reached, their complete public histories before the
round-r decisions agree, and Q's action list in that round agrees. In
particular, no test based on those histories can distinguish S from P before
the first substituted submission is resolved. The statement also permits
both matches to terminate before k, in which case their entire histories
agree and the switch is never reached.

Further suppose Q uses the retained-clone procedure in result 30, with P in
its initial catalogue. In the Q versus S match, the P clone remains active
through the beginning of round k, and its predicted actions in round k are
exactly the actions of S's internal P instance before substitution. If the
substituted actions have a different purchase signature, P is removed at the
beginning of round k+1, provided that round is reached. Earlier rejection of
P is impossible under these assumptions.

## Notation and proof

A history contains the two public snapshots after each completed round,
including the initial snapshots. A policy state is its own private memory;
it is not an engine or opponent object. Let h_r denote the history before
round r. Both matches have the same h_1 and the same initialized Q and P
states. Assume the histories and those states agree before r < k. Q receives
the same observation and returns the same actions and next state. S advances
its P instance on precisely P's input and submits the resulting actions, so
those actions and next P states also agree. The deterministic engine applies
the same two submissions to the same state and produces the same next
history and terminal result. This proves the induction through the first
reached round k. At its beginning Q still has the same observation and state,
so Q's submission is the same even though S may now substitute its own list.

For the catalogue statement, until k the actual submitted P actions equal
those of the retained clone, by the same deterministic state induction. Their
public purchase signatures therefore agree after every round before k, and
P is never deleted. In round k, the clone and S's internal P instance still
have equal inputs and states, so they produce the same pre-substitution
proposal. A differing submitted signature becomes visible in the next
observation. The prescribed deletion rule then removes P at k+1. This does
not imply that every other catalogue member is also removed.

## Concrete policy and empirical hypothesis

The implementation uses frozen economy17 with free_fallback="zero" and
foreign_attack_from=11 for P. At k it keeps P's construction actions, removes
its factory and minion purchases, and spends the remaining affordable budget
on copies of one declared tier, capped at 1000 entries. Starting at k+1 it
initializes a fresh frozen economy20 policy with the same parameters as
result 34 and calls it once per subsequent reached round. A null switch
round is a control that submits P forever. Original apply_action checks the
private projected state and rejects an invalid construction rather than
silently changing the plan. These operations access no hidden submission.

The falsifiable development hypothesis is that at least one declared delayed
switch defeats AdaptiveContinuation with attack_weight=4, whereas its
unchanged economy17 opponent loses. The initial switch rounds are 3, 5, 7,
9, 12 and 20, with tiers 3 and 5, both player assignments. The null-switch
control uses both assignments. This is a deliberately targeted development
pool, not held-out validation. A switch may buy zero copies, may occur after
termination, or may leave the signature unchanged. Each case must be recorded,
not counted as a successful deception. No result is asserted in advance.

## Dependencies and scope

The proof uses deterministic public-policy induction and the purchase-signature
visibility lemma in result 30. It proves an information limitation, not a
winning strategy, lower bound on damage, or inevitability of empty-catalogue
fallback. S is outside the fixed-membership hypothesis of result 30; a later
forecast failure does not contradict that result. Result 37 supplies the
observing AdaptiveContinuation policy. Source and behavioral checks will be
kept alongside this proof. No machine-checked formalization is claimed.
