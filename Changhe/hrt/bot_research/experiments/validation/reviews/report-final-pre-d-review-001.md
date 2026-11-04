# Final report consistency review before reserved D

Recorded 2026-10-31T22:35:52.501941+00:00. Actual model: GPT-6 Astra. Role: hrt-w3 independent report reviewer. The actual the main model collaboration is through the lead's dated notes/report and economy notes; this review is not attributed to Opus. The inspected report identifies itself as the draft last updated22:33Z. Its exact byte identity is pinned below.

Verdict: three publication corrections remain. The completed worker evidence confirms the arithmetic and exact frr1 theorem; the remaining issues concern counting conventions, the unmeasured diagonal and stale final-version wording. D is correctly reported as pending. Earlier ab15 and fresh56 construction-bias corrections are incorporated and are not repeated as recommendations.

1. Pool counts still omit overlap and selection overlap. Q1 and Q2 below remain in section5.15, and the summary also calls846 a condition count. The report has no804,416,406, weighted-membership or distinct-condition qualification. Economy18.23 and the lead's22:14:33 note have the same omission. The independent completed aggregation and its exact-input archive confirm that846 is the sum of pool memberships, covering804 distinct full-specification/scenario/seat conditions. The448 subtotal covers416 distinct conditions, ten of which also appear in excluded selection pool f5t. Therefore the ten-pool subtotal is not condition-disjoint from the four selection pools. The arithmetic is CONFIRMED; a distinct/unseen interpretation of846 or448 is REFUTED.

The exact retained views for g1 versus the declared best_v9e baseline/twins are:

| View | Count | g1 W-D-L | Baseline W-D-L | Worse | Better |
| --- | ---: | --- | --- | ---: | ---: |
| Full weighted pool memberships | 846 | 764-16-66 | 524-82-240 | 72 | 304 |
| Full distinct conditions | 804 | 726-16-62 | 504-64-236 | 68 | 282 |
| Other ten pools, weighted memberships | 448 | 388-14-46 | 310-76-62 | 50 | 124 |
| Other ten pools, distinct conditions | 416 | 356-14-46 | 300-58-58 | 50 | 102 |
| Distinct conditions outside the four named selection pools | 406 | 350-14-42 | 290-58-58 | 46 | 102 |

Required correction: label the846 and448 aggregates as weighted pool memberships in5.15 and the leading summary, and state the804/416/406 distinctions. Retain the weighted totals; do not silently substitute distinct totals into the pool-weighted table. The406 calculation excludes exact conditions from GROWERS, GUARDED_MAZE, HANDOFF and f5t. It is a retrospective descriptive subset, not proof of no earlier exposure, related-policy exposure or construction bias. The34 multiply represented keys produce42 excess memberships; the448 subtotal has32 excess memberships plus ten conditions shared with f5t. One decoded guarded_schedule alias was already included among those ten exclusions. This correction concerns distinct evidence, not a claim that every use of846 as a count of separately executed lead pool games is wrong.

Evidence: [original aggregation review](economy-gate-846-review-001.md), [row-provenance receipt](economy-gate-846-review-001.json), [archive addendum](economy-gate-846-review-001.archive-addendum.md), [all five reconstructed tables](economy-gate-846-review-001.archive-recheck.json), and [root's59-archive byte check](economy-gate-846-review-001.root-archive-check.json). Those completed audits preserved all59 numeric/source inputs and41,153,219 original bytes. Their one unavailable old full-report prose input is explicitly disclosed; no numeric input is missing. This review reread the completed receipts and checked all five g1 table tuples, without rerunning games, replay or archive reconstruction.

2. frr1 still leaves its diagonal convention implicit. Q3 defines a ten-strategy game from45 measured off-diagonal pairs,90 games in both physical seats. The displayed table uses dashes on the ten diagonal cells. Neither5.16 nor the summary says the exact theorem sets those unmeasured cells to0. The completed independent audit records self_play_games=0 and explicitly imposes zero. The report's rational necessity argument, converse, value0 and weak-dominance statements are CONFIRMED for that defined matrix. No numerical correction to them is needed.

Required correction immediately before the proposition: "The ten self-play diagonal entries are set to0 by convention; no self-play game was measured. The resulting skew-symmetric matrix defines the symmetric zero-sum game considered here." Retain "for this recorded matrix only." In the short summary, "the remaining third is split arbitrarily among AS1C, best_v9f and P5TNUBM" is clearer than wording that can sound as though each receives one third. The exact optimal set has g1=guard00=1/3, the three named weights summing to1/3, and all other weights0. Both players may independently choose any such mixture.

Evidence: [independent frr1 review](frr1-equilibrium-review-001.md), [standalone exact proof](../analysis/frr1_equilibrium/PROOF.md) and [90-game audit](../analysis/frr1_equilibrium/verification/independent_audit_001.json). This theorem is conditional on the retained W/D/L entries. The existing audit's static/loaded Python hashes do not authenticate historical runtime witness JSON, erased attempts or temporary historical edits. No stronger provenance claim has been added to the report, so these limits need not be presented as new numerical defects.

3. The clock caveat names an obsolete final fortress. Sections2 and7 correctly say that equal physical-seat histories do not establish machine-load independence, but both still call v41 final; Q4 retains that label, while the report header,5.15 and defense22:13 notes identify v46 as the final recommendation. The same defense note says v47 was rejected and v48 regression was pending. This is a CONFIRMED stale-version label, not evidence that the report's general clock warning is absent.

Required correction: call v41 a former finalist and include final v46 in the timed-opponent examples. The current frozen v46/plan.py defines TIME_BUDGET=3.0 at line562, constructs the deadline at583 and checks it during plan search. It therefore needs the same timing qualification. Existing statements that timings are shared-machine measurements rather than portable bounds should stay. The report's selector discussion is restricted to opening-selection evidence and does not assert an unrestricted full-continuation equivalence theorem. If a later revision adds the exact delayed-signal bound, retain the source proof's extra hypothesis that the selected continuation reproduces its baseline payoff despite clock-sensitive later planning. That condition is explicit in the [completed ambiguity results](../analysis/delayed_signal_ambiguity/RESULTS.md), and is not implied by matching public observations alone.

D status: CONFIRMED consistent with retained pre-D status, with no report correction required. Q5 calls D report-only after23:00Z, and the status paragraph says it is still open. The terminal pipeline log contains only the wrapper-start record and the time_gate_pending record with not_before_utc23:00. This is status evidence, not a terminal result or an independent proof that no unrecorded action ever occurred. No D opponent/scenario parameter manifest, policy import, constructor, decision, game, engine replay or test was inspected or invoked by this review. No results from the ongoing prospective V protocol are inferred or substituted for D.

Already incorporated, checked only: the ab15 example is now empty/lead_opening and its negative HP margin is classified by the engine draw label; fresh5/fresh6 construction bias against best_v9e is stated and the15 non-targeted opponents are separated; poolC is called selection evidence after the best_v9e/best_v9f choice; measured seat agreement is not promoted to machine-load invariance. No duplicate requests are made for these points.

The review was read-only except for this file. Permitted local work on core28 at nice19 used only Python standard-library reads, hashing and receipt parsing. No project module import, policy/game/replay/test execution, JavaScript/TypeScript, server/listener, RLScience or other cluster, remote compute, GPU, Lean/lake, protected-file write, git commit/push or online posting occurred. The reserved waiter and all other lanes' files were untouched.

Short exact report excerpts are preserved here because REPORT.md can change after review. Line numbers identify this byte version, and each quote's SHA256 covers exactly its displayed inner text, including any preserved newline. No later live-file hash is substituted for this review input.

Q1, REPORT.md line1789, SHA256 `267f98ee3be025f1f2ed3c792d88e236a396ff64f023f6e1500fcdf0d985ec60`:

```text
On all 846 R13 gate conditions
```

Q2, REPORT.md line1802, SHA256 `ac40b4388b7f73e9433c2b2c544c61a98ad7d3fb461a78de7e86feffa429c542`:

```text
On the other ten pools (448 conditions, all run after g1 was fixed at 17:53Z)
```

Q3, REPORT.md line1903, SHA256 `07709cc945ef406065254b5c4d5e96f6c20a75fa32281ca1615efe9ff3e9bbee`:

```text
Score each frr1 pair +1, 0 or -1 for the row bot (every pair has the same
  outcome in both seats), giving a symmetric zero-sum game on the ten bots with value 0.
```

Q4, REPORT.md line232, SHA256 `d3447724bbf2788d7b2e9b753f6e6053cfccec5c5ecfe2bdcc273a0314829cb2`:

```text
fortress versions v34 to v43, among them the lane's final v41 and its alternative
  v43
```

Q5, REPORT.md line10, SHA256 `7e8a40e5cb99af2a517ce606e3e89e0da72974f33607278a5e6afa8108ef528a`:

```text
hrt-w3's report-only terminal pool D (after 23:00Z, on best_v9e's hash)
```

Input identities at review time:

| Project-relative input | SHA256 |
| --- | --- |
| `bot_research/reports/REPORT.md` | `02a41100735dfea94e069f47bad11b9614d0a3d618c18895d6920e713448bcfc` |
| `../hrt-lead/NOTES_FOR_TEAM.md` | `ee736a376668fbb1dd2fbacbfbc8653329a7a00abd8047b5140e67aeb476b113` |
| `bot_research/notes/economy.md` | `a9312f30d3356515ab19bac5a8841b4a4c343453d10e5b69a5213ce7411e55d9` |
| `bot_research/notes/defense.md` | `d9f6ab890160c96fc8b3c95e241f790828e363db5a53d70ed03875d3644cb038` |
| `bot_research/notes/validation.md` | `62acd071c088b61578c779427586075bdb6abb621accd4fe6d4b3a6a161566fd` |
| `bot_research/experiments/validation/reviews/economy-gate-846-review-001.md` | `e1d124ada88bcabbe5fa3bd3fa1ff84af6bf0d7884c285e03ae2e21c9d345f5a` |
| `bot_research/experiments/validation/reviews/economy-gate-846-review-001.json` | `d243192a3d235f2c38d4a9707c9ddfd0287fbfd9006dedd616b5daed37d95af7` |
| `bot_research/experiments/validation/reviews/economy-gate-846-review-001.archive-addendum.md` | `0a2f5ba226566a160eba85c8e78d36c2e74d30f2d8325460e9ecee1af3f90171` |
| `bot_research/experiments/validation/reviews/economy-gate-846-review-001.archive-recheck.json` | `5d642288f04f21921718e11b98c0c90f7027cee3bdba4aa5fb83f0915eee24ef` |
| `bot_research/experiments/validation/reviews/economy-gate-846-review-001.root-archive-check.json` | `9da3a852525aa4cb069466223d10d2f27795685048981443fa476fd3a3f5c5be` |
| `bot_research/experiments/validation/reviews/frr1-equilibrium-review-001.md` | `8ca45ebc57a6a269ab36e153ffe9cd2bc3d9461b8d1d12d6ae1cbcd381a3951d` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/PROOF.md` | `e6656f1850ba2cf85deea5170edfcd5a73ab7a53db3830bcb34a7dbcdefd035d` |
| `bot_research/experiments/validation/analysis/frr1_equilibrium/verification/independent_audit_001.json` | `118f08bc7d87f3ff536368a60c51e6879bf273c6bd7e5c431d56ad1a2fbbd08d` |
| `bot_research/experiments/validation/analysis/delayed_signal_ambiguity/RESULTS.md` | `20feaf108399703f70ba82b09ee8d38d757801702e92f7ba73f19282fe6d1d88` |
| `bot_research/bots/defense/frozen/v46/plan.py` | `e71af9149c3afb611e1ac14668984ffae343efb6278cce513ea35c0fe5386545` |
| `bot_research/runs/validation/reserved-D-final-001-pipeline.log` | `ddbc5406222b3afd8e15dcc9771b9ddc2afbbbb99b3369b6643b3008720355c2` |
