#!/bin/bash
# floating sections (lead notes 15-19): L_red in the jet realization (FSEC, 2 workers) and the core S_1 on L^2(w_a) (S1 test then production)
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
PY=python3
L=numerics/logs
cd numerics/artifacts/code
date -u; echo "== FSEC production (L_red, Mh 4 stride 60, NMAX 19, 2 workers)"
$PY -u fsec.py FSEC 4 60 2 256 19 > $L/fsec_prod.log 2>&1
echo "fsec exit $?"; date -u
$PY -u fsec_assemble.py runs/FSEC > $L/fsec_prod_assemble.log 2>&1
date -u; echo "== S1 production (S_1 on R, Mh 4 stride 60, NMAX 19, 2 workers)"
FSEC_MODE=S1 $PY -u fsec.py S1 4 60 2 256 19 > $L/s1_prod.log 2>&1
echo "s1 exit $?"; date -u
$PY -u fsec_assemble.py runs/S1 > $L/s1_prod_assemble.log 2>&1
date -u; echo DONE
