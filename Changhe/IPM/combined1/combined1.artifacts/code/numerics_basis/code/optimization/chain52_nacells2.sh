#!/bin/bash
# core 52: NC-T-ORIGIN-INV seven-cell FLOAT proxies for 022, 023, 024, 025 (theory_v07 request 6 extends the list to 022).
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
for S in legqs25_m16to23_gpu_m16 legqs25p100_m9to15_gpu_m16 quot013_legqs25_m9to15_gpu_m32 combined_s25s50s100_m16to23_heldin14_gpu_m16; do
  [ -f candD2/${S}_na_cells.json ] || taskset -c 52 nice -n 19 $PY -B na_modes_cells.py candD2/${S}_exact.json 180 8356.474846731926 candD2/${S}_na_cells.json 32 > logs/na_cells_${S}.out 2>&1
done
echo NA_CELLS2_DONE >> logs/na_cells_combined_s25s50s100_m16to23_heldin14_gpu_m16.out
