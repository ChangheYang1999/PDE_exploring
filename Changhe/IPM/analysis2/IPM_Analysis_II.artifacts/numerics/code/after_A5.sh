#!/bin/bash
# wait for A5, project exactly, launch A6 (= A5 continuation with the soft branch-2 descendant penalty), then run the diagnostics chain for A5 after the A4 chain
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/nb_stableA5.log; do sleep 20; done
echo "A5 saved at $(date -u +%FT%TZ)" >> runs/after_A5.log
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_exact.py data/nb_stableA5_result.json $CK $FT data/nb_stableA5_exact.json 0,1 > runs/nb_stableA5_exact.log 2>&1
echo "A5 exact done at $(date -u +%FT%TZ)" >> runs/after_A5.log
N12_DPEN="2:100" ./code/nb_launch.sh nb_A6dpen 48 32 40 0.0002 data/nb_stableA5_result.json 0,1
echo "  (env N12_DPEN=2:100)" >> runs/nb_launch.log
while ! grep -q "done" runs/diag_chain.log; do sleep 30; done
./code/diag_chain.sh nb_stableA5
