#!/bin/bash
# after e2_j7_fromFrF: diagnostics (theory_v01 quantities) of its exact JSON, then the X3-objective (no H) variant from its coefficients
export PYTHONDONTWRITEBYTECODE=1
while kill -0 3132078 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_exact.json 200 1e4 RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_e2_j7.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_e2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_coefs.npy 7 4 0,1,2 200 60 x3_j7_n4_d012_mid200_fromE2 262144 16384 1 0 16 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/x3_j7_fromE2.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/x3_j7_fromE2.out
