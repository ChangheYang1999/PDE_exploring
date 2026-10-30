#!/bin/bash
# core 54 + GPU 7: C1-N1-022 = 016 basis (2174 generators) + legqs R0 = 25 (Q = 4, 12 functions per block) in the EXISTING higher blocks j = 1 (m = 16..19), j = 2, 3 (m = 16..23):
# 20 blocks x 12 = 240 functions, zero start -> 2414 generators (density modes 31 to 47). Same 67 rows as 016 (27 first-mode k, N4-160 probes n <= 17), same HELD-OUT set as 016
# (N4-160 probes n = 19..31 at K0 in {0,8,32,128,512} and the 25 registered probes); 12 GN steps (controlled comparison with 016) then 28 more (40 total); MID 16.
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda IPM_THREADS=1 OMP_NUM_THREADS=1
export IPM_ADD_LEGQS="1,2,3:16:23:25:12"
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=legqs25_m16to23_gpu_m16
taskset -c 54 nice -n 19 $PY -B run_quot.py candD2/quot013_legqs25_m9to15_cpu_m16_exact.json 180 12 ${TAG}_s12 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520 penalty > logs/${TAG}_s12.out 2>&1
unset IPM_ADD_LEGQS
taskset -c 54 nice -n 19 $PY -B run_quot.py candD2/${TAG}_s12_exact.json 180 28 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520 penalty > logs/$TAG.out 2>&1
for T in ${TAG}_s12 $TAG; do
IPM_DEVICE=cpu taskset -c 54 nice -n 19 $PY -B weak_tests3.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests3.json 32 > logs/weaktests3_$T.out 2>&1
done
IPM_DEVICE=cpu taskset -c 54 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c 54 nice -n 19 $PY -B diag2.py candD2/${TAG}_s12_exact.json 180 8356.474846731926 candD2/${TAG}_s12_diag2.json 32 > logs/diag2_${TAG}_s12.out 2>&1
taskset -c 54 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
