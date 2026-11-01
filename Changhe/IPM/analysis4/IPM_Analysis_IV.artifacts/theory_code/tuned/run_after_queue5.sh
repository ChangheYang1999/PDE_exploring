#!/bin/bash
# waits for run_after_queue4.sh (PID 3324151), then an independent polar probe of sin(9 theta) at delta = 4/7
while kill -0 3324151 2>/dev/null; do sleep 30; done
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
echo "start hh_tune 7 2 9 4 $(date -u +%H:%M:%SZ)" >> run_after_queue5.log
timeout 7200 nice -n 19 python3 hh_tune.py 7 2 9 4 > hh_tune_Q7h2_sin9.out 2>&1
echo "end hh_tune 7 2 9 4 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue5.log
