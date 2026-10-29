#!/bin/bash
# Re-validate every finished run whose validation.json predates the 21:15Z validator fixes (no "status" field), sequentially at low
# priority on one core; the leaderboard and failure map pick up updated values as they appear.  Logs to logs/revalidate_all.log.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1
for d in $(ls -d runs/*/ | sort); do
  d=${d%/}; b=$(basename $d)
  case "$b" in zz_*) continue;; esac
  [ -f "$d/result.json" ] || continue
  if [ -f "$d/validation.json" ] && grep -q '"status"' "$d/validation.json"; then continue; fi
  nice -n 19 "${PYTHON:-python3}" scripts/validate_candidate.py "$d" >> logs/revalidate_all.log 2>&1
done
echo "$(date -u +%FT%TZ) revalidate_all pass complete" >> logs/revalidate_all.log
