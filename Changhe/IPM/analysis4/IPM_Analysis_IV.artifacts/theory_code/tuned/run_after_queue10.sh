#!/bin/bash
# Longer double-precision tuned runs (orders 602 at delta = 2/7, 600 at delta = 1/4) at all twenty two-mode roots, to test
# whether the apparent growth constants fitted on orders <= 300 are stable (windows n >= 100 .. 500).  The amplitude is a
# power of two near 1/A, so the floating arithmetic is an exact rescaling of the unit-amplitude run (no overflow).
# NUMERICAL EVIDENCE only.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> run_after_queue10.log
  timeout 3000 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue10.log
}
E7=(1/16 1/2 1 1 1 1 1 1/2 1/4 1/8)
E8=(1/16 1/2 1 1 1 1 1/2 1/2 1/4 1/8)
for i in 1 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q7h1_root${i}_N602_f64.out 7 1 1:1,3:$b 602 ${E7[$((i-1))]}
done
for i in 1 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q8h1_root${i}_N600_f64.out 8 1 1:1,3:$b 600 ${E8[$((i-1))]}
done
echo "queue10 done $(date -u +%H:%M:%SZ)" >> run_after_queue10.log
