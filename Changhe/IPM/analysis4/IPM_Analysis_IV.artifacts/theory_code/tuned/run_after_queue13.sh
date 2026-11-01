#!/bin/bash
# Replaces the rest of queue 12 (stopped after the Q7 root 5 run at order 602): (1) exact first-compatibility polynomial,
# irreducibility, real roots and response structure at delta = 1/5 = 2/10 (c = 5/4) for f_1 = sin(theta) + b sin(3 theta)
# (tq_cert.py 10); (2) the remaining runs of queue 12 to orders 602 (Q7, roots 6..10) and 600 (Q8, roots 1..10),
# NUMERICAL EVIDENCE only.  Amplitudes are powers of two (exact rescaling).
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
L=run_after_queue13.log
while pgrep -f "hh_float.py 7 1 1:1,3:0.0659329806" > /dev/null; do sleep 5; done
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> $L
  timeout 3000 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> $L
}
echo "start tq_cert 10 $(date -u +%H:%M:%SZ)" >> $L
timeout 9000 nice -n 19 python3 tq_cert.py 10 > tq_cert_Q10.log 2>&1
echo "end tq_cert 10 rc=$? $(date -u +%H:%M:%SZ)" >> $L
E7=(1/16 1/2 1 1 1 1 1 1/2 1/4 1/8)
E8=(1/16 1/2 1 1 1 1 1/2 1/2 1/4 1/8)
for i in 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q7h1_root${i}_N602_f64.out 7 1 1:1,3:$b 602 ${E7[$((i-1))]}
done
for i in 1 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q8h1_root${i}_N600_f64.out 8 1 1:1,3:$b 600 ${E8[$((i-1))]}
done
