#!/bin/bash
# core 53 after chainL: high-k weak probes (k = 6144 .. 65536) for 007, 008, 009, 010, 012, 011 (v06 table; where is the max of m_k)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 1764480 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for T in d2w_j7_n4_E2bal_mid180 d2w_j7_n4_X3bal_mid180 d2w_j7_n4_X3balK_mid180 d2w_j7_n4_X3bal_legqs_mid180 d2w_j7_n4_E2balK_cpu_m8 d2w_j7_n4_E2bal_legqs_cpu_m8; do
  taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests2_highk.json 32 6144,8192,12288,16384,24576,32768,49152,65536 > logs/weaktests2_highk_${T}.out 2>&1
done
echo CHAIN_DONE >> logs/weaktests2_highk_d2w_j7_n4_E2bal_legqs_cpu_m8.out
