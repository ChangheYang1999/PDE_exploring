# Economy final recommendation gate: interim independent review

Written 2026-10-31T22:58:01.611785Z. Actual reviewer: GPT-6 Astra, distinct from the Opus lead and economy collaboration. This is a supplementary posthoc source and retained-result review, not a new strength sample. The inspection ran from 22:56:10.458161Z to 22:56:22.815919Z. This document refers only to that fixed input snapshot.

## Current verdict

**CONFIRMED:** the completed sweep supports selection of af5 by the stated selection rule. **OPEN:** the recommendation over g1. The captured afq56 file contains 54 of 86 conditions, and afg5 is absent. Partial results are not grounds for a final recommendation.

The two completed sweep runs contain exactly 290 distinct standard-start conditions each, with both physical seats for each of 145 exact opponent specifications. The af5, af6, g1 and V29 outcomes on those conditions are respectively 264-0-26, 238-4-48, 228-14-48 and 48-12-230. Both new sweep runs report zero harness errors, bot errors, rejected actions, scenario errors and detected source changes. Every paired af5/af6 outcome, normalized HP margin and ending round agrees across seats. These are checks of retained result rows and completion output; this review did not independently replay or regenerate games or validate every raw log's terminal event.

The original 18.22 rule requires more total wins than g1 and no pool with more than two fewer wins. af6 qualifies with 238 versus 228, its worst pool difference being -2 on f5t. af5 qualifies with 264 versus 228, its worst being -2 on GUARDED_MAZE. The additional 18.25 rule picks the qualifying value with more wins, with af6 as a tie-break. Therefore af5 is the selected value. The notes disclose that 50 partial af5 results were seen in a test before afs5 completed; the tie-break was added during that period. It did not determine the observed non-tie result. The retained notes provide a chronology, not an independently timestamped preregistration service.

## Denominators and paired reductions

**CONFIRMED:** the 14 named R13 pools contain 846 condition occurrences but only 402 distinct exact opponent specifications, each in two seats, hence 804 unique conditions. The 145 sweep specs and 257 remainder specs are disjoint and exhaust this unique gate. All 514 remainder conditions have equal V29/g1 WDL in the retained baseline rows. This is WDL equality, not a claim of equal action streams, HP margins or private states.

The later complete comparison should report both the individual named pools and the deduplicated 804-condition union. Summing pool rows is a valid explicitly weighted 846-occurrence table, but is not an 846-unique-condition sample. Twenty duplicate lane rows in the inspected baseline files agree in outcome, normalized margin and ending round; no conflicting duplicate was found. Opponents are matched by complete spec strings, scenario and candidate seat, never display labels.

The declared bootstrap is reproduced exactly: W=1, D=0.5, L=0; cluster by exact opponent spec while retaining both seats; 4,000 resamples using `random.Random(1)` over sorted opponent specs; report sorted sample indices 100 and 3899. Exact numerical input bytes are retained.

| Difference on the selected sweep | Mean | Lower | Upper |
| --- | ---: | ---: | ---: |
| af5 minus g1 | 0.1000000000 | 0.0379310345 | 0.1586206897 |
| af5 minus af6 | 0.0827586207 | 0.0275862069 | 0.1379310345 |
| af5 minus V29 | 0.7241379310 | 0.6275862069 | 0.8103448276 |

These intervals describe this selected list under its declared resampling method. They are not independent-seat intervals, a correction for choosing af5 over af6, or a confidence guarantee for a broader opponent population. Per-pool reductions are retained in `inspection.json`.

## Recommendation and freshness scope

The first recommendation condition is that af5 minus g1 on all 43 fresh56 specs has a paired cluster-bootstrap interval not entirely below zero. This means upper endpoint at least zero. It is a permissive non-refutation rule, not evidence by itself that af5 is superior or statistically noninferior.

The 18.26 added condition requires no R13 pool with more than two fewer af5 wins than g1 on the conditions covered by afs5 and afg5. It was stated after the sweep choice and afq56 launch, before any reported afg5 result. If afg5 is stopped incomplete, the notes explicitly require a recommendation conditional on the covered part. The separate prediction that at least 95% of its 514 outcomes agree with g1 permits at most 25 differences; it is not stated as an additional recommendation condition. Neither condition has been certified here on complete follow-up data.

Fresh56 is exactly fresh5 followed by fresh6: 27 plus 16 distinct specs, with zero exact-spec overlap with the 402-spec gate. Its responses to af5 are newly measured after af5 selection. However, the lists and older g1/V29 results were already available wholly or partly while the sweep was considered; these are not previously unseen opponent families. The notes also identify 28 W3 counter specs, most developed against best_v9e, and a 15-spec complement comprising five lead policies and ten fortress versions. The latter is a provenance category from the lane, not proof that all policies are statistically independent or unrelated to research selection. Report these groups separately, particularly for the eventual best_v9e comparison. This review has not checked completed bvf or afrr evidence.

## Source and evidence limits

All 359 recorded loaded Python source paths agree with current bytes, and all 88 inspected entry module hashes and static import-closure version digests agree. The af5 entry is the same frozen econ29 source as V29, with the exact declared query ending `fill_threat=true&attack_from=5`; econ29 SHA-256 is `0c71ec9bc7b772313cc302ed1296b586cdcf98ea3bc2cdf1044e60f5220c855c`.

This authenticates retained row claims against source bytes read during this review. The harness compares version/source hashes before and after each match and records no changes. Neither mechanism continuously monitors execution or excludes a transient change restored between checks. Python source digests do not authenticate every runtime data file, environment or deadline branch. The current raw logs, policy decisions and engine behavior were not independently re-executed.

The fixed inspection is `inspection-20261031T225610458161Z/inspection.json`, SHA-256 `5cc12012e159a33e7f4fb3302ada1d6ec9ed70ba5dfe1610ca3749a7d71573da`. Its exact input map is `inspection-20261031T225610458161Z/inputs.json`, SHA-256 `bc062c3fe55a54245fd583a21c0a37b60b23332b8c9c1aa25df6564d82fcffc0`. Gzip objects preserve original bytes and both original and compressed hashes. The inspector SHA-256 is `b742c10febb4bf80753ce83a2d901459e396ca6f57b154435b732d8c5b93da79`.

Key frozen input identities:

| Input | SHA-256 |
| --- | --- |
| economy notes snapshot | b19eb7169a753b516b6635e95282e500f8d01f3f37240388b949c52bd81766fa |
| dec22.py | 08c68cbdaf125bec22256cbae8a64798a1a2ef851dbf2ad04925c241f2e40838 |
| pooltab.py | b2e5020f96faa9b4cb88b4c41115f80a96eccb7d51c111da66321e8cb2793324 |
| afs5 results | 1f79519733de6661b9d633298ac819771c1b990bef28225140a3aba90600a5f7 |
| afs6 results | 62c59344d51f124ee714d3ac09dc20e0d01f6355542345d1eb0f95207fcd2766 |
| partial afq56 results, exactly 54 rows | 3f1754c12fd9956a0cdd3b2ad9d0bdf6b47d59820a909bc1d83a0df870782fd6 |

No policy import, constructor, decision, game, Engine replay or test ran. No JavaScript/TypeScript, server, cluster, remote compute, GPU or Lean tooling was used. Only this owned review folder was written.
