#!/bin/bash
# Core-55 queue E: after the running d2 B1 cover (pid 684299): resume the d2 theta cover (A, 2/25), resume B1 if INCOMPLETE, then the dyadic profile of d2.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
while kill -0 684299 2>/dev/null; do sleep 15; done
echo "queue E start $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 A 2/25 $OUT --seconds 5400 --resume > logs/d2_cover_A_resume.out 2>&1; echo "d2 cover A resume done $(date -u +%FT%TZ)"
if grep -q '"status": "INCOMPLETE"' $OUT/C1-A2-d2_cover_B1_9over10.json 2>/dev/null; then
  taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 B1 9/10 $OUT --seconds 5400 --resume > logs/d2_cover_B1_resume.out 2>&1; echo "d2 cover B1 resume done $(date -u +%FT%TZ)"
fi
taskset -c 55 nice -n 10 $PY -B certification/dyadic.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 $OUT -4 14 > logs/d2_dyadic.out 2>&1; echo "dyadic d2 done $(date -u +%FT%TZ) exit $?"
