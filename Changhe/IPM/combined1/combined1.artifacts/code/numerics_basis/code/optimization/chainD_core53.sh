#!/bin/bash
# after chainA: E2-balanced objective (hw = 20/21) with legqs multi-scale inner functions (R0 10, 100; 12 per block) from C1-N1-007 coefficients (zero-padded), then diag2
export PYTHONDONTWRITEBYTECODE=1
while kill -0 105368 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 60 d2w_j7_n4_E2bal_legqs_mid180 0.952380952380952 16 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_mid180_coefs.npy 0 0 10,100 12 26214400 1000000 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_n4_E2bal_legqs_mid180.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_legqs_mid180_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_E2bal_legqs_mid180_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_E2bal_legqs_mid180.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_E2bal_legqs_mid180.out
