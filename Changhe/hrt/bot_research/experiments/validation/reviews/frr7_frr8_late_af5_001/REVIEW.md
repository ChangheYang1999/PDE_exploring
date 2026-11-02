# Late AF5 campaigns: completed record and source review

Prepared 2026-10-31T23:44:36Z. Reviewer model: GPT-6 Astra. This review uses source text and retained JSON only. It makes no policy, constructor, engine, replay or existing project-checker calls. The independent readers use the Python standard library. The parent coordinates findings with the actual Opus lead; this receipt does not claim that Astra is Opus.

**Claim.** frr7 and frr8 supply complete, internally consistent descriptive evidence for their exact conditions. **Method.** Join full policy specification, scenario and physical candidate seat, authenticate source and raw-log bytes, and independently reduce all action, combat, income and terminal records. **Result.** frr7 is 13W4D11L on 28 conditions; frr8 is 2W0D0L on two conditions. Both final grids are complete, without duplicate or extra conditions, missing logs, rejected actions, bot errors or discarded-call exceptions. **Verdict: CONFIRMED for retained-record consistency.** This is not an independent engine replay or fresh-policy reproduction.

## Completion and exact conditions

`queue_h21.sh` states the two campaigns prospectively as descriptive and keeps every log. The retained queue log records frr7 from 23:20:46Z to 23:37:28Z, then frr8 to 23:41:54Z; both exit 0. Initial inspection preserved frr7 at 25/28 with frr8 absent. The second snapshot preserved completed frr7 while frr8 was not complete. `input_manifest_final_001.json` is the first snapshot here covering both completed campaigns. Earlier observations have not been overwritten.

AF5 is exactly the full V29 specification in `rr_specs.sh` plus `attack_from=5`, byte-identical as specification text to `experiments/economy/specs/af5.spec`. G1 uses `attack_from=7`; V29 leaves that argument at its default 2. All other explicitly supplied parameters remain part of each condition key. The opponent AS1C is the exact best_v9e factory with `attack_share=1.0&catch_up_share=0.5`, rather than the default best_v9e factory.

frr7 uses seven opponents, two fixed scripted starts, and both physical candidate seats: 7 x 2 x 2 = 28. Its opponents are best_v9e, best_v9f, v41, V29, g1, AS1C and v48. frr8 adds AF5 against v48 on the standard start in both seats. These two standard conditions do not overlap frr7 or economy's afrr, whose opponent set stops at the ten original frr1 strategies.

The following table reports AF5's W/D/L, HP difference and final round. An entry marked “both” holds in each physical seat. HP differences are AF5 HP minus opponent HP, not sums across seats.

| Opponent | mirror:1:2, both seats | asym:23:2, AF5 seat 0 | asym:23:2, AF5 seat 1 |
| --- | --- | --- | --- |
| best_v9e | W +2660, r22 | W +1250, r14 | L -4470, r21 |
| best_v9f | W +2660, r22 | W +1250, r14 | L -4470, r21 |
| AS1C | W +2660, r22 | W +1250, r14 | L -4470, r21 |
| v41 | L -15, r50 | W +2218, r22 | W +3215, r21 |
| V29 | D 0, r50 | W +1250, r14 | L -1250, r14 |
| g1 | D 0, r50 | W +1250, r14 | L -1250, r14 |
| v48 | L -15, r50 | L -9822, r19 | L -2385, r17 |

In frr8, AF5 beats v48 **795:740, +55 at round 50 in both seats**. Together frr7/frr8 contain 30 games, 1,804 player-round records and 504,024 accepted actions. The reader additionally checks the comparison campaigns frr2/frr4/frr5/frr6, for 158 games, 9,234 records and 2,739,683 accepted actions overall. These totals distinguish new reviewed games from reused comparison records.

## Exact overlap, rather than substituted self-play

**Claim.** AF5 preserves V29/g1's recorded scripted trajectories. **Method.** Compare complete canonical histories on exact full-opponent-specification, scenario and physical-seat joins. Canonicalization removes only the match identity metadata and snapshot policy names; it retains ordered actions, all other events and snapshot fields, player indices, rounds and results. Metadata identities are checked separately. **Result.** Against V29's retained comparison rows there are 24 exact matches, all with identical complete histories. Against g1 there are another 24 exact matches, also all identical. The two sets overlap in 20 AF5 conditions and their union covers all 28 frr7 conditions. Each comparator's four absent conditions are explicitly listed; none is filled with an invented self-play draw. **Verdict: CONFIRMED on these exact histories.**

Against v46 and v48's 24 common scripted conditions, AF5 has zero better, 13 equal and 11 worse W/D/L outcomes, separately for each fortress comparator. AF5 is 13W4D7L there; either fortress is 22W2D0L. No matched complete histories are equal, and none has the same W/D/L, HP and length triple. AF5's four frr7 conditions against v48 are additional observations outside these common grids.

On the two standard frr8 conditions, AF5 improves on V29's two losses to v48 in frr5. AF5 and g1 have identical complete histories and +55 margins against v48 in matching physical seats, although the source specifications differ. `record_audit_final_001.json` lists every common, unmatched and first-different-round condition; this review does not collapse physical seats into independent random samples.

## Initialization, source identity and the limit of a gate explanation

The tournament source uses a fresh spawned worker per game and resolves a fresh factory per side. Scenario overrides fix the first two submitted action lists. The underlying policy is still called on each actual observation during those rounds, after the override list is computed, and its private side effects persist even when its proposal is discarded. Exceptions from discarded calls are separately retained and are zero in these records. Thus these games do not use cold initialization at round three.

The source is compatible with a foreign-map gate suppressing ordinary attack purchases before round 11. It does **not** prove that `attack_from` is irrelevant to every scripted state. In frozen V29 `econ29.py`, the ordinary attack helper checks `hold` at line 669, but the finishing and doom branches at lines 740 and 806 test `attack_from` independently of that gate. Requested coordinates also enter private `state["req"]` even when a scripted override discards the proposal. The full-history equalities above are measured facts; a universal branch-equivalence claim remains **OPEN**.

Every row's entry SHA256, loaded-source map, recorded unchanged-source flag and static dependency version agrees with the archived inspected source. The v29, v46 and v48 package manifests also match in full. The v46 and v48 fortress entry bytes differ: `a0aa939d...` versus `067af590...`. Their equality in earlier measured histories never implied byte equality. The installed `bots/best.py` still equals frozen best_v9e, SHA256 `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87`; neither AF5 nor v48 is that installed entry point.

These checks bind the actual retained bytes and current sources. They do not establish uninterrupted historical source immutability, historical runtime JSON identities where the harness did not pin them, or absence of erased attempts. Constructors run before the harness's pre-match version sampling. Accepted-action arithmetic checks verify retained event consistency, not the counterfactual policy proposals omitted by the harness or every rule of combat.

## Runtime and reporting scope

The largest recorded AF5 call is 8.6205 seconds in frr7 and 9.0790 seconds in frr8. Corresponding v48 maxima are 1.1860 and 0.5705 seconds. Other frr7 maxima are best_v9e 2.3415, best_v9f 2.3928, AS1C 2.1881, v41 1.3001, V29 3.5153 and g1 3.3798 seconds. These are rounded elapsed wall times retained by the harness, not CPU times or certified runtime bounds. The result rows locate the game and physical seat but do not record the round of each maximum. Different measured latencies do not establish a causal machine-load effect. Later cutoff or timing invariance outside the inspected conditions remains **OPEN**.

**Claim.** The inspected report's AF5 seat-0 asym margin against its three lead opponents is +4470. **Method.** Read the exact archived report and original result and terminal records. **Result.** Each game ends 790:-460, giving **+1250**, at round 14. The -4470 reverse-seat losses are correct. **Verdict: REFUTED for that dated report sentence.** `report_discrepancy_001.json` preserves the claim and correction; the parent's separate raw-terminal check confirms it. A later report amendment does not change this historical receipt.

The campaign was specified descriptively after extensive research on these policies and starts. It is neither an independent held-out population sample nor a full test of economy hypothesis 18.31 over its separately specified opponents and scenarios. Its scripted outcomes favor v46/v48 over AF5 on the common conditions; its two standard outcomes favor AF5 over v48. Recommendation beyond those conditions needs the separate economy gate and finite-matrix evidence. This review does not independently repeat the 846-membership gate and does not inspect or tune against reserved D.

[The standalone AF5 matrix proof](af5_matrix_extension/PROOF.md) treats the separately authenticated standard-start frr1 plus afrr W/D/L object. It proves the new complete optimal set, with guard00 and AF5 each at one third and the remaining third split between AS1C and P5TNUBM. The theorem also handles unmeasured fortress edges explicitly. Its rational verification and historical-data and reproduction limitations are separate from the complete raw-log audit of frr7/frr8.
