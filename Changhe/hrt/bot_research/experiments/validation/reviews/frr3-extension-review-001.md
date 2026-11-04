# Independent review of the frr3 extension and runtime report

Recorded 2026-10-31T22:45:55.873468+00:00. Actual reviewer model: GPT-6 Astra, hrt-w3. the main model collaboration remains through the active team and dated lane notes; no external model client was invoked by this review. Findings were exchanged with the parent before finalization.

The fixed report snapshot is bot_research/reports/REPORT.md, SHA256 471620efbf169a2f9118b58c2c2a1fd640b8640c00de05bc034e67044e3175af, retained verbatim in frr3_extension_review_001/REPORT.snapshot.md. Its header says last update 22:39Z. Line references below refer to these fixed bytes, not a later revision.

Verdicts: **CONFIRMED** for the 20 retained frr3 outcomes, their physical-seat interpretation, the reported frr3 timing maxima and the matrix extension with an explicit new zero diagonal. **REFUTED as written** for an overall 0.30-second CPU maximum across the 74 shortcut histories. **OPEN** for the unrestricted causal statement that no outcome depends on runtime. Sections 2 and 7 also contain stale recommendation and cutoff descriptions.

## Retained frr3 conditions and outcomes

Method: standard-library JSON parsing, source AST inspection, file hashing and exact Fraction arithmetic, on core 28 at nice 19 with one thread. No project import, policy constructor, decision, new game, Engine call, replay, checker phase or game test was performed. No terminal holdout parameters were read. The complete frr3 artifact audit finished at 2026-10-31T22:43:39.120558+00:00. Its exact retained script and result are under frr3_extension_review_001/.

The 20 rows exactly match the queue's ten full parameterized opponent specifications, each with v46 in physical seat 0 and physical seat 1. This distinguishes best_v9e from AS1C, best_v9f from af2g, and V29 from g1. Every scenario is null. All initial records have the standard bundled rules and the exact standard player state. Every complete stream is ordered (round,player) from (0,0) through the terminal pair, with no earlier result. Match specifications, side metadata, action order, neighbor order, terminal winner, HP and result summaries agree. There are 1,884 records, 900,320 accepted action events, no rejected actions, bot errors, scenario errors, harness-error rows, reported source changes, missing logs or orphan logs. Eighteen games reach round 50 and two finish in round 11. These records imply 1,844 original external policy turns; this review made zero new calls.

The queue records start 22:08:43Z and normal exit 0 at 22:36:52Z. The driver output contains all counters 1 through 20 and completion in 1,688.1 seconds. There is no failed or incomplete attempt in the retained frr3 directory. The general tournament has no separate durable attempt ledger, so this does not exclude erased or never-recorded attempts.

| Opponent | v46 HP : opponent HP, both seats | v46 W-D-L | Rounds | Opponent maximum call, seconds |
| --- | ---: | ---: | ---: | ---: |
| best_v9e | 785 : 790 | 0-0-2 | 50 | 7.8265 |
| best_v9f | 785 : 790 | 0-0-2 | 50 | 6.4608 |
| af2g | 785 : 790 | 0-0-2 | 50 | 7.3510 |
| P5TNUBM | 785 : 785 | 0-2-0 | 50 | 10.0712 |
| v41 | 790 : 790 | 0-2-0 | 50 | 0.7236 |
| V29 | 795 : 790 | 2-0-0 | 50 | 7.6700 |
| g1 | 735 : 790 | 0-0-2 | 50 | 10.7188 |
| guard00 | 740 : 780 | 0-0-2 | 50 | 0.4163 |
| threat_defender | 800 : -1200 | 2-0-0 | 11 | 0.0977 |
| AS1C | 785 : 790 | 0-0-2 | 50 | 6.8095 |


Both seats give identical winner-normalized outcomes and margins in every pair. The report's 4-4-12 and all stated margins are correct. The new row agrees with v41's old W/D/L row, including the draw with v41. This is not HP-row or trajectory identity: the threat_defender margin is +2000 at round 11 for v46, against +800 at round 10 for v41.

## Current and historical identities

All recorded loaded-source hashes match current bytes: 72 Python files. Independently reconstructing the harness's static bot_research closure and harness digest gives 73 files, and every full specification's recorded digest and entry hash match. Their union has 83 files. In particular, frozen v46 fortress.py is a0aa939dd81fdbfd1ab4da4fd0c40cbc2e145058f5c01f6c606d27b4c28c15a7 and its plan.py is e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545. No frozen source was changed.

The prior frr1 receipt has SHA256 118f08bc7d87f3ff536368a60c51e6879bf273c6bd7e5c431d56ad1a2fbbd08d. I reconstructed its matrix from the unchanged 90 result rows and rechecked all 90 retained log hashes against that receipt. The prior proof and provenance limitations remain applicable. Python static digests and embedded balanced rules do not authenticate the historical bytes of every transitively read runtime JSON witness, including guard00's constructor data. The retained checkpoints also do not exclude temporary historical source edits. The algebraic theorem is conditional on the retained W/D/L entries and does not require a stronger historical claim.

The four standard x215_v46_lead streams reproduce the reported v46 margins -5 against best_v9e and +5 against V29 in both seats. Their source hashes match current bytes. x215 uses the frozen best_v9e :decide entrypoint, while frr3 uses @make. Source inspection shows that :decide constructs default Insurer at round 1 for its physical player, agreeing with @make for this fresh standard-start use. Full action-stream equality between those campaigns was not tested here. The largest x215 best_v9e wrapper time is 6.7029 seconds, agreeing with 6.70 in the report.

## Exact matrix extension

Claim: adding v46 preserves the frr1 optimal face and gives v46 zero weight in every optimal mixture.

Result: **CONFIRMED**, provided the unmeasured v46/v46 entry is explicitly set to zero, just as the ten old self entries are. The frr3 set contains no v46 self-play game. The report now qualifies the ten old diagonal entries, but the extension paragraph should explicitly extend this convention to the eleventh entry.

The standalone complete argument is frr3_extension_review_001/PROOF.md. In the eleven-label matrix, v46 and v41 have identical rows and columns. Combine their two weights into the old v41 coordinate. Every pair of eleven-label mixed strategies then has exactly the same payoff as its two combined ten-label vectors. Since the old optimal face requires total v41 weight zero, nonnegativity forces both v41 and v46 weights to be zero. Conversely, every old optimal mixture remains feasible and scores 1-p against v46, where p is its P5TNUBM weight, so this new score is at least 2/3. This proves necessity and sufficiency for the entire face, not only three checked vertices. The value remains zero, and the equilibrium-profile set remains the Cartesian square of that face.

The statement concerns the defined W/D/L matrix on these eleven labels and this start. It does not concern HP-difference payoffs, unmeasured self-play, new opponents, the full game, or a mixture implementation under arbitrary planner deadlines.

## Runtime numbers and causal scope

The frr3 maxima in section 7 all round correctly: g1 10.7188, P5TNUBM 10.0712, best_v9e 7.8265, V29 7.6700, af2g 7.3510, AS1C 6.8095 and best_v9f 6.4608 seconds. v46's largest call is 2.3491 seconds. The lead-bot game range is 92.084 to 132.461 seconds; g1/V29 range is 120.161 to 140.571 seconds. The two v41 games take 29.557 and 30.702 seconds; guard00 games take 23.084 and 23.726 seconds. The report's whole-second ranges are reasonable approximations. The frr1 and frr2 maxima are 4.5652 and 3.5093 seconds respectively, so their combined 4.57-second maximum is correct.

These are result-row aggregates of TimedBot's perf_counter measurements. Individual timing samples are held in memory during the match and are not stored in the raw game JSONL. This review authenticates the retained summaries and inspects their measurement code; it does not independently reconstruct individual durations from game records or produce new runtime measurements.

The sentence near lines 2134-2136 stating that the shortcut gave the same actions and states on 74 histories “with at most 0.30 s CPU per call” has an incorrect scope. All 74 authenticated protocol151 case receipts contain 1,204 calls per implementation. The shortcut implementation's overall maximum is **0.837026346 CPU seconds**, on C-mirror_7493_3-03-side0, round 4, in the unchanged foreign branch. **0.29886853 CPU seconds** is the maximum only across the two high-factory histories. The bound is also not a global guarantee: it is a measured maximum. Protocol151 includes an untimed eligibility preflight before both measured calls and shared module caches. Protocol152's separate shortcut-only, no-preflight high-factory maximum is 0.207627 CPU seconds. State either the two-history scope for 0.30 or the overall measured maximum 0.84, and preserve the timing-method caveat. The action/state agreement count itself is correct.

The phrases “no recorded outcome depends on this” and “no outcome depends on it” do not follow merely from absence of a runner timeout. The bundled runner has no decision-time limit, so none of these completed frr3 games was awarded by a runner timeout. That is the directly supported statement. The unchanged native default insurer contains no deadline; its native shortcut transition theorem is stronger than a timing observation under its precise hypotheses. Foreign delegation has a finite deadline and its reproduced actions remain empirical evidence. Several opponents also contain their own cutoffs, so universal game-outcome invariance under speed or scheduling changes is not established by observed seat agreement or by these timing maxima.

There is a useful narrower observation: every recorded v46 call in frr3 is below its three-second default planner budget, consistent with the cutoff not binding in these executions under ordinary agreement between the wall-clock and monotonic-clock intervals. This neither records the planner's deadline branch decisions nor proves what happens under a different load. No cutoff sensitivity experiment was performed here. Suggested wording is: “These completed games incurred no runner timeout. The retained paired outcomes agree, and the separately specified candidate-action reproductions matched; these observations do not establish load independence for opponents with planner cutoffs.”

## Recommendation labels and report corrections

The fixed report's sections 2 and 7 still call v41 final and list only v34-v43 as the later three-second-cutoff family. Frozen v46 also has TIME_BUDGET = 3.0 and deadline checks in plan.py, and fortress.py calls that planner without overriding its default budget. Include v46 explicitly and describe v41 as the version used in frr1/frr2, not as the final lane recommendation.

A further dated lane update was visible during this review: notes/defense.md at 22:39Z says v48 replaced v46 as the lane's final recommendation, and the 22:40Z addendum repeats it. The exact excerpt and review-time note hash are retained. This is an attribution update, not a re-evaluation of v48 here. The frr3 label should remain v46 because those are the actual pinned policy bytes; the report can call it the lane recommendation when frr3 was queued. Current frozen v48 plan.py has the same three-second cutoff as v46. No unmeasured frr3 result is transferred to v48 by this review.

Required edits are therefore narrow: state the eleventh imposed diagonal zero; restrict the 0.30-second number to the two high-factory histories; replace unrestricted runtime-causality prose with exact observed-reproduction/no-runner-timeout statements; and reconcile the final-version and cutoff labels. No frr3 outcome or optimal-face numerical correction is needed. The report and every other lane's files were left unchanged.

## Retained identities and execution limits

All supporting paths are relative to the project. No JavaScript or TypeScript, server/listener, RLScience or other cluster, remote compute, GPU, Lean/lake, protected write, git commit/push or online posting was used. Core 28 has no continuing job from this review and will be free before the 23:00 reservation.

| Artifact under frr3_extension_review_001/ | SHA256 |
| --- | --- |
| REPORT.snapshot.md | 471620efbf169a2f9118b58c2c2a1fd640b8640c00de05bc034e67044e3175af |
| read_artifacts.py | f80479f0db229218991d8127743a0efdc4589553fb8efa7cf01064d3ecb67833 |
| audit.json | 28982a17f012ddcf87eaf379b16b04ae1a9014135b615caf7a9a6cf5ffb08ecb |
| PROOF.md | 2fadc704e204dcdfa51f7041a124254485d95e01f6a32d202a828b902169f86b |
| frr1_identity_supplement.json | 01ff6b07dccb91c18036f956e9f1261aa3f49830037a7810d7e9accf0100180f |
| runtime_scope.json | db68da6400df334acca7e1df3764c94feff51cb5900df470de15f608e349a1a4 |
| runtime_and_repeat_supplement.json | ab8136463b74d34959ab3f311a2b476f362ecf4684fa34fe8bdca6a55adb145d |
| defense_2239_excerpt.md | ad59ad3414f4145def4f3ce1b0137e8e32adfc3153fbb10f5a5667b167eb0116 |

The audit receipt also retains all 20 raw log hashes, full parameterized specifications, source maps, rule identity and reviewed source/report hashes. This review is descriptive retained evidence, not a new pre-game declaration.
