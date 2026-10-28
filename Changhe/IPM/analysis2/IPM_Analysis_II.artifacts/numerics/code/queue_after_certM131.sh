#!/bin/bash
# waits for the state-131 M covering to finish, then runs the post-processing and the cheap state-131 certificates (C3-131, C2-131) with at most 3 workers
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
PY="${PYTHON:-python3}"
export OMP_NUM_THREADS=1
CK=../../../case4/IPM_case4.artifacts/checkpoints/state131_last_unverified/accepted_00000131.json
while ! grep -q "^done" runs/certM_131.log; do sleep 30; done
echo "$(date -u +%FT%TZ) covering done; post-processing" 
$PY code/post_certM.py data/certM_131.jsonl data/farfield_M_cert_131.json data/certM_131_summary.json 1.810319210199998 10.300294891831177 > runs/post_certM_131.log 2>&1
$PY code/post_certM_B2.py data/certM_131.jsonl data/farfield_M_cert_131.json 4076476460239181/2251799813685248 data/certM_131_B2.json > runs/post_certM_B2_131.log 2>&1
echo "$(date -u +%FT%TZ) post-processing done; launching C3-131 chain, C2-131 far-field certificates (3 workers)"
( $PY code/origin_taylor.py data/state131_exact.json data/state131_origin_taylor_deg34.json 34 > runs/origin_taylor_131_deg34.log 2>&1 && \
  ORIGIN_N4_OUT=$PWD/data/origin_N4_131.json $PY code/origin_N4.py data/state131_origin_taylor_deg34.json data/state131_exact.json $CK > runs/origin_N4_131.log 2>&1 ; echo "$(date -u +%FT%TZ) C3-131 chain finished rc $?" ) &
( FARFIELD_F_OUT=$PWD/data/farfield_F_cert_131.json $PY code/farfield_F_cert.py data/state131_exact.json 10 20 30 50 100 300 1000 10000 > runs/farfield_F_cert_131.log 2>&1 ; echo "$(date -u +%FT%TZ) C2-131 farfield_F_cert finished rc $?" ) &
( FARFIELD_F_OUT=$PWD/data/farfield_F_sharp_131.json $PY code/farfield_F_sharp.py data/state131_exact.json 10 300 1e9 0.02 > runs/farfield_F_sharp_131.log 2>&1 ; echo "$(date -u +%FT%TZ) C2-131 farfield_F_sharp finished rc $?" ) &
wait
echo "$(date -u +%FT%TZ) queue finished"
