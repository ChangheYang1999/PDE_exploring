#!/bin/bash
# the second half of the gate cases on GPU 5 after the (release-code) profiling finishes
cd "$(dirname "$0")/.."; PY=python3
while pgrep -f 'validation/profile_d6' > /dev/null; do sleep 15; done
echo "$(date -u +%FT%TZ) GPU 5 free; gates C5 start"
CUDA_VISIBLE_DEVICES=5 OMP_NUM_THREADS=1 nice -n 10 $PY -u validation/gates.py --tag full_C5 --cases manu_near_edge,manu_a,S01_shift_a,S05_shift_c,manu_allm_c > validation/logs/gates_full_C5.log 2>&1
echo "$(date -u +%FT%TZ) gates C5 done exit $?"
