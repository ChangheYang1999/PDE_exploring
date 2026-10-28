#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
echo "wscan chain start $(date -u +%FT%TZ)" >> runs/wscan_chain.log
OMP_NUM_THREADS=1 nice -n 5 $P code/w_scan.py data/nb_d2_exact.json data/w_scan_d2.json 128 0.001 1024 12 > runs/w_scan_d2.log 2>&1
echo "d2 done $(date -u +%FT%TZ)" >> runs/wscan_chain.log
OMP_NUM_THREADS=1 nice -n 5 $P code/w_scan.py data/state131_T1_exact.json data/w_scan_131.json 128 0.001 1024 12 > runs/w_scan_131.log 2>&1
echo "131 done $(date -u +%FT%TZ)" >> runs/wscan_chain.log
OMP_NUM_THREADS=1 nice -n 5 $P code/w_scan.py data/nb_Mpen2_exact.json data/w_scan_Mpen2.json 128 0.001 1024 12 > runs/w_scan_Mpen2.log 2>&1
echo "Mpen2 done $(date -u +%FT%TZ)" >> runs/wscan_chain.log
