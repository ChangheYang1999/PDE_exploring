#!/bin/bash
# Re-validate finished free-c_l runs (their earlier retro-validation used the start c_l exponents), sequentially, low priority.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1
for d in $(ls -d runs/*/ | sort); do d=${d%/}; [ -f "$d/result.json" ] || continue
  grep -q '"free_cl": true' "$d/result.json" || continue
  grep -q '"loader_fixed": true' "$d/validation.json" 2>/dev/null && continue
  nice -n 19 "${PYTHON:-python3}" scripts/validate_candidate.py "$d" >> logs/revalidate_freecl.log 2>&1 && "${PYTHON:-python3}" - "$d" <<'PY'
import json, sys, os
p = os.path.join(sys.argv[1], "validation.json"); v = json.load(open(p)); v["loader_fixed"] = True; json.dump(v, open(p, "w"), indent=1, default=float)
PY
done
echo "$(date -u +%FT%TZ) revalidate_freecl pass complete" >> logs/revalidate_freecl.log
