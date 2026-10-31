#!/bin/bash
cd RUN_ROOT/numerics/degree6_free_parameters_48h; PY=python3; LOG=validation/logs/ddcheck_chain.log
echo "$(date -u +%FT%TZ) start dd_elementary self-test (CPU)" >> $LOG
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 nice -n 10 taskset -c 31-34 $PY -u validation/dd_elementary.py > validation/logs/dd_elementary_test.log 2>&1; echo "$(date -u +%FT%TZ) dd_elementary exit $?" >> $LOG
for spec in "$@"; do c=${spec%%:*}; col=${spec#*:}; echo "$(date -u +%FT%TZ) start dd_chain check $c $col (GPU 6)" >> $LOG
  CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 31-34 $PY -u validation/dd_chain.py $c $col Jcw,Jf,Jc cuda:0 > validation/logs/dd_chain_check_${c}_${col//:/_}.log 2>&1; echo "$(date -u +%FT%TZ) dd_chain check $c $col exit $?" >> $LOG; done
echo "$(date -u +%FT%TZ) ddcheck chain done" >> $LOG
