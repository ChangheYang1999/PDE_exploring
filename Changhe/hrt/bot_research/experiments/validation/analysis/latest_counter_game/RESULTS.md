# A fixed game after counter adaptation

Checked 2026-10-31T17:48:14.854687+00:00.

CONFIRMED: the specified cycle B>C>D>B holds in the paired recorded game.

B is frozen best_v9e. D is the adaptive Fortress38 continuation. C is the round3/tier2 public-clone attacker, with its D model unchanged even against B and itself. All exact specifications are in verification/full_games.json and the declaration.

Twelve recorded games define three off-diagonal pairings and three measured self-play cases, each in both physical assignments. Eight games are new and four are explicitly reused. Every assignment pair has the same complete normalized history. Reused games and repeated histories add no independent evidence.

| Row policy | B | C | D |
|---|---:|---:|---:|
| B | 0 | 1 | -1 |
| C | -1 | 0 | 1 |
| D | 1 | -1 | 0 |

Payoff is +1 for a win, 0 for a draw and -1 for a loss under the engine result. The table is a description of these finite standard-start games.

| Pair, first policy perspective | Outcome | Final HP | Ending round | Source |
|---|---|---|---:|---|
| C vs B | L | 755:800 | 50 | New |
| B vs B | D | 785:785 | 50 | New |
| C vs C | D | 752:752 | 50 | New |
| D vs D | D | -40:-40 | 8 | New |
| C vs D | W | 800:656 | 50 | Reused |
| B vs D | L | 740:755 | 50 | Reused |

Exact rational arithmetic verifies that the uniform one-third mixture has zero expected payoff against every column, and holds every row to zero. Together these inequalities certify maximin value0 for this recorded three-policy table. They do not certify the mixture against a fourth policy, a different initial state or a different load-dependent execution.

All eight new games pass strict accounting, original-engine replay, explicit source/data checks and 632 fresh action-generating decisions across both policies. No rejected action, observation mutation or bot error is recorded. Reused edges retain their original fresh-counter and handoff audits; the C-D edge additionally has exact private-model forecast checks. C is permitted to forecast incorrectly against B or itself: the actual C action generator is what is held fixed and independently regenerated.

Reproduce the four latest-counter-game manifests using run_data_development, then strict, replay, data and check_fixed_game_histories checks. Reproduce the two named reused campaigns or restore their exact recorded evidence, then run publish_latest_counter_game. The pipeline log keeps complete bounded commands. Use the existing Python, disabled bytecode, the research temporary directory, one numerical thread, assigned affinity and low priority.
