#!/bin/bash
# after run_after_queue7.sh (PID 3565662): the largest roots overflow float64 at unit amplitude (Q7 root 1 at order 293),
# so rerun them at amplitude 1/16 (the program rescales to unit amplitude); then the fourth single-harmonic center
# sin(17 theta) at delta = 6/13 (h = 3). NUMERICAL EVIDENCE only (apparent radii).
while kill -0 3565662 2>/dev/null; do sleep 30; done
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> run_after_queue8.log
  timeout 5400 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue8.log
}
b=$(grep -E "^  \[" tq_cert_Q7.log | awk '{print $NF}' | sed -n 1p); run hhf_Q7h1_root1_N301_f64e16.out 7 1 1:1,3:$b 301 1/16
b=$(grep -E "^  \[" tq_cert_Q8.log | awk '{print $NF}' | sed -n 1p); run hhf_Q8h1_root1_N304_f64e16.out 8 1 1:1,3:$b 304 1/16
run hhf_Q13h3_sin17_N299_f64.out 13 3 17 299 1
echo "queue8 done $(date -u +%H:%M:%SZ)" >> run_after_queue8.log
