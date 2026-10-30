#!/bin/bash
# core $1 + GPU 7: C1-N1-025 = COMBINED run: start = 016's exact JSON (2174 generators) + legqs R0 = 50 and R0 = 100 in j = 1..3, m = 9..15 (252 + 252) + legqs R0 = 25 in the
# existing higher blocks j = 1 (m = 16..19), j = 2, 3 (m = 16..23) (240) -> 2918 generators. Objective = balanced E_2 + 1e12 I^2 over the 81 rows of 021 (67 + 14 HELD-IN
# mid-field rows n = 19..31 at K0 = 128, 512, these 14 rows with weight 1e16 instead of 1e12: at 1e12 the 021 rows (I about 5e-6) cost 25 each against an objective of 1.3e7 and were inert). HELD-OUT (as 021): the 25 registered probes n in {19,23,25,29,31} x K in {600,900,1200,1800,2400} and the N4-160 probes n >= 19 at
# K0 in {0, 8, 32}. 60 GN steps, MID 16; then weak_tests2/3 (CPU) and diag2 (GPU) at MID 32.
CORE=$1
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES=7 IPM_DEVICE=cuda IPM_THREADS=1 OMP_NUM_THREADS=1 IPM_STEPNORM=1 IPM_NHELDIN=14 IPM_WPAIR_HELDIN=1e16
export IPM_ADD_LEGQS="1,2,3:9:15:50:12;1,2,3:9:15:100:12;1,2,3:16:23:25:12"
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
TAG=combined_s25s50s100_m16to23_heldin14_gpu_m16
taskset -c $CORE nice -n 19 $PY -B run_quot.py candD2/quot013_legqs25_m9to15_cpu_m16_exact.json 180 60 $TAG 0.952380952380952 16 26214400 3000000 1e12 0,1,2,3,4,5,6,7,8,12,16,24,32,48,64,96,128,192,256,384,512,768,1024,1536,2048,3072,4096,3:1,3:9,3:33,3:129,3:513,5:2,5:10,5:34,5:130,5:514,7:3,7:11,7:35,7:131,7:515,9:4,9:12,9:36,9:132,9:516,11:5,11:13,11:37,11:133,11:517,13:6,13:14,13:38,13:134,13:518,15:7,15:15,15:39,15:135,15:519,17:8,17:16,17:40,17:136,17:520,19:137,21:138,23:139,25:140,27:141,29:142,31:143,19:521,21:522,23:523,25:524,27:525,29:526,31:527 penalty > logs/$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c $CORE nice -n 19 $PY -B weak_tests3.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests3.json 32 > logs/weaktests3_$TAG.out 2>&1
IPM_DEVICE=cpu taskset -c $CORE nice -n 19 $PY -B weak_tests2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_weaktests2.json 32 > logs/weaktests2_$TAG.out 2>&1
taskset -c $CORE nice -n 19 $PY -B diag2.py candD2/${TAG}_exact.json 180 8356.474846731926 candD2/${TAG}_diag2.json 32 > logs/diag2_$TAG.out 2>&1
echo CHAIN_DONE >> logs/diag2_$TAG.out
