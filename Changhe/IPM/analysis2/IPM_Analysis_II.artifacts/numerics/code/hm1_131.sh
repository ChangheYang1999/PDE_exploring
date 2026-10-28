#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
for c in "50 100" "10 20" "100 200" "1 2"; do set -- $c; OMP_NUM_THREADS=1 nice -n 5 $P code/hminus1_diag.py data/state131_exact.json data/hminus1_diag_131_c$1_$2.json -7 9 0.05 64 2 $1 $2 > runs/hminus1_131_c$1_$2.log 2>&1; cp data/hminus1_diag_131_c$1_$2_Fgrid.npz data/hminus1_diag_131_Fgrid_shared.npz 2>/dev/null; done
