#!/bin/bash
# core 53 + GPU 7: C1-N1-021 = 020 basis (016 basis + 252 legqs R0 = 50; scales 25 and 50; 2426 generators), objective = balanced E_2 + 1e12 I^2 over 81 rows:
# the 67 rows of 016..020 (27 first-mode k, N4-160 angular probes n <= 17) PLUS 14 HELD-IN mid-field rows: N4-160 probes n = 19..31 odd at K = (n-1)/2 + 128 and + 512.
# HELD-OUT (fixed before the run, never rows): the 25 registered probes n in {19,23,25,29,31} x K in {600,900,1200,1800,2400} and the N4-160 probes n >= 19 at K0 in {0, 8, 32}.
# 40 GN steps, MID 16; then weak_tests2/3 (CPU) and diag2 (GPU) at MID 32.
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=legqs25p50_heldin14_gpu_m16
taskset -c 53 nice -n 19 $PY -B run_quot.py candD2/quot013_legqs25p50_m9to15_cpu_m16_exact.json 180 40 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520,19:137,21:138,23:139,25:140,27:141,29:142,31:143,19:521,21:522,23:523,25:524,27:525,29:526,31:527 penalty > logs/$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c 53 nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c 53 nice -n 19 $PY -B weak_tests3.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests3.json 32 > logs/weaktests3_$TAG.out 2>&1
taskset -c 53 nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
