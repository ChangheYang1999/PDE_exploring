#!/bin/bash
# core 52: bridge probes (k = 1e5 .. 1e7) for 008 and 009 (far-field contrast with 007)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for T in d2w_j7_n4_X3bal_mid180 d2w_j7_n4_X3balK_mid180; do
  taskset -c 52 nice -n 19 $PY -B weak_tests2.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests2_bridge.json 32 100000,200000,500000,1000000,2000000,3162278,5000000,10000000 > logs/weaktests2_bridge_${T}.out 2>&1
done
echo CHAIN_DONE >> logs/weaktests2_bridge_d2w_j7_n4_X3balK_mid180.out
