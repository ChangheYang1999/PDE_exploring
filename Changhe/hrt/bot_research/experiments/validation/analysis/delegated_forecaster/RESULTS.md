# Public-clone timing challenge

Checked 2026-10-31T17:46:08.258178+00:00.

The finite-family claim is CONFIRMED: at least one of the twenty declared public-clone timing attackers defeats the Fortress 38 continuation in both physical assignments.

From the forecaster's perspective, the forty games against the template continuation give 38W/2D/0L; the forty against Fortress 38 give 38W/2D/0L. Every declared timing and defense-first setting is included. The settings that win in both assignments are recorded explicitly in the verification receipt. Failure of this finite family would not prove that the target is unexploitable.

Each cell gives the forecaster outcome, HP forecaster:target, final round and actual minion-purchase count. Equal assignments share a cell; differing assignments are explicit. The model parameters match the actual target. Its independently initialized private copy receives one copied public observation per reached round and never reads pending target actions.

| Forecaster setting | Against template continuation | Against Fortress 38 continuation |
|---|---|---|
| clone_r3_tier2_df0 | W 800:656 r50, buy 4 | W 800:656 r50, buy 4 |
| clone_r3_tier2_df1 | W 800:656 r50, buy 4 | W 800:656 r50, buy 4 |
| clone_r3_tier3_df0 | W 800:644 r50, buy 1 | W 800:644 r50, buy 1 |
| clone_r3_tier3_df1 | W 800:644 r50, buy 1 | W 800:644 r50, buy 1 |
| clone_r4_tier3_df0 | W 800:514 r50, buy 2 | W 800:514 r50, buy 2 |
| clone_r4_tier3_df1 | W 800:514 r50, buy 2 | W 800:514 r50, buy 2 |
| clone_r4_tier4_df0 | W 800:440 r50, buy 1 | W 800:440 r50, buy 1 |
| clone_r4_tier4_df1 | W 800:440 r50, buy 1 | W 800:440 r50, buy 1 |
| clone_r5_tier3_df0 | W 800:306 r50, buy 4 | W 800:306 r50, buy 4 |
| clone_r5_tier3_df1 | W 800:306 r50, buy 4 | W 800:306 r50, buy 4 |
| clone_r5_tier4_df0 | W 800:500 r50, buy 1 | W 800:500 r50, buy 1 |
| clone_r5_tier4_df1 | W 800:500 r50, buy 1 | W 800:500 r50, buy 1 |
| clone_r6_tier4_df0 | W 800:80 r50, buy 3 | W 800:80 r50, buy 3 |
| clone_r6_tier4_df1 | W 800:80 r50, buy 3 | W 800:80 r50, buy 3 |
| clone_r7_tier4_df0 | W 520:-100 r9, buy 5 | W 520:-100 r9, buy 5 |
| clone_r7_tier4_df1 | W 800:440 r50, buy 2 | W 800:440 r50, buy 2 |
| clone_r7_tier5_df0 | W 520:-40 r9, buy 2 | W 520:-40 r9, buy 2 |
| clone_r7_tier5_df1 | D 800:800 r50, buy 0 | D 800:800 r50, buy 0 |
| clone_r8_tier5_df0 | W 520:-40 r9, buy 3 | W 520:-40 r9, buy 3 |
| clone_r8_tier5_df1 | W 800:240 r50, buy 2 | W 800:240 r50, buy 2 |

All eighty games pass strict accounting, original-engine replay and source/data archive checks. The eight component prefixes passed 64 reached rounds before the game manifests were declared. Fresh checks reproduce 3508 forecaster decisions and 3508 independent target decisions. All actual target forecasts agree, and original incoming damage equals the predicted residual on every round. Observations are unchanged and submitted actions are legal. The handoff checker independently reconstructs 3508 target calls and 0 starts. 40 of forty assignment pairs have identical complete canonical histories.

The corresponding template/Fortress 38 experiments have exactly equal complete records through round four in all forty pairs after removing only their run identifier. Selected growth-branch histories agree completely. These are direct checks on the observed histories, not an arbitrary-load determinism guarantee. The conditional induction in PROOF.md requires deterministic policy transitions; teammate planner deadlines make that hypothesis a separate issue from the exact agreement actually measured here.

These are targeted development opponents with access to public target source, not hidden information and not untouched final validation. Measured decision-call totals and maxima for both players are retained by target mode. The experiment does not change best.py or its reserved-pool evidence.

The first eight version 001 games omitted forecast traces because the initial driver used isolated_match. They passed engine replay but could not validate forecasts. Version 002 used forecast_match via run_data_forecasts, with unchanged policies and conditions. All eight repeated complete histories agree exactly. TRACE_CORRECTION.md and the retained initial failure log record this instrument correction; those repeats are not additional strength evidence.

Reproduce the ten version 002 delegated-forecaster manifests with run_data_forecasts, then the strict, replay, summary, archive, forecast, target-policy, handoff and fresh-forecaster checks named in the campaign logs. Use the original project environment, disabled bytecode, the research temporary directory, assigned affinity, one numerical thread and low priority. verification/full_games.json pins the evidence and publisher.
