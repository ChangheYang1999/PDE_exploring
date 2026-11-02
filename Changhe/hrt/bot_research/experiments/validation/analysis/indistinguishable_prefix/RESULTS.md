# Route-branch prefix results

Checked 2026-10-31T16:42:13.897222+00:00.

CONFIRMED: opposite fixed-branch preferences after identical full public prefixes.

Counter outcomes: route_adaptive: 2W/0D/2L; route_early: 2W/0D/2L; route_growth: 2W/0D/2L.

The targets share the same P5TNUBM opening with no round-one poke. Baseline continues that policy; flood buys tier1 entries from round4. Public names are held fixed. All ten full-prefix comparisons agree, including the entire observations before rounds1,2,3 and4, without masking names or other fields. Both policies were freshly regenerated on every recorded observation, in addition to the route-selector check. Each deterministic selector that commits to E or G from this common history must lose to one of these two targets. The equal mixture has exact maximin utility0 in this two-by-two W/L game, with win utility+1 and loss utility-1. A third policy, another opening or later adaptation is outside this statement. No impossibility for the full game follows.

Each row represents both physical assignments, which have identical normalized complete trajectories. Outcomes and HP are from the counter perspective.

| Target | Counter mode | Selected branch | Enemy route length at round4 | Projected lead | Counter outcome | HP counter:target | Final round |
|---|---|---|---:|---:|---|---|---:|
| baseline | route_adaptive | early | 40 | 60 | W | 800:740 | 50 |
| baseline | route_early | early | 40 | 60 | W | 800:740 | 50 |
| baseline | route_growth | growth | 40 | 60 | L | 566:800 | 50 |
| flood | route_adaptive | early | 40 | 60 | L | -495:420 | 7 |
| flood | route_early | early | 40 | 60 | L | -495:420 | 7 |
| flood | route_growth | growth | 40 | 60 | W | 800:-40 | 8 |

All12 games pass strict accounting, original-engine replay, pinned source and data checks, and fresh selector regeneration. All344 fresh selector decisions agree and leave observations unchanged; no submitted action is rejected and no bot error occurs. There are6 identical assignment pairs and4 exact adaptive-versus-selected-branch controls. Repeated deterministic trajectories are reproducibility checks, not independent samples. The growth planner retains a three-second cutoff; these observed identities are not an unconditional guarantee under arbitrary load.

The proof gives exact hypotheses and scope. verification/full_games.json pins the manifests, audit receipts, result and replay files, and publisher. Reproduction uses run_anonymous_development with prefix-fork-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_route_histories, followed by check_prefix_fork. Use the documented project-root environment, existing Python, disabled bytecode, assigned affinity, one thread and low priority. This development experiment does not change best_v9e or its final pool-C evidence.

The independent both-policy check regenerates688 decisions and validates ten complete public-prefix equalities. The anonymous wrapper is verified as an exact transformation of the standard wrapper affecting only display names, its self-source root and its module description.
