| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.counters.guard_continuation:@make | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 6.69 (0.41) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 2 | 0 | 0 | 520.0 | 520 | 10.0 | 0 | 0 | 0 | 1.97 (0.85) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier4&attack_round=7&attack_share=1.0 | 2 | 0 | 0 | 2 | -96.0 | -96 | 50.0 | 0 | 0 | 0 | 8.02 (0.67) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier5&attack_round=7&attack_share=1.0 | 2 | 0 | 0 | 2 | -140.0 | -140 | 50.0 | 0 | 0 | 0 | 7.69 (0.65) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier5&attack_round=8&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 7.72 (0.37) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 0 | 0 | 2 | -5.0 | -5 | 50.0 | 0 | 0 | 0 | 7.71 (0.57) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak" | 2 | 2 | 0 | 0 | 10.0 | 10 | 50.0 | 0 | 0 | 0 | 5.87 (0.23) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 2 | 2 | 0 | 0 | 10.0 | 10 | 50.0 | 0 | 0 | 0 | 5.85 (0.22) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.bots.economy.frozen.v2.econ:@make | 2 | 2 | 0 | 0 | 10.0 | 10 | 50.0 | 0 | 0 | 0 | 6.70 (1.28) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.experiments.lead.v4:@make | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 10.05 (0.51) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | bot_research.harness.baselines:@eco_then_flood | 2 | 2 | 0 | 0 | 580.0 | 580 | 10.0 | 0 | 0 | 0 | 1.47 (0.69) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | 22 | 10 | 6 | 6 | 0.591 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 2 | 0 | 0 | 1.000 | 5.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier4&attack_round=7&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 96.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier5&attack_round=7&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 140.0 |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.15 | 22 | 10 | 6 | 6 | 0.591 | 80.8 |
| bot_research.bots.counters.guard_continuation:@make | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.experiments.lead.v4:@make | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.15}&tier=tier5&attack_round=8&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 2 | 0 | 0 | 2 | 0.000 | -10.0 |
| bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak" | 2 | 0 | 0 | 2 | 0.000 | -10.0 |
| bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 0 | 0 | 2 | 0.000 | -520.0 |
| bot_research.harness.baselines:@eco_then_flood | 2 | 0 | 0 | 2 | 0.000 | -580.0 |
| bot_research.bots.economy.frozen.v2.econ:@make | 2 | 0 | 0 | 2 | 0.000 | -10.0 |
