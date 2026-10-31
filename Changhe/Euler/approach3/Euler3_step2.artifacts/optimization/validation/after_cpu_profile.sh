#!/bin/bash
# After the CPU timing (PID given) finishes: corrected T3 on one core (lead 01:02Z (b)) and the M2 test of mode dd_fp64jac on the other cores.
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
PID=$1
while kill -0 $PID 2>/dev/null; do sleep 20; done
echo "$(date -u +%FT%TZ) cpu profile finished; launching T3 (core 34) and D1 dd2j (cores 31-33)" >> validation/logs/after_cpu_profile.log
export CUDA_VISIBLE_DEVICES= PYTHONDONTWRITEBYTECODE=1
OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 setsid nohup nice -n 10 taskset -c 34 $PY -u validation/d1_test_T3.py > validation/logs/d1_test_T3.log 2>&1 < /dev/null &
OMP_NUM_THREADS=3 MKL_NUM_THREADS=3 nice -n 10 taskset -c 31-33 $PY -u validation/d1_anchor_precision.py --tag v2j_fp64jac_cpu --precision dd2j > validation/logs/d1_v2j_cpu.log 2>&1
echo "$(date -u +%FT%TZ) D1 dd2j (CPU) done exit $?" >> validation/logs/after_cpu_profile.log
