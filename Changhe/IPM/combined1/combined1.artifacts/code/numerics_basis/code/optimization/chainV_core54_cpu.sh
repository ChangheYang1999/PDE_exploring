#!/bin/bash
# core 54 after chainU: exact quotient bases of 007 and 013, then gn_spectrum on the 007 quotient (physical spectrum, no zero-potential directions)
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 3402544 2>/dev/null; do sleep 10; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
taskset -c 54 nice -n 19 $PY -B quotient_basis.py candD2/d2w_j7_n4_E2bal_mid180_exact.json candD2/d2w_j7_n4_E2bal_mid180_quot_exact.json > logs/quotient_007.out 2>&1
taskset -c 54 nice -n 19 $PY -B quotient_basis.py candD2/d2w_j7_n4_E2bal_pairU_cpu_m16_exact.json candD2/d2w_j7_n4_E2bal_pairU_cpu_m16_quot_exact.json > logs/quotient_013.out 2>&1
taskset -c 54 nice -n 19 $PY -B gn_spectrum.py candD2/d2w_j7_n4_E2bal_mid180_quot_exact.json 180 16 candD2/007_quot_gn_spectrum.json > logs/gn_spectrum_007_quot.out 2>&1
echo CHAIN_DONE >> logs/gn_spectrum_007_quot.out
