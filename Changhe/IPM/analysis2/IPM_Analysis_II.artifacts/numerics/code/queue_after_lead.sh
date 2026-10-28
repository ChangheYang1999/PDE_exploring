#!/bin/bash
# after the lead-weight norms (queue_leadnorms3) finish: m12 lead norms, then m14 when a slot is free
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while [ ! -f runs/queue_leadnorms3.done ]; do sleep 20; done
nice -n 5 $P code/n12_norms.py data/n12_m12_exact.json -6.9 9.21 240 24 L data/n12_m12_exact_lead.json > runs/lead_n12_m12_exact.log 2>&1
while [ $(pgrep -fc "python3 .*code/n12_run[.]py") -ge 1 ]; do sleep 30; done
echo "launching m14 at $(date -u +%FT%TZ)" >> runs/queue_m14.log
OMP_NUM_THREADS=1 nice -n 5 $P $PWD/code/n12_run.py $CK $FT $PWD/data/n12_m14 120 24 0.3 1:19:B8+26,2:29:B4+14,3:39:B4+14 80 1e3 0.3 $PWD/data/n12_m10_result.json > runs/n12_m14.log 2>&1
echo "m14 finished at $(date -u +%FT%TZ)" >> runs/queue_m14.log
