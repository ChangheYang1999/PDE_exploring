# Lower-bound initialization in the frozen fortress threshold search

## Statement and hypotheses

Consider the unmodified `_kill_threshold` in `bot_research/bots/defense/frozen/v28/fortress.py`, with the bundled balanced rules, no buildings, the engine's shortest path from (0,0) to (11,11), and a positive defender HP value h with h <= 140. For the default n_max = 2000, the function returns 2, although the smallest positive count of tier5 entries dealing at least h damage is 1.

This is a component counterexample to the function's claim to return the smallest lethal count. The defender HP can be 5, within the ordinary game's positive HP range. We do not claim that the empty-map/5-HP combination has been reached by either recorded bot, or that a measured full-game result changes because of this error.

## Notation and argument

Let D(n) be damage from n new tier5 entries on this empty map during one round, under the unchanged combat procedure. There are 22 edges from spawn to base on its shortest path. A single entry spawns at tick 0 and reaches the base before the 250-tick horizon. With no turrets it loses no HP. Tier5 base damage is 140, so D(1) = 140 and 1 is the smallest positive lethal count for the stated h.

Every n with 1 <= n <= 60 also gives at least one arrival. In particular the first entry has no damaging interaction, and all these entries spawn within the first 60 ticks. Thus D(n) >= 140 for every such n.

The implementation starts lo = 1 and tests n = 60. This succeeds and sets hi = 60. Its binary loop tests mid = (lo+hi)//2 while hi-lo > 1. Every tested mid is at least 2 and at most 59, hence lethal. Therefore lo stays 1 and hi repeatedly decreases until hi = 2. The function returns hi, namely 2. Its initialization silently treats count 1 as a known nonlethal lower bound without checking that premise.

A second boundary issue is independent. If n_max < 60, the geometric loop tests nothing and returns None, even if D(1) >= h. More generally it does not probe the final bound n_max when the next geometric step exceeds it. These are statements about the helper's algorithm, not a claim that the default 2000 upper bound misses a lethal count in a recorded match.

## Dependencies, scope, and verification

Dependencies: bundled tier5 damage 140, tick horizon 250, empty-map pathfinding, spawn/arrival ordering, and the frozen helper's source. No monotonicity theorem for armed maps is used. No engine code is changed. A component checker will compare the frozen return with exact positive-count enumeration and reproduce D(1) using the original `simulate_map` function. The result is informal and computational; no proof-assistant formalization is claimed.
