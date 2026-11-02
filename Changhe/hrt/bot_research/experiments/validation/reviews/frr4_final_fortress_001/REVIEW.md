# Independent review of frr4 and the pending final fortress extension

Prepared 2026-10-31T23:09:37.669493+00:00. Reviewer model: GPT-6 Astra. This is a source and retained-record review. No policy was imported, constructed or called; no Engine, replay, project checker, test or new game was executed. The parent reviews these findings and exchanges them with the actual Claude Opus lead. This receipt does not claim a separate Opus execution by this reviewer.

**Verdict: CONFIRMED for the completed v46 frr4 record and its limited descriptive comparison. OPEN for completed frr5/frr6 results or a transfer of frr4's score to v48.** Two literal report statements need narrowing, and one timing parenthesis needs clarification. These were sent to the parent, who independently verified the record counterexamples.

The exact initial inputs were read at 23:05:03.186688Z to 23:05:05.723821Z. [The input manifest](input_manifest_001.json) binds 166 original files to gzip archives by both compressed and original SHA-256 and byte length. It includes all 24 frr4 logs, ten then-completed frr5 logs, results from frr2/frr3/x215/x230, the current report, lead team notes, defense notes, queue scripts, and source dependencies. [The independent aggregation](record_audit_001.json) and [source addendum](source_addendum_001.json) retain full specifications, every checked condition and every error list. All archives were re-read successfully; no sampled subset substitutes for the frr4 raw audit.

## 1. Exact conditions and outcomes

**Claim.** frr4 completed 24 distinct conditions and v46 scored 22 wins, two draws and no losses.

**Method.** Join each result by complete opponent specification, scenario and physical candidate seat against `queue_h17.sh` and `rr_specs.sh`; reconstruct the result and both player summaries from each original log. The candidate is `bot_research.bots.defense.frozen.v46.fortress:@make`. Opponents are best_v9e, best_v9f, v41, V29, g1 and AS1C with the exact parameters in the aggregation. In particular g1 adds `attack_from=7` to V29; AS1C uses `attack_share=1.0&catch_up_share=0.5` on best_v9e.

**Result.** The grid is six opponents, two prescribed openings and both seats, with no missing, duplicate or unexpected condition. Below each cell gives candidate HP minus opponent HP and the ending round. Both mirror assignments agree.

| Opponent | mirror:1:2, either seat | asym:23:2, v46 seat 0 | asym:23:2, v46 seat 1 |
|---|---:|---:|---:|
| best_v9e | +1555, r14 | +2385, r17 | +4222, r18 |
| best_v9f | +1555, r14 | +2385, r17 | +4222, r18 |
| AS1C | +1555, r14 | +2385, r17 | +4222, r18 |
| V29 | +15, r50 | +2385, r17 | +9822, r19 |
| g1 | +15, r50 | +2385, r17 | +9822, r19 |
| v41 | draw, r50 | +5455, r21 | +1265, r20 |

**Verdict: CONFIRMED.** The log records cover 602 game rounds and 1,252 round/player records. They contain 425,716 accepted actions: 416,191 factories, 5,938 minions, 2,003 turrets and 1,584 walls. Rejected actions, bot errors and separately recorded scripted-round policy exceptions are all zero. Reconstructed accepted/spent/error totals, terminal HPs, damage/hits and player summaries agree exactly. Per-round gold, HP, income, building-count and interleaved action-order accounting passes; integer terminal rules agree at every reached round. This is record consistency, not an independent combat replay or fresh policy reproduction.

## 2. What varies, and what was selected

**Claim.** These are distinct tested conditions, not independent random repetitions or new selection evidence.

**Method and result.** `mirror:1:2` forces rounds 1 and 2 using seed 1 on both maps. `asym:23:2` uses physical-seat seeds 46 and 47. The same initial two-round public history, after removing only player names, appears in all twelve games for each scenario. The harness calls and advances each actual policy during those rounds, discards its proposal, and submits the scripted actions. Thus the run implies 1,204 external policy calls, including 96 discarded scripted-round calls. No decision-call receipt is independently recreated here. Rules stay the bundled balanced rules.

The original queue records 22:36:52Z to 22:49:43Z for frr4; summed game wall times are 756.188 seconds, while the queue interval also includes worker and recording overhead. The v46 extension is descriptive: the standard-start frr3 result remains 4W/4D/12L over ten opponents and both seats. frr4 and frr3 have disjoint scenario conditions. Neither changes the selection that the lead says closed at 19:50Z.

**Verdict: CONFIRMED within this scope.** No claim of a sampled win probability, held-out selection test, or universal strength follows.

## 3. Combined table and report corrections

**Claim.** Combining frr2 and frr4 gives the reported seven-policy round robin on these two scripted starts.

**Method and result.** Exact full-spec and physical-seat joins give 84 distinct conditions, exactly the complete seven-policy grid without self play. Reaggregating retained rows gives v46 22W/2D/0L; V29 and g1 each 12W/2D/10L; v41 10W/2D/12L; and best_v9e, best_v9f and AS1C each 6W/4D/14L. frr2 raw logs were not replayed or independently reaggregated here; its 60 result rows and source identities were checked.

**Verdict: CONFIRMED for these totals.** The archived report's phrase “by 2385 in seat 0 against every opponent” is false for v41, where the margin is 5455. Its sentence “v46 is the only one of the seven bots that wins this start in seat 1” is also false literally: each of the five non-v41 frr2 policies beats v41 from seat 1. The supported statement is that v46 alone wins asym:23:2 from seat 1 **against every other tested policy**. The parent independently verified both corrections; this reviewer did not edit the report.

## 4. Source identity and runtime scope

**Claim.** The archived frr4 result binds v46 and the source closure examined here, without detected drift.

**Method and result.** All recorded entry hashes and loaded-source hashes match archived current bytes. The frr4 union contains 62 loaded Python source paths. Independently reconstructing the harness's static import-closure digest matches every recorded version. The v46 entry SHA-256 is `a0aa939dd81fdbfd1ab4da4fd0c40cbc2e145058f5c01f6c606d27b4c28c15a7`, and its version digest is `6bfb67f918a51319ed635e1d8c145d33fcfd051684c3c4860bb734a5ed7d5c58`. Each row records `source_changed=false`. The two frozen package SHA256SUMS files each match all 13 entries. All 80 active source/data paths from the audited frr4/frr5 prefix were unchanged at the addendum check. Initial log rules equal the separately archived `td_game/balanced.json` plus the documented configuration defaults.

**Verdict: CONFIRMED for detected identity consistency; historical prelaunch cryptographic authentication remains limited.** The runner retains its final loaded-source map and before/after flag, not both complete maps; its version digest covers Python, not every data dependency. This review preserves current exact bytes and raw rule metadata, not an unrecorded historical seal. In particular current `queue_h17.sh` has a modification time after frr4 completed, so its “Written” comment alone is not evidence that these exact script bytes were fixed before launch. This does not produce a policy-source mismatch: the actual result specifications and hashes all agree.

Recorded maximum wall times per decision are V29 8.7107 s, g1 8.6045 s, v46 1.9972 s, v41 1.3061 s, best_v9e 1.4440 s, AS1C 1.4501 s and best_v9f 2.0464 s. These support the rounded report numbers. V29/g1 maxima occur in mirror games **ending at round 50**; the retained aggregate timers do not identify the round of the slowest call. They are wall times, not CPU times or enforced budgets. The frozen fortress planner retains a three-second gun-search deadline. Observed seat agreement and these maxima do not establish load-independent actions or outcomes.

## 5. What the evidence says about v48

**Claim.** frr4's v46 result cannot simply be relabeled as a completed v48 result.

**Method and result.** v48's fortress entry has SHA-256 `067af590c9d2fceef852cc4ac3516d31e01919993f98755cbed44a05d68c37f5`. It changes the active-roster gun-check gate, reserves a smaller passing finish during defensive spending, spends the whole remaining slack on capacity defense under that reserve, and restores the reserve for the later attack step. Among the 13 frozen Python files, only fortress.py differs between v46 and v48. These are behavioral changes.

The retained defense runs x215/v46 and x230/v48 match on all twenty exact opponent/scenario/seat conditions in WDL, both terminal HPs and game length. For x215 versus frr4, only four V29 conditions are literal full-spec matches: x215 uses `best_v9e:decide`, whereas frr4 uses `best_v9e:@make`. The former renews a default Insurer on round 1 and the latter constructs the same default Insurer before play. Under this explicit wrapper normalization all eight overlapping conditions agree; the round-1 timed constructor location differs. Neither that agreement nor the twenty-condition regression proves complete-history or future-clock equivalence. The broader defense-lane regression pools were not audited here.

**Verdict: CONFIRMED as bounded supporting evidence for the defense recommendation; OPEN as a transfer of the complete frr4 score.** `bots/best.py` still has the best_v9e hash `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. “Final v48” refers to the frozen defense-lane recommendation, not the selected overall best entry. The live, unfrozen defense/fortress.py also has different defaults and should not be named interchangeably with frozen v48.

## 6. Dated pending-run status

**Claim.** frr5 and frr6 are not completed evidence at this inspection.

**Method and result.** `queue_h19.sh` explicitly schedules frozen v48 against the same ten standard-start opponents (20 games), then the same six opponents on the two scripted starts (24 games), both seats, with no selection change. Its retained modification time is 22:45:12Z, `rr_specs.sh` is 22:45:06Z, and the queue records frr5 starting 22:49:46Z. This is a dated written plan and launch record, not an independently timestamped hash declaration.

At the initial snapshot, frr5 had ten completed distinct rows: 0W/4D/6L, all with complete raw and source checks and the same terminal outcomes, both HPs and lengths as their frr3 counterparts. At the separately archived [status extension](status_snapshot_002.json), completed 23:08:28.618340Z, it had eleven of twenty rows, a **partial** 1W/4D/6L; the extra row receives status inspection only. frr5 had no completed summary or queue-end record. frr6 result, output and summary files were absent. No incomplete game is counted, and these prefixes are not merged into completed totals.

**Verdict: OPEN for the two completed campaigns.** Their completion and any later report revision require a separately dated follow-up. The review does not inspect reserved D opponent parameters or results. All work stayed local, with one lightweight reader on core 30 at nice 19; no prohibited tooling or service was used.
