# The early-heavy counter depends on accurate anticipatory defense

Checked 2026-10-31T15:09:48.508145+00:00.

REFUTED: either visible-roster defense or the older P5TNUB model preserves the early-heavy win against P5TNUBM. All eight interventions lose. This is evidence of model dependence in these conditions, not a claim that no other defender could win.

Each row represents both physical assignments. Outcome is from the P5TNUBM target's perspective; HP is target:counter. These are standard-start development games on the unchanged bundled engine. They do not use reserved pool C.

| Counter setting | Target outcome in each seat | HP | Final round |
|---|---|---|---:|
| visible_handoff6 | W | 740:-457 | 15 |
| oldmodel_handoff6 | W | 740:647 | 50 |
| visible_handoff7 | W | 740:-125 | 14 |
| oldmodel_handoff7 | W | 740:-361 | 17 |

Each intervention retains the round-five tier4 and the handoff deadline. The visible variant still advances the exact model but does not use predicted purchases in its defensive threat list. The old-model variant changes only the model specification and its parameter dictionary. Their exact-model reference games are the handoff-six and handoff-seven strike games from early-heavy-handoff-001. Those four reference games are reused comparisons, not new samples.

All 8 games pass strict condition accounting, complete original-engine replay, and source/data archive checks. All 4 assignment pairs have identical normalized histories. There are no bot errors or rejected submitted actions. These deterministic paired games are not independent population samples.

Fresh counter instances reproduce all 192 recorded decisions from unchanged public observations and return legal lists. There are 118 full-action target-model disagreements. The outer strike filter omits 104 now-unaffordable parent proposals across the games; these are explicitly recorded local filtering decisions, not submitted invalid actions. The parent has no internal rejections. No minion is purchased after handoff.

All 8 declared matched interventions have changed complete histories. First differences and round-by-round summaries are in the comparison artifact. The parameter interventions are full policies.

Exact source hashes and specifications are in [the declaration](../../early-heavy-knowledge-001.json). The counter uses a separately initialized public-policy clone; it never reads pending submissions, engine objects or an opponent instance.

Audit inputs:

- strict: `bot_research/runs/validation/early-heavy-knowledge-strict-001.json`.
- replay: `bot_research/runs/validation/early-heavy-knowledge-replay-001.json`.
- summary: `bot_research/runs/validation/early-heavy-knowledge-summary-001.json`.
- data: `bot_research/runs/validation/early-heavy-knowledge-data-001.json`.
- comparison: `bot_research/runs/validation/early-heavy-knowledge-comparison-001.json`.
- histories: `bot_research/runs/validation/early-heavy-knowledge-forecast-histories-001.json`.
- reference_summary: `bot_research/runs/validation/early-heavy-handoff-summary-001.json`.
- reference_replay: `bot_research/runs/validation/early-heavy-handoff-replay-001.json`.

Reproduce from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Use a new output directory and repeat with `--resume` until all declared cases finish:

```sh
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/early-heavy-knowledge-001.json --output-dir bot_research/runs/validation/early-heavy-knowledge-reproduction --max-seconds 500 --match-timeout 300
```
