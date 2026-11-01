#!/bin/bash
# pauses the sin15 reproduction (PID 874556) while the delta = 4/7 response minima and radii run, then resumes it
# (one busy computation at a time)
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
kill -STOP 874556 2>/dev/null
echo "pause sin15, start tq_radiush 7 2 $(date -u +%H:%M:%SZ)" >> run_radiush_Q7.log
timeout 5400 nice -n 19 python3 tq_radiush.py 7 2 4:16 8:24 6:16 > tq_radiush_Q7h2.out 2>&1
echo "end tq_radiush 7 2 rc=$? $(date -u +%H:%M:%SZ)" >> run_radiush_Q7.log
kill -CONT 874556 2>/dev/null
echo "resumed sin15 $(date -u +%H:%M:%SZ)" >> run_radiush_Q7.log
