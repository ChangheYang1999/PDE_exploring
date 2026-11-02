Completed scenario review, 2026-10-31T23:49:08.593410+00:00.

H18.31a holds on all 120 declared comparisons. scnaf5, V29 and g1 each have 113 wins, no draws and 7 losses. Every exact opponent/scenario/physical-seat join agrees on recorded winner, candidate-oriented HP margin and round count. There are zero af5/V29 differences and zero g1/V29 baseline differences. Equality of these three recorded values is the tested claim; complete action-history equality was not tested.

The exact design is five opponents from opp_clockfree5.txt, 12 named scenario starts, and both seats: 5 x 12 x 2 = 120 distinct conditions. The opponent specifications are the eco6_t5 archetype, frozen lead_best_b, frozen lead_best_a, frozen v2 with late_round=6 and phi=0.0, and frozen lead_v4. Full entry strings, af5/g1/V29 parameters and all joins are retained in the inspection JSON. Each scenario has ten conditions and identical W-D-L for all three candidates:

| Scenario | W-D-L for each candidate |
| --- | --- |
| mirror:51:2 | 10-0-0 |
| asym:52:2 | 10-0-0 |
| mirror:53:3 | 10-0-0 |
| asym:54:3 | 9-0-1 |
| asym:55:2 | 10-0-0 |
| mirror:56:3 | 10-0-0 |
| mirror:61:2 | 8-0-2 |
| asym:62:2 | 10-0-0 |
| mirror:63:3 | 8-0-2 |
| asym:64:3 | 9-0-1 |
| asym:65:2 | 9-0-1 |
| mirror:66:3 | 10-0-0 |

The joined baseline subsets are exactly 60 V29 records from the complete 816-row hs3 file, 60 V29 records from the complete 612-row hs4 file, and 120 g1 records from the complete 408-row hs34g1 file. All 120 new scnaf5 records are used. This is 360 selected candidate/baseline records for 120 conditions, with no duplicate or omitted matching condition. The candidate run has a summary and one console completion line reporting 510.9 seconds. Its result bytes remained unchanged throughout this review. Partial scnaf5 reads made before completion were limited to status and were not reduced as completed evidence.

All selected records report zero harness errors, bot errors, rejected actions, scenario errors and source changes. The archive audit verifies 85 input identities, 56 recorded loaded-source paths and six entry/static-closure identities, with no findings. Current source matches are receipt-bound evidence, not continuous runtime monitoring or a complete environment/data closure. The largest recorded af5 call in this campaign is 1.7023 elapsed wall seconds, line104, physical seat1 against frozen lead_v4 on asym:54:3. It is a rounded observation, not CPU time, a runtime bound or a guarantee for other conditions. The clock-free list label does not prove universal clock independence of surrounding runtime behavior.

The dated section18.31 condition was written before these scnaf5 calls and requires the exact finite comparisons above. Its standard-start restriction on an observed scenario mismatch is not triggered. This does not establish unrestricted scenario transfer, generic scenario superiority, or an unbiased strength sample. These starts and opponents already had V29/g1 baselines. The previously qualified af5 standard-start recommendation, the separate 95-percent agreement prediction, and this finite scenario control remain distinct. afs4/afs3 remain development evidence and do not retune or replace the selected af5 recommendation.

The actual reviewer model is GPT-6 Astra, distinct from the Opus lead/economy collaboration. The review used standard-library source, archive and result inspection on core30 at nice19, with no policy, constructor, game, Engine, replay or test calls. Earlier artifacts, chronology corrections and narrative addenda remain unchanged. The notes snapshot captured here still contains the section18.34 runtime sentence corrected by [addendum012](REPEAT_NARRATIVE_REVIEW_012.md); no 0.8-second claim is adopted here.

Read [inspection](scenario-control-20261031T234828252397Z/inspection.json), [input identities](scenario-control-20261031T234828252397Z/inputs.json), and [reader](inspect_scenarios_007.py). Reader SHA-256: ff2b64e836a9e3db5a0d87765d7aa117f28b9c5cf57d7ac09a42e9e1208af6d9. Inspection SHA-256: 746dd4d3a8a0b0710114692f4a0fe824444c4c8af0f9e61234aaf5f2749dddec. Input map SHA-256: db1c3bd0ce13a58ef5ce81fa356b8899de24819259fad610ea139119e7662272. scnaf5 results SHA-256: bbd96349b4ecbed3d70dea844cee3d5046367e9b5e51505c80b77339b211f32a.
