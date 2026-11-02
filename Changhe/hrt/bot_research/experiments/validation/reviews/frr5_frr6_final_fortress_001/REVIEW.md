# Completed frr5 and frr6 independent review

Written 2026-10-31T23:31:39.477589+00:00. Actual reviewer model: GPT-6 Astra. The work used source inspection and independent Python standard-library readers of retained JSON. It made zero policy constructor, decision, game engine, replay or existing project-checker calls. The research-storytelling skill and its analyzed writing references guided the explanatory prose. The parent reviewed the matrix argument and coordinates the findings with the Opus lead.

**CONFIRMED for the retained conditions:** final fortress v48 gives 4W4D12L on frr5 and 22W2D0L on frr6. Every matched condition reproduces v46's W/D/L, both terminal HP values, end round and canonical retained history. There are 44 matched conditions across 88 games in frr3 through frr6, with 44 new v48 games. This does not establish identical implementations or policies on untested observations.

The [initial inspection](INSPECTION_001.md) remains unchanged. It checked thirteen frr6 games and separately archived a later sixteen-game snapshot without presenting either as complete. The final snapshot began at 23:30:00 UTC, after frr6's queue recorded exit 0 at 23:28:24. It contains all twenty-four result rows, their logs and the final summary. The declaration commands specify twenty-four conditions, not twenty-eight. frr5 has all twenty rows and a completed summary; its output reports completion in 1708.7 seconds. The report gives its interval as 22:49:46 to 23:18:15 UTC. The h19 shell was stopped before starting frr6, while its frr5 child continued; h20 launched frr6 at 23:15:51. This scheduling change is preserved in both queue logs.

The standard start uses v48 against ten exact opponent specifications, once in each physical seat. The table gives v48's result, its HP minus its opponent's HP, and the ending round. Both seats agree in these three quantities. Full specifications, including every factory parameter and JSON-valued option, are in `record_audit_final.json` under `specs`; joins use those full strings, start and physical candidate seat rather than abbreviated names.

| frr5 opponent | Outcome, HP difference, end round in each seat |
|---|---|
| best_v9e | L, -5, 50 |
| best_v9f | L, -5, 50 |
| af2g | L, -5, 50 |
| P5TNUBM | D, 0, 50 |
| v41 | D, 0, 50 |
| V29 | W, +5, 50 |
| g1 | L, -55, 50 |
| guard00 | L, -40, 50 |
| threat_defender | W, +2000, 11 |
| AS1C | L, -5, 50 |

frr6 uses six of those opponents, two scripted starts and both physical seats. Each entry is outcome, HP difference, end round. The mirror column applies separately to both seats.

| Opponent | mirror:1:2, each seat | asym:23:2, v48 seat 0 | asym:23:2, v48 seat 1 |
|---|---|---|---|
| best_v9e | W, +1555, 14 | W, +2385, 17 | W, +4222, 18 |
| best_v9f | W, +1555, 14 | W, +2385, 17 | W, +4222, 18 |
| v41 | D, 0, 50 | W, +5455, 21 | W, +1265, 20 |
| V29 | W, +15, 50 | W, +2385, 17 | W, +9822, 19 |
| g1 | W, +15, 50 | W, +2385, 17 | W, +9822, 19 |
| AS1C | W, +1555, 14 | W, +2385, 17 | W, +4222, 18 |

**CONFIRMED, record consistency:** [aggregate_records.py](aggregate_records.py) checks all 88 logs, 6,272 records and 2,652,072 accepted action events across frr3 through frr6. The v48 half contains 3,136 records and 1,326,036 accepted events. No condition is missing, duplicated or unexpected. No recorded rejection, bot error, scripted-call exception, source mismatch or arithmetic discrepancy was found. Checks cover the complete round/player grid, accepted costs, action interleaving, HP and gold balances, income components, factory/turret/wall counts, cross-player damage and hit totals, every player-summary field and terminal result. All three summary tables in each of the four campaigns reproduce from raw result rows. The final [record audit](record_audit_final.json) and [supplementary checks](supplementary_checks_final.json) retain the details and every error list.

All twenty frr3/frr5 and twenty-four frr4/frr6 comparisons also agree in their canonical histories. Canonicalization removes the top-level match metadata and each snapshot's policy name, then retains every event, action order, snapshot field, schema, physical player, round and result. Initial rules, specifications, scenario and metadata are checked separately against the result row. This is equality of retained public records. Discarded proposals, private states and unlogged combat ticks are outside that comparison. The counts describe fixed development conditions, not independent samples from an opponent population.

**CONFIRMED, initialization semantics:** source inspection of `harness/tournament.py`, `harness/match.py` and `harness/scenarios.py` shows a fresh spawned process per match and one factory construction per side. During each of the first two scripted rounds, the wrapper computes the script and still calls the underlying policy once on the actual observation. It discards that proposal, retains its private effects, and returns the script. No such call raised a recorded exception. This differs from an initialization that skips policy calls. Mirror seed 1 is shared between the physical players; asym seed 23 becomes seeds 46 and 47 by physical seat. Swapping candidate seats therefore changes its assigned initial geometry. No private-state reproduction audit was performed here.

**CONFIRMED, source distinction:** twelve of thirteen frozen Python package files are byte-identical between v46 and v48; `fortress.py` differs. The [retained diff](source_diff_v46_v48.patch) shows that v48 counts the active roster in the gun gate, reserves a sampled finishing attack through defense, and permits capacity defense to spend all unreserved gold when that reserve exists. Reserve sizing uses a binary search whose monotonicity is a heuristic premise. The source explicitly calls the sampled gun test a counterexample search, not a certificate. Equal public histories do not show that every changed private branch was inactive.

The frozen fortress source hashes are `a0aa939dd81fdbfd1ab4da4fd0c40cbc2e145058f5c01f6c606d27b4c28c15a7` for v46 and `067af590c9d2fceef852cc4ac3516d31e01919993f98755cbed44a05d68c37f5` for v48. Both package manifests match all their retained files. Entry hashes, recorded loaded-source hashes and independently reconstructed static Python closure versions match the archived inputs. The installed `bot_research/bots/best.py` remains byte-identical to frozen best_v9e, SHA256 `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`. Thus v48 is the defense lane's final recommendation, not the published entry point. The queues call these runs descriptive and leave the earlier selection unchanged.

**CONFIRMED, conditional matrix claim:** [the standalone proof](finite_matrix_extension/PROOF.md) shows that either or both added fortress rows receive zero weight in every optimum of the recorded finite W/D/L game. It permits any unplayed mutual entry q, with reverse entry -q and imposed zero diagonals. The original dual mixture on AS1C, g1 and guard00 gives each added row strictly negative payoff -1; every original optimum gives each added column at least 2/3. Hence no assumption that v46 versus v48 draws is needed. The [exact row certificate](finite_matrix_extension/verification/row_certificate.json) binds the raw standard-start joins and rational arithmetic. The earlier frr1 theorem and its provenance limits remain dependencies. This does not claim optimal play in the unrestricted game or deadline-independent randomized-policy execution.

**CONFIRMED, measured timing; OPEN, causal or load-invariance claims:** v48's maximum recorded call is 2.2469 seconds in frr5 and 1.2626 in frr6; v46's corresponding maxima are 2.3491 and 1.9972. frr5's largest opponent maximum is P5TNUBM's 14.0318 seconds; frr6's is g1's 9.5765. These are elapsed durations, not CPU measurements. The report's rounded maxima agree with retained rows. The wrapper uses perf_counter, while the nested three-second gun-planner deadline uses time.time. Consistent clock progression supports nonactivation of that deadline on these sub-three-second fortress calls. A different load could cross it. The records identify the game containing each maximum, not its decision round or the timer branch. No causal timing change is inferred from comparisons between runs.

The final archived report, SHA256 `8de4aec524de6bb570db6d25a517a609633b5683e87fbbf76bca5441ee337270`, correctly states the completed frr5/frr6 outcomes and this clock qualification. Two wording refinements remain useful: replace “44 games of frr3 to frr6” with “44 matched conditions across 88 games”; and clarify that “This is the gold effect” does not attribute P5TNUBM's 10.07-to-14.03-second difference to changed gold, since the matched public gold histories are identical. Other defense-lane regression pools and artificial-state claims cited nearby were not independently audited in this review.

**OPEN provenance limits:** the retained source checkpoints and final current-byte check do not prove uninterrupted historical immutability. Queue comments predate launch, but this review's exact archives were collected later. The harness's Python closure omits runtime JSON; balanced rules are embedded and checked in every initial record, while the currently archived guard witness does not acquire a historical launch pin merely by being archived now. Constructors precede the harness's pre-match version checkpoint. No durable attempt ledger establishes absence of erased attempts. Recorded acceptance and arithmetic consistency are not a new engine legality check or replay. A fresh factory in the original harness is not an independent fresh-policy reproduction audit.

The [reading-order index](README.md) links the proof and evidence. Three dated input manifests preserve initial, supporting and final snapshots with exact compressed and original hashes and lengths; live reports and notes may subsequently change. The final manifest contains 229 inputs with no detected stat changes during collection. [seal_001.json](seal_001.json) binds this review and the completed archive, current-source and closed-record rechecks. The earlier incomplete inspection and its evidence remain intact.
