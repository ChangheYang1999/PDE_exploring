# Economy final gate review

Read `INTERIM_REVIEW.md` first. The fixed partial inspection is under `inspection-20261031T225610458161Z/`; `inspection.json` contains all reductions and source comparisons, and `inputs.json` maps original project-relative inputs to exact content-addressed gzip snapshots under `inputs/`. No partial inspection is a completed recommendation gate.

`inspect_records.py` imports only the Python standard library. It reads existing result files, not policies or the engine. Run a new inspection after the follow-up campaigns finish; it creates a new dated folder and preserves previous snapshots. From the project root, on an available authorized core30:

```sh
PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" PYTHONPATH="$PWD" \
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 \
nice -n 19 taskset -c 30 .venv/bin/python -B \
  bot_research/experiments/validation/reviews/economy_final_gate_001/inspect_records.py
```

The completion fields require all exact expected unique conditions, a retained summary, and a completion line. A finished inspector is not the same as a completed game campaign. Inspect errors, source discrepancies and missing conditions before interpreting tables. The script does not certify strength, uninterrupted runtime identity, raw-log terminal consistency, or universal behavior. Its bootstrap follows the economy lane's declared method exactly.
