#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) D1 dd2t (dd values, fp64 tangents) start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v2t_fp64tangent --precision dd2t > validation/logs/d1_v2t.log 2>&1
echo "$(date -u +%FT%TZ) cost ddt start"
nice -n 10 taskset -c 31-34 $PY -u validation/lm_cost_compare.py ddt > validation/logs/lm_cost_compare_ddt.log 2>&1
echo "$(date -u +%FT%TZ) done"
