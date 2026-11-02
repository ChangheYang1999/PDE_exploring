# Earlier walls preserve the heavy-strike budget

Checked 2026-10-31T17:49:26.648460+00:00.

CONFIRMED for the declared finite family: 9 maps stop four new tier2 copies in round three and retain at least 260 gold for round four. The original combat engine checked all 24595 budget-feasible maps. Earlier walls collect path income before the guard is bought; this changes the cash constraint that defeated the preceding search.

| Witness | Wall round | Layout | Turret | Total cost | Total factories | Round-four gold | Route length |
|---|---:|---|---|---:|---:|---:|---:|
| guard00 | 1 | lead_opening | splash(1,3) | 80 | 14 | 267 | 42 |
| guard01 | 1 | cash_rank_3 | splash(10,5) | 105 | 13 | 271 | 70 |
| guard02 | 1 | cash_rank_10 | splash(3,1) | 100 | 13 | 270 | 58 |
| guard03 | 2 | cash_rank_3 | splash(10,5) | 105 | 13 | 270 | 70 |
| guard04 | 2 | cash_rank_9 | splash(10,5) | 103 | 13 | 264 | 66 |
| guard05 | 1 | cash_rank_9 | splash(10,5) | 103 | 13 | 261 | 66 |
| guard06 | 1 | cash_rank_1 | gun2(5,9) | 126 | 12 | 261 | 72 |
| guard07 | 1 | cash_rank_2 | gun2(5,9) | 127 | 12 | 260 | 72 |

The 8 selected witnesses are the best-ranked distinct wall-round/layout pairs, under the ranking fixed before the search. Every selected opening and third-round action list passed the unchanged engine, and its predicted gold exactly matched the engine. The first witness builds the 20-wall lead opening in round one and splash(1,3) in round three: it has 14 factories and 267 gold at decision four.

The extra component checks delimit the result. Each selected splash map stops all tested tier1/tier2 counts (1,2,4,8) but every tested tier3/tier4 copy reaches the base. The two selected gun2 maps stop one tier3 but leak with two or more, and leak with eight tier2 copies. This is not a universal defense.

The enumeration took 43.319467 seconds on one assigned core at low priority. There were 457284 route-legal type/cell assignments across both wall schedules. The receipt preserves counts per layout, selected original records and all extra components. The exact witness JSON is counters/data/early_wall_guard_001.json.

Reproduce by running experiments.validation.design_early_wall_guard with a fresh --output path under bot_research, using the existing Python, disabled bytecode, research temporary directory, one numerical thread, assigned affinity and low priority. The complete argument is in PROOF.md. A bot using a witness still needs full-game tests, including a public-clone opponent updated to that exact bot.
