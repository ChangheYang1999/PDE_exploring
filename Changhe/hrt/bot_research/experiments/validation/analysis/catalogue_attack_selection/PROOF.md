# Attack selection from a retained public catalogue

## Exact statement and hypotheses

Fix one reached round of the unchanged bundled game. Assume the actual
opponent is a fixed deterministic member h of the initial catalogue and the
clone protocol satisfies every hypothesis of stateful_catalogue/PROOF.md.
Let A be the nonempty retained set. The counter has already chosen a legal
construction list C. It does not revise C while choosing its own purchases.
All local combat quantities below refer to this same round and these exact
post-construction maps. Assume the damage evaluator equals the original
combat procedure on the rosters and maps being compared.

Let P be a finite set of affordable ordered purchase sequences containing the
empty sequence. For each a in A and p in P, let d_a(p) be the damage to the
opponent when its forecast action list is applied and the counter appends p
to its active roster. Let r_a be incoming damage against C under a's
forecast roster. Write c(p) for the purchase cost, H for own current HP and
K for the opponent's current HP. Define

    g(p) = min_{a in A} (d_a(p) - d_a(empty)).

Then the actual marginal damage of p is at least g(p). In particular, if
max_a r_a < H and min_a d_a(p) >= K, choosing p destroys the opponent's base
and leaves the counter's base positive in this round. The unchanged engine
therefore records a win for the counter, without a simultaneous-destruction
draw.

For a nonnegative rational weight w, put U(p) = w*g(p) - c(p). If no safe
lethal sequence is selected, maximizing a tuple whose first varying entry
is U over P gives U(p) >= 0. This last fact concerns only the stated
one-round surrogate. It is not a bound on future HP, income or game value.

## Argument

The catalogue retention proof gives h in A and exact current actions for
its clone. Own construction and the opponent's purchases affect separate
player states before combat. Applying the forecast actions and C therefore
reconstructs the two actual combat maps and active rosters, apart from the
counter's still unchosen p.

By the exact-evaluation hypothesis, actual marginal outgoing damage is
exactly d_h(p) - d_h(empty). The minimum defining g(p) is no greater than
this member, proving the first assertion. Actual incoming damage is r_h,
which is at most max_a r_a. Actual outgoing damage is d_h(p), which is at
least min_a d_a(p). The two displayed HP inequalities thus imply positive
own final HP and nonpositive opposing final HP. The engine settles both
combat directions before checking destruction, so its destruction rule
returns the counter as winner.

For the utility assertion, the empty sequence has zero cost and zero
marginal damage under every model, hence U(empty) = 0. A maximizer over a
set containing it has utility at least zero. Deterministic cost and length
tie breakers do not alter that inequality.

## Scope and failure cases

Catalogue membership and initial private-state synchronization are essential.
An outside-catalogue policy can agree with the public history and deviate in
the current round. An empty-catalogue visible-state fallback has no version
of the stated forecast guarantee. Its computed values are predictions only.

The finite purchase set need not contain the best affordable sequence.
Rational scoring avoids a floating-point tie error but does not make the
weight a correct economic value. Construction is held fixed during attack
selection; the policy does not optimize construction and attacks jointly.
Future rosters expire and opponents react, so a positive surrogate utility
can still cause a full-game loss. A safe-lethal label is conditional on the
forecast hypotheses and exact combat evaluation, not on a policy name.

The current-route immunity lemma permits skipping purchase search when
every retained post-action map has splash exposure at least the largest
configured minion HP. That statement concerns those fixed current maps;
it does not prove permanent immunity after later route changes.

## Dependencies and verification plan

Dependencies are stateful_catalogue/PROOF.md, current_immunity/PROOF.md,
the bundled action-isolation and simultaneous-settlement rules, and exact
local combat evaluation. No machine-checked proof is claimed.

The planned implementation is bots/counters/adaptive_catalogue.py. It will
advance the parent catalogue exactly once, retain its construction, remove
its factory purchases, search a deterministic bounded set of attack
sequences, and reinvest the remainder. A disabled-search control must return
identical actions to the parent's no-attack controller. Component checks
will compare selected outgoing and incoming damage with the original
combat procedure, check legal actions and unchanged observations, and
retain exact true-model action checks. Full-game evidence is separate from
this conditional argument and will be registered in verification/.

This argument was written before implementing the adaptive attack policy.
