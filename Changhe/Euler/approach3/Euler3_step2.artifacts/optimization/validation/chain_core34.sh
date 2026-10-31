#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core34.log; PY=python3
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) core 34: gates S09_own" >> $LOG
CORES=34 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S09_own S09_own 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 34: G6 mpmath" >> $LOG
nice -n 10 taskset -c 34 $PY -u validation/g6_mpmath.py > validation/logs/g6_mpmath_cpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) g6 exit $?" >> $LOG
echo "$(date -u +%FT%TZ) core 34: supplementary one-thread timing (section 9 repetition)" >> $LOG
nice -n 10 taskset -c 34 $PY -u validation/cpu_profile_supplement.py 1 > validation/logs/cpu_profile_supplement_threads1.log 2>&1; echo "$(date -u +%FT%TZ) supplement exit $?" >> $LOG
echo "$(date -u +%FT%TZ) core 34 chain complete" >> $LOG
