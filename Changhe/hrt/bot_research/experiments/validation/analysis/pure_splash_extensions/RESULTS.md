# Minimum pure-splash extension: checked result

2026-10-31T14:50:50.745352+00:00

For the fixed original two-splash map, the minimum number of extra
splashes that excludes every tier3 arrival is three, costing180.
This assumes no other new construction, removal or relocation.

| Extra splashes | Proposed sets | Legal sets | Maximum exposure |
| ---: | ---: | ---: | ---: |
| 0 | 1 | 1 | 80 |
| 1 | 140 | 139 | 130 |
| 2 | 9730 | 9589 | 170 |

Three added splashes at(10,3),(8,2),(1,2) give exposure200.
The tier3 HP threshold is180. On a pure-splash map, a single tier3
born at tick0 arrives whenever exposure is below180; proof is in
PROOF.md. Thus the lower cardinalities fail the stated universal
exclusion property. The three-splash witness proves sufficiency.

The search took5.297486 seconds. An independent
checker enumerated complete set coverage, rebuilt every candidate in
reverse construction order, checked all paths and exposures, and ran
original combat with one active tier3 on each legal map. It also checked
the three-splash witness. All9730 combat checks agree with the exposure
criterion. Checker elapsed17.572807 seconds.

This minimum does not extend to guns, walls or combinations of them.
The full-game180-cost extension was already tested in early_guard_extension:
it loses against P5TNUB and both v29 strike settings at H10 and H12.
That result illustrates why minimum component defense and winning game
spending are different questions. Pool C was not used.

Reproduce from the project root using the existing environment and a new
output filename:

```sh
PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 TMPDIR="$PWD/bot_research/tmp" \
  nice -n 19 taskset -c 28 .venv/bin/python -B -m \
  bot_research.experiments.validation.check_pure_splash_extensions \
  --data bot_research/bots/counters/data/pure_splash_extensions_001.json \
  --output bot_research/runs/validation/pure-splash-extension-check-reproduction.json
```
