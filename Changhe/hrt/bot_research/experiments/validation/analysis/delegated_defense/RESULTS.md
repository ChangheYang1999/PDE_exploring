# Frozen defensive continuation results

Checked 2026-10-31T17:03:29.661934+00:00.

CONFIRMED: at least one frozen delegate wins all six focused target settings.

Counter outcomes: delegated_template: 6W/0D/6L; delegated_econ20: 8W/2D/2L; delegated_fortress38: 12W/0D/0L.

All 36 games were declared after the 18 reached-state component checks and before any of these full games. Targets are the common-prefix baseline and tier1 flood, the three long-route delayed tier5 growers, and best_v9e. This is a focused development comparison after failures were diagnosed. Each row covers both physical assignments, which agree on the complete normalized history.

| Target | Counter continuation | Outcome | HP counter:target | Final round | Delegate starts |
|---|---|---|---|---:|---|
| baseline | delegated_template | W | 800:740 | 50 | None |
| baseline | delegated_econ20 | W | 776:740 | 50 | 5 |
| baseline | delegated_fortress38 | W | 788:740 | 50 | 5 |
| flood | delegated_template | W | 715:80 | 50 | None |
| flood | delegated_econ20 | W | 715:-40 | 9 | 5 |
| flood | delegated_fortress38 | W | 715:-210 | 9 | 5 |
| lead_opening_g6_tier5 | delegated_template | L | -180:320 | 11 | None |
| lead_opening_g6_tier5 | delegated_econ20 | W | 100:-12 | 12 | 5 |
| lead_opening_g6_tier5 | delegated_fortress38 | W | 380:-115 | 11 | 5 |
| cash_rank_1_g6_tier5 | delegated_template | L | -40:440 | 9 | None |
| cash_rank_1_g6_tier5 | delegated_econ20 | L | -40:440 | 9 | 5 |
| cash_rank_1_g6_tier5 | delegated_fortress38 | W | 240:-100 | 11 | 5 |
| cash_rank_10_g6_tier5 | delegated_template | L | -180:320 | 11 | None |
| cash_rank_10_g6_tier5 | delegated_econ20 | W | 100:-12 | 12 | 5 |
| cash_rank_10_g6_tier5 | delegated_fortress38 | W | 380:-115 | 11 | 5 |
| best_v9e | delegated_template | W | 755:740 | 50 | None |
| best_v9e | delegated_econ20 | D | 740:740 | 50 | 5 |
| best_v9e | delegated_fortress38 | W | 755:740 | 50 | 5 |

All 36 games pass strict accounting, original-engine replay, source/data checks and 930 fresh counter decisions. Observations are unchanged, all submitted actions are legal, and no bot error is recorded. All twelve template controls reproduce their earlier complete trajectories. For each target and assignment, all three variants have exactly the same recorded states and actions through round four after removing only the run identifier. A separate checker reconstructed every handoff trace using public states and original combat without importing the controller. The component check independently verified legal round-five actions and combat against the recorded simultaneous target action.

These results apply to starting the frozen defenders on the reached maps, with fresh legitimate state at handoff. They do not compare their ordinary round-one openings. The teammate planners may contain time limits; exact observed pair/control agreement is not a guarantee under arbitrary machine load. The verification receipt records measured counter call totals and maxima by mode.

Reproduction: use run_anonymous_development with delegated-defense-001.json, then audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives and check_delegated_histories. Compare controls with delegated-defense-controls-001.json. The original component command is check_delegated_component. Use the fixed project Python environment, disabled bytecode, research temporary directory, assigned affinity, one thread and low priority. All evidence is pinned by verification/full_games.json. This development result does not alter best_v9e or its final pool-C evidence.
