#!/bin/bash
# D6FP 2026-10-29T04:14Z (lead 04:05Z, SPEC v1.11): core 32 after the lagJ smoke and its G7 driver (pid 2683217): S05_own part B (G2G4, G3, G5),
# then G6, then G8 (controls, tables), then the section 9 supplement, then confirmations of 3.1 (S01_shift_a, S05_shift_c) until the release.
# A file validation/STOP_CHAIN32 stops the chain before the next item. Log: validation/logs/chain_core32.log
cd "$(dirname "$0")/.."; LOG=validation/logs/chain_core32.log; PY=python3
export CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "$(date -u +%FT%TZ) chain core 32 v2 started; waiting for the G7 driver (pid 2683217) to exit" >> $LOG
while kill -0 2683217 2>/dev/null; do sleep 20; done
echo "$(date -u +%FT%TZ) G7 driver finished" >> $LOG
run() { [ -f validation/STOP_CHAIN32 ] && { echo "$(date -u +%FT%TZ) STOP_CHAIN32 present: skipping $1" >> $LOG; return; }; echo "$(date -u +%FT%TZ) core 32: $1" >> $LOG; shift; "$@"; echo "$(date -u +%FT%TZ) exit $?" >> $LOG; }
run "gates S05_own part B (G2G4,G3,G5) tag cpu_v1_S05_own_G2G5" env CORES=32 SNAPSHOT=0 bash -c 'nice -n 10 taskset -c 32 $0 -u validation/gates.py --tag cpu_v1_S05_own_G2G5 --cases S05_own --device cpu --sections G2G4,G3,G5 > validation/logs/gates_cpu_v1_S05_own_G2G5.log 2>&1' $PY
run "G6 mpmath" bash -c "nice -n 10 taskset -c 32 $PY -u validation/g6_mpmath.py > validation/logs/g6_mpmath_cpu_v1.log 2>&1"
run "G8 controls" bash -c "nice -n 10 taskset -c 32 $PY -u validation/g8_controls.py > validation/logs/g8_controls_cpu_v1.log 2>&1"
run "G8 tables" bash -c "nice -n 10 taskset -c 32 $PY -u validation/g8_tables.py > validation/logs/g8_tables_cpu_v1.log 2>&1"
run "section 9 supplement (one thread)" bash -c "nice -n 10 taskset -c 32 $PY -u validation/cpu_profile_supplement.py 1 > validation/logs/cpu_profile_supplement_threads1.log 2>&1"
run "confirmation gates S01_shift_a" env CORES=32 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S01_shift_a S01_shift_a 1
run "confirmation gates S05_shift_c" env CORES=32 SNAPSHOT=0 bash scripts/run_cpu_battery.sh cpu_v1_S05_shift_c S05_shift_c 1
echo "$(date -u +%FT%TZ) chain core 32 v2 complete" >> $LOG
