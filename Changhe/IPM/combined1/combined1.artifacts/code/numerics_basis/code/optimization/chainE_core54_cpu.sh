#!/bin/bash
# CPU continuation of the E2-balanced run from C1-N1-007 (reduced radial mesh: middle order 8), 30 steps, then CPU diag2
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 30 d2w_j7_n4_E2bal_cpu_m8 0.952380952380952 8 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_mid180_coefs.npy 0 0 none 12 26214400 3000000 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_n4_E2bal_cpu_m8.out 2>&1
taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_cpu_m8_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_cpu_m8_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_E2bal_cpu_m8.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_E2bal_cpu_m8.out
