# Fresh and persistent forecasts of Lead10

Completed audit: 2026-10-31T07:31:49.976492+00:00.

This is a development comparison on the unchanged engine, using the fixed Lead10 C2 adaptive snapshot (SHA256 2c3f4f7ec4698e24299801f8cc2fc0cd07bd7d9b6ccece1db8bd627273ce3eec). All 40 games completed legally and replayed exactly. The 20 reversed-seat pairs have identical normalized complete trajectories. No reserved opponent was used.

Each model played ten timing conditions in both seats. Both scored 10 wins, 10 draws and no losses. All 20 fresh/persistent comparisons have equal final HP and outcomes, but none has an identical complete trajectory. The opponent submitted the same action sequence in each comparison.

| Timing | Counter outcome | Final HP, counter first | First counter-action difference |
| --- | --- | --- | --- |
| tier3_r3 | W | 800:774 | round 8 |
| tier3_r5 | W | 800:774 | round 12 |
| tier4_r5 | W | 800:740 | round 12 |
| tier4_r7 | D | 800:800 | round 11 |
| tier4_r9 | D | 800:800 | round 11 |
| tier5_r7 | D | 800:800 | round 11 |
| tier5_r8 | W | 800:520 | round 12 |
| tier5_r9 | W | 800:240 | round 11 |
| tier5_r10 | D | 800:800 | round 11 |
| tier5_r11 | D | 800:800 | round 11 |

Each style produced 1,000 forecasts. The fresh model made 136 full-action errors, including 136 minion-purchase errors and 60 factory-purchase errors. Construction was correct in every fresh forecast. The persistent model made no errors. These are ordered action comparisons, not only equal purchase totals.

A concrete divergence occurs at round 8 of tier3/round3. Both counters enter with 74 factories and 1,150 gold. The fresh clone wrongly predicts two new tier1 purchases and buys one gun1 plus 56 factories. The persistent clone predicts no new minions and buys 57 factories. Both actual opponents build gun2 and gun3, buy three factories and send no new minions. The counter ends that round with 130 factories and 1,972 gold under the fresh model, versus 131 factories and 1,997 gold under the persistent model. Final HP remains 800:774 in both cases.

The stateful-forecast induction argument applies when the exact deterministic factory and initial private state are known, equal observations are supplied, and it is called once per round from the standard start. The narrower construction argument applies to this Lead10 snapshot with planner v7 and no foreign planner. It does not cover Lead13 sticky fortress state.

Candidate decision time sums were 410.603 seconds for fresh and 694.445 seconds for persistent; maxima were 5.770 and 7.830 seconds. These shared-machine measurements are descriptive. Original-engine replay took 35.213 seconds. The submitted attack count never exceeded five, but this does not prove equivalence to the lead screening cap because hypothetical attacks can differ.

Verdicts: fresh full-action exactness is REFUTED; persistent exactness on the 1,000 recorded observations is CONFIRMED; the construction projection claim on these observations is CONFIRMED; a win-rate improvement from correcting this model on the declared set is REFUTED. Wider strength improvements remain OPEN.

Evidence: stateful-lead-ten-audit-001.json, stateful-lead-ten-comparison-001.json, stateful-lead-ten-projections-001.json, stateful-lead-ten-replay-audit-001.json and stateful-lead-ten-summary-001.json in this directory. The declarations are experiments/validation/stateful-lead-ten-001.json and stateful-lead-ten-comparisons-001.json, relative to bot_research.
