#!/bin/bash
# wait for nb_b6, project exactly with the order-7 targets, axis profile, then its diagnostics chain after the Mpen2 chain (4 'done' lines)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/nb_b6.log; do sleep 20; done
echo "b6 saved at $(date -u +%FT%TZ)" >> runs/after_b6.log
N12_EXTRA_ORDERS=$PWD/data/stationary_order7.json OMP_NUM_THREADS=1 nice -n 5 $P code/n12_exact.py data/nb_b6_result.json $CK $FT data/nb_b6_exact.json 0,1 > runs/nb_b6_exact.log 2>&1
echo "b6 exact done at $(date -u +%FT%TZ)" >> runs/after_b6.log
OMP_NUM_THREADS=1 nice -n 5 $P code/axis_profile.py data/state131_exact.json data/state131_origin_taylor.json data/nb_Mpen2_exact.json data/nb_b6_exact.json > runs/axis_profile_b6.log 2>&1
echo "b6 axis done at $(date -u +%FT%TZ)" >> runs/after_b6.log
while [ $(grep -c "done" runs/diag_chain.log) -lt 4 ]; do sleep 30; done
./code/diag_chain.sh nb_b6
