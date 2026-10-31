#!/bin/bash
# D6FP 2026-10-29T04:50Z: GPU 6 (restored 02:51:04Z), host core 32, in sequence: (1) M3 for dd_fp64jac in the registered GPU form
# (validation/lm_cost_compare.py ddj: five accepted iterations from S01 against the GPU dd2 run in validation/lm_cost_compare.json);
# (2) the lagJ SMOKE with the G7 kill and resume (20 iterations on S01, dd_fp64jac, complete gradient every 4; driver validation/lagj_g7_driver.sh);
# (3) gates S05_own (full battery, tag gpu_v1_S05_own). Log: validation/logs/gpu6_chain.log. Stop file validation/STOP_GPU6.
cd "$(dirname "$0")/.."; LOG=validation/logs/gpu6_chain.log; PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
step() { [ -f validation/STOP_GPU6 ] && { echo "$(date -u +%FT%TZ) STOP_GPU6 present: skipping $1" >> $LOG; return 1; }; echo "$(date -u +%FT%TZ) GPU 6: $1" >> $LOG; return 0; }
if step "M3 GPU form: lm_cost_compare.py ddj (output validation/lm_cost_compare_ddj.json)"; then
  nice -n 10 taskset -c 32 $PY -u validation/lm_cost_compare.py ddj > validation/logs/lm_cost_compare_ddj_gpu6.log 2>&1; echo "$(date -u +%FT%TZ) M3 exit $?" >> $LOG
fi
if step "lagJ SMOKE with G7 on GPU 6"; then
  CORES=32 bash scripts/run_smoke_job.sh 6 smk_lagJ_gpu --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 20 --ckpt_interval 60 --time_limit 7200 \
     --extra '{"lag_jacobian": true, "precision_mode": "dd_fp64jac", "threads": 1, "complete_gradient_every": 4}' \
     --note "lagJ SMOKE with G7 (SPEC v1.10 3.5 (b)) on GPU 6 after the restoration of 02:51:04Z: at most 20 iterations on S01, dd_fp64jac, complete gradient at fresh-J steps and every 4 accepted steps; killed after the first checkpoint following a reused-J accepted step and resumed" >> $LOG 2>&1
  RUN=$(ls -d runs/smk_lagJ_gpu_* | head -1); PID=$(pgrep -f "worker_d6.py $RUN/job.json" | head -1)
  echo "$(date -u +%FT%TZ) smoke run $RUN pid $PID; G7 driver starts (relaunch on GPU 6)" >> $LOG
  bash validation/lagj_g7_driver.sh $RUN $PID 32 6 >> $LOG 2>&1
fi
if step "gates S05_own (full) on GPU 6"; then
  bash scripts/run_gpu_battery.sh 6 32 gpu_v1_S05_own S05_own >> $LOG 2>&1
fi
echo "$(date -u +%FT%TZ) GPU 6 chain complete" >> $LOG
