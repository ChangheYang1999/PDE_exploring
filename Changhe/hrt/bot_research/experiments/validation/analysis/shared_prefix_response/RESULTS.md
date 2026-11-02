# Public response selection after a shared first move

Checked 2026-10-31T19:24:34.079194+00:00.

H1, nonloss against G,H,I and a positive payoff against their uniform mixture: CONFIRMED. The exact mean payoff is 2/3.
H2, nonloss against every prior policy B,C,D,G,H,I: REFUTED.

J processes the first observation through both H and I and requires their first action lists to agree. On round two it chooses H when the opponent has at least twenty walls and an empty roster; otherwise it chooses I. The choice then stays fixed. It reads no opponent name or private state. This rule was selected after inspecting the earlier table and is development evidence.

| Opponent | Selected response | Outcome | HP J:opponent | End round | Walls after round 1 |
|---|---|---|---|---:|---:|
| B | I | L | 755:800 | 50 | 20 |
| C | I | D | 752:752 | 50 | 0 |
| D | I | W | 800:656 | 50 | 0 |
| G | H | W | 500:380 | 50 | 20 |
| H | I | W | 800:656 | 50 | 0 |
| I | I | D | 752:752 | 50 | 0 |
| J | I | D | 752:752 | 50 | 0 |

Each row represents both physical assignments, with identical complete canonical histories. Fourteen new games pass independent original-engine replay, source/data archival checks, legal-action checks and fresh regeneration of all 1400 external decisions. An additional 700 standalone-response calls agree with every recorded J action, including round one. Six prefix component cases passed before the full games.

The older uniform G,H,I mixture has payoff -2/3 against J under the measured pairwise outcomes. Its exact six-policy certificate remains correct on its original six columns. This seventh-policy challenge shows why that certificate cannot be extended to an unrestricted game guarantee.

The selected response consumes the actual public history from the first move; it is not reset at the branch. The conditional proof in PROOF.md explains why matching shared prefixes suffice, and the full-history checks account for wall-clock-bounded dependencies on these runs. This does not establish optimality against unknown policies or altered starting states.

Reproduction: the two shared-prefix manifests, run_data_development, audit_development_strict, replay_audit, audit_data_archives, check_fixed_game_histories, check_shared_prefix_histories, and this publisher. Bounded commands and real timestamps are in runs/validation/shared-prefix-001-pipeline.log.
