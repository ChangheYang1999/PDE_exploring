#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
OMP_NUM_THREADS=1 nice -n 10 $P code/hminus1_diag.py data/state088_exact.json data/hminus1_diag_088.json -7 9 0.05 64 2 1 2 > runs/hminus1_c1_2.log 2>&1
for c in "10 20" "50 100" "100 200"; do set -- $c; OMP_NUM_THREADS=1 nice -n 10 $P code/hminus1_diag.py data/state088_exact.json data/hminus1_diag_088_c$1_$2.json -7 9 0.05 64 2 $1 $2 > runs/hminus1_c$1_$2.log 2>&1; cp data/hminus1_diag_088_Fgrid.npz data/hminus1_diag_088_c$1_$2_Fgrid.npz 2>/dev/null; done
