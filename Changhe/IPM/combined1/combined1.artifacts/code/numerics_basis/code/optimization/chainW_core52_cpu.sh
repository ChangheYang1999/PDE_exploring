#!/bin/bash
# core 52 after chainR2 (014) and chainV (quotient bases): pairing run on the EXACT QUOTIENT basis of 013 (1922 generators, no zero-potential directions), 102 rows (27 first-mode + 75 angular), weight 1e12, MID 16, 12 steps -> C1-N1-015; then weak_tests2/3 + diag2
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 2869128 2>/dev/null || kill -0 3713285 2>/dev/null; do sleep 15; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
Q=candD2/d2w_j7_n4_E2bal_pairU_cpu_m16_quot_exact.json
if [ ! -f $Q ]; then echo "quotient JSON missing" > logs/chainW.err; exit 1; fi
TAG=quot013_pairQ_cpu_m16
taskset -c 52 nice -n 19 $PY -B run_quot.py $Q 180 12 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520,19:9,19:17,19:41,19:137,19:521,21:10,21:18,21:42,21:138,21:522,23:11,23:19,23:43,23:139,23:523,25:12,25:20,25:44,25:140,25:524,27:13,27:21,27:45,27:141,27:525,29:14,29:22,29:46,29:142,29:526,31:15,31:23,31:47,31:143,31:527 penalty > logs/$TAG.out 2>&1
taskset -c 52 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c 52 nice -n 19 $PY -B weak_tests3.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests3.json 32 > logs/weaktests3_$TAG.out 2>&1
taskset -c 52 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
