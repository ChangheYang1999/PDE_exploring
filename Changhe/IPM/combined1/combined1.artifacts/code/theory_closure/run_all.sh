#!/bin/bash
# Re-run every c1-t1 artifact script. Usage (from artifacts/):  bash run_all.sh [OUTDIR]
# Without OUTDIR the stored *.out files next to each script are overwritten; with OUTDIR the outputs go there
# (then compare with: for f in OUTDIR/*.out; do cmp "$f" */$(basename "$f"); done).
set -u
PY=python3
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
HERE=$(cd "$(dirname "$0")" && pwd)
OUT=${1:-}
[ -n "$OUT" ] && mkdir -p "$OUT" && OUT=$(cd "$OUT" && pwd)
for job in closure_calc/closure_calc closure_calc/tail_budget closure_calc/six_branch_K closure_calc/l2_sector_cost closure_calc/bl2_trade \
           graded_calc/graded_calc graded_calc/graded_instance graded_calc/graded_l2 \
           checks/check_T2R1_T4007 checks/check_T4013_T4017 checks/check_T2R3 checks/check_T4041 checks/check_T4051 \
           checks/check_T4054 checks/check_T4047 checks/check_T4060 checks/check_T4097 checks/check_T4107 checks/check_T4127 checks/check_T4128 \
           checks/check_T4146 checks/check_T4153 checks/origin_inv_table checks/check_joint_ceiling checks/check_T4170 checks/check_T4182 checks/c_shift_diag checks/check_T4185 checks/theta0_007 checks/check_T4199 checks/check_T4205 checks/tail_profiles_007 \
           checks/check_T4206 checks/t4206_angular_sup checks/check_T4222 checks/check_T4211 checks/check_T4229 checks/check_T4234 \
           checks/check_T4235x checks/check_T4251 checks/annulus_admissible checks/check_T4281 checks/check_T4295 checks/check_T4314 checks/check_T4322 checks/check_T4359 checks/check_TP6 checks/check_T4372 checks/check_T4381 checks/check_N4refdiff checks/check_T4397 checks/check_T4410 checks/check_R1044 checks/check_T4425 checks/v08_factors_007 checks/h18_table_ratios checks/row_refs checks/h18_verdicts checks/check_T4458 checks/check_T4462 checks/check_N4396 checks/check_T4469 checks/check_T4474 checks/check_N4409 checks/check_v50 checks/check_N4418 checks/check_N4425 checks/check_N4427 \
           transfer_checks/transfer_numbers; do
  dir=$(dirname "$job"); name=$(basename "$job")
  dest=${OUT:+$OUT/$name.out}; dest=${dest:-$HERE/$dir/$name.out}
  start=$(date +%s)
  (cd "$HERE/$dir" && taskset -c 50,51 nice -n 19 "$PY" -B "$name.py") > "$dest" 2>&1
  echo "$job rc=$? $(( $(date +%s) - start ))s"
done
