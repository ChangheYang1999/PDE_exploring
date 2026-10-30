#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
taskset -c 54 nice -n 19 $PY -B weak_tests2.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 180 8356.474846731926 candD2/d2w_j7_n4_E2bal_mid180_weaktests2.json 32 > logs/weaktests2_007.out 2>&1
taskset -c 54 nice -n 19 $PY -B test_pair.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 60 4 1e13 > logs/test_pair.out 2>&1
echo CHAIN_DONE >> logs/test_pair.out
