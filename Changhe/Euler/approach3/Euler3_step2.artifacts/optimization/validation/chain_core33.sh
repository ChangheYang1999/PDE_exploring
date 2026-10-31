#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core33.log; PY=python3
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) core 33: gates S01_own" >> $LOG
CORES=33 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S01_own S01_own 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 33: G8 controls" >> $LOG
nice -n 10 taskset -c 33 $PY -u validation/g8_controls.py > validation/logs/g8_controls_cpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) g8_controls exit $?" >> $LOG
nice -n 10 taskset -c 33 $PY -u validation/g8_tables.py > validation/logs/g8_tables_cpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) g8_tables exit $?" >> $LOG
echo "$(date -u +%FT%TZ) core 33 chain complete" >> $LOG
