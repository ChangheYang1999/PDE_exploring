#!/bin/bash
# core 53 after chainM: bridge probes k = 1e5 .. 1e7 for 007 (mesh to r = 8356 covers r_peak up to 2600) to meet the exact far-field regime of far_weak.py
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 1824721 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 180 8356.474846731926 candD2/d2w_j7_n4_E2bal_mid180_weaktests2_bridge.json 32 100000,200000,500000,1000000,2000000,3162278,5000000,10000000 > logs/weaktests2_bridge_007.out 2>&1
echo CHAIN_DONE >> logs/weaktests2_bridge_007.out
