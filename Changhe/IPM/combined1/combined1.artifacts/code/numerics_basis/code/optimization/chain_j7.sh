#!/bin/bash
# wait for the j7 optimization, then exact finalization and FLOAT diagnostics
export PYTHONDONTWRITEBYTECODE=1
while kill -0 2913876 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 52 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/finalize_from_npy.py RUN_ROOT/numerics_N1N2/numerics/optimization/candB/candB_j7_n4_d012_FrF_R10000_mid200_coefs.npy 7 4 0,1,2 candB_j7_n4_d012_FrF_R1e4_mid200 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/finalize_j7.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 52 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/candidate_diag.py RUN_ROOT/numerics_N1N2/numerics/optimization/candB/candB_j7_n4_d012_FrF_R1e4_mid200_exact.json 200 mid 1e4 RUN_ROOT/numerics_N1N2/numerics/optimization/candB/candB_j7_n4_d012_FrF_R1e4_mid200_diag_mid200.json > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag_j7_mid200.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag_j7_mid200.out
