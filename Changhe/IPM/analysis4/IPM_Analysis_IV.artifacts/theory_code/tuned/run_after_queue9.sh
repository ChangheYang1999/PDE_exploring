#!/bin/bash
# cross-check of the block-maximum fit against the earlier 1024-bit fits at delta=1/3 (Q=6), after queue8
cd "$(dirname "$0")"
while kill -0 3965922 2>/dev/null; do sleep 20; done
export OMP_NUM_THREADS=1
run() { echo "start $1 ${*:2} $(date -u +%H:%M:%SZ)" >> run_after_queue9.log; timeout 5400 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1; echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue9.log; }
for r in 1 2 3 4 5 6; do
  b=$(grep -E "^  \[" tq_cert_Q6.log | awk '{print $NF}' | sed -n ${r}p)
  e=1; [ $r -eq 1 ] && e=1/8
  run hhf_Q6h1_root${r}_N300_f64.out 6 1 1:1,3:$b 300 $e
done
echo "queue9 done $(date -u +%H:%M:%SZ)" >> run_after_queue9.log
