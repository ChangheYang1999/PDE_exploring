#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 1257813 2>/dev/null; do sleep 20; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/weak_tests.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_mid180_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_mid180_weaktests.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/weaktests_d2w_j7_n4_X3bal_mid180.out 2>&1
taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/weak_tests.py external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json 160 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/C1-A2-d2_weaktests.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/weaktests_d2.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/weaktests_d2.out
