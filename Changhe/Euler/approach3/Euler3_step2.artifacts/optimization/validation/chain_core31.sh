#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core31.log
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
while kill -0 1229750 2>/dev/null; do sleep 20; done
echo "$(date -u +%FT%TZ) core 31: T3 finished; gates manu_large_omega" >> $LOG
CORES=31 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_manu_large_omega manu_large_omega 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 31 chain complete" >> $LOG
