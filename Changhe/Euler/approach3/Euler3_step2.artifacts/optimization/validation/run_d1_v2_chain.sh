#!/bin/bash
# GPU 5: fields_dd unit test, D1 v2 (dd2), then the J_c assembly test with the repaired target correction.
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
export CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) test_fields_dd start"
nice -n 10 taskset -c 31-34 $PY -u validation/test_fields_dd.py > validation/logs/test_fields_dd2.log 2>&1
echo "$(date -u +%FT%TZ) D1 v2 start"
nice -n 10 taskset -c 31-34 $PY -u validation/d1_anchor_precision.py --tag v2_dd2 --precision dd2 > validation/logs/d1_v2_dd2.log 2>&1
echo "$(date -u +%FT%TZ) test_jc_assembly (repaired target correction) start"
nice -n 10 taskset -c 31-34 $PY -u validation/test_jc_assembly.py > validation/logs/test_jc_assembly2.log 2>&1
echo "$(date -u +%FT%TZ) chain done"
