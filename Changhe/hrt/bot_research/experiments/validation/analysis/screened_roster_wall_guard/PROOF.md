# A cheap wall guard for the screened round-six attack

## Exact question and finite domain

Use the original C02 standard-start round6 state from affordable-roster-coverage-001, with frozen best_v9e's recorded round6 action fixed. The attacking side has190gold, four splash towers at (10,1), (1,0), (1,1), (1,2), no active roster and no walls. Its purchase (tier2,tier2,tier3) costs180 and damages the target by26, but the fixed target action sends one tier3 and damages this side by26 as well. Walls cost1 under the bundled configuration, leaving a wall budget of10.

Test exactly five wall packages: empty; the three cells (0,4),(1,4),(2,4); those three plus (3,3); those four plus (3,2); and those five plus (3,1). These zero-, three-, four-, five-, and six-wall packages are a small declared geometric family, not an exhaustive search over wall sets. Coordinates and their order are retained in the declaration. No package will be added after observing these results.

H1: at least one listed affordable, legal package, bought in round6 together with the screened roster, leaves the attacker at800HP and the target at774HP. OPEN before execution. A failed action or different fixed target action invalidates that intervention; it is not silently removed.

## Argument and verification

The first three walls obstruct immediate downward movement from the initial corridor. The later column3 walls are intended to redirect the route beside the three left splash towers. Whether the engine's deterministic shortest route has this effect is checked, not assumed. Every intervention starts from the same independently replayed five-round history. Every original-prefix action and proposed wall/purchase is checked by the unchanged Engine; compare all prefix records exactly. For each package retain the entire six-round replay, every action result, resulting route, per-copy splash exposure count, both HP values and source hashes.

Because the target's own map and our roster order are unchanged, and the two combats use separate defending maps, our wall construction cannot change the incoming roster it faces in that round. Thus a successful original-engine comparison establishes an affordable one-round guard on this exact state. It does not establish a win over a complete game, nor a globally cheapest wall defense. A subsequent full-policy experiment must use fresh candidate decisions and retain its own declaration, both assignments and independent audits.

Dependencies: the exact original witness and source closure pinned in screened-roster-wall-guard-001.json; analysis/affordable_roster_coverage/PROOF.md; the original action, pathfinding, combat and Engine code. No proof-assistant verification is claimed.
