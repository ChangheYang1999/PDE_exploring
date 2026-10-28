#!/bin/bash
# after m8 finishes: m9 = m5 family, sigma = 0.15 objective, 48 angles, 60 steps from the m8 final state
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/n12_m8.log 2>/dev/null; do sleep 30; done
while [ $(pgrep -fc "python3 .*code/n12_run.py") -ge 2 ]; do sleep 20; done
INIT=$(ls -t data/n12_m8_coefs_iter*.npy | head -1)
echo "launching m9 at $(date -u +%FT%TZ) from $INIT" >> runs/queue_m9.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m9 120 48 0.15 1:19:16 60 1e3 0.05 $INIT > runs/n12_m9.log 2>&1
echo "m9 finished at $(date -u +%FT%TZ)" >> runs/queue_m9.log
