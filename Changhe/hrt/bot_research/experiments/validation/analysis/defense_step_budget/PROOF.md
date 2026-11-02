# A defensive-search budget and a surviving-round witness

## Statement and exact scope

Fix the bundled rules and the position before round 41 of the completed
`best-v9b-free-scenarios-fullretry450-001/results/case0006.json` game. The
counter occupies player 0, uses the asym:3:2 prescribed opening and the
round-5 tier3 attack, and faces the unchanged best_v9b entry point. Its
recorded HP is 790 and its gold is 639450. The opponent's actual submitted
round-41 action list is fixed to the one recorded in this game.

The following is a conditional feasibility statement. If the checker
produces a legal construction list A from this observation and original
combat after A causes damage strictly below 790, then there exists a legal
defense that keeps this counter alive through this round against that
fixed opponent action list. If its damage is zero, the counter preserves
all 790 HP in this round. No statement about later rounds or a full-game
win follows. Until the witness is checked, existence remains open.

## Notation and argument

Let O be the two public player snapshots before round 41. Let B be the
opponent's recorded action list. Apply B to an independent copy of the
opponent's player state. For a candidate defense A, apply A to an independent
copy of the counter's player state with its actual starting gold. Every
application must be accepted by the unchanged action implementation.

The two action lists modify separate player states, so their actual
interleaving cannot change the resulting buildings, rosters or remaining
gold. Compute the counter's resulting shortest path with the original
pathfinder and simulate the resulting incoming ordered roster with the
original combat function. Let D(A) be its total base damage. The counter's
HP after combat is exactly 790 - D(A). Hence D(A) < 790 proves survival
through that round. Factories bought after this construction do not alter
combat and are unnecessary for this feasibility witness.

For comparison, the actual default controller uses at most 15 steps in its
layout-free fallback. Its recorded incoming damage is 1120. Reproducing
its construction and damage from O checks that the experiment starts from
the intended position. The planned alternatives change only the maximum
number of greedy search steps to 1, 5, 30 or 60. They do not establish a
minimum-cost defense, an optimal layout, or a best full-game step budget.

## Dependencies and verification

Dependencies are the exact replay and result hashes, the frozen replay
source receipt, original action legality, original pathfinding and combat,
and the existing FreeForecast defensive proposal generator. The generator
may be heuristic: feasibility depends on checking its returned actions,
not on trusting its search rationale. This argument was written before the
new component experiment. No proof-assistant formalization is claimed.
