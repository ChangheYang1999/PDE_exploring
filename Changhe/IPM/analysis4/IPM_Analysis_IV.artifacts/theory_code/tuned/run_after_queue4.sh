#!/bin/bash
# waits for run_after_queue3.sh (PID 2552984), then the delta = 2/7 and 1/4 two-mode certificates
while kill -0 2552984 2>/dev/null; do sleep 30; done
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
echo "start tq_cert 7 $(date -u +%H:%M:%SZ)" >> run_after_queue4.log
timeout 7200 nice -n 19 python3 tq_cert.py 7 > tq_cert_Q7.log 2>&1
echo "end tq_cert 7 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue4.log
timeout 7200 nice -n 19 python3 tq_cert.py 8 > tq_cert_Q8.log 2>&1
echo "end tq_cert 8 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue4.log
