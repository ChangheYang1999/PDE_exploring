#!/bin/bash
# Core-55 queue G: wlap/wl2/weak norms for d2 (validation against N4-053) and 007 (theory_v02 item 1), then the cover resumes and the dyadic profile of d2.
LANE=RUN_ROOT/numerics_N3; cd $LANE
PY=python3
export PYTHONDONTWRITEBYTECODE=1 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
OUT=certification/results
echo "queue G start $(date -u +%FT%TZ)"
taskset -c 55 nice -n 10 $PY -B certification/wlap_norms.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 $OUT > logs/d2_wlap.out 2>&1; echo "wlap d2 done $(date -u +%FT%TZ) exit $?"
taskset -c 55 nice -n 10 $PY -B certification/wlap_norms.py source_copy/candidates/C1-N1-007-d2w-j7-e2bal.json C1-N1-007-d2w-j7-e2bal $OUT > logs/007_wlap.out 2>&1; echo "wlap 007 done $(date -u +%FT%TZ) exit $?"
taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 A 2/25 $OUT --seconds 5400 --resume > logs/d2_cover_A_resume.out 2>&1; echo "d2 cover A resume done $(date -u +%FT%TZ)"
if grep -q '"status": "INCOMPLETE"' $OUT/C1-A2-d2_cover_B1_9over10.json 2>/dev/null; then
  taskset -c 55 nice -n 10 $PY -B certification/bernstein_cover.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 B1 9/10 $OUT --seconds 5400 --resume > logs/d2_cover_B1_resume.out 2>&1; echo "d2 cover B1 resume done $(date -u +%FT%TZ)"
fi
taskset -c 55 nice -n 10 $PY -B certification/dyadic.py source_copy/exact_refs/nb_d2_exact.json C1-A2-d2 $OUT -4 14 > logs/d2_dyadic.out 2>&1; echo "dyadic d2 done $(date -u +%FT%TZ) exit $?"
