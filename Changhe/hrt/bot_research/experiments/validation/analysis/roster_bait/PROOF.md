# A visible roster can activate the early insurance predicate

## Exact statement and hypotheses

Fix the bundled balanced rules, the standard initial state, and deterministic
policies using only public observations and private state. Let B be the
FeatureBluff grower with growth_rounds=6 and its declared optional round-one
gun. Define B_L to act exactly as B except in round two: retain B's construction,
buy an affordable declared ordered list L of tier1/tier2 entries, then buy as
many factories as the remaining gold and the unchanged factory cap allow.
Assume the selected entries are affordable and round three is reached.

Against any fixed deterministic observing policy Q, the B and B_L games have
identical public histories before round two and Q submits the same round-two
actions. If L is nonempty, Q's round-three observation contains a roster entry
with bought_round=2 and configured HP at most70. Therefore the roster part of
the frozen V23R relevance predicate is true at that observation. This does not
assert that its joint plan is affordable, selected, or strategically harmful.

## Complete proof

Both growers submit B's exact round-one list on the same initial observation.
The observing policy starts with the same private state and observation, so it
also submits the same list. Deterministic action application and combat give
the same state and public observation at the beginning of round two. Q has
seen the same history, so its second submission agrees. Current submissions
are hidden until they resolve; Q cannot yet react to L.

Each accepted round-two purchase creates a roster entry with bought_round=2
and expires_after_round=13 because the configured lifespan is12. Combat uses
respawned copies and does not delete the roster entry when a copy dies or
arrives. Thus an accepted entry persists into the round-three observation.
The two allowed types have configured HP20 and70. The frozen predicate tests
whether an opponent roster entry has bought_round at least2 and HP at most70;
the purchased entry satisfies both inequalities. This proves the predicate
claim, independently of turret coverage or the copies' combat outcome.

The later histories need not agree: purchases consume gold, reduce factories,
can cause damage and bounties, and remain active for later rounds. Those effects
prevent attribution of a full-game outcome to the predicate alone.

## Experiment and dependencies

Compare mid_relevant=false and true for the same private frozen V23 policy,
against L=[], [tier1], [tier1,tier1], [tier1,tier1,tier1], and [tier2]. For each
list use either no turret or the weak covering round-one gun1 at(0,2), and both
physical assignments. This gives40 declared development conditions. The
prediction to test is whether any nonempty no-turret list changes an otherwise
winning relevance-filter game into a loss. It is an open empirical hypothesis,
not a consequence of the predicate lemma.

Dependencies: unchanged actions.py roster creation, engine observations and
cleanup, combat copy semantics, bundled configuration, and the frozen V23R
predicate. Component checks must establish affordability, legal actions and
input immutability. Every full result requires strict accounting and original
engine replay. No reserve-C conditions or formal proof assistant are used.
