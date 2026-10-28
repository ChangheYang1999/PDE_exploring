#!/bin/bash
# certified sups (C2) for state 131: 2 percent cells, 80 angles, r in [0.005, 100], K = 6, one worker; starts when at most one other heavy python worker runs
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
while [ $(pgrep -fc "python3 .*code/(n12_run|n12_norms|cert_sups)[.]py") -ge 2 ]; do sleep 30; done
echo "launching cert_sups at $(date -u +%FT%TZ)" >> runs/queue_sups.log
OMP_NUM_THREADS=1 nice -n 5 $P code/cert_sups.py data/state131_exact.json ../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json data/certSups_131.jsonl 0.005 100 1.02 80 1 6 > runs/certSups_131.log 2>&1
echo "cert_sups finished at $(date -u +%FT%TZ)" >> runs/queue_sups.log
