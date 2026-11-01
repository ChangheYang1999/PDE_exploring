#!/bin/bash
# replaces the remainder of run_after_queue6.sh (stopped after its tq_bounds_radius 7 step); waits for the running
# tq_bounds_radius 8 (timeout PID 3370553); then floating tuned continuations (NUMERICAL EVIDENCE: apparent radii):
# the ten two-mode roots at delta = 2/7 and at delta = 1/4 (h = 1), the three certified single harmonics (h = 2),
# then long double reruns for the error estimate (hardest two-mode roots, single harmonics at about half length)
while kill -0 3370553 2>/dev/null; do sleep 30; done
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
echo "end tq_bounds_radius 8 (observed by queue7) $(date -u +%H:%M:%SZ)" >> run_after_queue7.log
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> run_after_queue7.log
  timeout 5400 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue7.log
}
i=0
for b in $(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | head -10); do
  i=$((i+1)); run hhf_Q7h1_root${i}_N301_f64.out 7 1 1:1,3:$b 301 1
done
i=0
for b in $(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | head -10); do
  i=$((i+1)); run hhf_Q8h1_root${i}_N304_f64.out 8 1 1:1,3:$b 304 1
done
run hhf_Q5h2_sin7_N300_f64.out 5 2 7 300 2
run hhf_Q7h2_sin9_N301_f64.out 7 2 9 301 1/2
run hhf_Q9h2_sin11_N306_f64.out 9 2 11 306 1/2
b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n 3p); run hhf_Q7h1_root3_N301_ld.out 7 1 1:1,3:$b 301 1 longdouble
b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n 3p); run hhf_Q8h1_root3_N304_ld.out 8 1 1:1,3:$b 304 1 longdouble
run hhf_Q5h2_sin7_N150_ld.out 5 2 7 150 2 longdouble
run hhf_Q7h2_sin9_N154_ld.out 7 2 9 154 1/2 longdouble
run hhf_Q9h2_sin11_N153_ld.out 9 2 11 153 1/2 longdouble
echo "queue7 done $(date -u +%H:%M:%SZ)" >> run_after_queue7.log
