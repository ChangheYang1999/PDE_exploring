#!/bin/bash
# core 53: scale comparison with 016: same start (013 quotient), same 67 rows, legqs functions at R0 = 50 instead of 25 (blocks j = 1..3, m = 9..15, 12 per block), MID 16, 12 steps -> C1-N1-017; then weak_tests2/3 + diag2
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1 IPM_ADD_LEGQS=1,2,3:9:15:50:12
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=quot013_legqs50_m9to15_cpu_m16
taskset -c 53 nice -n 19 $PY -B run_quot.py candD2/d2w_j7_n4_E2bal_pairU_cpu_m16_quot_exact.json 180 12 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520 penalty > logs/$TAG.out 2>&1
taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c 53 nice -n 19 $PY -B weak_tests3.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests3.json 32 > logs/weaktests3_$TAG.out 2>&1
taskset -c 53 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
