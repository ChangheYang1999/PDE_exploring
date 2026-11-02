| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=10&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 6.00 (0.75) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=11&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 6.08 (0.77) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=3&tier="tier3"&attack_share=1.0 | 2 | 0 | 0 | 2 | -26.0 | -26 | 50.0 | 0 | 0 | 0 | 3.67 (0.54) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=5&tier="tier3"&attack_share=1.0 | 2 | 0 | 0 | 2 | -26.0 | -26 | 50.0 | 0 | 0 | 0 | 9.56 (1.73) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=5&tier="tier4"&attack_share=1.0 | 2 | 0 | 0 | 2 | -60.0 | -60 | 50.0 | 0 | 0 | 0 | 3.74 (0.56) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=7&tier="tier4"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 6.01 (0.75) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=7&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 6.04 (0.75) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=8&tier="tier5"&attack_share=1.0 | 2 | 0 | 0 | 2 | -140.0 | -140 | 50.0 | 0 | 0 | 0 | 7.07 (1.29) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=9&tier="tier4"&attack_share=1.0 | 2 | 0 | 0 | 2 | -360.0 | -360 | 50.0 | 0 | 0 | 0 | 5.26 (0.57) |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=9&tier="tier5"&attack_share=1.0 | 2 | 0 | 0 | 2 | -560.0 | -560 | 50.0 | 0 | 0 | 0 | 5.57 (0.68) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | 20 | 0 | 8 | 12 | 0.200 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=3&tier="tier3"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 26.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=5&tier="tier3"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 26.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=5&tier="tier4"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 60.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=9&tier="tier4"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 360.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=8&tier="tier5"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 140.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=9&tier="tier5"&attack_share=1.0 | 2 | 2 | 0 | 0 | 1.000 | 560.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=7&tier="tier4"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=7&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=10&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.experiments.lead.known_counter:@timing?model="v5"&model_parameters={"attack_mode":"robust"}&attack_round=11&tier="tier5"&attack_share=1.0 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.experiments.lead.v5:@make?attack_mode="robust" | 20 | 0 | 8 | 12 | 0.200 | -117.2 |
