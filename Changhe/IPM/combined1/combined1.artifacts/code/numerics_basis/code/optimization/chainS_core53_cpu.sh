#!/bin/bash
# core 53 after chainM2: weak_tests3 (angular probes) for 007 (baseline held-out tests), then bridge probes for 008 and 009
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 2619087 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
taskset -c 53 nice -n 19 $PY -B weak_tests3.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 180 8356.474846731926 candD2/d2w_j7_n4_E2bal_mid180_weaktests3.json 32 > logs/weaktests3_007.out 2>&1
for T in d2w_j7_n4_X3bal_mid180 d2w_j7_n4_X3balK_mid180; do
  taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests2_bridge.json 32 100000,200000,500000,1000000,2000000,3162278,5000000,10000000 > logs/weaktests2_bridge_${T}.out 2>&1
done
echo CHAIN_DONE >> logs/weaktests2_bridge_d2w_j7_n4_X3balK_mid180.out
