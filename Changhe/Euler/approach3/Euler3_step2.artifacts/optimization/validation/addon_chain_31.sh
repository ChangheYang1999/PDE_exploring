#!/bin/bash
# (k) step add-on (SPEC v1.18 3.6 (k)) for the 3.1 cases with failing coefficient columns, one process at a time in the fourth host slot (GPU given).
cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3
GPU=$1; shift
for c in "$@"; do
  echo "$(date -u +%FT%TZ) add-on $c start (GPU $GPU)" >> validation/logs/addon_chain_31.log
  CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY -u validation/g1_step_addon.py $c validation/gates_gpu_v1_$c.json > validation/logs/g1_step_addon_$c.log 2>&1
  echo "$(date -u +%FT%TZ) add-on $c done exit $?" >> validation/logs/addon_chain_31.log
done
