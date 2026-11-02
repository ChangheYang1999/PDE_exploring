| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make | bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 [v:74e0c6e1] | 2 | 2 | 0 | 0 | 305.0 | 305 | 14.0 | 0 | 0 | 0 | 1.36 (0.25) |
| bot_research.experiments.lead.frozen.best_v9e:@make?fail_limit=2 | bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 [v:74e0c6e1] | 2 | 2 | 0 | 0 | 305.0 | 305 | 14.0 | 0 | 0 | 0 | 1.34 (0.25) |
| bot_research.experiments.lead.frozen.best_v9e:@make?poke_reactive="turret_only" | bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 [v:74e0c6e1] | 2 | 2 | 0 | 0 | 305.0 | 305 | 14.0 | 0 | 0 | 0 | 1.36 (0.25) |
| bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null | bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 [v:74e0c6e1] | 2 | 0 | 0 | 2 | -815.0 | -815 | 9.0 | 0 | 0 | 0 | 0.72 (0.25) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make | 2 | 2 | 0 | 0 | 1.000 |
| bot_research.experiments.lead.frozen.best_v9e:@make?fail_limit=2 | 2 | 2 | 0 | 0 | 1.000 |
| bot_research.experiments.lead.frozen.best_v9e:@make?poke_reactive="turret_only" | 2 | 2 | 0 | 0 | 1.000 |
| bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null | 2 | 0 | 0 | 2 | 0.000 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.experiments.lead.frozen.best_v9e:@make | 2 | 2 | 0 | 0 | 1.000 | 305.0 |
| bot_research.experiments.lead.frozen.best_v9e:@make?poke_reactive="turret_only" | 2 | 2 | 0 | 0 | 1.000 | 305.0 |
| bot_research.experiments.lead.frozen.best_v9e:@make?fail_limit=2 | 2 | 2 | 0 | 0 | 1.000 | 305.0 |
| bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 [v:74e0c6e1] | 8 | 2 | 0 | 6 | 0.250 | -25.0 |
| bot_research.experiments.lead.frozen.best_v9f:@make?passive_until=null | 2 | 0 | 0 | 2 | 0.000 | -815.0 |

Version warning: 2 spec/version labels from mixed-version results; 0 matches with source changed during the match.

Harness failures: 4
- bot_research.experiments.lead.frozen.best_v9e:@make?robust_k=null vs bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 (None): ValueError: unknown parameters ['robust_k']
- bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 vs bot_research.experiments.lead.frozen.best_v9e:@make?robust_k=null (None): ValueError: unknown parameters ['robust_k']
- bot_research.experiments.lead.frozen.best_v9e:@make?behind_mode="current" vs bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 (None): ValueError: unknown parameters ['behind_mode']
- bot_research.bots.counters.guarded_maze:@make?layout="empty"&growth_rounds=4&guard_round=3&bait=["tier1"]&bait_round=2&tier="tier5"&factory_cap=2000&purchase_cap=1000 vs bot_research.experiments.lead.frozen.best_v9e:@make?behind_mode="current" (None): ValueError: unknown parameters ['behind_mode']
