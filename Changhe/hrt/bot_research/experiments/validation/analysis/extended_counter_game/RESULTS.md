# Five fixed policies after two counter revisions

Checked 2026-10-31T18:54:30.421848+00:00.

H1, the original uniform B/C/D mixture remains nonnegative against G and H, is REFUTED. Its exact payoff against G is -2/3, and against H is -2/3. H2, G weakly improves on D in every column with at least one strict improvement, is REFUTED.

B is frozen best_v9e, C is the round-three tier2 attacker retaining its original private D model, D is the adaptive Fortress38 continuation, G is early-wall guard00 and H is the HP-triggered grower with lead_from=8 and deadline=12. This is a deliberately extended development table, not an unseen opponent sample.

| Row policy | B | C | D | G | H |
|---|---:|---:|---:|---:|---:|
| B | 0 | 1 | -1 | -1 | -1 |
| C | -1 | 0 | 1 | -1 | -1 |
| D | 1 | -1 | 0 | 0 | 0 |
| G | 1 | 1 | 0 | 0 | -1 |
| H | 1 | 1 | 0 | 1 | 0 |

Every cell uses the original engine outcome: +1 win, 0 draw, -1 loss. All fifteen pairings, including five self-play cases, have two measured physical assignments. Ten games are new and twenty are explicitly reused. Each assignment pair has the same canonical history.

| Pair | Outcome | Final HP | Round | Source |
|---|---|---|---:|---|
| C vs B | L | 755:800 | 50 | Reused |
| B vs B | D | 785:785 | 50 | Reused |
| C vs C | D | 752:752 | 50 | Reused |
| D vs D | D | -40:-40 | 8 | Reused |
| C vs D | W | 800:656 | 50 | Reused |
| B vs D | L | 740:755 | 50 | Reused |
| G vs B | W | 770:740 | 50 | Reused |
| G vs D | D | 740:740 | 50 | Reused |
| G vs H | L | 380:500 | 50 | Reused |
| H vs D | D | -40:-40 | 8 | Reused |
| C vs G | L | -100:800 | 12 | New |
| B vs H | L | 660:755 | 50 | New |
| C vs H | L | 520:656 | 50 | New |
| G vs G | D | 740:740 | 50 | New |
| H vs H | D | -40:-40 | 8 | New |

Exact rational arithmetic certifies the following optimal mixture for this five-policy table: B=0, C=0, D=0, G=0, H=1. Its expected payoffs against B,C,D,G,H are 1, 1, 0, 1, 0. The finite value is exactly zero. This does not certify play against a sixth policy or a changed start.

All 680 new action-generating decisions are independently regenerated, with legal actions, unchanged observations, matching original-engine replays and verified source/data archives. All old receipts and their input hashes are rechecked. No game or audit failure is omitted. The complete receipt records policy specifications, every result path, HP, round and actual decision timings.

Reproduce the five extended-counter-game manifests with run_data_development, audit_development_strict, replay_audit, audit_data_archives and check_fixed_game_histories, then run publish_extended_counter_game. Restore archived old inputs before rechecking their receipts. The exact fraction calculation is local and deterministic. A hidden mixture draw would occur before a match; it cannot be revealed to an opponent before that opponent selects its policy.
