#!/bin/bash
# wait for cert_M to finish, then run cert_F (6 workers)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
while ! grep -q "^done" runs/certM_088.log; do sleep 30; done
echo "cert_M finished at $(date -u +%FT%TZ); starting cert_F" >> runs/queue_certF.log
OMP_NUM_THREADS=1 nice -n 5 "${PYTHON:-python3}" code/cert_F.py data/state088_exact.json ../../../case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json data/certF_088.jsonl 0.005 300 1.02 80 6 0.45 8 0.3 data/state088_origin_taylor.json > runs/certF_088.log 2>&1
echo "cert_F finished at $(date -u +%FT%TZ)" >> runs/queue_certF.log
OMP_NUM_THREADS=1 nice -n 5 "${PYTHON:-python3}" code/cert_W.py data/state088_exact.json ../../../case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json data/certW_088.jsonl 0.005 2.0 1.02 80 6 8 > runs/certW_088.log 2>&1
echo "cert_W finished at $(date -u +%FT%TZ)" >> runs/queue_certF.log
OMP_NUM_THREADS=1 nice -n 5 "${PYTHON:-python3}" code/cert_W.py data/state088_exact.json ../../../case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json data/certW_annulus_088.jsonl 2.0 10.0 1.02 80 6 8 > runs/certW_annulus_088.log 2>&1
echo "cert_W annulus finished at $(date -u +%FT%TZ)" >> runs/queue_certF.log
OMP_NUM_THREADS=1 nice -n 5 "${PYTHON:-python3}" code/cert_H.py data/state088_exact.json ../../../case4/IPM_case4.artifacts/checkpoints/state088_handoff/accepted_00000088.json data/certH_088.jsonl 0.005 1000 1.03 60 6 6 > runs/certH_088.log 2>&1
echo "cert_H finished at $(date -u +%FT%TZ)" >> runs/queue_certF.log
