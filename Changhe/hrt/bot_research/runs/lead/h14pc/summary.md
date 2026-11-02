| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=4&budget_fraction=0.65 | 2 | 2 | 0 | 0 | 480.0 | 480 | 50.0 | 0 | 0 | 0 | 12.76 (1.01) |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=6&budget_fraction=0.65 | 2 | 2 | 0 | 0 | 560.0 | 560 | 50.0 | 0 | 0 | 0 | 12.59 (0.81) |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]&x=9&y=2 | 2 | 0 | 2 | 0 | 0.0 | 0 | 50.0 | 0 | 0 | 0 | 9.28 (0.56) |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | bot_research.bots.counters.guard_geometry:@make?roster=["tier2"]&x=10&y=2 | 2 | 2 | 0 | 0 | 5.0 | 5 | 50.0 | 0 | 0 | 0 | 8.13 (0.68) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | 8 | 6 | 2 | 0 | 0.875 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make?attack_share=1.0&catch_up_share=0.5 | 8 | 6 | 2 | 0 | 0.875 | 261.2 |
| bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]&x=9&y=2 | 2 | 0 | 2 | 0 | 0.500 | 0.0 |
| bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=4&budget_fraction=0.65 | 2 | 0 | 0 | 2 | 0.000 | -480.0 |
| bot_research.bots.counters.budget_timing:@make?tier="tier4"&attack_round=6&budget_fraction=0.65 | 2 | 0 | 0 | 2 | 0.000 | -560.0 |
| bot_research.bots.counters.guard_geometry:@make?roster=["tier2"]&x=10&y=2 | 2 | 0 | 0 | 2 | 0.000 | -5.0 |
