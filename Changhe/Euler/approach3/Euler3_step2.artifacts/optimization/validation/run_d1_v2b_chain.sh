#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) D1 v2 (complete: radial contraction and twist in dd) start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v2b_full --precision dd2 > validation/logs/d1_v2b_full.log 2>&1
echo "$(date -u +%FT%TZ) term split (complete v2) start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_term_split.py --variants dd2 --tag _v2b > validation/logs/d1_term_split_v2b.log 2>&1
echo "$(date -u +%FT%TZ) invariance start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_invariance.py > validation/logs/d1_invariance.log 2>&1
echo "$(date -u +%FT%TZ) chain done"
