#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1
while kill -0 3234260 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
R=8356.474846731926
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/hminus1_check.py external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json 160 $R > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/hminus1_d2_v4.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_exact.json 180 $R RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3_mid180_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_X3.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_exact.json 200 $R RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_e2_j7.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 53 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json 160 $R RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/C1-A2-d2_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2.out
