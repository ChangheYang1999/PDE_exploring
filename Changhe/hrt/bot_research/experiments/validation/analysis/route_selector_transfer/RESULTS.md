# Route-branch transfer results

Checked 2026-10-31T16:41:04.865150+00:00.

CONFIRMED: the unchanged adaptive selector avoids defeat on the five declared transfer targets.

Counter outcomes: route_adaptive: 10W/0D/0L; route_early: 4W/0D/6L; route_growth: 10W/0D/0L.

These five frozen teammate policies were selected before this30-game transfer matrix. Every target and all three counter modes are retained. The test extends development coverage, without creating held-out evidence or altering the installed bot. The separately reported route-builder challenge exposes losses of this same selector and must be considered alongside this table. The defense worker retains fortress38 as its recommendation and describes fortress39 as a trade-off.

Each row represents both physical assignments, which have identical normalized complete trajectories. Outcomes and HP are from the counter perspective.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
| F38 | route_adaptive | early | 42 | 25 | W | 765:740 | 50 |
| F38 | route_early | early | 42 | 25 | W | 765:740 | 50 |
| F38 | route_growth | growth | 42 | 25 | W | 765:240 | 50 |
| F39 | route_adaptive | early | 42 | 25 | W | 765:740 | 50 |
| F39 | route_early | early | 42 | 25 | W | 765:740 | 50 |
| F39 | route_growth | growth | 42 | 25 | W | 765:660 | 50 |
| E20 | route_adaptive | growth | 22 | 10 | W | 618:-40 | 10 |
| E20 | route_early | early | 22 | 10 | L | -9:320 | 14 |
| E20 | route_growth | growth | 22 | 10 | W | 618:-40 | 10 |
| E27 | route_adaptive | growth | 22 | 10 | W | 618:-40 | 10 |
| E27 | route_early | early | 22 | 10 | L | -9:320 | 14 |
| E27 | route_growth | growth | 22 | 10 | W | 618:-40 | 10 |
| E29 | route_adaptive | growth | 22 | 10 | W | 618:-40 | 10 |
| E29 | route_early | early | 22 | 10 | L | -9:320 | 14 |
| E29 | route_growth | growth | 22 | 10 | W | 618:-40 | 10 |

All30 games pass strict accounting, original-engine replay, pinned source and data checks, and fresh selector regeneration. All804 fresh selector decisions agree and leave observations unchanged; no submitted action is rejected and no bot error occurs. There are15 identical assignment pairs and10 exact adaptive-versus-selected-branch controls. Repeated deterministic trajectories are reproducibility checks, not independent samples. The growth planner retains a three-second cutoff; these observed identities are not an unconditional guarantee under arbitrary load.

The proof gives exact hypotheses and scope. verification/full_games.json pins the manifests, audit receipts, result and replay files, and publisher. Reproduction uses run_data_development with route-transfer-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_route_histories. Use the documented project-root environment, existing Python, disabled bytecode, assigned affinity, one thread and low priority. This development experiment does not change best_v9e or its final pool-C evidence.
