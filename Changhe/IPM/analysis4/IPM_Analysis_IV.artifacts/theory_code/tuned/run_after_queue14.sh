#!/bin/bash
# Replaces the tail of queue 13 (its runner was stopped while tq_cert.py 10 kept running): waits for tq_cert.py 10, then
# (1) double-precision tuned runs to order 300 at the fourteen real roots at delta = 1/5 (c = 5/4); (2) the remaining runs
# of queue 12 to orders 602 (Q7, roots 6..10) and 600 (Q8, roots 1..10).  NUMERICAL EVIDENCE only.  Amplitudes are powers
# of two (exact rescaling).
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
L=run_after_queue14.log
while pgrep -f "tq_cert.py 10" > /dev/null; do sleep 10; done
echo "tq_cert 10 finished $(date -u +%H:%M:%SZ)" >> $L
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> $L
  timeout 3000 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> $L
}
E10=(1/16 1/2 1 1 1 1 1 1 1/2 1/2 1/2 1/2 1/2 1/2)
n=$(grep -cE "^  \[" tq_cert_Q10.log)
for i in $(seq 1 $n); do
  b=$(grep -E "^  \[" tq_cert_Q10.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q10h1_root${i}_N300_f64.out 10 1 1:1,3:$b 300 ${E10[$((i-1))]}
done
E7=(1/16 1/2 1 1 1 1 1 1/2 1/4 1/8)
E8=(1/16 1/2 1 1 1 1 1/2 1/2 1/4 1/8)
for i in 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q7h1_root${i}_N602_f64.out 7 1 1:1,3:$b 602 ${E7[$((i-1))]}
done
for i in 1 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q8h1_root${i}_N600_f64.out 8 1 1:1,3:$b 600 ${E8[$((i-1))]}
done
