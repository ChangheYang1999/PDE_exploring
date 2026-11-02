| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.counters.guard_continuation:@make | 2 | 0 | 0 | 2 | -60.0 | -60 | 50.0 | 0 | 0 | 0 | 6.68 (0.56) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 2 | 0 | 0 | 835.0 | 835 | 9.0 | 0 | 0 | 0 | 1.84 (0.73) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier4&attack_round=7&attack_share=1.0 | 2 | 0 | 0 | 2 | -60.0 | -60 | 50.0 | 0 | 0 | 0 | 7.96 (0.53) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier5&attack_round=10&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 7.99 (0.37) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier5&attack_round=8&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 7.77 (0.35) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 2 | 0 | 0 | 130.0 | 130 | 50.0 | 0 | 0 | 0 | 7.46 (0.48) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak" | 2 | 2 | 0 | 0 | 1557.0 | 1557 | 37.0 | 0 | 0 | 0 | 4.01 (0.24) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 2 | 2 | 0 | 0 | 17.0 | 17 | 50.0 | 0 | 0 | 0 | 5.93 (0.28) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.bots.economy.frozen.v2.econ:@make | 2 | 2 | 0 | 0 | 10.0 | 10 | 50.0 | 0 | 0 | 0 | 6.71 (1.24) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.experiments.lead.v4:@make | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 10.04 (0.51) |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | bot_research.harness.baselines:@eco_then_flood | 2 | 2 | 0 | 0 | 880.0 | 880 | 10.0 | 0 | 0 | 0 | 1.78 (0.75) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | 22 | 12 | 6 | 4 | 0.682 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.counters.guard_continuation:@make | 2 | 2 | 0 | 0 | 1.000 | 60.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier4&attack_round=7&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 60.0 |
| bot_research.bots.defense.frozen.v29.fortress:@make?attack_share=0.25 | 22 | 12 | 6 | 4 | 0.682 | 300.8 |
| bot_research.experiments.lead.v4:@make | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier5&attack_round=8&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.counters.stateful_public:@timing?model_spec=bot_research.bots.defense.frozen.v29.fortress:@make&model_parameters={"attack_share": 0.25}&tier=tier5&attack_round=10&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 2 | 0 | 0 | 2 | 0.000 | -17.0 |
| bot_research.bots.economy.frozen.v15.econ15:@make?free_fallback="leak" | 2 | 0 | 0 | 2 | 0.000 | -1557.0 |
| bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 0 | 0 | 2 | 0.000 | -835.0 |
| bot_research.harness.baselines:@eco_then_flood | 2 | 0 | 0 | 2 | 0.000 | -880.0 |
| bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 0 | 0 | 2 | 0.000 | -130.0 |
| bot_research.bots.economy.frozen.v2.econ:@make | 2 | 0 | 0 | 2 | 0.000 | -10.0 |
