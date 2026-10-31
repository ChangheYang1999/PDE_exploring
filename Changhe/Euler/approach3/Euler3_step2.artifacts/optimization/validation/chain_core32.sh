#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core32.log; PY=python3
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) core 32: table-cache regression (extended)" >> $LOG
nice -n 10 taskset -c 32 $PY -u validation/test_table_cache.py > validation/logs/test_table_cache.log 2>&1
if grep -q "ALL_PASS True" validation/logs/test_table_cache.log; then echo "$(date -u +%FT%TZ) regression ALL_PASS" >> $LOG; else echo "$(date -u +%FT%TZ) regression FAILED: see validation/logs/test_table_cache.log; chain stops (the other chains keep running on the same code; decision by numerics)" >> $LOG; exit 1; fi
echo "$(date -u +%FT%TZ) core 32: lagJ SMOKE with G7" >> $LOG
CORES=32 bash scripts/run_smoke_job.sh cpu smk_lagJ --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 20 --ckpt_interval 300 --time_limit 21600 \
   --extra '{"lag_jacobian": true, "precision_mode": "dd_fp64jac", "threads": 1, "complete_gradient_every": 4}' \
   --note "lagJ SMOKE with G7 (SPEC v1.10 3.5 (b)): at most 20 iterations on S01, one thread, dd_fp64jac, complete gradient at fresh-J steps and every 4 accepted steps (R5); killed after the first checkpoint following a reused-J accepted step and resumed" >> $LOG 2>&1
RUN=$(ls -d runs/smk_lagJ_* | head -1); PID=$(pgrep -f "worker_d6.py $RUN/job.json" | head -1)
echo "$(date -u +%FT%TZ) smoke run $RUN pid $PID; G7 driver starts" >> $LOG
bash validation/lagj_g7_driver.sh $RUN $PID 32 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 32: gates S20_own" >> $LOG
CORES=32 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S20_own S20_own 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 32 chain complete" >> $LOG
