#!/bin/bash
# CPU core 54: weak-pairing rows (ipm_opt3, PENALTY mode, uniform weight 1e15) from C1-N1-007, balanced E2 objective as 007, 27 k values, MID 16, 12 steps; then weak_tests2 + diag2
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1

cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=d2w_j7_n4_E2bal_pairU_cpu_m16
taskset -c 54 nice -n 19 $PY -B run_pair.py 7 4 180 12 $TAG 0.952380952380952 16 candD2/d2w_j7_n4_E2bal_mid180_coefs.npy 0 0 none 12 26214400 3000000 1e15 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096 none penalty > logs/$TAG.out 2>&1
taskset -c 54 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c 54 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
