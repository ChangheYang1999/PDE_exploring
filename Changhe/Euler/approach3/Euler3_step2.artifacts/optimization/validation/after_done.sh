#!/bin/bash
# D6FP 2026-10-29T02:41Z: after the CPU timing prints DONE (cores free again; the pause watcher resumes T3 and the smoke): (1) the table-cache
# bitwise regression on core 32 (validation/test_table_cache.py); (2) if it passes: freeze the snapshot (status/RELEASE_SNAPSHOT_cpu_v1_<ts>.md),
# launch the lagJ SMOKE (20 iterations, S01, cfg lag_jacobian true, precision dd_fp64jac, one thread) on core 32 and the release-battery gates
# for S01_own on core 33 (one thread). Log: validation/logs/after_done.log
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; LOG=validation/logs/after_done.log
PY=python3
echo "$(date -u +%FT%TZ) after_done waiting for DONE in cpu_profile_S01.log" >> $LOG
while ! grep -q "^DONE" validation/logs/cpu_profile_S01.log 2>/dev/null; do
  if ! kill -0 739083 2>/dev/null; then echo "$(date -u +%FT%TZ) profile process gone without DONE" >> $LOG; break; fi
  sleep 20
done
sleep 5
echo "$(date -u +%FT%TZ) timing finished; running test_table_cache.py on core 32" >> $LOG
CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 10 taskset -c 32 $PY -u validation/test_table_cache.py > validation/logs/test_table_cache.log 2>&1
if grep -q "ALL_PASS True" validation/logs/test_table_cache.log; then
  echo "$(date -u +%FT%TZ) table cache regression PASS" >> $LOG
  TS=$(date -u +%Y%m%dT%H%M%SZ); $PY scripts/source_state.py > status/RELEASE_SNAPSHOT_cpu_v1_${TS}.md 2>&1
  echo "$(date -u +%FT%TZ) snapshot status/RELEASE_SNAPSHOT_cpu_v1_${TS}.md written (mode dd_fp64jac, conditional on M1)" >> $LOG
  CORES=32 bash scripts/run_smoke_job.sh cpu smk_lagJ --start starts/S01_nest6_cl0.45_om1.0_p0.pt --max_iter 20 --ckpt_interval 300 --time_limit 14400 \
     --extra '{"lag_jacobian": true, "precision_mode": "dd_fp64jac", "threads": 1, "complete_gradient_every": 4}' \
     --note "lagJ SMOKE (SPEC 3.5 (b), R2): at most 20 iterations on S01, one thread, dd_fp64jac; complete gradient every 4 accepted steps (R5)" >> $LOG 2>&1
  CORES=33 SNAPSHOT=0 setsid nohup bash scripts/run_cpu_battery.sh cpu_v1_S01 S01_own 1 > /dev/null 2>&1 < /dev/null &
  echo "$(date -u +%FT%TZ) gates cpu_v1_S01 S01_own launched on core 33 (pid $!)" >> $LOG
else
  echo "$(date -u +%FT%TZ) table cache regression FAILED or crashed: nothing launched (see validation/logs/test_table_cache.log)" >> $LOG
fi
