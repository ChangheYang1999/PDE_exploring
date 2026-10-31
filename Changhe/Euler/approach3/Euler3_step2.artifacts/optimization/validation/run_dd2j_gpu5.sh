#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) D1 dd2j (dd values, all-float64 Jacobian path) start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v2j_fp64jac --precision dd2j > validation/logs/d1_v2j.log 2>&1
echo "$(date -u +%FT%TZ) cost ddj start"
nice -n 10 taskset -c 31-34 $PY -u validation/lm_cost_compare.py ddj > validation/logs/lm_cost_compare_ddj.log 2>&1
echo "$(date -u +%FT%TZ) done"
