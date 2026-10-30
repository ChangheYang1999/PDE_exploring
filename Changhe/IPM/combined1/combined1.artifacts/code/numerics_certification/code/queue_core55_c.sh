#!/bin/bash
# Core-55 queue C: after queue B (pid 283450): dyadic profile of d2 with the cached-conversion code.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
while kill -0 283450 2>/dev/null; do sleep 15; done
echo "queue C start $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/dyadic.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 $OUT -4 14 > logs/d2_dyadic.out 2>&1; echo "dyadic d2 done $(date -u +%FT%TZ) exit $?"
