# Six fixed policies and a changed private model

Checked 2026-10-31T19:09:04.520586+00:00.

H1, I weakly improves on C against every prior policy with at least one strict improvement, is CONFIRMED. The payoff differences I minus C against B,C,D,G,H are 0, 0, 0, 0, 2.

B is frozen best_v9e, C is the round-three tier2 attacker with a fixed private D model, D is the adaptive Fortress38 continuation, G is early-wall guard00, and H is the HP-triggered grower with lead_from=8 and deadline=12. I changes only C’s private model to that same H. Each attacker retains its one model on all edges.

| Row | B | C | D | G | H | I |
|---|---:|---:|---:|---:|---:|---:|
| B | 0 | 1 | -1 | -1 | -1 | 1 |
| C | -1 | 0 | 1 | -1 | -1 | 0 |
| D | 1 | -1 | 0 | 0 | 0 | -1 |
| G | 1 | 1 | 0 | 0 | -1 | 1 |
| H | 1 | 1 | 0 | 1 | 0 | -1 |
| I | -1 | 0 | 1 | -1 | 1 | 0 |

Payoffs are +1 for a win, 0 for a draw and -1 for a loss. Each cell pair comes from both physical assignments of the same standard start. Thirty-two games are explicitly reused; ten are new. All twenty-one assignment pairs have identical canonical histories. These are selected development conditions, not independent samples.

| New or directly reused I edge | Outcome | HP I:opponent | End round | Source |
|---|---|---|---:|---|
| I vs H | W | 800:656 | 50 | Reused |
| I vs B | L | 755:800 | 50 | New |
| I vs C | D | 752:752 | 50 | New |
| I vs D | W | 800:656 | 50 | New |
| I vs G | L | -20:800 | 12 | New |
| I vs I | D | 752:752 | 50 | New |

Pure policies with nonnegative payoffs in every column: none.
Measured directed three-policy cycles: B > C > D > B; B > I > D > B; B > I > H > B; G > I > H > G.

Exact rational arithmetic verifies finite-game value zero with weights B=0, C=0, D=0, G=1/3, H=1/3, I=1/3. Its column payoffs are 1/3, 2/3, 1/3, 0, 0, 0. The saved receipt contains every feasible vertex found by the proposal search and the direct inequality checks.

All 848 new external action decisions were independently regenerated and matched the recorded histories. Submitted actions are legal, observations are unchanged, source/data archives match and original-engine replays agree. The reused table and the I-H source, replay, fresh-decision and prediction receipts were also rechecked. Wrong internal forecasts on other edges do not invalidate a fixed policy and are not reported as exact predictions.

Changing a private model can change all later observations and actions. This is a comparison of two complete policies, not an isolated intervention at an otherwise fixed history. A finite-table certificate proves no guarantee against a seventh policy or a different start.

Reproduction uses the five six-policy-game manifests with run_data_development, audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories, followed by check_six_policy_arithmetic and publish_six_policy_game. Restore archived old inputs before rechecking their receipts. The bounded commands and real timestamps are retained in runs/validation/six-policy-game-001-pipeline.log.
