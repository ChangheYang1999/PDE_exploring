# Pool C: best_v9e

Published 2026-10-31T16:29:09.546664+00:00.

This is the independent final validation of the installed bot. Selection was fixed before these games.

Entry point: `bot_research.bots.best:decide`. Source SHA256: `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. The declaration and all source archives still match. Verdict: CONFIRMED for the exact finite table below, conditional on the stated environment and inputs. No claim of general optimality is made.

Wins/draws/losses are candidate outcomes from the original engine. HP difference is candidate minus opponent.

| Start | W/D/L, both seats | Seat 0 W/D/L | Seat 1 W/D/L | Worst HP difference | Ending rounds | Largest candidate call, seconds |
|---|---|---|---|---:|---|---:|
| standard | 18/6/0 | 9/3/0 | 9/3/0 | 0 | 9, 11, 12, 13, 14, 17, 50 | 0.867711 |
| mirror_7493_3 | 24/0/0 | 12/0/0 | 12/0/0 | 719 | 10, 11, 12, 13, 14, 15 | 0.652982 |
| asym_8669_2 | 24/0/0 | 12/0/0 | 12/0/0 | 526 | 11, 12, 13, 25 | 1.052337 |

All 72 prescribed conditions have complete results and independent original-engine replays. There are no bot errors, submitted rejected actions or source changes in the selected results. All 36 opponent/start combinations have both player assignments; 36 of their complete normalized trajectories agree. The engine is deterministic. The seat swaps test assignment effects and observed symmetry. They are not independent random samples.

The standard row begins from the normal game state. The two other rows prescribe legal initial histories from the unchanged manifest and skip policy calls for the first three or two rounds. Those rows test continuation from externally supplied positions, including the bot's foreign-map behavior. They are not merged into a single standard-start win rate.

The manifest was declared at 09:11:05Z. Both candidate specifications were registered at 2026-10-31T16:15:59.320339+00:00, before either comparison campaign. This campaign began 2026-10-31T16:15:59.837916+00:00 and its last selected game completed 2026-10-31T16:21:52.299067+00:00; elapsed time was 352.461151 seconds. The selected games sum to 318.503196 seconds. Timing is low-priority wall time on shared hardware, not a portable speed bound; the sum of match times is not aggregate team runtime.

There are 0 failed or invalid attempts in the complete accounting, retained separately. The earliest valid completion is selected once per exact condition. All failures, if any, are listed in the linked strict receipt.

The separation audit found 0 exact parameter overlaps and 0 exact prescribed-history overlaps with records preceding this campaign. It leaves 8 recognized scenario inputs unresolved. The detailed receipts state coverage and every qualification. Implementations and families are shared with development, so these are held-out parameter settings and legal histories, not unseen policy families. For the comparison candidate, overlap with the earlier primary C campaign is expected by design.

Fresh-process entry-point checks verify all 72 games and 1104 actual policy decisions per entry point. Direct `decide`, the default factory and the recorded candidate return exactly the same legal actions and leave observations unchanged. The 120 prescribed opening rounds are not counted as policy calls. These repeated checks add no strength sample.

The complete per-opponent HP, outcome and ending-round table is in `bot_research/runs/validation/reserved-C-best-v9e-001-summary.md`. The strict, replay, separation and loss receipts share this campaign prefix. No C-informed revision is permitted to reuse C as confirmatory evidence.

Reproduction uses `late_validation` with the exact declared candidate and hash, a new relative output directory, `--max-seconds 480 --match-timeout 300`, and `--resume` in later bounded invocations. Then run `audit_late_campaign`, `replay_campaign_bounded`, `summarize_reserved_replays` and `render_late_summary`. The pipeline log records every exact command. Use the supplied Python environment from the project root with bytecode disabled, the assigned low-priority affinity, single-thread numerical libraries and the required research temporary directory. No server or external compute is used.
