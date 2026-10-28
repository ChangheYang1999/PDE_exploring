#!/bin/bash
# wait until fewer than 2 n12_run.py workers are running, then launch m8 (continuation of m5 on a 48-angle grid)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while [ $(pgrep -fc "code/n12_run.py") -ge 2 ]; do sleep 20; done
echo "launching m8 at $(date -u +%FT%TZ)" >> runs/queue_m8.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m8 120 48 0.3 1:19:16 60 1e3 0.05 $PWD/data/n12_m5_coefs_iter39.npy > runs/n12_m8.log 2>&1
echo "m8 finished at $(date -u +%FT%TZ)" >> runs/queue_m8.log
