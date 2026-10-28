#!/bin/bash
# after m11 ends: finalize m11 (exact + norms), then launch m14 (three sectors with Legendre blocks, init from the m10 result) when a slot is free
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/n12_m11.log || ! grep -q "^FINAL" runs/n12_m11.log; do sleep 30; done
nice -n 5 $P code/n12_exact.py data/n12_m11_result.json $CK $FT data/n12_m11_exact.json > runs/n12_m11_exact.log 2>&1
nice -n 5 $P code/n12_norms.py data/n12_m11_exact.json -6.9 9.21 240 24 0.15,0.3,0.4 data/n12_m11_norms.json > runs/n12_m11_norms.log 2>&1
while [ $(pgrep -fc "python3 .*code/n12_run[.]py") -ge 2 ]; do sleep 30; done
echo "launching m14 at $(date -u +%FT%TZ)" >> runs/queue_m14.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m14 120 24 0.3 1:19:B8+26,2:29:B4+14,3:39:B4+14 80 1e3 0.3 $PWD/data/n12_m10_result.json > runs/n12_m14.log 2>&1
echo "m14 finished at $(date -u +%FT%TZ)" >> runs/queue_m14.log
