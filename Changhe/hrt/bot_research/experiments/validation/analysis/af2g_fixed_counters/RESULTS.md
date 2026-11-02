# Fixed development counters against af2g

Checked 2026-10-31T19:23:05.328199+00:00.

H1, no outcome regression from best_v9e: CONFIRMED. H2, at least one earlier loss becomes a draw or win: REFUTED. Ten new candidate outcomes: {'L': 8, 'W': 2}. Transitions from the ten old controls: {'L->L': 8, 'W->W': 2}.

af2g is frozen best_v9f with passive_until=null. No other parameter was changed. These five counter specifications were fixed before the af2g games. Four were selected because they beat best_v9e, and the fifth, I, was a negative control that best_v9e beats. This targeted development screen is not a held-out test and does not evaluate the lead's wider R13 acceptance rule.

| Counter | Old best_v9e | Old HP | New af2g | New HP | End round |
|---|---|---|---|---|---:|
| D | L | 740:755 | L | 740:755 | 50 |
| G | L | 740:770 | L | 740:770 | 50 |
| H | L | 660:755 | L | 660:755 | 50 |
| I | W | 800:755 | W | 800:-111 | 16 |
| guarded_R4_half | L | 740:755 | L | 740:755 | 50 |

Each row represents both physical assignments; the five new pairs have identical complete normalized histories. All ten new games pass strict condition accounting, original-engine replay, source/data archives, observation immutability, sequential action legality, and 864 freshly regenerated external decisions. All ten old records are separately replayed on the original engine and their frozen archives and original hashes are checked. Old games are reused, not counted again as new evidence. Zero submitted rejections, bot errors or source drift occurred in the new games.

New candidate decision timing: 432 actual calls, 84.486416 seconds total, largest 0.774566 seconds. These are observed timings on a shared machine, not worst-case bounds.

Reproduce using af2g-fixed-counters-001.json and the exact bounded commands recorded in runs/validation/af2g-fixed-counters-001-pipeline.log. Restored old replays retain their original hashes. Pool D and the installed entry point are not read by these policy executions. No result here establishes global optimality or robustness to arbitrary future opponents.
