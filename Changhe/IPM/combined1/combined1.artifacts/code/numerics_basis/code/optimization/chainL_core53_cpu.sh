#!/bin/bash
# core 53: extended weak tests (k to 4096) for 008, 009, 010 (v06 table)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for T in d2w_j7_n4_X3bal_mid180 d2w_j7_n4_X3balK_mid180 d2w_j7_n4_X3bal_legqs_mid180; do
  taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests2.json 32 > logs/weaktests2_${T}.out 2>&1
done
echo CHAIN_DONE >> logs/weaktests2_d2w_j7_n4_X3bal_legqs_mid180.out
