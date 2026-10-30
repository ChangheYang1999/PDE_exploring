#!/bin/bash
# after chain4: continue the d2 warm start (X3 objective) from its coefficients for 60 more steps, then diag2
export PYTHONDONTWRITEBYTECODE=1
while kill -0 3549334 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 60 d2w_j7_n4_X3_mid180_c2 0 16 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_coefs.npy > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3_c2.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_c2_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_c2_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_X3_c2.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_X3_c2.out
