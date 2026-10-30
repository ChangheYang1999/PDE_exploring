#!/bin/bash
# core 52 after chainW (015 diagnostics): weak_tests3 baselines with the theory_v04 held-out set for 007, 013, 014 (same FLOAT rule as 015/016/017)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 4123699 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for T in d2w_j7_n4_E2bal_mid180 d2w_j7_n4_E2bal_pairU_cpu_m16 d2w_j7_n4_E2bal_pairB_cpu_m16; do
  taskset -c 52 nice -n 19 $PY -B weak_tests3.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests3b.json 32 > logs/weaktests3b_${T}.out 2>&1
done
echo CHAIN_DONE >> logs/weaktests3b_d2w_j7_n4_E2bal_pairB_cpu_m16.out
