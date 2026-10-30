#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1
while kill -0 26618 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
CUDA_VISIBLE_DEVICES=7 OMP_NUM_THREADS=1 taskset -c 54 nice -n 19 python3 -B RUN_ROOT/numerics_N1N2/numerics/optimization/diag2.py RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_legqs_mid180_exact.json 180 8356.474846731926 RUN_ROOT/numerics_N1N2/numerics/optimization/candD2/d2w_j7_n4_X3bal_legqs_mid180_diag2.json 32 > RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_X3bal_legqs_mid180.out 2>&1
echo CHAIN_DONE >> RUN_ROOT/numerics_N1N2/numerics/optimization/logs/diag2_d2w_j7_n4_X3bal_legqs_mid180.out
