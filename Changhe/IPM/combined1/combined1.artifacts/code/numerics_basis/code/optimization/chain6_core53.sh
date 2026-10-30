#!/bin/bash
# after chain4: balanced objective from the d2 warm-start result: X3 proxy + near-field log-measure term (2^18 * 10^2) + kappa penalty (weight 1e6 -> kappa^2 term comparable to X3^2 when kappa ~ 1)
export PYTHONDONTWRITEBYTECODE=1
while kill -0 3549334 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 60 d2w_j7_n4_X3bal_mid180 0 16 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_coefs.npy 0 0 none 12 26214400 1000000 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3bal.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_mid180_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_mid180_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_X3bal.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_X3bal.out
