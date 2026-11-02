# No-defense grower controls

Recorded: 2026-10-31T07:43:55.444758+00:00

Opponent: fixed Lead10 C2 adaptive. Standard start, both player assignments. Growth lasts through round 6, then the counter spends on tier5; first defensive round is 51, beyond the game horizon.

| Early gun | Result in each seat | Counter HP | Opponent HP | End round |
|---|---|---:|---:|---:|
| turret0_defend51 | L | -125 | 520 | 12 |
| turret2_defend51 | W | 605 | -460 | 9 |

All four games pass source and legality checks and unchanged-engine replay. Both normalized seat pairs have identical complete trajectories. A fresh blind FeatureBluff recomputation matches every action over all 42 recorded rounds. All model forecasts also match, although they do not affect the disabled defensive branch.

The original sixteen defensive games all win. Adding defense therefore reverses the no-gun result, while the round-2-gun baseline already wins. This comparison does not establish that exact forecasting is necessary: the intervention enables the entire defensive policy. The separate visible-roster ablation addresses that question.

These controls were declared after the original results. They are development evidence, not a reserved-pool score. Sixteen descriptive comparison pairs reuse four controls; the pairs are not independent samples.

Evidence: forecast-grower-nodefense-{strict,forecast-audit,blind-audit,replay-audit,summary}-001.json; forecast-grower-strict-001.json.
