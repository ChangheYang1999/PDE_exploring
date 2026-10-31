#!/bin/bash
# D6FP release battery on the FROZEN source (lead 23:41Z item 2): records the source state, then runs on GPUs 5 and 6:
#   GPU 5: gates.py set A (S01_own, S05_own, manu_small_omega, manu_large_omega), then the G7 resume test, then profiling (worker path)
#   GPU 6: gates.py set B (manu_near_edge, manu_a, S01_shift_a, S05_shift_c), then g3_addon on all eight cases, then G8 controls/tables
# Usage: scripts/run_frozen_battery.sh <tag>
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
TAG=$1; [ -z "$TAG" ] && { echo "usage: run_frozen_battery.sh <tag>"; exit 1; }
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
TS=$(date -u +%Y%m%dT%H%M%SZ)
$PY scripts/source_state.py > status/RELEASE_SNAPSHOT_${TAG}_${TS}.md 2>&1
echo "$(date -u +%FT%TZ) frozen battery $TAG: source state recorded in status/RELEASE_SNAPSHOT_${TAG}_${TS}.md" | tee -a validation/logs/frozen_battery_${TAG}.log
(
  export CUDA_VISIBLE_DEVICES=5
  echo "$(date -u +%FT%TZ) [gpu5] gates set A start" >> validation/logs/frozen_battery_${TAG}.log
  nice -n 10 taskset -c 31-34 $PY -u validation/gates.py --tag ${TAG}_A --cases S01_own,S05_own,manu_small_omega,manu_large_omega > validation/logs/gates_${TAG}_A.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu5] gates set A done exit $?; resume test start" >> validation/logs/frozen_battery_${TAG}.log
  bash scripts/resume_test_d6.sh 5 ${TAG} > validation/logs/resume_${TAG}.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu5] resume test done exit $?; profiling start" >> validation/logs/frozen_battery_${TAG}.log
  nice -n 10 taskset -c 31-34 $PY -u validation/lm_cost_compare.py fp64,ddt > validation/logs/lm_cost_${TAG}.log 2>&1
  nice -n 10 taskset -c 31-34 $PY -u validation/profile_d6.py --out profiling/profile_${TAG}.json > validation/logs/profile_${TAG}.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu5] profiling done exit $?" >> validation/logs/frozen_battery_${TAG}.log
) &
(
  export CUDA_VISIBLE_DEVICES=6
  echo "$(date -u +%FT%TZ) [gpu6] gates set B start" >> validation/logs/frozen_battery_${TAG}.log
  nice -n 10 taskset -c 31-34 $PY -u validation/gates.py --tag ${TAG}_B --cases manu_near_edge,manu_a,S01_shift_a,S05_shift_c > validation/logs/gates_${TAG}_B.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu6] gates set B done exit $?; g3_addon start" >> validation/logs/frozen_battery_${TAG}.log
  nice -n 10 taskset -c 31-34 $PY -u validation/g3_addon.py --tag ${TAG} --cases S01_own,S05_own,manu_small_omega,manu_large_omega,manu_near_edge,manu_a,S01_shift_a,S05_shift_c > validation/logs/g3_addon_${TAG}.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu6] g3_addon done exit $?; G8 start" >> validation/logs/frozen_battery_${TAG}.log
  nice -n 10 taskset -c 31-34 $PY -u validation/g8_controls.py > validation/logs/g8_controls_${TAG}.log 2>&1
  nice -n 10 taskset -c 31-34 $PY -u validation/g8_tables.py --tag ${TAG} > validation/logs/g8_tables_${TAG}.log 2>&1
  echo "$(date -u +%FT%TZ) [gpu6] G8 done exit $?" >> validation/logs/frozen_battery_${TAG}.log
) &
wait
echo "$(date -u +%FT%TZ) frozen battery $TAG complete" >> validation/logs/frozen_battery_${TAG}.log
