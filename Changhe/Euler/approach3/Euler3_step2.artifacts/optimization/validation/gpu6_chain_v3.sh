#!/bin/bash
# D6FP 2026-10-29T05:15Z (SPEC v1.13 3.6 (a), (d)): GPU 6, host core 32, snapshot gpu_v1, in sequence:
# (1) M3 reproduction on gpu_v1: lm_cost_compare.py ddj (counts and costs within 1e-10 of the 04:48Z record); output renamed lm_cost_compare_ddj_gpu_v1.json;
# (2) controlled float64 run alone on GPU 6: lm_cost_compare.py fp64 -> lm_cost_compare_fp64_gpu6_controlled.json (ratio against (1));
# (3) G7 on gpu_v1 (validation/g7_gpu_driver.sh 6 32 g7_gpu_v1); (4) gates S05_own (full) on GPU 6. Log validation/logs/gpu6_chain.log; stop file validation/STOP_GPU6.
cd "$(dirname "$0")/.."; LOG=validation/logs/gpu6_chain.log; PY=python3
export CUDA_VISIBLE_DEVICES=6 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
step() { [ -f validation/STOP_GPU6 ] && { echo "$(date -u +%FT%TZ) STOP_GPU6 present: skipping $1" >> $LOG; return 1; }; echo "$(date -u +%FT%TZ) GPU 6 (gpu_v1): $1" >> $LOG; return 0; }
if step "M3 reproduction on gpu_v1 (lm_cost_compare.py ddj)"; then
  nice -n 10 taskset -c 32 $PY -u validation/lm_cost_compare.py ddj > validation/logs/lm_cost_compare_ddj_gpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) exit $?" >> $LOG
  [ -f validation/lm_cost_compare_ddj.json ] && mv validation/lm_cost_compare_ddj.json validation/lm_cost_compare_ddj_gpu_v1.json
fi
if step "controlled float64 run alone on GPU 6 (lm_cost_compare.py fp64)"; then
  nice -n 10 taskset -c 32 $PY -u validation/lm_cost_compare.py fp64 > validation/logs/lm_cost_compare_fp64_gpu6.log 2>&1; echo "$(date -u +%FT%TZ) exit $?" >> $LOG
  [ -f validation/lm_cost_compare_fp64.json ] && mv validation/lm_cost_compare_fp64.json validation/lm_cost_compare_fp64_gpu6_controlled.json
fi
if step "G7 on gpu_v1 (production configuration)"; then
  bash validation/g7_gpu_driver.sh 6 32 g7_gpu_v1 >> $LOG 2>&1
fi
if step "gates S05_own (full) on GPU 6"; then
  bash scripts/run_gpu_battery.sh 6 32 gpu_v1_S05_own S05_own >> $LOG 2>&1
fi
echo "$(date -u +%FT%TZ) GPU 6 chain v3 complete" >> $LOG
