#!/bin/bash
# sequential FLOAT diagnostics for an exact n12 file: M scan (128 angles), Hdot^-1 low component, lead-weight norms (240 x 128). usage: diag_chain.sh NAME
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"; N=$1
echo "diag chain $N start $(date -u +%FT%TZ)" >> runs/diag_chain.log
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_Mscan.py data/${N}_exact.json data/${N}_Mscan.json 128 0.001 1024 12 > runs/${N}_Mscan.log 2>&1
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_hminus1.py data/${N}_exact.json data/${N}_hm1.json 300 128 1e-3 1e4 0.02 3 > runs/${N}_hm1.log 2>&1
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_norms.py data/${N}_exact.json -6.9 9.21 240 128 L,0.3 data/${N}_exact_lead.json > runs/${N}_norms.log 2>&1
echo "diag chain $N done $(date -u +%FT%TZ)" >> runs/diag_chain.log
