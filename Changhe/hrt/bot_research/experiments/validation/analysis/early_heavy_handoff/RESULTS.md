# One round-five tier4 wins with an early exact-model handoff

Checked 2026-10-31T15:09:49.034616+00:00.

CONFIRMED: one tier4 in round five followed by exact-public-model defense from round six or seven beats P5TNUBM in both assignments, 755:740. REFUTED: the same claim for handoffs eight and nine; both lose. Every no-strike control loses.

Each row represents both physical assignments. Outcome is from the P5TNUBM target's perspective; HP is target:counter. These are standard-start development games on the unchanged bundled engine. They do not use reserved pool C.

| Counter setting | Target outcome in each seat | HP | Final round |
|---|---|---|---:|
| early0_handoff6 | W | 800:755 | 50 |
| early1_handoff6 | L | 740:755 | 50 |
| early0_handoff7 | W | 800:755 | 50 |
| early1_handoff7 | L | 740:755 | 50 |
| early0_handoff8 | W | 800:755 | 50 |
| early1_handoff8 | W | 740:729 | 50 |
| early0_handoff9 | W | 800:755 | 50 |
| early1_handoff9 | W | 740:563 | 50 |

The checked opening component shows the target buying three splashes in round five, with total splash exposure190 and no gun. One tier4 survives, dealing60. The counter had already lost45 to the three opening tier1 copies, so it leads755:740. With handoff six or seven it takes no later damage. Handoff eight concedes26 later, and handoff nine concedes192. The intervention changes the counter's factory purchases and all later play as well; it is not an isolated estimate of the value of60 damage.

All 16 games pass strict condition accounting, complete original-engine replay, and source/data archive checks. All 8 assignment pairs have identical normalized histories. There are no bot errors or rejected submitted actions. These deterministic paired games are not independent population samples.

Fresh counter instances reproduce all 800 recorded decisions from unchanged public observations and return legal lists. There are 0 full-action target-model disagreements. The outer strike filter omits 104 now-unaffordable parent proposals across the games; these are explicitly recorded local filtering decisions, not submitted invalid actions. The parent has no internal rejections. No minion is purchased after handoff.

All 8 declared matched interventions have changed complete histories. First differences and round-by-round summaries are in the comparison artifact. The parameter interventions are full policies.

Exact source hashes and specifications are in [the declaration](../../early-heavy-handoff-001.json). The counter uses a separately initialized public-policy clone; it never reads pending submissions, engine objects or an opponent instance.

Audit inputs:

- strict: `bot_research/runs/validation/early-heavy-handoff-strict-001.json`.
- replay: `bot_research/runs/validation/early-heavy-handoff-replay-001.json`.
- summary: `bot_research/runs/validation/early-heavy-handoff-summary-001.json`.
- data: `bot_research/runs/validation/early-heavy-handoff-data-001.json`.
- comparison: `bot_research/runs/validation/early-heavy-handoff-comparison-001.json`.
- histories: `bot_research/runs/validation/early-heavy-handoff-forecast-histories-001.json`.
- opening: `bot_research/runs/validation/early-heavy-opening-001.json`.

Reproduce from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Use a new output directory and repeat with `--resume` until all declared cases finish:

```sh
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/early-heavy-handoff-001.json --output-dir bot_research/runs/validation/early-heavy-handoff-reproduction --max-seconds 500 --match-timeout 300
```
