| candidate | opponent | n | W | D | L | mean HP diff | min HP diff | mean end round | cand rejected | cand errors | opp errors | cand decide s/match (max call) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | bot_research.bots.counters.guard_continuation:@make | 2 | 2 | 0 | 0 | 20.0 | 20 | 50.0 | 0 | 0 | 0 | 27.90 (2.70) |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 2 | 0 | 0 | 540.0 | 540 | 7.0 | 0 | 0 | 0 | 2.91 (2.18) |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 2 | 0 | 0 | 315.0 | 315 | 8.0 | 0 | 0 | 0 | 1.04 (0.24) |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | bot_research.harness.baselines:@eco_then_flood | 2 | 2 | 0 | 0 | 820.0 | 820 | 7.0 | 0 | 0 | 0 | 2.27 (1.83) |

| candidate | matches | W | D | L | score (W + D/2) / n |
| --- | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | 8 | 8 | 0 | 0 | 1.000 |

| bot (all matches, both perspectives) | matches | W | D | L | score | mean HP diff |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| bot_research.bots.defense.frozen.v27.fortress:@make [v:c317241b] | 8 | 8 | 0 | 0 | 1.000 | 423.8 |
| bot_research.harness.baselines:@eco_then_flood | 2 | 0 | 0 | 2 | 0.000 | -820.0 |
| bot_research.bots.counters.pool:@archetype?name="eco6_t5" | 2 | 0 | 0 | 2 | 0.000 | -540.0 |
| bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10 | 2 | 0 | 0 | 2 | 0.000 | -315.0 |
| bot_research.bots.counters.guard_continuation:@make | 2 | 0 | 0 | 2 | 0.000 | -20.0 |

Version warning: 2 spec/version labels from mixed-version results; 0 matches with source changed during the match.

Harness failures: 2
- bot_research.bots.defense.frozen.v27.fortress:@make vs bot_research.bots.counters.relevant_turret_guard:@make (None): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
- bot_research.bots.counters.relevant_turret_guard:@make vs bot_research.bots.defense.frozen.v27.fortress:@make (None): TypeError: GuardContinuation.__init__() got an unexpected keyword argument 'continuation'
