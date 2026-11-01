#!/bin/bash
# Order-doubling checks, NUMERICAL EVIDENCE only: double-precision tuned runs to order 600 at the fourteen roots of P_20
# (delta = 1/5) and to order 612 at the ten roots of P_18 (delta = 2/9), for comparison with the order-300 and order-306
# runs.  Amplitudes are powers of two (exact rescaling), chosen so that A*eps is near 1.  Starts after queue 15 ends.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
L=run_after_queue16.log
PY=python3
while pgrep -f "[r]un_after_queue15.sh" > /dev/null; do sleep 20; done
echo "queue 16 start $(date -u +%H:%M:%SZ)" >> $L
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> $L
  timeout 3000 nice -n 19 $PY hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> $L
}
E10=(1/32 1/4 1/2 1 1 1 1 1 1/2 1/2 1/2 1/4 1/4 1/8)
for i in $(seq 1 14); do
  b=$(grep -E "^  \[" tq_cert_Q10.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q10h1_root${i}_N600_f64.out 10 1 1:1,3:$b 600 ${E10[$((i-1))]}
done
E9=(1/16 1/4 1 1 1 1 1/2 1/2 1/4 1/8)
for i in $(seq 1 10); do
  b=$(grep -E "^  \[" tq_cert_Q9.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q9h1_root${i}_N612_f64.out 9 1 1:1,3:$b 612 ${E9[$((i-1))]}
done
echo "queue 16 end $(date -u +%H:%M:%SZ)" >> $L
