#!/bin/bash
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 1624573 2>/dev/null; do sleep 5; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
taskset -c 54 nice -n 19 python3 -B test_pair2.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 1e13 > logs/test_pair2.out 2>&1
echo CHAIN_DONE >> logs/test_pair2.out
