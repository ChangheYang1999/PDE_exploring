#!/bin/bash
# after validation/after_cpu_profile.sh (PID given) finishes: supplementary CPU timing at 2 threads with 3 samples per entry (verifier review of the sample counts; R1 compares 1, 2, 4), cores 31-32 (T3 may still be on core 34)
cd RUN_ROOT/numerics/degree6_free_parameters_48h
PY=python3
PID=$1
while kill -0 $PID 2>/dev/null; do sleep 30; done
export CUDA_VISIBLE_DEVICES= PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 CPU_PROFILE_THREADS=2 CPU_PROFILE_N=3 CPU_PROFILE_OUT=cpu_profile_S01_threads2_n3.json CPU_PROFILE_SKIP_FULLJ=1
echo "$(date -u +%FT%TZ) supplementary CPU profile (2 threads, n=3) start" >> validation/logs/after_cpu_profile.log
nice -n 10 taskset -c 31-32 $PY -u validation/cpu_profile_S01.py > validation/logs/cpu_profile_S01_threads2.log 2>&1
echo "$(date -u +%FT%TZ) supplementary CPU profile done exit $?" >> validation/logs/after_cpu_profile.log
