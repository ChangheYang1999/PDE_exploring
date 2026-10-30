#!/bin/bash
# Core-55 queue A: FLOAT theta scans (coordinator request 22:29Z), then the dyadic profile of d2.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
for pair in "source_copy/exact_refs/nb_d2_exact.json C1-A2-d2" "source_copy/exact_refs/nb_Mpen2_exact.json C1-A2-Mpen2" "source_copy/candidates/C1-N1-004-4branch-l2fw.json C1-N1-004-4branch-l2fw" "source_copy/candidates/C1-N1-002-7branch-frf.json C1-N1-002-7branch-frf" "source_copy/candidates/C1-N1-003-8branch-frf.json C1-N1-003-8branch-frf"; do
  set -- $pair
  taskset -c 55 nice -n 10 $PY -B certification/theta_scan.py $1 $2 $OUT > logs/${2}_theta.out 2>&1
  echo "theta $2 done $(date -u +%FT%TZ) exit $?"
done
taskset -c 55 nice -n 10 $PY -B certification/dyadic.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 $OUT -4 14 > logs/d2_dyadic.out 2>&1
echo "dyadic d2 done $(date -u +%FT%TZ) exit $?"
