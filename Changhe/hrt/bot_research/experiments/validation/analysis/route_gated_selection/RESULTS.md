# Route-gated selection: repair

Checked 2026-10-31T16:31:54.204588+00:00.

CONFIRMED: the route gate removes the ten previous adaptive losses on the disclosed24-target development set.

Counter outcomes: route_adaptive: 40W/8D/0L.

The route gate is a repair chosen after the previous outcomes were known. It keeps the early strike for a positive no-enemy-action projection only when the visible enemy route is longer than the spawn/base Manhattan distance. Otherwise it chooses growth. The early and growth branches are unchanged. Forty-eight predeclared comparisons reproduce the corresponding old forced-branch histories, so the improvement is attributable to selecting between these branches on this fixed set. The old controls add no independent sample. All four declared nominee opening-count variants remain wins. An aggressive route-building challenge is reported separately, with no general robustness inference here.

Each row represents both physical assignments with identical normalized histories. All outcomes and HP below are from the counter's perspective; the target name identifies the opposing policy.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
| P4TNUB | route_adaptive | early | 40 | 15 | W | 755:740 | 50 |
| P5TNUBM | route_adaptive | early | 40 | 15 | W | 755:740 | 50 |
| best_v9e | route_adaptive | early | 40 | 15 | W | 755:740 | 50 |
| F36 | route_adaptive | early | 42 | 25 | W | 765:740 | 50 |
| F37 | route_adaptive | early | 42 | 25 | W | 765:740 | 50 |
| lead8 | route_adaptive | growth | 22 | 60 | D | -40:-40 | 8 |
| E25RM | route_adaptive | growth | 22 | 10 | W | 618:-40 | 10 |
| E30 | route_adaptive | growth | 22 | 10 | W | 618:-40 | 10 |
| rush_t1 | route_adaptive | growth | 22 | -145 | W | 650:-40 | 8 |
| rush_t2 | route_adaptive | growth | 22 | -96 | W | 560:-40 | 8 |
| rush_t3 | route_adaptive | growth | 22 | -44 | W | 462:-40 | 8 |
| heavy_t4 | route_adaptive | growth | 22 | 60 | W | 800:-40 | 8 |
| eco3_t1 | route_adaptive | growth | 22 | 60 | W | 800:-40 | 8 |
| eco5_t1 | route_adaptive | growth | 22 | 60 | W | 800:-40 | 8 |
| eco5_t3 | route_adaptive | growth | 22 | 60 | D | -526:-40 | 8 |
| eco6_t5 | route_adaptive | growth | 22 | 60 | D | -40:-40 | 8 |
| splash_t2 | route_adaptive | growth | 22 | 60 | W | 728:-40 | 8 |
| splash3_t4 | route_adaptive | growth | 22 | 60 | W | 620:-40 | 8 |
| gun_t3 | route_adaptive | growth | 22 | 60 | W | 540:-40 | 8 |
| mixed5 | route_adaptive | growth | 22 | 60 | D | -40:-40 | 8 |
| P5M_poke0 | route_adaptive | early | 40 | 60 | W | 800:740 | 50 |
| P5M_poke2 | route_adaptive | early | 40 | 30 | W | 770:740 | 50 |
| P5M_poke3 | route_adaptive | early | 40 | 15 | W | 755:740 | 50 |
| P5M_poke4 | route_adaptive | growth | 40 | -5 | W | 740:660 | 50 |

All48 full games pass strict accounting, original-engine replay, source and data pinning, and fresh policy regeneration. All1148 regenerated decisions reproduce their recorded submissions, leave the input observation unchanged and pass action legality. There are576 locally filtered planner proposals; no submitted action is rejected. All24 assignment pairs and48 complete-history controls agree. Assignment swaps and fixed-branch controls are reproducibility evidence, not independent random samples.

The growth delegate retains a three-second planner cutoff. These observations do not establish unconditional reproducibility under arbitrary machine load. Selection reads only public observations and legitimate local state. The installed best_v9e and the pool-C validation are unchanged by this experiment.

The manifests, strict/replay/data/history audits and pipeline logs are listed by digest in verification/full_games.json. Reproduce using run_data_development on the named manifests, audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, and check_route_histories, under the documented project-root Python environment, disabled bytecode, assigned affinity, single thread and low priority. The repair also uses the separately declared compare_recorded_controls input.
