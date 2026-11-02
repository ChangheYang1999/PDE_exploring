# Route-gated selection: challenge

Checked 2026-10-31T16:37:08.151432+00:00.

CONFIRMED: the declared route-builder matrix contains a selector loss avoided by its alternative fixed branch.

Counter outcomes: route_adaptive: 18W/2D/12L; route_early: 16W/0D/16L; route_growth: 24W/8D/0L.

The sixteen opponents are existing MazeGrower policies: four exact layouts, growth through round3 or6, and repeated tier1 or tier5 purchases thereafter. There is no bait. All targets and all three modes are retained below. The predicate uses public geometry, but geometry does not restrict hidden current or later purchases. This matrix challenges the selection rule after its repair; it is development evidence, not a random draw of unseen opponents. Every adaptive history agrees with its selected forced branch. A different fixed branch can still lose, so none is claimed to dominate the others.

Controlled failure witnesses, with HP from the counter perspective:

- `cash_rank_10_g3_tier1`: early loses [-495, 420]; growth gives W [800, -40].
- `cash_rank_10_g6_tier5`: early loses [-180, 320]; growth gives D [-40, -40].
- `cash_rank_1_g3_tier1`: early loses [-545, 420]; growth gives W [800, -40].
- `cash_rank_1_g6_tier5`: early loses [-40, 440]; growth gives D [-180, -40].
- `lead_opening_g3_tier1`: early loses [-495, 420]; growth gives W [800, -40].
- `lead_opening_g6_tier5`: early loses [-180, 320]; growth gives D [-40, -40].

Each row represents both physical assignments with identical normalized histories. All outcomes and HP below are from the counter's perspective; the target name identifies the opposing policy.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
| empty_g3_tier1 | route_adaptive | growth | 22 | 60 | W | 800:-40 | 8 |
| empty_g3_tier1 | route_early | early | 22 | 60 | L | -410:420 | 7 |
| empty_g3_tier1 | route_growth | growth | 22 | 60 | W | 800:-40 | 8 |
| empty_g3_tier5 | route_adaptive | growth | 22 | 60 | W | 240:-40 | 8 |
| empty_g3_tier5 | route_early | early | 22 | 60 | W | 100:80 | 50 |
| empty_g3_tier5 | route_growth | growth | 22 | 60 | W | 240:-40 | 8 |
| empty_g6_tier1 | route_adaptive | growth | 22 | 60 | W | 800:-40 | 8 |
| empty_g6_tier1 | route_early | early | 22 | 60 | W | 800:80 | 50 |
| empty_g6_tier1 | route_growth | growth | 22 | 60 | W | 800:-40 | 8 |
| empty_g6_tier5 | route_adaptive | growth | 22 | 60 | D | -40:-40 | 8 |
| empty_g6_tier5 | route_early | early | 22 | 60 | L | -180:80 | 16 |
| empty_g6_tier5 | route_growth | growth | 22 | 60 | D | -40:-40 | 8 |
| lead_opening_g3_tier1 | route_adaptive | early | 40 | 60 | L | -495:420 | 7 |
| lead_opening_g3_tier1 | route_early | early | 40 | 60 | L | -495:420 | 7 |
| lead_opening_g3_tier1 | route_growth | growth | 40 | 60 | W | 800:-40 | 8 |
| lead_opening_g3_tier5 | route_adaptive | early | 40 | 60 | W | 100:80 | 50 |
| lead_opening_g3_tier5 | route_early | early | 40 | 60 | W | 100:80 | 50 |
| lead_opening_g3_tier5 | route_growth | growth | 40 | 60 | W | 240:-40 | 8 |
| lead_opening_g6_tier1 | route_adaptive | early | 40 | 60 | W | 800:80 | 50 |
| lead_opening_g6_tier1 | route_early | early | 40 | 60 | W | 800:80 | 50 |
| lead_opening_g6_tier1 | route_growth | growth | 40 | 60 | W | 800:-40 | 8 |
| lead_opening_g6_tier5 | route_adaptive | early | 40 | 60 | L | -180:320 | 11 |
| lead_opening_g6_tier5 | route_early | early | 40 | 60 | L | -180:320 | 11 |
| lead_opening_g6_tier5 | route_growth | growth | 40 | 60 | D | -40:-40 | 8 |
| cash_rank_1_g3_tier1 | route_adaptive | early | 70 | 60 | L | -545:420 | 7 |
| cash_rank_1_g3_tier1 | route_early | early | 70 | 60 | L | -545:420 | 7 |
| cash_rank_1_g3_tier1 | route_growth | growth | 70 | 60 | W | 800:-40 | 8 |
| cash_rank_1_g3_tier5 | route_adaptive | early | 70 | 60 | W | 100:80 | 50 |
| cash_rank_1_g3_tier5 | route_early | early | 70 | 60 | W | 100:80 | 50 |
| cash_rank_1_g3_tier5 | route_growth | growth | 70 | 60 | W | 240:-40 | 8 |
| cash_rank_1_g6_tier1 | route_adaptive | early | 70 | 60 | W | 800:80 | 50 |
| cash_rank_1_g6_tier1 | route_early | early | 70 | 60 | W | 800:80 | 50 |
| cash_rank_1_g6_tier1 | route_growth | growth | 70 | 60 | W | 800:-40 | 8 |
| cash_rank_1_g6_tier5 | route_adaptive | early | 70 | 60 | L | -40:440 | 9 |
| cash_rank_1_g6_tier5 | route_early | early | 70 | 60 | L | -40:440 | 9 |
| cash_rank_1_g6_tier5 | route_growth | growth | 70 | 60 | D | -180:-40 | 8 |
| cash_rank_10_g3_tier1 | route_adaptive | early | 56 | 60 | L | -495:420 | 7 |
| cash_rank_10_g3_tier1 | route_early | early | 56 | 60 | L | -495:420 | 7 |
| cash_rank_10_g3_tier1 | route_growth | growth | 56 | 60 | W | 800:-40 | 8 |
| cash_rank_10_g3_tier5 | route_adaptive | early | 56 | 60 | W | 100:80 | 50 |
| cash_rank_10_g3_tier5 | route_early | early | 56 | 60 | W | 100:80 | 50 |
| cash_rank_10_g3_tier5 | route_growth | growth | 56 | 60 | W | 240:-40 | 8 |
| cash_rank_10_g6_tier1 | route_adaptive | early | 56 | 60 | W | 800:80 | 50 |
| cash_rank_10_g6_tier1 | route_early | early | 56 | 60 | W | 800:80 | 50 |
| cash_rank_10_g6_tier1 | route_growth | growth | 56 | 60 | W | 800:-40 | 8 |
| cash_rank_10_g6_tier5 | route_adaptive | early | 56 | 60 | L | -180:320 | 11 |
| cash_rank_10_g6_tier5 | route_early | early | 56 | 60 | L | -180:320 | 11 |
| cash_rank_10_g6_tier5 | route_growth | growth | 56 | 60 | D | -40:-40 | 8 |

All96 full games pass strict accounting, original-engine replay, source and data pinning, and fresh policy regeneration. All1974 regenerated decisions reproduce their recorded submissions, leave the input observation unchanged and pass action legality. There are1152 locally filtered planner proposals; no submitted action is rejected. All48 assignment pairs and32 complete-history controls agree. Assignment swaps and fixed-branch controls are reproducibility evidence, not independent random samples.

The growth delegate retains a three-second planner cutoff. These observations do not establish unconditional reproducibility under arbitrary machine load. Selection reads only public observations and legitimate local state. The installed best_v9e and the pool-C validation are unchanged by this experiment.

The manifests, strict/replay/data/history audits and pipeline logs are listed by digest in verification/full_games.json. Reproduce using run_data_development on the named manifests, audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, and check_route_histories, under the documented project-root Python environment, disabled bytecode, assigned affinity, single thread and low priority. The repair also uses the separately declared compare_recorded_controls input.
