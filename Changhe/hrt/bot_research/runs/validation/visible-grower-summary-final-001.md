# Exact model versus visible-roster grower defense

Recorded: 2026-10-31T08:17:48.600813+00:00

Both controllers win all 16 declared games against the fixed Lead10 C2 adaptive policy. The visible-roster controller assumes no new opponent purchases when choosing defense; growth, flood timing, optional early gun and defensive start rules are unchanged.

| Gun round; first defense round | Exact-model HP | Visible-roster HP | Exact / visible end round |
|---|---|---|---|
| turret0_defend1 | 800:-320 | 780:-180 | 10 / 9 |
| turret0_defend4 | 755:380 | 673:380 | 50 / 50 |
| turret0_defend6 | 725:380 | 643:380 | 50 / 50 |
| turret0_defend8 | 645:380 | 633:380 | 50 / 50 |
| turret2_defend1 | 800:-40 | 735:-180 | 10 / 10 |
| turret2_defend4 | 755:520 | 709:660 | 50 / 50 |
| turret2_defend6 | 725:-40 | 635:-40 | 9 / 9 |
| turret2_defend8 | 695:-320 | 665:-460 | 9 / 9 |

All 16 visible-roster conditions pass strict source and legality checks. All eight reversed-seat pairs have identical normalized complete histories. All 17 completed attempts pass unchanged-engine replay. One original 180-second timeout is retained; a separately declared 300-second retry resolved it and repeated the other seat as a control.

The empty-action prediction is deliberately wrong in 442 of 474 selected-game rounds: 130 construction mismatches, 56 minion-purchase mismatches and 422 factory-purchase mismatches. These categories overlap. Wrong predictions are an intentional intervention, not invalid game outcomes.

Exact public-action forecasting is not necessary to win any of these sixteen conditions: the otherwise identical visible-roster controller also wins all sixteen. This does not establish which other defensive controller is sufficient against other targets.

The earlier no-defense ablation loses without an early gun and wins with the round-2 gun. Taken together, the experiments support a role for defense in the no-gun conditions, while refuting the necessity of exact forecasting for these wins. They do not identify an optimal defense policy.

Evidence: visible-grower-{strict,forecasts,replay,summary}-final-001.json and forecast-grower-strict-001.json. The comparison declaration is in experiments/validation/visible-grower-final-comparisons-001.json.
