#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 52 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/hminus1_check.py external/ipm_source/analysis2/IPM_Analysis_II.artifacts/certificates/numerics_data/nb_d2_exact.json 160 8356.474846731926 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/hminus1_d2_v3.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 52 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 60 d2w_j7_n4_X3_hom4_ms_legqs 0 16 none 4 0,16,48 10,100 12 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3_hom4_ms_legqs.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3_hom4_ms_legqs.out
