# Exact identification within a finite public-policy catalogue

## Statement and notation

Fix the bundled game rules and a finite set H of deterministic opponent
policies. Each policy's decision is reconstructible from the public observation
and its specified initial state. In this experiment the policies are stateless,
or have a flag determined by permanent public buildings. The actual opponent
is one fixed h in H throughout the match. There are no action rejections or
policy exceptions for its predicted actions.

For a decision in round r, let S_r be the following signature of the opposing
player after applying that player's submitted actions: number of factories,
the ordered list of building types and coordinates, and the ordered list of
minion types bought in round r that will remain in the next observation. The
signature ignores HP, gold, names and roster IDs. The standard roster lifetime
is twelve rounds, so every new purchase survives the cleanup of its first
round. Combat changes none of these signature fields. Consequently S_r can
be read exactly from the public observation at the start of round r+1.

Initialize H_1 = H. After observing round r, retain exactly those candidates
in H_r whose predicted S_r equals the observed signature; call the retained
set H_(r+1). Then the true policy h belongs to H_r at every reached round.
If, on a reached round, every other retained policy predicts a different
signature from h, then H_(r+1) is the singleton {h}. A singleton's current
predicted actions are the actual opponent actions, under the same hypotheses.

## Proof

The true policy belongs to H_1 by assumption. Suppose it belongs to H_r.
Its reconstructed decision receives exactly the public observation used by
the actual opponent. Determinism and the state-reconstruction hypothesis give
the same action list. Applying it to a copied public player state gives the
same factory count, building list and new roster entries. Own-side action
interleaving cannot alter these fields on the opposing player, and combat,
income and cleanup do not alter the specified signature. Its prediction
therefore equals the next observed signature, so it is retained. Induction
proves non-elimination. The singleton conclusion follows by removing every
other candidate at a separating observation. Exact current prediction then
follows again from determinism and state reconstruction.

## Implementation scope

The identifying counter uses this elimination rule, preserving purchase order.
If every candidate is contradicted, it records a catalogue reset and tries the
full catalogue again. That behavior is an explicitly heuristic recovery rule
for an opponent outside the fixed-catalogue assumptions, including policy
switches. It is not part of the non-elimination theorem.

Before identification, the counter considers the current forecasts of all
retained candidates. Its defense and purchase searches are bounded heuristics.
This proof establishes neither that identification eventually occurs nor that
any returned defense is sufficient, and it makes no win-rate claim. Policies
can remain observationally indistinguishable along the entire realized game.
No private pending actions, live engine object, opponent instance, file lookup
of hidden information or call stack is used to form a forecast.

## Dependencies and verification

The argument uses the bundled action isolation, permanent construction and
roster lifetime rules, plus the stated determinism hypotheses. The supporting
implementation is bots/counters/identifying_counter.py, relative to
bot_research/. Verification evidence will be registered in the neighboring
verification directory. No theorem-prover verification is claimed.
