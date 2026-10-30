#!/bin/bash
# after e2_j7_fromFrF: diag2 of its exact JSON, then the d2 warm start with moment homotopy and multi-scale switch-on (X3 objective)
export PYTHONDONTWRITEBYTECODE=1
while kill -0 3132078 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_exact.json 200 1e4 RUN_ROOT/numerics_N1N2/numerics/optimization/candE2/e2_j7_n4_d012_mid200_fromFrF_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_e2_j7.out 2>&1
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/run_from_d2.py 7 4 180 60 d2w_j7_n4_X3_hom4_ms 0 16 none 4 0,16,48 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3_hom4_ms.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/d2w_j7_X3_hom4_ms.out
