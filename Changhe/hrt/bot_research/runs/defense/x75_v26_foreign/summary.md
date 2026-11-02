| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v26.fortress:@make [v:d12e3e3a] | bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 8 | 7 | 1 | 0 | 402.8 | 105 | 8.4 | 0 | 0 | 0 | 6.73 (3.88) |
| bot_research.bots.defense.frozen.v26.fortress:@make [v:d12e3e3a] | bot_research.bots.counters.relevant_turret_guard:@make [v:a5b5f28f] | 4 | 3 | 0 | 1 | 1088.8 | -1985 | 36.2 | 0 | 0 | 0 | 30.92 (4.09) |
| bot_research.bots.defense.frozen.v26.fortress:@make [v:d12e3e3a] | bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 8 | 6 | 0 | 2 | 578.4 | -1920 | 21.5 | 0 | 0 | 0 | 19.15 (4.59) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v26.fortress:@make [v:d12e3e3a] | 20 | 16 | 1 | 3 | 0.825 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v26.fortress:@make [v:d12e3e3a] | 20 | 16 | 1 | 3 | 0.825 | 610.2 |
| bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback="zero"&foreign_attack_from=11 | 8 | 2 | 0 | 6 | 0.250 | -578.4 |
| bot_research.bots.counters.relevant_turret_guard:@make [v:a5b5f28f] | 4 | 1 | 0 | 3 | 0.250 | -1088.8 |
| bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 8 | 0 | 1 | 7 | 0.062 | -402.8 |

Version warning: 4 spec/version labels from mixed-version results; 2 matches with source changed during the match.

Harness failures: 4
- bot_research.bots.defense.frozen.v26.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (mirror:22:3): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.frozen.v26.fortress:@make (mirror:22:3): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.defense.frozen.v26.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (asym:23:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.frozen.v26.fortress:@make (asym:23:2): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
