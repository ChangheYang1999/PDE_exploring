#!/bin/bash
# wait for the Mpen run, project exactly, launch Mpen2 (continuation with the same penalty), then run its diagnostics chain after the A4 and A5 chains
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
FT=data/state131_formal_tail.json
while ! grep -q "^saved" runs/nb_Mpen.log; do sleep 20; done
echo "Mpen saved at $(date -u +%FT%TZ)" >> runs/after_Mpen.log
OMP_NUM_THREADS=1 nice -n 5 $P code/n12_exact.py data/nb_Mpen_result.json $CK $FT data/nb_Mpen_exact.json 0,1 > runs/nb_Mpen_exact.log 2>&1
echo "Mpen exact done at $(date -u +%FT%TZ)" >> runs/after_Mpen.log
N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN="2:100" ./code/nb_launch.sh nb_Mpen2 48 32 40 0.0002 data/nb_Mpen_result.json 0,1
echo "  (env N12_MTAU=3.805 N12_MBETA=1e6 N12_DPEN=2:100)" >> runs/nb_launch.log
while [ $(grep -c "done" runs/diag_chain.log) -lt 2 ]; do sleep 30; done
./code/diag_chain.sh nb_Mpen
