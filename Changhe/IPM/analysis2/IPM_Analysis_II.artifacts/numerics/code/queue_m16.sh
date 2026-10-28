#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
echo "launching m16 at $(date -u +%FT%TZ)" >> runs/queue_m16.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m16 120 48 0.3 1:19:B8+26,1:19:X8+8 60 1e3 0.3 $PWD/data/n12_m10_result.json > runs/n12_m16.log 2>&1
echo "m16 finished at $(date -u +%FT%TZ)" >> runs/queue_m16.log
echo "launching m14 at $(date -u +%FT%TZ)" >> runs/queue_m14.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m14 120 24 0.3 1:19:B8+26,2:29:B4+14,3:39:B4+14 80 1e3 0.3 $PWD/data/n12_m10_result.json > runs/n12_m14.log 2>&1
echo "m14 finished at $(date -u +%FT%TZ)" >> runs/queue_m14.log
