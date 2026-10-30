#!/bin/bash
# core 54 after the 013 diag2: held-out angular probes (weak_tests3) on 013, then the Newton-step diagnostic on 007 and 013, then na_modes_cells for 008, 009, 010
export PYTHONDONTWRITEBYTECODE=1 CUDA_VISIBLE_DEVICES= IPM_DEVICE=cpu IPM_THREADS=1 OMP_NUM_THREADS=1
while kill -0 3049364
3064521
3064823
3064825 2>/dev/null; do sleep 5; done
cd RUN_ROOT/numerics_N1N2/numerics/optimization
PY=python3
T=d2w_j7_n4_E2bal_pairU_cpu_m16
taskset -c 54 nice -n 19 $PY -B weak_tests3.py candD2/${T}_exact.json 180 8356.474846731926 candD2/${T}_weaktests3.json 32 > logs/weaktests3_$T.out 2>&1
echo WT3_DONE >> logs/weaktests3_$T.out
taskset -c 54 nice -n 19 $PY -B newton_step.py candD2/d2w_j7_n4_E2bal_mid180_exact.json 180 24 candD2/007_newton_step.json > logs/newton_step_007.out 2>&1
taskset -c 54 nice -n 19 $PY -B newton_step.py candD2/${T}_exact.json 180 24 candD2/013_newton_step.json > logs/newton_step_013.out 2>&1
for S in d2w_j7_n4_X3bal_mid180 d2w_j7_n4_X3balK_mid180 d2w_j7_n4_X3bal_legqs_mid180; do
  taskset -c 54 nice -n 19 $PY -B na_modes_cells.py candD2/${S}_exact.json 180 8356.474846731926 candD2/${S}_na_cells.json 32 > logs/na_cells_${S}.out 2>&1
done
echo CHAIN_DONE >> logs/na_cells_d2w_j7_n4_X3bal_legqs_mid180.out
