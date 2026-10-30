#!/bin/bash
# Core-56 queue v3: wait for the d2 audit (pid 2968524); then chains for C1-N1-002, 003, 004; then Mpen2 Hdot^-1 and audit; then b6.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
while kill -0 2968524 2>/dev/null; do sleep 10; done
echo "queue v3 start $(date -u +%FT%TZ)"
for C in C1-N1-002-7branch-frf C1-N1-003-8branch-frf C1-N1-004-4branch-l2fw; do
  certification/run_candidate.sh source_copy/candidates/$C.json $C 56 24
  echo "$C chain done $(date -u +%FT%TZ)"
done
taskset -c 56 nice -n 10 $PY -B certification/hminus1.py C1-A2-Mpen2 source_copy/exact_refs/nb_Mpen2_exact.json $OUT 24 > logs/Mpen2_hminus1.out 2>&1
echo "Mpen2 hminus1 done $(date -u +%FT%TZ)"
taskset -c 56 nice -n 10 $PY -B certification/audit_e2norms.py C1-A2-Mpen2 $OUT source_copy/exact_refs/nb_Mpen2_exact.json > logs/Mpen2_audit.out 2>&1
echo "Mpen2 audit done $(date -u +%FT%TZ)"
certification/run_candidate.sh source_copy/exact_refs/nb_b6_exact.json C1-A2-b6 56 24
echo "b6 chain done $(date -u +%FT%TZ)"
