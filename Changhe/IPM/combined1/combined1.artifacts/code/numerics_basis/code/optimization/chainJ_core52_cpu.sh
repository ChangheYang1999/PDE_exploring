#!/bin/bash
# wait for diag2 (PID 1591540) then run the extended weak tests on d2w_j7_n4_E2bal_legqs_cpu_m8 (core 52)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 1591540 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
taskset -c 52 nice -n 19 python3 -B weak_tests2.py candD2/d2w_j7_n4_E2bal_legqs_cpu_m8_exact.json 180 8356.474846731926 candD2/d2w_j7_n4_E2bal_legqs_cpu_m8_weaktests2.json 32 > logs/weaktests2_d2w_j7_n4_E2bal_legqs_cpu_m8.out 2>&1
echo CHAIN_DONE >> logs/weaktests2_d2w_j7_n4_E2bal_legqs_cpu_m8.out
