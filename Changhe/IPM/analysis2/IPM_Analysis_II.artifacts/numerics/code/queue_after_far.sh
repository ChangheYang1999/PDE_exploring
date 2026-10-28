#!/bin/bash
# waits for the far extension covering (10^4..10^6) and post-processes it (summary with the exterior file, B2 byproducts, M_1/M_2/M_3)
cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." || exit 1
PY="${PYTHON:-python3}"; export OMP_NUM_THREADS=1
while ! grep -q "^done" runs/certM_131_far.log; do sleep 20; done
echo "$(date -u +%FT%TZ) far covering done; post-processing"
$PY code/post_certM.py data/certM_131_far.jsonl data/farfield_M_cert_131.json data/certM_131_far_summary.json 1.810319210199998 10.300294891831177 > runs/post_certM_131_far.log 2>&1
$PY code/post_certM_B2.py data/certM_131_far.jsonl data/farfield_M_cert_131.json 4076476460239181/2251799813685248 data/certM_131_far_B2.json > runs/post_certM_B2_131_far.log 2>&1
$PY code/post_certM_Mk.py data/certM_131_far.jsonl 4076476460239181/2251799813685248 data/certM_131_far_Mk.json > runs/post_certM_Mk_131_far.log 2>&1
echo "$(date -u +%FT%TZ) post-processing done"
