#!/bin/bash
# Core-56 queue after the Mpen2 e2norms job: audit d2, Hdot^-1 Mpen2, audit Mpen2, then the full chain for b6.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
while pgrep -f 'e2norms.py source_copy/exact_refs/nb_Mpen2' >/dev/null; do sleep 10; done; rm -f $OUT/C1-A2-Mpen2_polynomials.json
echo "queue start $(date -u +%FT%TZ)"
taskset -c 56 nice -n 10 $PY -B certification/audit_e2norms.py C1-A2-d2 $OUT source_copy/exact_refs/nb_d2_exact.json > logs/d2_audit.out 2>&1
echo "d2 audit done $(date -u +%FT%TZ) exit $?"
taskset -c 56 nice -n 10 $PY -B certification/hminus1.py C1-A2-Mpen2 source_copy/exact_refs/nb_Mpen2_exact.json $OUT 24 > logs/Mpen2_hminus1.out 2>&1
echo "Mpen2 hminus1 done $(date -u +%FT%TZ) exit $?"
taskset -c 56 nice -n 10 $PY -B certification/audit_e2norms.py C1-A2-Mpen2 $OUT source_copy/exact_refs/nb_Mpen2_exact.json > logs/Mpen2_audit.out 2>&1
echo "Mpen2 audit done $(date -u +%FT%TZ) exit $?"
certification/run_candidate.sh source_copy/exact_refs/nb_b6_exact.json C1-A2-b6 56 24
echo "b6 chain done $(date -u +%FT%TZ)"
