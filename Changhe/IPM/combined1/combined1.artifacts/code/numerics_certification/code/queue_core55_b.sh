#!/bin/bash
# Core-55 queue B: after the d2 dyadic run (pid 218650): Bernstein covers for d2 (theta <= 2/25, M1 >= 9/10, M >= 19/5), then Mpen2 theta cover.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
while kill -0 218650 2>/dev/null; do sleep 10; done
echo "queue B start $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 A 2/25 $OUT --seconds 2400 > logs/d2_cover_A.out 2>&1; echo "d2 cover A done $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 B1 9/10 $OUT --seconds 2400 > logs/d2_cover_B1.out 2>&1; echo "d2 cover B1 done $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 M 19/5 $OUT --seconds 2400 > logs/d2_cover_M.out 2>&1; echo "d2 cover M done $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_Mpen2_exact.json C1-A2-Mpen2 A 2/25 $OUT --seconds 2400 > logs/Mpen2_cover_A.out 2>&1; echo "Mpen2 cover A done $(date -u +%FT%TZ)"
