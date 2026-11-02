# Certified splash thresholds along a staged guard sequence

## Exact statement and hypotheses

Use the bundled balanced rules, with 250 ticks per combat round. Fix a legal
wall set W and an ordered list of distinct splash cells c1,...,cm, disjoint
from W, spawn and base. Suppose every prefix of these cells is legally
constructible. Write Pi for the exact engine route after prefix i is built,
and Li for its number of edges. Define

Si = 10 times the number of pairs (p,c) with p in Pi before the base,
c among c1,...,ci, and Chebyshev distance between p and c equal to one.

Assume there are no guns or other buildings. During a combat on this fixed
prefix map, an active copy of HP h and roster index k reaches the base if
and only if h > Si and (k modulo 250) + Li <= 249. Its incoming base damage
is its configured damage. This remains true when other copies have different
types. If the checked sequence has Si nondecreasing, every already excluded
HP threshold stays excluded after a later complete prefix is installed.

## Complete argument

An eligible copy occupies each non-base route cell once before arrival.
Every adjacent splash hits every live copy on that cell; other copies do not
consume its attack. Thus a putative arriving copy receives exactly Si damage
before arrival. If h <= Si, nonpositive HP is reached at or before the last
relevant attack and the copy is removed, contradicting arrival. If h > Si,
every partial sum is at most Si, so the copy stays alive throughout traversal.
It then arrives precisely when its spawn tick plus Li lies within ticks0..249.
For an ineligible copy, the combat ends first and cleanup causes no arrival.
The argument applies separately to every copy because splash has no shared
target limit. Finally, Si >= Sj for i >= j preserves each inequality h <= Sj.

The monotonicity condition must be checked. Retaining old turrets by itself
does not imply it, because adding a building can change the chosen route.
The result covers combat on each recorded prefix, not unbuilt intermediate
plans, earlier survival, affordability in a full match, or game victory.

## Executable dependencies and experiment

The proposed search greedily maximizes Si among legal next cells, breaking
ties by route length and then increasing coordinates. It is not a global
optimization over sequences. Exact cells, routes and scores are written to
JSON, then checked with original action application and original combat.
No proof assistant formalization is claimed. A separate predeclared experiment
will compare two or three timed guards with the already measured single guard.
