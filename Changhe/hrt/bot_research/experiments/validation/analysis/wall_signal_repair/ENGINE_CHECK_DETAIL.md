# Which reached-state repairs prevent damage

Derived 2026-10-31T19:50:26.230154+00:00 from the completed original-engine comparison. No new policy or engine calls.

| Opponent | Round | Parent action intervention damage | Submitted L damage |
|---|---:|---:|---:|
| J | 7 | 280 | 0 |
| J | 8 | 280 | 0 |
| J | 9 | 140 | 0 |
| J | 10 | 280 | 0 |
| J | 11 | 420 | 0 |
| H | 7 | 280 | 0 |
| H | 8 | 280 | 0 |
| H | 9 | 140 | 0 |
| H | 10 | 280 | 0 |
| H | 11 | 420 | 0 |
| I | 8 | 0 | 0 |

Every row represents both assignments. The five H and J interventions prevent damage on the reached L histories. Against I, the sole selected repair changes construction but prevents no current-round damage because both plans receive zero damage in that intervention. A private-model improvement therefore need not improve actual defense against a different policy.

These rows are separate one-round counterfactuals from L states. Their damage amounts must not be added and described as a single K20 trajectory: after an intervention, future states and decisions could change, and the original K20 game ends earlier. The complete-game comparison is separately recorded in RESULTS.md.
