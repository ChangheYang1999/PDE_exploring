#!/bin/bash
# D1 chain on GPU 5: v0 on the verifier's snapshot source (reproduction), v0 on the current source, v1 (dd) on the current source.
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
SNAP=RUN_ROOT/verifier/artifacts/production_snapshots/stable_adopted_20261028T220415Z
echo "$(date -u +%FT%TZ) D1 v0 snapshot start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v0_snapshot --precision fp64 --src-root $SNAP > validation/logs/d1_v0_snapshot.log 2>&1
echo "$(date -u +%FT%TZ) D1 v0 current start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v0_current --precision fp64 > validation/logs/d1_v0_current.log 2>&1
echo "$(date -u +%FT%TZ) D1 v1 dd start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v1_dd --precision dd > validation/logs/d1_v1_dd.log 2>&1
echo "$(date -u +%FT%TZ) D1 chain done"
