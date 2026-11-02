# Recent teammate transfer and branch ablation

Checked 2026-10-31T17:43:53.972993+00:00.

CONFIRMED: adaptive avoids defeat on all six declared recent targets in both assignments.

All 36 declared games are included. Each cell gives counter outcome, HP counter:target and ending round. Equal physical assignments share a cell; differences are explicit. These six targets were disclosed before evaluation. This is development coverage, not a fresh held-out result.

| Target | Adaptive | Forced early | Forced growth | Adaptive selection |
|---|---|---|---|---|
| fortress40 | W 770:740 r50 | W 770:740 r50 | L 464:800 r50 | early |
| fortress41 | W 770:740 r50 | W 770:740 r50 | L 490:660 r50 | early |
| V33C | W 755:740 r50 | W 755:740 r50 | W 755:520 r50 | early |
| econ29_r1guard60 | W 780:-40 r8 | W 760:-252 r10 | W 780:-40 r8 | growth |
| best_v9e | W 755:740 r50 | W 755:740 r50 | W 755:520 r50 | early |
| P5TNUBM | W 755:740 r50 | W 755:740 r50 | L 755:800 r50 | early |

Mode totals and measured low-priority wall time on shared hardware:

- adaptive: 12W/0D/0L; 516 calls, 79.207634 seconds summed, maximum 0.590508 seconds.
- early: 12W/0D/0L; 520 calls, 78.151289 seconds summed, maximum 0.656892 seconds.
- growth: 6W/0D/6L; 516 calls, 48.253229 seconds summed, maximum 2.531256 seconds.

Another fixed branch improves W/D/L in 0 of the twelve adaptive conditions. Both fixed branches lose in 0 conditions. The full receipt identifies each condition without selecting a favorable subset.

All 1552 freshly regenerated counter decisions agree, all observations remain unchanged, and all submitted actions are legal. Original-engine replay, source/data archives and strict accounting pass for every game. Independent reconstruction agrees on 1552 handoff calls and 22 starts. The twelve three-way groups have exactly equal complete records through round three. Each adaptive game has exactly the same complete history as its selected fixed-mode control. Of eighteen assignment pairs, 18 have identical canonical histories. Neither these pairs nor repeated histories are independent samples.

All three modes deliberately use the same display name to keep observations comparable. The legacy per-campaign generic summary groups by display name, so its assignment-pair count and abbreviated Markdown table do not distinguish the three specifications. This publication instead keys all conditions by full specification and physical assignment. The strict audit retains all six conditions per target; its condition accounting is unaffected. Use this table and verification/full_games.json for the complete comparison.

The empirical agreement does not prove load-independent policy behavior: teammate planners contain wall-clock search cutoffs. The result concerns the frozen sources and recorded conditions only. It does not promote a counter to best.py.

Reproduce each recent-transfer manifest through run_data_development, audit_development_strict, replay_audit, summarize_plain_campaign, audit_data_archives, check_delegated_histories and audit_delegation, then run publish_recent_transfer. The exact bounded commands are retained in runs/validation/recent-transfer-001-pipeline.log. Use new output names, the existing environment, disabled bytecode, the research temporary directory, one numerical thread, assigned affinity and low priority.
