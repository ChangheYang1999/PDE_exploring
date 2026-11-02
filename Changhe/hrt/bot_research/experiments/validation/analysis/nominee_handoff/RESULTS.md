# Early-defense nominees against disclosed handoff counters

Published 2026-10-31T15:02:41.790173+00:00.

The disclosed counters do not all retain their wins: P5TNUBM wins all ten conditions. P4TNUB remains vulnerable to the public-HP trigger and both forecast deadlines. The original forecast model is deliberately unchanged and differs from both targets.

Every row below represents both physical assignments. HP is target:counter, and W/L is from the target's perspective. These are standard-start development conditions on the unchanged bundled engine. They do not use reserved pool C.

| Target | Counter | Outcome in each seat | HP | Final round |
|---|---|---|---|---:|
| P4TNUB | lead8 | L | 660:755 | 50 |
| P4TNUB | forecasttrue_r9 | L | 520:583 | 50 |
| P4TNUB | forecastfalse_r9 | W | 520:-71 | 15 |
| P4TNUB | forecasttrue_r10 | L | 520:609 | 50 |
| P4TNUB | forecastfalse_r10 | W | 520:-45 | 15 |
| P5TNUBM | lead8 | W | 800:-1439 | 21 |
| P5TNUBM | forecasttrue_r9 | W | 800:677 | 50 |
| P5TNUBM | forecastfalse_r9 | W | 800:-415 | 15 |
| P5TNUBM | forecasttrue_r10 | W | 800:423 | 50 |
| P5TNUBM | forecastfalse_r10 | W | 800:-389 | 15 |

Across the declared games: P4TNUB: 4W, 0D, 6L; P5TNUBM: 10W, 0D, 0L.

All 20 games pass strict condition accounting, original-engine replay and source/data archive checks. All 10 assignment pairs have identical normalized complete histories. These paired executions are reproducibility checks, not independent random samples. No bot errors or rejected submitted actions occurred.

Fresh counter instances reproduce every forecast-counter action on 520 recorded public observations, with unchanged inputs and legal outputs. There are 450 complete-action prediction disagreements with the target. Such disagreement is distinct from counter-policy reproduction. The additional 4 public-HP histories also reproduce exactly; the counter buys no minions after handoff.

Of 8 paired full-policy interventions, 0 have identical full histories. This comparison cannot establish a one-round causal effect.

The exact target and opponent specifications, parameters and declared input hashes are in [the manifest](../../nominee-handoff-001.json). The audit artifacts are:

- strict: `bot_research/runs/validation/nominee-handoff-strict-001.json`.
- replay: `bot_research/runs/validation/nominee-handoff-replay-001.json`.
- summary: `bot_research/runs/validation/nominee-handoff-summary-001.json`.
- data: `bot_research/runs/validation/nominee-handoff-data-001.json`.
- forecast_histories: `bot_research/runs/validation/nominee-handoff-forecast-histories-001.json`.
- comparison: `bot_research/runs/validation/nominee-handoff-forecast-comparison-001.json`.
- hp_histories: `bot_research/runs/validation/nominee-f36-hp-histories-001.json`.

To reproduce, run from the project root with `PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH="$PWD"`, `OMP_NUM_THREADS=1`, and `TMPDIR="$PWD/bot_research/tmp"`. Choose a new output directory, then repeat with `--resume` until all declared cases finish:

```sh
nice -n 19 taskset -c 28 .venv/bin/python -B -m bot_research.experiments.validation.run_data_development --manifest bot_research/experiments/validation/nominee-handoff-001.json --output-dir bot_research/runs/validation/nominee-handoff-reproduction --max-seconds 500 --match-timeout 300
```

The recorded match runtimes and audit runtimes are in their result files. No repeated deterministic condition is counted as an additional independent sample.
