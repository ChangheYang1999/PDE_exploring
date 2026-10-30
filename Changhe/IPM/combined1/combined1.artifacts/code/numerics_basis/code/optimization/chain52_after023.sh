#!/bin/bash
# core 52 after the 023 snapshot: NC-T-ORIGIN-INV seven-cell FLOAT proxies (modes 1 + 3; theory_v06 request 5) for C1-N1-011 .. 021 (MID 32), then the mode 33..47 sweep for 023.
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for S in d2w_j7_n4_E2bal_legqs_cpu_m8 d2w_j7_n4_E2balK_cpu_m8 d2w_j7_n4_E2bal_pairU_cpu_m16 d2w_j7_n4_E2bal_pairB_cpu_m16 quot013_pairQ_cpu_m16 quot013_legqs25_m9to15_cpu_m16 quot013_legqs50_m9to15_cpu_m16 quot013_legqs25_cont12_cpu_m16 quot013_legqs50_cont12_cpu_m16 quot013_legqs25p50_m9to15_cpu_m16 legqs25p50_heldin14_gpu_m16; do
  [ -f candD2/${S}_na_cells.json ] || taskset -c 52 nice -n 19 $PY -B na_modes_cells.py candD2/${S}_exact.json 180 8356.474846731926 candD2/${S}_na_cells.json 32 > logs/na_cells_${S}.out 2>&1
done
echo NA_CELLS_DONE >> logs/na_cells_legqs25p50_heldin14_gpu_m16.out
T=legqs25p100_m9to15_gpu_m16
IPM_NMAX=47 taskset -c 52 nice -n 19 $PY -B weak_tests3.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests3c_n47.json 32 > logs/weaktests3c_n47_$T.out 2>&1
echo N47_DONE >> logs/weaktests3c_n47_$T.out
