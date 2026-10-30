#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
for T in d2w_j7_n4_E2bal_mid180 d2w_j7_n4_X3balK_mid180 d2w_j7_n4_X3bal_legqs_mid180; do
  taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/weak_tests.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/${T}_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/${T}_weaktests.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/weaktests_${T}.out 2>&1
done
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/weaktests_d2w_j7_n4_X3bal_legqs_mid180.out
