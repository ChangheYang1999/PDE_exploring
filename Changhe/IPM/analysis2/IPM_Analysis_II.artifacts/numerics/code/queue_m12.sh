#!/bin/bash
# when a worker slot frees: m12 = m8 family (branch 1, 16 monomials) + Legendre block, 48 angles, Tikhonov 1e-2 toward the checkpoint, 60 steps
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while [ $(pgrep -fc "python3 .*code/n12_run[.]py") -ge 2 ]; do sleep 30; done
echo "launching m12 at $(date -u +%FT%TZ)" >> runs/queue_m12.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m12 120 48 0.3 1:19:B8+26 60 1e3 1.0 none 1.0 1e-2 > runs/n12_m12.log 2>&1
echo "m12 finished at $(date -u +%FT%TZ)" >> runs/queue_m12.log
