# Exhaustive first-round rosters against a fixed opening

## Statement and hypotheses

Use the unchanged bundled balanced rules and standard initial state. Each
player initially has 100 gold. Fix one observing policy, initialized afresh
for each test, whose first decision uses only its public observation. Among
opponents that purchase only minions in round one, the maximum damage dealt
to that policy in that round is the maximum obtained by testing the 27 ordered
rosters enumerated below. The claim concerns round one only. It does not
assert that the maximum is zero, or that the opening wins a full game.

## Notation and complete argument

A roster is an ordered finite word over the minion types. Its cost is the sum
of its entry costs. The costs of tier1, tier2 and tier3 are 15, 40 and 100;
tier4 and tier5 each cost more than 100. There are seven all-tier1 words,
including the empty word. A word with exactly one tier2 contains between zero
and four tier1 entries. For a fixed number m of tier1 entries there are m+1
possible positions for tier2, giving 1+2+3+4+5=15 words. A word with two tier2
entries contains either zero or one tier1, giving 1+3=4 words. Three tier2
entries are unaffordable. One tier3 alone gives the remaining word. Thus the
complete set has 7+15+4+1=27 elements.

More generally, the recursive enumerator emits the current prefix and recurses
on every type whose positive cost fits the remaining budget. Its invariant is
that spent cost plus remaining budget equals 100. Every emitted word is legal
and every legal word follows exactly one branch, by its successive letters.
Positive costs ensure termination. The recursion therefore agrees with the
count above without relying on an unordered multiset approximation.

The fixed observing policy has the same initial public information against
every word, because current submissions are hidden. Its first action list is
therefore identical within each player assignment. Original-engine execution
of every word with that action list yields the exact round-one outcome, so
taking the finite maximum is exhaustive for these hypotheses. Testing both
assignments also detects any actual seat-dependent policy behavior. Ordered
rosters are retained because dense active-entry indices affect spawn times.

## Verification and scope

The component checker tests the actual proposed V18FT and V24G definitions
from the declared direct-entrypoint manifest. It checks observation immutability,
identical first submissions across opponent words, action acceptance, and exact
source hashes. It records every one-round replay and both players' HP. The
computed maxima will be recorded as empirical evaluations of the unchanged
engine, not as a claim of a stronger all-round defense theorem.

No opponent construction, factory purchase, later decision or scripted initial
state is included. This result neither compares full-game strength nor licenses
an inference that spending more on round-one defense improves later outcomes.
Dependencies are the balanced configuration, actions, engine, state, pathfinding,
combat, and the two explicitly declared policy implementations. No proof assistant
is used.
