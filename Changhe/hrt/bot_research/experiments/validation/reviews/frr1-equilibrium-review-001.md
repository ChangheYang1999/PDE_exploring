# Independent review of the frr1 equilibrium characterization

Recorded at 2026-10-31T22:20:47.936610+00:00. Finalized at 2026-10-31T22:21:36.764457+00:00. Reviewer model: GPT-6 Astra, hrt-w3 counters and independent validation. Actual Claude Opus 5.5 collaboration is through the lead's dated notes and report; this review independently reconstructs the data and checks the lead's argument. No external model client was invoked for this audit.

Verdict: **CONFIRMED for the explicitly defined recorded matrix.** The equilibrium set, necessity argument and weak-dominance claims in report section 5.16 are correct. The only proposed qualification is to state that the ten diagonal zeros are imposed by convention, since the 90-game tournament contains no self-play observations.

## Claim reviewed

The lead's `2026-10-31T22:14:33Z` entry in `../hrt-lead/NOTES_FOR_TEAM.md` and `bot_research/reports/REPORT.md`, section 5.16, say that every max-min mixture puts exactly 1/3 on g1, exactly 1/3 on guard00, and the remaining 1/3 in any nonnegative split over AS1C, best_v9f and P5TNUBM. The five other policies, including best_v9e, have zero weight in every such mixture. The report expressly limits the proposition to the recorded matrix.

The report paragraph beginning “The standard-start matrix as a game” was read in full, including its three inequalities and converse. Its exact UTF-8 bytes up to, but not including, the following bullet have SHA256 `ba7efad69f13acb0436300164f8ac151f0a132acae0b4d8c0714d7972e3d8e50`. The current lead notes file read for collaboration has SHA256 `ee736a376668fbb1dd2fbacbfbc8653329a7a00abd8047b5140e67aeb476b113`. These are review-time identity pins, not retrospective claims of a pre-game declaration. The exact paragraph, dated lead entry, complete queue log, queue script, specification script and two analysis helpers are preserved in `bot_research/experiments/validation/analysis/frr1_equilibrium/verification/review_input_excerpts_001.json`, SHA256 `3d881789b1ad02e8af719b27095367167b602ce5242ddf61d01964ea715c8444`. The complete report hash matches the version from which this excerpt was captured.

## Method and retained-data findings

I read the tournament, match, runner, protocol, configuration and outcome code without importing them. I then independently parsed the retained result file and all 90 logs with a standard-library script on assigned core 28 at nice 19 and one thread. No policy import, constructor, decision, game, engine replay or test involving the game was run. No terminal holdout parameter file was read. The permitted offline audit ran from 2026-10-31T22:19:18.491557+00:00 to 2026-10-31T22:19:21.267847+00:00.

The full parameterized specification strings in the receipt are the policy identities. Module suffixes would conflate best_v9e with AS1C, best_v9f with af2g, and V29 with g1. For the expected ordered list, the checker independently constructs all 45 unordered pairs, each with physical seats 0 and 1. It requires exact equality with the recorded pair IDs, candidate seats and full specifications. Each policy has nine opponents and exactly 18 games.

Every retained condition is `scenario = null`. All 180 initial player records have HP 800, gold 100, zero factories, turrets and walls, empty buildings and roster, and path length 22. Their rules objects equal the current bundled JSON rules exactly, including the 12 by 12 map and round limit 50. Each log binds both specifications, pair ID, candidate side, action order, neighbor order and tick order.

All 7,772 raw records occur in the exact sequence `(round, player) = (0,0),(0,1),...,(last,0),(last,1)` for their game. Both final records match the result row's winner, reason, HP and recorded terminal snapshot fields. No earlier record is terminal. The final winner also agrees with a direct reading of the engine's HP/round-limit outcome rule. All 651,202 action events are accepted. There are zero raw bot-error events, zero row-level bot errors, zero scenario errors and zero harness-error rows. All 90 referenced logs exist, and the log directory contains no extra logs. The metadata has one run stamp, `20261031T213053`.

The queue log records frr1 starting at 2026-10-31T21:30:53Z and ending at 2026-10-31T22:06:03Z with exit 0. The driver output has all progress counters 1 through 90 and a normal completion line reporting 2,109.8 seconds. The result file contains exactly 90 rows. There is no retained failed or incomplete frr1 attempt in this examined artifact set. This does not establish the absence of erased or never-recorded attempts: the general tournament driver has no independent durable attempt ledger and no per-game timeout. Its ordinary exception path would append an error row; a crash before returning a row could instead leave a partial or orphan log. None is present in this run's retained directory.

Both physical assignments agree for every unordered pair, not only on W/D/L but also on the HP margin after reversing perspective. Therefore either assignment yields the same off-diagonal matrix entry. There is one game per ordered pair, not repeated stochastic trials. All 18 games involving threat_defender end by base destruction in rounds 9 to 12; the other 72 reach round 50. The slowest retained decision is 4.5652 seconds, which rounds to the report's 4.57 seconds.

The independently recomputed standings are:

| Bot | W | D | L |
| --- | ---: | ---: | ---: |
| best_v9e | 8 | 6 | 4 |
| best_v9f | 8 | 8 | 2 |
| af2g | 8 | 6 | 4 |
| P5TNUBM | 6 | 10 | 2 |
| v41 | 4 | 2 | 12 |
| V29 | 4 | 0 | 14 |
| g1 | 6 | 0 | 12 |
| guard00 | 16 | 0 | 2 |
| threat_defender | 0 | 0 | 18 |
| AS1C | 12 | 4 | 2 |


## Source and rules identities

All 90 rows have `source_changed = false`. Each full specification has exactly one recorded entry hash and one recorded static source-version digest across all its games. There are seven distinct digest values because the ten policies include three pairs that share source modules with different parameters.

The union of recorded loaded-source maps contains 66 Python files, each with one consistent hash. All 66 match current bytes. Independently reconstructing the harness's static `bot_research` import closure plus the harness Python files reproduces all ten recorded version digests. That static union also has 66 files, of which ten were not in the loaded-source union. The combined source coverage is 76 files, with exact pins in the receipt. Both results and source identities were checked again before writing the receipt. The current frozen best_v9e entry hash is `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`.

These current and recorded identity comparisons support the source binding available in the general harness. They are not proof that no source file changed transiently during history. The initial log rules provide an independent data binding for `td_game/balanced.json`; Python source hashes alone would not have pinned that JSON. The canonical rules-object SHA256 is `4f4032de69e65f7f9b05f2dc5521c6f7c1cd076355dc4e39599b8974d6e5dba5`. The result and log audit is not a combat replay or independent authentication of every engine state transition.

These Python comparisons follow the harness's source-digest definition only. They do not authenticate transitive runtime JSON data. In particular, `EarlyWallGuard.__init__` reads `bot_research/bots/counters/data/early_wall_guard_001.json`; this audit did not compare that witness file with an earlier runtime-data pin. Its historical bytes, and those of other runtime data not embedded in the logs, remain outside the provenance claim. The matrix theorem is conditional on the retained payoffs and does not require that missing claim.

## Exact proof and assessment of the report

The standalone proof is `bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md`. It displays the entire independently reconstructed matrix, states the zero-diagonal hypothesis, proves value 0 with feasible exact primal and dual strategies, proves the necessary zero weights using the strictly negative dual coordinates, and proves sufficiency for every split, including boundary mixtures.

For an exact certificate, let z put 1/3 each on AS1C, g1 and guard00. In the receipt's coordinate order,

`z^T M = (1/3, 0, 1/3, 0, 1, 1/3, 0, 0, 1, 0)`

and `M z` is the negative transpose. The primal and dual bounds meet at 0. Any optimal mixture must give zero weight to the five strictly negative coordinates of the dual vector. With only the other strategies remaining, let a, b and t be the weights on g1, guard00 and the remaining three-policy group. The columns guard00, g1 and AS1C force `a >= t >= b >= a`, so a = b = t = 1/3.

The lead's direct necessity proof is independently correct. For arbitrary weights, write `t = 1-a-b`, `r = weight(best_v9e, af2g, v41, V29, threat_defender)` and `u = weight(v41, threat_defender)`. Its three columns give

`a >= t >= b+2u >= b >= a+r >= a`.

All quantities r and u are nonnegative; equality of the chain's endpoints forces r=u=0 and a=b=t=1/3. No approximate linear-programming conclusion is needed.

For weights c, d and p on AS1C, best_v9f and P5TNUBM with c+d+p=1/3, the full payoff vector is

`(c, 0, c, 0, 1-p, 1/3, 0, 0, 1, 0)`.

This verifies the report's zero, c and strictly positive column claims exactly. The offline checker separately evaluates all three vertices using `Fraction`. The written argument, rather than vertex checking alone, proves that no other mixtures are optimal. The dual optimal set is the same set, so the complete Nash-profile set is its Cartesian square, not merely profiles where both players use identical weights.

Both reported weak-dominance statements also hold. AS1C exceeds best_v9e by 1 exactly in the columns AS1C, best_v9e and af2g; best_v9f exceeds best_v9e by 1 exactly in the AS1C column. All other differences are zero. Weak dominance alone would not establish necessary zero weight; the report's inequalities do establish it.

## Publication wording and limits

No numerical correction to the matrix, standings or equilibrium set is needed. Suggested replacement for the opening of the equilibrium paragraph:

> For distinct bots, score each recorded frr1 pair +1, 0 or -1 for the row bot. Both physical seats give the same outcome. Set the ten unmeasured self-play diagonal entries to 0 by convention. The resulting skew-symmetric payoff matrix defines a symmetric zero-sum game with value 0.

Retain the existing restriction “for this recorded matrix only.” The theorem does not describe an HP-payoff game, other starting states, other opponents or the full tower-defense game. It supplies no basis to change `bots/best.py` and does not establish repeatability of wall-clock-limited policy choices. In particular, absence of best_v9e from this matrix's optimal face is a statement about these ten policy labels and these W/D/L entries.

## Evidence identities

The finalized proof is SHA256 `e6656f1850ba2cf85deea5170edfcd5a73ab7a53db3830bcb34a7dbcdefd035d`. The earlier receipt and checker remain unchanged; the explicit runtime-data limitation was added to this review and the proof after root review at 2026-10-31T22:21:36.764457+00:00.

All paths below are relative to the project. The receipt includes every one of the 90 raw log hashes and all source maps. Its canonical log-path-to-SHA256 mapping has SHA256 `ddbc0aabde139269063f8015bb31735a18febb5f5d0f7032c980966ffd5d7e83`, using JSON with sorted keys, separators `(',', ':')`, and no trailing newline.

| Relative path | SHA256 |
| --- | --- |
| `bot_research/experiments/lead/queue_h15.sh` | `6446f7f69d530f8136a443c42b4161ac4512b22ad77fc25b973724a7a4583c53` |
| `bot_research/experiments/lead/rr_specs.sh` | `ac939aea54a2decd7e993fe83c42ebd4ec0376efd1a6ec466354f42217a57c9f` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/INDEX.md` | `35f11f752fbdfbda29e352cfde85e8330e7e129a91e3b70ccfd37adbd352aa97` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md` | `e6656f1850ba2cf85deea5170edfcd5a73ab7a53db3830bcb34a7dbcdefd035d` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/verification/check_frr1_matrix.py` | `7d56bde0fb3a62a785d80d5913a8850d8e94c9d7a35738ba56e396e964071e8f` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json` | `118f08bc7d87f3ff536368a60c51e6879bf273c6bd7e5c431d56ad1a2fbbd08d` |
| `bot_research/harness/match.py` | `56ecf235680e117b524e56a5d4f65f7b610de7e792ccd202658f228381e1c4a5` |
| `bot_research/harness/tournament.py` | `561ac17b8e7467dacfd98e820a83d424d286101f3f568e40294339573221e151` |
| `bot_research/reports/REPORT.md` | `c9091d7bf775182d2988606b9dda9b1c58d5de7480af378410c1bc1e113cb7a2` |
| `bot_research/runs/lead/frr1.out` | `ffe7508229b88cb0797eecf34aa48ffeb3e78fca16e9bb1ad57709c892c5239d` |
| `bot_research/runs/lead/frr1/results.jsonl` | `2df0933ba2f8872c064d5edbfd1640d07713c3335a107b4e2aa0de9350113b00` |
| `bot_research/runs/lead/frr1/summary.md` | `52d255dc024c2fa7d26b1ee80086aa9e242d226326e0a77bc59f580e77d8e543` |
| `bot_research/runs/lead/queue_h15A.log` | `602373aef7d3e31784b4b1c3fc003ad46a97ae69361b545e9df397baeca77cd3` |
| `bot_research/tmp/rr_nash.py` | `59fa1d60c252cc626dcc94b4a71f4ce4202cef4d33e474d5cc55be6850c4d462` |
| `bot_research/tmp/rr_table.py` | `b0e28d58c506b01f0e9be3581976e76613f946d2a1d02df827aa288e8fc57eea` |
| `td_bots/protocol.py` | `b20cc2ae7ed13013cd2504e8e26665acdbc8c6c07f65fd6ee13dc9216874ebaa` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/runner.py` | `cca08518177cfb6a102e2483765e66fa595539e7fc04c546bbe0cf20836f2bed` |


The report and queue-spec files are mutable research documents. Their listed hashes bind the versions read at this review, while the retained result bytes and complete exact specification strings define the empirical matrix. No other lane's file was edited.
