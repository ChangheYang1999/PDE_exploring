#!/bin/bash
# Usage: bash gen_audit.sh shape.npz tag "r0 R N nq Mmax; r0 R N nq Mmax; ..." [Rfit_phys]
# With a 4th argument (physical fit radius of a bounded-domain fit, e.g. construct5) the field uses the lead's two-term
# exterior extension beyond R_shape L (gen_shape.py 'closure') and vaudit adds regions r <= Rfit and r > Rfit.
cd "$(dirname "$(readlink -f "$0")")/../code"
export PYTHONDONTWRITEBYTECODE=1
fail=0; shape=$1; tag=$2; IFS=';' read -ra cfgs <<< "$3"; clo=""
if [ -n "$4" ]; then export VAUDIT_RFIT=$4; clo=closure; fi
for c in "${cfgs[@]}"; do
  read r0 R N nq M <<< "$c"
  name=${tag}_N${N}_q${nq}_R${R}
  echo "$(date -u +%FT%TZ) start $name $clo $4" >> ../runs/audit/gen_audit_${tag}.log
  python3 gen_shape.py $shape $r0 $R $N $nq ../runs/gen4/$name.npz $clo > ../runs/audit/$name.log 2>&1
  rc1=$?
  timeout 2400 python3 vaudit.py ../runs/gen4/$name.npz $M ../runs/audit/$name.json 20 24 >> ../runs/audit/$name.log 2>&1
  rc2=$?
  echo "$(date -u +%FT%TZ) end $name exit gen_shape $rc1 vaudit $rc2" >> ../runs/audit/gen_audit_${tag}.log
  [ $rc1 -ne 0 ] || [ $rc2 -ne 0 ] && fail=1
  rm -f ../runs/gen4/$name.npz
done
# exit status 1 if any gen_shape or vaudit step failed (exit codes recorded in gen_audit_<tag>.log; fixed 2026-10-19)
exit $fail
