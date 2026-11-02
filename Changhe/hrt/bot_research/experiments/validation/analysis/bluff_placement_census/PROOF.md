# Exhaustive placement census for a fixed one-gun bluff policy

Written: 2026-10-31T11:46:53.143427+00:00

## Statement, hypotheses and notation

Fix the bundled balanced rules, standard initial state, and the declared
namespace-frozen V23R policy. For every cell of the 12 by 12 board, test the
round-one action of building one gun1 using the original apply_action on a
fresh standard player. Let L be exactly the cells where that action is
accepted. For each c in L define B_c to be FeatureBluff with turret_round=1,
turret_kind=gun1, turret cell c, growth_rounds=6, tier=tier5, factory_cap=2000,
and purchase_cap=1000. The policy buys no other buildings.

If the campaign contains exactly one valid original-engine game for each
(c,s) in L times {0,1}, with candidate physical side s, its outcome table is
an exhaustive census of this finite placement family under these fixed
conditions. It establishes neither a win probability over unmentioned
opponents nor a claim about all legal strategies.

## Complete argument

The nested coordinate loops enumerate each board cell exactly once. A fresh
state for every acceptance test prevents one trial's construction or spending
from affecting another. Selecting exactly accepted cells defines L without
assuming that every nonterminal cell is legal. The manifest gives one unique
opponent specification per selected cell and the runner takes both sides.
The post-run checker independently repeats the legality enumeration, checks
that its set equals the manifest positions, then requires one audited result
for every Cartesian-product element and no extra element. Thus there is
neither a missing case nor an extra case in the asserted finite census.
Original-engine replay verifies the recorded action transitions and outcomes.

For mechanism analysis the checker also measures route coverage and the
original-combat outcome of fixed diagnostic rosters on each single-gun map.
These diagnostic combats classify the map's immediate defensive effect.
Their correlation with full-game results does not isolate a causal effect:
placement also changes public observations, route geometry, and targeting.
The earlier two weak-covering witnesses have the stronger zero-kill proof in
../weak_covering_bluff/PROOF.md. No stronger geometric theorem is assumed here.

## Dependencies and scope

Dependencies are original apply_action, shortest_path, simulate_map, the
independent strict/replay auditors, the frozen candidate and FeatureBluff
sources, and the manifest's complete position list. The checker must bind
these files by hash. A timeout or invalid case makes the exhaustive claim
OPEN even if every completed case fits a pattern. Both assignments remain
separate executions; identical histories are counted and are not independent
random samples. No formal theorem-prover check is claimed.
