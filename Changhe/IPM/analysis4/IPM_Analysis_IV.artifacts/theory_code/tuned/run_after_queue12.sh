#!/bin/bash
# Replaces queues 10 and 11 (killed after the Q7 root 1 run): (1) exact first-compatibility polynomial, irreducibility,
# real roots and response structure at delta = 2/9 (c = 9/7) for f_1 = sin(theta) + b sin(3 theta) (tq_cert.py 9);
# (2) double-precision tuned runs to order 306 at its real roots; (3) runs to orders 602 (Q7, roots 2..10) and 600 (Q8,
# roots 1..10) to test the stability of the apparent growth constants.  Amplitudes are powers of two (exact rescaling).
# Everything after (1) is NUMERICAL EVIDENCE only.
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
L=run_after_queue12.log
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> $L
  timeout 3000 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> $L
}
echo "start tq_cert 9 $(date -u +%H:%M:%SZ)" >> $L
timeout 9000 nice -n 19 python3 tq_cert.py 9 > tq_cert_Q9.log 2>&1
echo "end tq_cert 9 rc=$? $(date -u +%H:%M:%SZ)" >> $L
n=$(grep -cE "^  \[" tq_cert_Q9.log)
for i in $(seq 1 $n); do
  e=1/2; [ $i -eq 1 ] && e=1/16
  b=$(grep -E "^  \[" tq_cert_Q9.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q9h1_root${i}_N306_f64.out 9 1 1:1,3:$b 306 $e
done
E7=(1/16 1/2 1 1 1 1 1 1/2 1/4 1/8)
E8=(1/16 1/2 1 1 1 1 1/2 1/2 1/4 1/8)
for i in 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q7h1_root${i}_N602_f64.out 7 1 1:1,3:$b 602 ${E7[$((i-1))]}
done
for i in 1 2 3 4 5 6 7 8 9 10; do
  b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n ${i}p); run hhf_Q8h1_root${i}_N600_f64.out 8 1 1:1,3:$b 600 ${E8[$((i-1))]}
done
echo "queue12 done $(date -u +%H:%M:%SZ)" >> $L
