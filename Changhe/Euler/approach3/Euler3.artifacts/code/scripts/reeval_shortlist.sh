#!/bin/bash
# Re-evaluate every shortlisted state that lacks a 7.3b quantity or the structure block (run after shortlist.py; then run shortlist.py again).
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
GPU=${1:-1}
FILES=$(.venv/bin/python - <<'PY'
import json, os
need = ("rho_u_max_holdout", "rho_u_max_holdout_half", "sigma_u_max", "sigma_u_max_half", "sigma_Om", "a_max", "a_max_half", "structure", "tau_F_R8", "Q_sw", "tau1_floored", "a_eff", "core_resolved", "E_ren")
for it in json.load(open("reports/STAGE1_SHORTLIST.json")):
    r = it["record"]
    if any(r.get(k) is None for k in need):
        print(os.path.join(os.getcwd(), r["zfile"]))
PY
)
[ -z "$FILES" ] && { echo "nothing to re-evaluate"; exit 0; }
echo "$FILES" | wc -l
CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 .venv/bin/python scripts/reevaluate_holdout.py --device cuda:0 $FILES
