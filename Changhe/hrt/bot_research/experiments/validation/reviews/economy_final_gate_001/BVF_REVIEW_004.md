# Completed bvf retained-record review

Written 2026-10-31T23:25:03.631525Z. The reviewer is GPT-6 Astra. This is a supplementary source and record review, not a new strength sample. Opus collaboration remains in the lead and economy notes; this file does not claim an independent Opus review.

The completed bvf records confirm economy18.30's counts, margins, family reductions and numerical intervals. Exact matching on opponent spec, standard scenario and physical candidate seat joins all 86 bvf conditions to the retained afq56, fresh5a and fresh6 conditions. No duplicate or missing condition, reported error, rejected action, changed-source flag, or metadata inconsistency was found. All four policies have the same WDL, normalized HP margin and round count in both seats against each of the 43 specs.

| Subset | Conditions | best_v9e | af5 | g1 | V29 |
| --- | ---: | --- | --- | --- | --- |
| LEAD | 10 | 0-8-2 | 4-0-6 | 2-0-8 | 2-0-8 |
| W1_FORTRESS | 20 | 20-0-0 | 20-0-0 | 18-0-2 | 4-0-16 |
| W3_COUNTERS | 56 | 36-4-16 | 54-0-2 | 50-0-6 | 36-2-18 |
| All | 86 | 56-12-18 | 78-0-8 | 70-0-16 | 42-2-42 |
| LEAD_PLUS_FORTRESS | 30 | 20-8-2 | 24-0-6 | 20-0-10 | 6-0-24 |

The declared cluster bootstrap uses exact opponent specs as clusters, retaining both seats, W=1, D=0.5 and L=0, sorted opponent order, 4,000 resamples, random.Random(1), and sorted endpoint indices 100 and 3899. The reproduced full-list g1 minus best_v9e mean is 0.09302325581395349 with interval [-0.06976744186046512, 0.2558139534883721]. This satisfies the stated H18.20 non-refutation rule; it does not establish superiority. The descriptive af5 minus best_v9e mean is 0.18604651162790697 with interval [0.05813953488372093, 0.32558139534883723]. No prospective af5 prediction was stated for bvf.

For W3_COUNTERS, g1 minus best_v9e is 0.21428571428571427 [0, 0.42857142857142855]. For LEAD_PLUS_FORTRESS it is -0.13333333333333333 [-0.3, 0.03333333333333333]; af5 minus best_v9e is 0 [-0.13333333333333333, 0.13333333333333333]. These intervals describe this selected list and clustering rule. They do not account for opponent development, correlated policies, candidate selection or unmeasured deadline variation.

Two narrative qualifications remain. First, economy18.30's phrases “built against neither bot” and “bias ... shows in the split” exceed what family membership and this comparison alone establish. The 15-spec complement proves LEAD plus W1_FORTRESS provenance, not absence of development against best_v9e or guaranteed unbiasedness. This review therefore calls it LEAD_PLUS_FORTRESS. Second, economy18.29's proposed “load-dependent difference” would require evidence separating load from other causes; a changed repeated outcome alone establishes a repeat discrepancy. Neither qualification changes the reproduced numbers.

The best_v9e maximum recorded decide time is 6.4594 seconds at bvf row55, physical side0. The opposing-policy maximum is 5.6143 seconds at row28, forecast_handoff on physical side0. These are rounded elapsed wall times measured with time.perf_counter, not CPU time, a cold-call certificate or a three-second guarantee. The completed log reports 1798.6 elapsed seconds. Completion evidence consists of all86 exact conditions, the summary and one completion line; this review did not independently timestamp the historical start or finish.

All 185 distinct loaded-source claims and 38 entry/static-closure claims in bvf match the captured current bytes. The candidate is exactly bot_research.experiments.lead.frozen.best_v9e:@make. The archived baseline bytes remain those of the completed fresh56 review. These checks bind recorded source claims and current receipt-time identities, not continuous runtime monitoring or every runtime data and environment dependency. No policy, constructor, game, Engine, replay or test was executed. No full action-history regeneration was attempted.

At 23:24:32Z, afg5 had472 of514 rows without a summary and afrr had5 of20 without a summary. Those observations are status only. No partial outcome reduction enters this review. The af5 recommendation's18.26 covered-pool condition remains OPEN here; the separate95percent agreement prediction is not the recommendation gate. The preserved chronology clarification still applies: partial exposure was disclosed before completion; notes report rule/code before the first partial-row test, and stronger independent ordering is not established. The four exact afrr overlaps and the fifth guard00 default/explicit parameter alias remain as recorded in FRESH56_REVIEW_003.md.

Evidence is in bvf-20261031T232428135728Z/inspection.json and inputs.json. All233 input entries have verified compressed hashes, raw hashes and lengths, with project-relative keys. Existing content-addressed objects were reused. The retained notes snapshot has SHA256 ec470475ab59662a64b58458a8652a7c5a5c8c06dbca9fec121b1a33a46f29e3. The bvf result SHA256 is fb01780f42d0b33528cf3248b89987a7b4bec8520489afbd596d5cd382f2f571. Inspection SHA256 is 71ecca24d07f1787a8bd081bc49c61589efa5eb0df6ffe76da2954f7a80ca3a9; input-map SHA256 is 153b7b40fb05ec29e3be8a749b471749a7a9b3c0275302a0307880b25df5f438. The manifest binds the inspector and helper source bytes.

A later read-only rerun, when authorized, uses the project root:

```sh
env PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$PWD" nice -n 19 taskset -c 30 .venv/bin/python -B bot_research/experiments/validation/reviews/economy_final_gate_001/inspect_bvf_004.py
```
