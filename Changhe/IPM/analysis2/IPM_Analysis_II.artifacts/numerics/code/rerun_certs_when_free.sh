#!/bin/bash
# rerun the two certificate scripts (schema change: exact binary endpoints) when fewer than 3 n12 workers are busy
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
P="${PYTHON:-python3}"
while [ $(./code/busy_count.sh) -ge 3 ]; do sleep 20; done
echo "rerun certs start $(date -u +%FT%TZ)" >> runs/rerun_certs.log
OMP_NUM_THREADS=1 nice -n 5 $P code/wnorm_cert.py data/state131_exact.json 3 20,30,35 > runs/wnorm_cert_131.log 2>&1
OMP_NUM_THREADS=1 nice -n 5 $P code/wnorm_cert_multi.py data/state131_exact.json 3 35,32,31 > runs/wnorm_cert_multi_131.log 2>&1
sha256sum data/wnorm_cert_131.json data/wnorm_cert_multi_131.json >> runs/rerun_certs.log
echo "rerun certs done $(date -u +%FT%TZ)" >> runs/rerun_certs.log
