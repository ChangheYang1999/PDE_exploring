#!/bin/bash
# core 52: controlled comparison: 007 basis/objective with the q = 1 descendant of branch 3 zeroed exactly as well (first survivor becomes the invariant (8,0)); MID 16, 12 steps from 007; then weak_tests2 + diag2
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1 IPM_DESC_ZERO=0,1,2,3
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=d2w_j7_n4_E2bal_desc3_cpu_m16
taskset -c 52 nice -n 19 $PY -B run_pair.py 7 4 180 12 $TAG 0.952380952380952 16 candD2/d2w_j7_n4_E2bal_mid180_coefs.npy 0 0 none 12 26214400 3000000 0 0 none penalty > logs/$TAG.out 2>&1
taskset -c 52 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c 52 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
