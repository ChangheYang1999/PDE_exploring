# Completed afrep retained-record review

At 2026-10-31T23:41:02.056414Z, this supplementary review by GPT-6 Astra verified the completed two-game afrep reproduction against its exact afrr controls. Opus lead/economy collaboration is separate. The review used only standard-library reads and reductions. No policy, constructor, Engine, game, replay or test was executed.

H18.33 passes: af5 wins by 410 HP at round 50 in both physical seats, matching afrr's recorded outcome, normalized HP margin and round count. The exact default frozen best_v9e opponent, standard start and af5 specification are bound in the receipts. The prediction was written after both earlier afrr outcomes were exposed. These are repeated observations, not an independent fresh strength sample or a new recommendation gate.

Each retained log contains exactly 102 rows: both players at round 0 and after rounds 1 through 50. The reader checks round/seat uniqueness, initial names/specifications/scenario/metadata, accepted-action records, and terminal HP, gold, factories, turrets, walls and path length against the result row. It captures the complete log bytes and their SHA256 values. This authenticates the association with the retained records at review time; it does not replay engine transitions or regenerate decisions.

Both logs record the same HP chronology by policy role:

| Round | af5 HP | best_v9e HP | Recorded damage during the round |
| --- | ---: | ---: | --- |
| 0 | 800 | 800 | Initial state |
| 1 | 785 | 795 | af5 takes15; best_v9e takes5 |
| 9 | 785 | 655 | best_v9e takes140 |
| 10 | 785 | 375 | best_v9e takes280 |
| 50 | 785 | 375 | No HP changes after round10 |

The log summary reports one af5 outgoing hit for 140 damage in round9 and two for 280 in round10. This explains the arithmetic of the recorded terminal margin. It does not establish why the policy selected its actions, a private-state equivalence, or a causal effect of compute load. A hypothetical differing repeat would also need further evidence before attributing its difference to load.

The audit verifies 68 archived inputs with no findings. Both result rows report zero harness errors, bot errors, rejected actions, source changes and scenario errors. Reported source and entry/static-closure identities match captured current bytes. These matches are receipt-bound, not continuous runtime monitoring or a complete runtime data/environment closure. The greatest recorded elapsed wall call is 0.5154 seconds for af5 and 2.9551 for best_v9e within these two games. These numbers imply neither CPU-time bounds nor runtime guarantees in other settings.

Read afrep-20261031T234033189508Z/inspection.json for exact comparisons, HP/combat events and minion-purchase records. Its inputs.json binds the retained inputs and complete logs. afrep_review_manifest_011.json binds this review and reader. All published paths are relative. The completed standard-start gate and the pending scenario control remain separate.
