#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) test T start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_test_T.py > validation/logs/d1_test_T.log 2>&1
echo "$(date -u +%FT%TZ) gradient block share start"
nice -n 10 taskset -c 31-34 $PY -u validation/gradient_block_share.py > validation/logs/gradient_block_share.log 2>&1
echo "$(date -u +%FT%TZ) done"
