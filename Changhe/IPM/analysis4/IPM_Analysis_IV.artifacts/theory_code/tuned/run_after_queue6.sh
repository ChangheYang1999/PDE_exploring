#!/bin/bash
# waits for run_after_queue4.sh (PID 3324151); then floating tuned continuations of the three certified single
# harmonics (float64 and long double, for an error estimate), then the exact polar probe of sin(9 theta) at delta = 4/7;
# first the all-k response bounds and Section 12.5 box radii at delta = 2/7 and 1/4
while kill -0 3324151 2>/dev/null; do sleep 30; done
cd "$(dirname "$0")"
export OMP_NUM_THREADS=1
run() {
  echo "start $* $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
  timeout 5400 nice -n 19 python3 hh_float.py "${@:2}" > "$1" 2>&1
  echo "end $1 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
}
for QQ in 7 8; do
  echo "start tq_bounds_radius $QQ $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
  timeout 3600 nice -n 19 python3 tq_bounds_radius.py $QQ > tq_bounds_radius_Q$QQ.out 2>&1
  echo "end tq_bounds_radius $QQ rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
done
run hhf_Q5h2_sin7_N300_f64.out 5 2 7 300 2
run hhf_Q7h2_sin9_N301_f64.out 7 2 9 301 1/2
run hhf_Q9h2_sin11_N306_f64.out 9 2 11 306 1/2
run hhf_Q5h2_sin7_N300_ld.out 5 2 7 300 2 longdouble
run hhf_Q7h2_sin9_N301_ld.out 7 2 9 301 1/2 longdouble
run hhf_Q9h2_sin11_N306_ld.out 9 2 11 306 1/2 longdouble
echo "start hh_tune 7 2 9 4 $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
timeout 7200 nice -n 19 python3 hh_tune.py 7 2 9 4 > hh_tune_Q7h2_sin9.out 2>&1
echo "end hh_tune 7 2 9 4 rc=$? $(date -u +%H:%M:%SZ)" >> run_after_queue6.log
