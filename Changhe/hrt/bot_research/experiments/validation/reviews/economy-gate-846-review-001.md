Independent review of economy note 18.23 and REPORT section 5.15

Prepared: 2026-10-31T22:15:42.258207Z. Final retained-row aggregation: 2026-10-31T22:14:10.313415Z to 2026-10-31T22:14:11.366615Z. Verdict: CONFIRMED for the published pool-weighted arithmetic; REFUTED if 846 is described as the number of distinct conditions or the 448 subtotal as disjoint from the four selection pools. Full policy-history equivalence and generalization beyond these opponents remain OPEN in this review.

The updated table can replace the older 838-membership table. Counting each condition once in each pool containing it gives the exact note 18.23 totals:

| Candidate | Pool memberships | Candidate W-D-L | Baseline W-D-L | Worse | Better |
| --- | ---: | --- | --- | ---: | ---: |
| V29 | 846 | 584-18-244 | 524-82-240 | 150 | 208 |
| g1 | 846 | 764-16-66 | 524-82-240 | 72 | 304 |
| g0 | 846 | 748-22-76 | 524-82-240 | 84 | 298 |

Here an outcome is W if the engine winner equals the candidate's seat, D if winner is null, and L otherwise. Better and worse use W > D > L, not HP ordering. The baseline comprises frozen best_v9e and its declared development twins, with the exact mapping below. Both seats and every listed pool are included. The result supports complementary strengths on these retained opponents. It does not establish domination: g1 is worse on 72 pool memberships, or 68 distinct conditions.

Method and completeness

The reviewer read experiments/economy/gate_vs_base.py statically, then wrote a separate standard-library aggregation, economy_gate_846_review_001.py in this directory. The review did not import or execute that economy script, a policy, or the engine. There were no policy constructors, decision calls, games, replays, or statistical resamples. The independent code read the retained JSONL bytes and joined by the complete candidate specification and (complete opponent specification, scenario, candidate seat). It checked signed HP against both recorded terminal HP values. It preserved the source file and line number for every joined row. The JSON receipt beside this review contains all 846 pool memberships, their baseline and three candidate rows, and the input hashes.

The original script selects baseline rows by substring, excludes catch_up_share=1.0, and silently overwrites duplicate baseline keys. This review first reconstructed that selection, then asserted the exact full specification allowed in each pool. Each pool selected exactly one permitted baseline specification, with the expected row count. There were no duplicate keys within any baseline pool, no selected baseline error rows, and no conflicting baseline (W-D-L, signed HP, rounds) across repeated cross-pool conditions. Thus substring selection and overwrite behavior did not alter this table.

The 21 named candidate run files included four absent files: runs/economy/g1ff/results.jsonl, g1fm/results.jsonl, g1fc/results.jsonl and afs5/results.jsonl. Their absence did not remove a gate condition. Every candidate had all 804 distinct gate conditions. The exact target specs occurred in 987 V29 rows, 960 g1 rows and 958 g0 rows across the present files, representing 961, 934 and 932 unique conditions respectively. Each candidate had 26 extra rows, all with identical outcome, signed HP and rounds: 16 repeats between gate1 and stdg or stdg2, and ten between gate1 and fam2b. None was a conflict; out-of-gate conditions were excluded. The receipt records every repeated row separately before deduplication.

All 804 distinct gate conditions have scenario=null. Each of the 402 opponent specifications appears in both seats. For each candidate, the W-D-L, signed HP difference and number of rounds agree between seats for all 402 pairs. The baseline has the same agreement within every pool. This is a comparison of observed terminal records, not a check of complete canonical histories or a proof that timed opponents behave identically on another execution.

Across all 3,336 joined source rows, including candidate repeats and baseline pool memberships, both players have zero recorded rejected actions and bot errors; every source_changed flag is false. All recorded td_game and td_bots source hashes agree with the current bytes. The recorded engine.py hash is c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d. Candidate and baseline opponent entry hashes and recorded version digests agree in every exact-condition join. These checks validate the retained metadata and aggregation. They do not replace original-engine history replay, fresh decisions, deadline audits, or a complete non-Python data dependency audit.

Exact specifications and baseline twins

V29 is the complete spec below. g1 appends exactly &attack_from=7. g0 appends exactly &r1_units=0&attack_from=7. The review required literal full-string equality for these joins; it did not merge other parameter settings.

```text
bot_research.bots.economy.frozen.v29.econ29:@make?free_fallback="zero"&foreign_attack_from=11&doom="next"&fac_cap=400&sat_reach=true&replan=true&foreign_sat_from=11&replan_gain=400&replan_base=true&own_in_layout="replan"&own_min_s=1200&min_cap=3000&active_cap=4000&fill=true&fill_reserve=true&fill_threat=true
```

All three use the entry-source hash 0c71ec9bc7b772313cc302ed1296b586cdcf98ea3bc2cdf1044e60f5220c855c and recorded version ce2aac794167150b798d9abffb430cf4aa8afd4a273090d79329a1418645b806 throughout the joined rows. The version identifies source code, not the parameter setting; the full spec is still necessary.

Let P denote this exact query:

```text
big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true
```

| Baseline entry and query | Pool memberships | Pools | Entry SHA-256 |
| --- | ---: | --- | --- |
| experiments.lead.frozen.best_v9e:@make, no query | 252 | PCS, TIMING, STRIKE1, f5t, HANDOFF, SCREENED | 70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87 |
| experiments.lead.v19:@make?P&foreign_target="econ20" | 546 | TIMING2, PUNISH, BLUFFCOV, TARGETED3_P5TF, GROWERS, GUARDED_MAZE, STAGED | c5610e472bf3f35bb3e093a2cd8734c26f8af01d01b121f1348b95bcadd84b57 |
| experiments.lead.v18:@make?P | 48 | TARGETED2 | 8f444f28a6d0f490b7ad29cf3a97a5c2f338a7c2fdd6faf4acfed1dd5471c327 |

Each abbreviated module above starts with bot_research. The JSON receipt contains the expanded full strings and version hashes. Frozen best_v9e documents the displayed v19 setting as its development twin. tests/test_best.py specifies prefix comparisons, and experiments/lead/same_actions.py specifies full action-trajectory comparisons. This audit inspected their source but did not run them or inspect every historical twin-validation transcript. Its numeric baseline table is therefore a reconstruction using those declared twins, not a newly established universal full-history equivalence theorem.

The additional v18-to-v19 mapping is conditional on an ordinary standard start and successful calls on the actual consecutive observations. Source: td_game/state.py, engine.py and actions.py start with no buildings and add a building only at a submitted coordinate; lead/v16.py records requested building cells, and v17.py also records its added insurance buildings. v18's catch-up addition buys minions. Therefore the own-building-minus-requested set stays empty on this route of execution. v19's added target changes only the foreign-map branch, whose predicate stays false. With query P, its other behavior is inherited from v18. This argument does not justify reusing v18 as an econ20 twin after a scripted or externally injected building prefix. All selected scenarios here are null.

Distinct conditions and the 448 subtotal

The full table contains 846 pool memberships but only 804 distinct exact conditions, or 402 distinct opponent specifications in both seats. There are 34 keys occurring in more than one pool: 26 occur twice and eight occur three times. The 42 extra memberships are intentional consequences of summing the pool tables, not additional game evidence. The overlap pattern counts, including both seats, are:

| Pools sharing a condition | Shared keys | Extra memberships |
| --- | ---: | ---: |
| TIMING, TARGETED2 | 16 | 16 |
| TIMING, TIMING2, TARGETED2 | 8 | 16 |
| TIMING, f5t | 6 | 6 |
| f5t, BLUFFCOV | 2 | 2 |
| f5t, PUNISH | 2 | 2 |

Removing repeated pool memberships gives this descriptive table. Cross-pool baseline outcome, HP and rounds agreed on every repeated key, so deduplication requires no conflicting-result choice.

| Candidate | Distinct conditions | Candidate W-D-L | Baseline W-D-L | Worse | Better |
| --- | ---: | --- | --- | ---: | ---: |
| V29 | 804 | 546-14-244 | 504-64-236 | 146 | 186 |
| g1 | 804 | 726-16-62 | 504-64-236 | 68 | 282 |
| g0 | 804 | 712-22-70 | 504-64-236 | 78 | 276 |

The four excluded selection pools are GROWERS, GUARDED_MAZE, HANDOFF and f5t. Their 398 memberships are 398 distinct conditions. The other ten pools are PCS, TIMING, TIMING2, STRIKE1, TARGETED2, PUNISH, BLUFFCOV, TARGETED3_P5TF, SCREENED and STAGED. Their note 18.23 subtotal is reproduced exactly:

| Candidate | Other-pool memberships | Candidate W-D-L | Baseline W-D-L | Worse | Better |
| --- | ---: | --- | --- | ---: | ---: |
| V29 | 448 | 318-8-122 | 310-76-62 | 92 | 100 |
| g1 | 448 | 388-14-46 | 310-76-62 | 50 | 124 |
| g0 | 448 | 378-20-50 | 310-76-62 | 56 | 118 |

Those 448 memberships cover 416 distinct conditions. Ten of the 416 also occur in f5t: economy.timing, frozen.v13.econ13, frozen.v15.econ15 with free_fallback="leak", feature_bluff with turret_round=1, and guarded_schedule with schedule=[[1,"tier1",1],[5,"tier4",200]], all at their full specs listed below and in both seats. Excluding f5t as a pool therefore does not remove every selection-pool opponent from the remaining table.

After deduplicating the ten pools, V29 is 286-8-122, g1 356-14-46, g0 346-20-50 and the baseline 300-58-58 over 416 conditions. Removing the ten conditions shared with the four selection pools leaves:

| Candidate | Distinct conditions disjoint from those four pools | Candidate W-D-L | Baseline W-D-L | Worse | Better |
| --- | ---: | --- | --- | ---: | ---: |
| V29 | 406 | 280-4-122 | 290-58-58 | 88 | 78 |
| g1 | 406 | 350-14-42 | 290-58-58 | 46 | 102 |
| g0 | 406 | 342-20-44 | 290-58-58 | 50 | 96 |

The 406-condition table is an additional descriptive calculation, not a prospective test newly registered by this review. It is disjoint from the four named pools by exact spec. This does not show absence of all previous developmental exposure, behavioral aliases, related families, or lead-side selection bias.

A separate alias check decoded query parameters with the documented parse_qsl and JSON-value rules, without constructing policies. opp_key5.txt has zero literal full-string overlaps with the ten-pool union, but its URL-encoded guarded_schedule schedule decodes to the literal schedule in PUNISH and f5t. This is the same factory and kwargs, covering two seats. These two conditions are already among the ten removed above. The check does not attempt equivalence between different modules or omitted and explicit default parameters.

Note 17.14 records g1 as fixed at 17:53Z. The log filename timestamps on the selected candidate rows of the other ten pools range from 18:46:27Z to 21:29:40Z. This is consistent with matches after the recorded fix time. Later execution alone does not establish an unseen condition when its opponent also appears in earlier selection evidence. This review does not convert filename timestamps or a retrospective note into a prospective declaration receipt.

REPORT section 5.15 scope correction

At the reviewed report hash, section 5.15 says fresh5 and fresh6 compare the bots on opponents "not chosen from either bot's results". That sentence is too broad. Economy note 18.20 explicitly states before bvf that most W3 counters in both sets were built against best_v9e and that this family favors g1 by construction. The retained opp_fresh56_pools.json contains 43 opponents: 28 W3 counters, five lead bots and ten fortress bots. Its NOT_BUILT_AGAINST label covers the latter 15, not all 43. The report should distinguish "not used to choose g1" from "not developed against either candidate" and retain the separately reported 15-opponent subset. This audit verifies that scope mismatch and the group counts; it does not assert or recompute unfinished bvf outcomes.

The table arithmetic is ready for reporting with its weighting and twin qualifications. The strongest defensible comparison here remains conditional on these specified retained opponents and standard starts. A larger weighted win count does not remove the observed regressions, and counts from adaptively developed opponents are not independent population estimates.

Exact overlap list follows. Each row identifies one full opponent specification; scenario is null and both seats occur. Input identities after the list identify the bytes reviewed. No other lane's files were modified.

| Full opponent specification | Pool memberships |
| --- | --- |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.25` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5` | TIMING, TIMING2, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=1.0` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=5&budget_fraction=0.25` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=5&budget_fraction=0.5` | TIMING, TIMING2, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=5&budget_fraction=1.0` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=5&budget_fraction=0.25` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=5&budget_fraction=0.5` | TIMING, TIMING2, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=5&budget_fraction=1.0` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=6&budget_fraction=0.25` | TIMING, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=6&budget_fraction=0.5` | TIMING, TIMING2, TARGETED2 |
| `bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=6&budget_fraction=1.0` | TIMING, TARGETED2 |
| `bot_research.bots.economy.timing:@make` | TIMING, f5t |
| `bot_research.bots.economy.frozen.v13.econ13:@make` | TIMING, f5t |
| `bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak"` | TIMING, f5t |
| `bot_research.bots.counters.feature_bluff:@make?turret_round=1` | f5t, BLUFFCOV |
| `bot_research.bots.counters.guarded_schedule:@make?schedule=[[1,"tier1",1],[5,"tier4",200]]` | f5t, PUNISH |

Input SHA-256 identities at the aggregation time

| Project-relative input | SHA-256 |
| --- | --- |
| `../hrt-w2/scratch/g0.spec` | `ffe5b72ec41318353fdb194a0d21038f25825691cf2ce47d73130365975892c6` |
| `../hrt-w2/scratch/g1.spec` | `1cd961292dd9d36ade08496c534336a63cd27b2c682ae657f9e465e1f791cc05` |
| `../hrt-w2/scratch/v29.spec` | `6c578803c423ea7737428393cf0bfd4e2f5daa2e16d69a54bea3d52b29fc0535` |
| `bot_research/experiments/economy/gate_vs_base.py` | `b1f2a9ad0e8f83c565f47fedba436bb69fa2416dbbf2265356760f4abd8e68ed` |
| `bot_research/experiments/economy/opp_fresh56.txt` | `2fa5bfcd86f2189800081c19fba24a11e275cfc4ee489b4bdfe800dff2a494e4` |
| `bot_research/experiments/economy/opp_fresh56_pools.json` | `75761228b8e2fa8a7e14ed8c3ce1a5aa9a81c79dce9a757a1e4a1f756273417d` |
| `bot_research/experiments/economy/opp_key5.txt` | `5a45f5edbf2573522054cf1678a4772e9acdd95834357a46496267e7bfaf3cba` |
| `bot_research/experiments/lead/frozen/best_v9e.py` | `70ef8eab00ceca625b0f7459b8a12282d3391ce72cc2b812b6a8e6cf63a2fd87` |
| `bot_research/experiments/lead/same_actions.py` | `a92a3175963f231e0efa5f4146402a7438bf3325298159abef3766d34bfa97b7` |
| `bot_research/experiments/lead/v16.py` | `206312d5d042ae6a0e66e6375cb772c8a4072ee99d6c71f20ef50863e57f48bf` |
| `bot_research/experiments/lead/v17.py` | `1da55a11562df20255295edfc31863c0e716a82a4a3d1f76311ceed1611878ce` |
| `bot_research/experiments/lead/v18.py` | `8f444f28a6d0f490b7ad29cf3a97a5c2f338a7c2fdd6faf4acfed1dd5471c327` |
| `bot_research/experiments/lead/v19.py` | `c5610e472bf3f35bb3e093a2cd8734c26f8af01d01b121f1348b95bcadd84b57` |
| `bot_research/experiments/validation/reviews/economy_gate_846_review_001.py` | `14df25eb7a8c8eba080be45373ef74bbeec27ea9a6d9c5a69e51152df34a669c` |
| `bot_research/harness/match.py` | `56ecf235680e117b524e56a5d4f65f7b610de7e792ccd202658f228381e1c4a5` |
| `bot_research/notes/economy.md` | `663e64d240719f87fac196043641a0fb8790207c886eb8a92759f0f3d1cdc568` |
| `bot_research/reports/REPORT.md` | `99228b17e4dcae1bed283c16ec0ba72dda57951bb4b1b13bf003ba306099cd50` |
| `bot_research/runs/economy/afs6/results.jsonl` | `fddae0c4a1e87c31d50d38dae2bc7d8dcc7c7b8b0c3b815fc9180e84a7793377` |
| `bot_research/runs/economy/fam2b/results.jsonl` | `8dc5135044e6a88340e646f91c0d347fe5914cbfa5d90b15d579a3d12c7babdd` |
| `bot_research/runs/economy/fresh5a/results.jsonl` | `55cfcef36fb80cf1b850cf3c31def41b2cb06de20431904b9795a0387a20d0d0` |
| `bot_research/runs/economy/fresh5b/results.jsonl` | `c1baccea5fcc81135afd385b3343351f346043ff361a74cdc84d22054c7c9f37` |
| `bot_research/runs/economy/fresh6/results.jsonl` | `f717e2cc4f32a1bd092e3ed56131749d0c695ddc050f764b01e37140990ff4a6` |
| `bot_research/runs/economy/g1chk/results.jsonl` | `faba81da6e1e98d374419d3b77b9a39ec857a3888cbcc48ae1ec3abc0807d916` |
| `bot_research/runs/economy/g1fg/results.jsonl` | `ea7c71607e5e936b21fe8b27a2ea17ead36c3aaf437a6cfab9e3b1461d53ddd1` |
| `bot_research/runs/economy/gate1/results.jsonl` | `d10773c5a3e0770048f6570589a8e80c830e77f605c72afe7aa835aafb0d949f` |
| `bot_research/runs/economy/gmaze1/results.jsonl` | `d7e76eaa89b56c0471667fc35fd78323cb2b1d86fd6d17805f62f770c73eacb4` |
| `bot_research/runs/economy/grow1/results.jsonl` | `db174a6b31c7d409367b7991d16b7a8be6c80b7d1b667a34579ca7040b9eeaac` |
| `bot_research/runs/economy/hand2/results.jsonl` | `224732c9ec4666736e681db8a1a0b560278ce579826a64b0961cf2e87dc1f7f7` |
| `bot_research/runs/economy/hand3/results.jsonl` | `e59e68c9338855ae6e1e66efb1e1f55eb246169cfca2dbd65a3f58e008531423` |
| `bot_research/runs/economy/hand4/results.jsonl` | `3e9cdd892b1a8cb3e31c62894e35c72a909a5cbc6e34b45ff405c9a98ea80566` |
| `bot_research/runs/economy/pcs1/results.jsonl` | `063feb81d0dd21a200033a7dc10845029078acbe7b4d189590de3bb2f76bf1f7` |
| `bot_research/runs/economy/smoke31/results.jsonl` | `cbd5fe0b9f3ba1e032e9ef103408bdd1b06dbd818da63ccd1f233fb33d4637ce` |
| `bot_research/runs/economy/stdg/results.jsonl` | `339a8949f1a0a681ff50407326808a3a4e0baf7762655e86c9467c9234732183` |
| `bot_research/runs/economy/stdg2/results.jsonl` | `1d4f929d1ce872d5255f19638090e2640ad34c5ca969b492700c74deb054d783` |
| `bot_research/runs/economy/strike1b/results.jsonl` | `6e9f2208f16cc80bd07f785202faf9d22a2967fb87fc5d8b16a5b856000dccde` |
| `bot_research/runs/lead/ab1/results.jsonl` | `d8ec60575a436a1603782f63c86675478156b26bcf06f727894df98f3ef8336f` |
| `bot_research/runs/lead/bse_hd/results.jsonl` | `6e20d48fc3b066b9e5a663799e0178a8067008dd0602d56a11239d7d688ec7aa` |
| `bot_research/runs/lead/bse_sg/results.jsonl` | `d6bbd0949003df69337c53589f406d88be4a7959df01e79f52f2c0c15e01f296` |
| `bot_research/runs/lead/bse_tm/results.jsonl` | `29fa2b51c9886b00b1bb1c97a611c1f54ec1201c0c3e3cf72d133e01f6f1f067` |
| `bot_research/runs/lead/g13pc/results.jsonl` | `24078db0c511ee12a0159381c699aad6358201d7cec9e492a77d19fd49c7ffd1` |
| `bot_research/runs/lead/g9a/results.jsonl` | `0e4768315497b2d6bcf310194de61f2a0c8934014d3598705ed4671a6296dc00` |
| `bot_research/runs/lead/pu1/results.jsonl` | `6c39c76bd74e66737973f00ba6322e9654413cd7928104009592f372dad1684b` |
| `bot_research/runs/lead/t9k/results.jsonl` | `8cde3b7e3f1fcde6c7f0d0026e52220e9ecb83fdadf0a4862f59cf3532ede0c7` |
| `bot_research/runs/lead/tm2/results.jsonl` | `ad6584ab242f6158687dbbc834492510ad4b28dd200bca3dcf98a85edc7c7193` |
| `bot_research/tests/test_best.py` | `07ec39bb28f9daa245741bfe2d852c105f35b3e035f53b7b744377a822e19010` |
| `bot_research/tmp/base_b9a_v18f.jsonl` | `5cfb3c7e1714be8e3f70e86698d32c70e05278ef9905c450a16ca2836fe4f794` |
| `bot_research/tmp/base_gm2_v18f.jsonl` | `800c0f849475feb6ec14cd568998f360490f4bf5c840c7b8aaaecbb419546bb7` |
| `bot_research/tmp/base_st1_v18f.jsonl` | `d3c6db48e649f219595c8146e927a8225c804e5532c49af04a8cf6c48afd119f` |
| `bot_research/tmp/base_t8f_v18f.jsonl` | `e1ba3e92afe7474876ba7e471b6e38b9f719b65330f46cb8ac265f6901f1fa7b` |
| `bot_research/tmp/h14_gate.py` | `c01ed584cb728b93aeee8d5536bec50e4f807e6ade07fd25efc7c268b68aa77f` |
| `td_bots/__init__.py` | `4933fcf593f27a0c64c487f5399510e4eb8864118f8adaca61830049a79fa92c` |
| `td_bots/protocol.py` | `b20cc2ae7ed13013cd2504e8e26665acdbc8c6c07f65fd6ee13dc9216874ebaa` |
| `td_game/__init__.py` | `1a4268eeace53ec3b488ba2868c601c2be879d3ece5d36df3f99d70ac5b4646a` |
| `td_game/actions.py` | `d3b482371c4bf43f3da0028b4425d899be1b949a97a2c786617ee813a15f5f66` |
| `td_game/combat.py` | `17265171d1e2ab4c60b07f9b4f473a19667aef4a2110aeb2c07f1cb39f965228` |
| `td_game/config.py` | `ab1ca08d78081382e9f9a4ca7bff4985d101ec7b7621ecddfa48e46418701716` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/pathfinding.py` | `5ecce5a8737d43e3add703e4143f28a1d2bb8fb62e84a2d7f29be441749ae8b2` |
| `td_game/runner.py` | `cca08518177cfb6a102e2483765e66fa595539e7fc04c546bbe0cf20836f2bed` |
| `td_game/state.py` | `5d6df44f76a0f84d95d130e080a2e966bad02d06e08824cc818d6b08185b375f` |

Reproduction: run economy_gate_846_review_001.py from the project root with the documented Python environment, bytecode disabled, TMPDIR set to bot_research/tmp, nice 19, affinity core 30 and OMP/BLAS thread counts one. Its only imports are standard-library modules; its operations parse and hash existing data and write this review's JSON receipt. The input list includes the exact scratch spec files originally supplied by the economy lane; their complete text is retained in the JSON receipt and above. No input hash changed during the recorded aggregation.

Retained review artifact `economy_gate_846_review_001.py`: SHA-256 `14df25eb7a8c8eba080be45373ef74bbeec27ea9a6d9c5a69e51152df34a669c`.

Retained review artifact `economy-gate-846-review-001.json`: SHA-256 `d243192a3d235f2c38d4a9707c9ddfd0287fbfd9006dedd616b5daed37d95af7`.

Retained review artifact `economy-gate-846-review-001.aggregation.txt`: SHA-256 `567f3ec860093f0064e0c988f6beee8baca3208b58d419a04bfa0d4c6f2d07a2`.
