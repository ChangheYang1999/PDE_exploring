#!/bin/bash
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while [ ! -f runs/routeU_norms.done ]; do sleep 15; done
while [ $(pgrep -fc "python3 .*code/(n12_run|n12_norms).py") -ge 2 ]; do sleep 15; done
echo "launching m10 at $(date -u +%FT%TZ)" >> runs/queue_m10.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m10 120 48 0.3 1:19:B8,26 60 1e3 1.0 > runs/n12_m10.log 2>&1
echo "m10 finished at $(date -u +%FT%TZ)" >> runs/queue_m10.log
