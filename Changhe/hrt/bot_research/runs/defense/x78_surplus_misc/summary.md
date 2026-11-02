| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.fortress:@make [v:7fa232e5] | bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 6 | 5 | 1 | 0 | 367.0 | 105 | 7.8 | 0 | 0 | 0 | 4.94 (2.85) |
| bot_research.bots.defense.fortress:@make [v:7fa232e5] | bot_research.experiments.lead.v4:@make | 6 | 3 | 3 | 0 | 496.7 | -250 | 27.0 | 0 | 0 | 0 | 24.62 (6.51) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.fortress:@make [v:7fa232e5] | 12 | 8 | 4 | 0 | 0.833 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.fortress:@make [v:7fa232e5] | 12 | 8 | 4 | 0 | 0.833 | 431.8 |
| bot_research.experiments.lead.v4:@make | 6 | 0 | 3 | 3 | 0.250 | -496.7 |
| bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 6 | 0 | 1 | 5 | 0.083 | -367.0 |

Version warning: 2 spec/version labels from mixed-version results; 0 matches with source changed during the match.

Harness failures: 6
- bot_research.bots.defense.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (None): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.fortress:@make (None): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.defense.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (asym:3:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.fortress:@make (asym:3:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.fortress:@make (asym:23:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.defense.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (asym:23:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
