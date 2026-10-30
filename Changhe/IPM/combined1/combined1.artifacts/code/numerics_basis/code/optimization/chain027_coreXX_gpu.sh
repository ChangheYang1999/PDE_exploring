#!/bin/bash
# core $1 + GPU 7: C1-N1-027 = CONTROL for 026: 022 continued 60 steps with the plain 67 rows (no held-in rows). Held-out file heldout/HELDOUT_027.md sha256 c99eb804dc6c390c4db9d9cfb7a5231a9b982a93f1c1b2b501e9b20af4829d7e.
CORE=$1
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda IPM_THREADS=1 OMP_NUM_THREADS=1 IPM_STEPNORM=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=legqs25_m16to23_cont60_gpu_m16
taskset -c $CORE nice -n 19 $PY -B run_quot.py candD2/legqs25_m16to23_gpu_m16_exact.json 180 60 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520 penalty > logs/$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c $CORE nice -n 19 $PY -B weak_tests3.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests3.json 32 > logs/weaktests3_$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c $CORE nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c $CORE nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
