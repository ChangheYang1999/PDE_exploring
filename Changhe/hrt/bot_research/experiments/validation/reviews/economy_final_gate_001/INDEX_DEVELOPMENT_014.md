# Development sweep review reading order

Written 2026-10-31T23:59:46.046465Z.

1. `AFS4_DEVELOPMENT_REVIEW_014.md`: completed afs4 interpretation and limits.
2. `development-afs4-20261031T235855304064Z/inspection.json`: exact finite joins and reductions.
3. `development-afs4-20261031T235855304064Z/inputs.json`: 233 authenticated input archives.
4. `inspect_development_sweeps_014.py` and `review_record_tools_004.py`: standard-library readers, without policy imports or calls.
5. `development_review_manifest_014.json`: dated source and output identities.

A later retained-record rerun from the project root creates a new dated output directory:

```sh
env PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$PWD" nice -n 19 taskset -c 30 .venv/bin/python -B bot_research/experiments/validation/reviews/economy_final_gate_001/inspect_development_sweeps_014.py --run afs4
```

After afs3 completes, its completed-control invocation is:

```sh
env PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONPATH="$PWD" nice -n 19 taskset -c 30 .venv/bin/python -B bot_research/experiments/validation/reviews/economy_final_gate_001/inspect_development_sweeps_014.py --run afs3 --afs4-input-map bot_research/experiments/validation/reviews/economy_final_gate_001/development-afs4-20261031T235855304064Z/inputs.json --afs4-input-map-sha e7d41583b61869427d90b0f0d6e70edf9593006ef01a151b91af522917246e86 --afs4-inspection-sha 9d207ef0629873141da19ec269b3e083b82a0b9d5f6e1c287224e66e797ef2fa
```

The reader refuses outcome reduction for an unfinished run without explicit supplied stop evidence. A documented stopped run may additionally pass `--stopped-evidence` with a relative path. Mere passage of the stop time is insufficient. Neither partial results nor these development comparisons change the af5 recommendation. No previous sealed artifact is overwritten.
