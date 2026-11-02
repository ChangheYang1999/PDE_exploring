# Exact P5TNUBM forecasting does not restore the counter win

Published 2026-10-31T15:01:17.850182+00:00.

The counter-repair hypothesis is REFUTED on both declared deadlines and assignments. The target remains undamaged and wins 800:755. Exact action prediction is confirmed on these 200 reached calls, but it supplies no winning guarantee.

Every row below represents both physical assignments. HP is target:counter, and W/L is from the target's perspective. These are standard-start development conditions on the unchanged bundled engine. They do not use reserved pool C.

| Target | Counter | Outcome in each seat | HP | Final round |
|---|---|---|---|---:|
| P5TNUBM | v30forecast_r9 | W | 800:755 | 50 |
| P5TNUBM | v30forecast_r10 | W | 800:755 | 50 |

Across the declared games: P5TNUBM: 4W, 0D, 0L.

All 4 games pass strict condition accounting, original-engine replay and source/data archive checks. All 2 assignment pairs have identical normalized complete histories. These paired executions are reproducibility checks, not independent random samples. No bot errors or rejected submitted actions occurred.

Fresh counter instances reproduce every forecast-counter action on 200 recorded public observations, with unchanged inputs and legal outputs. There are 0 complete-action prediction disagreements with the target. Such disagreement is distinct from counter-policy reproduction. All model predictions agree here. The old-model comparison changes only the model specification and its parameter dictionary.

Of 4 paired full-policy interventions, 0 have identical full histories. This comparison cannot establish a one-round causal effect.

After handoff, all 166 recorded rounds cause zero damage to the counter. The earlier 45-point HP deficit remains.

The exact target and opponent specifications, parameters and declared input hashes are in [the manifest](../../retargeted-forecast-001.json). The audit artifacts are:

- strict: `bot_research/runs/validation/retargeted-forecast-strict-001.json`.
- replay: `bot_research/runs/validation/retargeted-forecast-replay-001.json`.
- summary: `bot_research/runs/validation/retargeted-forecast-summary-001.json`.
- data: `bot_research/runs/validation/retargeted-forecast-data-001.json`.
- forecast_histories: `bot_research/runs/validation/retargeted-forecast-forecast-histories-001.json`.
- comparison: `bot_research/runs/validation/retargeted-forecast-comparison-001.json`.

To reproduce, run from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Choose a new output directory, then repeat with `--resume` until all declared cases finish:

```sh
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/retargeted-forecast-001.json --output-dir bot_research/runs/validation/retargeted-forecast-reproduction --max-seconds 500 --match-timeout 300
```

The recorded match runtimes and audit runtimes are in their result files. No repeated deterministic condition is counted as an additional independent sample.
