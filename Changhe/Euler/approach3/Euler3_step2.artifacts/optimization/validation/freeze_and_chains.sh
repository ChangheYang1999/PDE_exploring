#!/bin/bash
# D6FP 2026-10-29 (lead 02:48:22Z battery order, SPEC v1.10): after the CPU timing prints DONE, freeze the snapshot (status/RELEASE_SNAPSHOT_cpu_v1_<ts>.md,
# marker status/SNAPSHOT_cpu_v1.ready) and start one chain per core (one thread each):
#  core 32: extended table-cache regression -> lagJ SMOKE (20 it, S01, dd_fp64jac, complete gradient every 4) with the G7 kill/resume driver -> gates S20_own
#  core 33: gates S01_own -> G8 (g8_controls.py, g8_tables.py)
#  core 34: gates S09_own -> G6 (g6_mpmath.py) -> supplementary one-thread timing (SPEC v1.10 section 9 repetition)
#  core 31: (after T3 exits) gates manu_large_omega
# Log: validation/logs/freeze_and_chains.log; per-core logs validation/logs/chain_core<core>.log
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd "$ROOT"; LOG=validation/logs/freeze_and_chains.log
PY=python3
echo "$(date -u +%FT%TZ) waiting for DONE in cpu_profile_S01.log (profile pid 739083)" >> $LOG
while ! grep -q "^DONE" validation/logs/cpu_profile_S01.log 2>/dev/null; do
  if ! kill -0 739083 2>/dev/null; then echo "$(date -u +%FT%TZ) profile process gone without DONE" >> $LOG; break; fi
  sleep 15
done
sleep 3
TS=$(date -u +%Y%m%dT%H%M%SZ); $PY scripts/source_state.py > status/RELEASE_SNAPSHOT_cpu_v1_${TS}.md 2>&1; cp status/RELEASE_SNAPSHOT_cpu_v1_${TS}.md status/RELEASE_SNAPSHOT_cpu_v1.md
echo "cpu_v1 ${TS}" > status/SNAPSHOT_cpu_v1.ready
echo "$(date -u +%FT%TZ) snapshot frozen: status/RELEASE_SNAPSHOT_cpu_v1_${TS}.md (PRECISION_MODE dd_fp64jac, TABLE_CACHE on; conditional on M1 and M3)" >> $LOG
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
# ---- core 32
cat > validation/chain_core32.sh <<'EOC'
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
EOC
# ---- core 33
cat > validation/chain_core33.sh <<'EOC'
#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core33.log; PY=python3
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) core 33: gates S01_own" >> $LOG
CORES=33 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S01_own S01_own 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 33: G8 controls" >> $LOG
nice -n 10 taskset -c 33 $PY -u validation/g8_controls.py > validation/logs/g8_controls_cpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) g8_controls exit $?" >> $LOG
nice -n 10 taskset -c 33 $PY -u validation/g8_tables.py > validation/logs/g8_tables_cpu_v1.log 2>&1; echo "$(date -u +%FT%TZ) g8_tables exit $?" >> $LOG
echo "$(date -u +%FT%TZ) core 33 chain complete" >> $LOG
EOC
# ---- core 34
cat > validation/chain_core34.sh <<'EOC'
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
EOC
# ---- core 31 (after T3)
cat > validation/chain_core31.sh <<'EOC'
#!/bin/bash
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core31.log
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
while kill -0 1229750 2>/dev/null; do sleep 20; done
echo "$(date -u +%FT%TZ) core 31: T3 finished; gates manu_large_omega" >> $LOG
CORES=31 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_manu_large_omega manu_large_omega 1 >> $LOG 2>&1
echo "$(date -u +%FT%TZ) core 31 chain complete" >> $LOG
EOC
chmod +x validation/chain_core3*.sh
for c in 32 33 34 31; do setsid nohup bash validation/chain_core$c.sh > /dev/null 2>&1 < /dev/null & echo "$(date -u +%FT%TZ) chain core $c started pid $!" >> $LOG; done
