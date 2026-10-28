#!/bin/bash
# wait for nb_d2 (hard j = 0,1,2 descendants), project exactly with DESC 0,1,2, axis profile, then its diagnostics chain after the b6 chain (5 'done' lines)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/nb_d2.log; do sleep 20; done
echo "d2 saved at $(date -u +%FT%TZ)" >> runs/after_d2.log
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_exact.py data/nb_d2_result.json $CK $FT data/nb_d2_exact.json 0,1,2 > runs/nb_d2_exact.log 2>&1
echo "d2 exact done at $(date -u +%FT%TZ)" >> runs/after_d2.log
OMP_NUM_THREADS=1 nice -n 5 $P code/axis_profile.py data/state131_exact.json data/state131_origin_taylor.json data/nb_d2_exact.json > runs/axis_profile_d2.log 2>&1
echo "d2 axis done at $(date -u +%FT%TZ)" >> runs/after_d2.log
while [ $(grep -c "done" runs/diag_chain.log) -lt 5 ]; do sleep 30; done
./code/diag_chain.sh nb_d2
