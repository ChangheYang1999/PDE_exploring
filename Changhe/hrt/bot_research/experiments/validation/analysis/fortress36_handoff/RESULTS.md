# Frozen fortress v36 against disclosed handoff counters

Published 2026-10-31T15:01:17.724705+00:00.

The claim that v36 wins all ten conditions is REFUTED: the public-HP trigger wins in both assignments. The four forecast and visible-roster settings are beaten. These are complete-policy results; they do not isolate either of v36's two added options.

Every row below represents both physical assignments. HP is target:counter, and W/L is from the target's perspective. These are standard-start development conditions on the unchanged bundled engine. They do not use reserved pool C.

| Target | Counter | Outcome in each seat | HP | Final round |
|---|---|---|---|---:|
| F36 | lead8 | L | 520:765 | 50 |
| F36 | forecasttrue_r9 | W | 240:-215 | 13 |
| F36 | forecastfalse_r9 | W | 240:-215 | 13 |
| F36 | forecasttrue_r10 | W | 240:-215 | 13 |
| F36 | forecastfalse_r10 | W | 240:-215 | 13 |

Across the declared games: F36: 8W, 0D, 2L.

All 10 games pass strict condition accounting, original-engine replay and source/data archive checks. All 5 assignment pairs have identical normalized complete histories. These paired executions are reproducibility checks, not independent random samples. No bot errors or rejected submitted actions occurred.

Fresh counter instances reproduce every forecast-counter action on 104 recorded public observations, with unchanged inputs and legal outputs. There are 88 complete-action prediction disagreements with the target. Such disagreement is distinct from counter-policy reproduction. The additional 2 public-HP histories also reproduce exactly; the counter buys no minions after handoff.

Of 4 paired full-policy interventions, 0 have identical full histories. This comparison cannot establish a one-round causal effect.

The exact target and opponent specifications, parameters and declared input hashes are in [the manifest](../../fortress36-handoff-001.json). The audit artifacts are:

- strict: `bot_research/runs/validation/fortress36-handoff-strict-001.json`.
- replay: `bot_research/runs/validation/fortress36-handoff-replay-001.json`.
- summary: `bot_research/runs/validation/fortress36-handoff-summary-001.json`.
- data: `bot_research/runs/validation/fortress36-handoff-data-001.json`.
- forecast_histories: `bot_research/runs/validation/fortress36-handoff-forecast-histories-001.json`.
- comparison: `bot_research/runs/validation/fortress36-handoff-forecast-comparison-001.json`.
- hp_histories: `bot_research/runs/validation/nominee-f36-hp-histories-001.json`.

To reproduce, run from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Choose a new output directory, then repeat with `--resume` until all declared cases finish:

```sh
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/fortress36-handoff-001.json --output-dir bot_research/runs/validation/fortress36-handoff-reproduction --max-seconds 500 --match-timeout 300
```

The recorded match runtimes and audit runtimes are in their result files. No repeated deterministic condition is counted as an additional independent sample.
