#!/bin/bash
# Usage: bash extra_checks.sh shape.npz tag "r0 R N nq Mmax" [closure]
# Generates one field with gen_shape.py, then runs mk_traces + cl_from_h (identity-free c_l from h(P) = 1) and vd14 (D14 centre
# relations) and vzeros (Hmin); deletes the field afterwards. Output in runs/audit/<tag>_extra.log.
cd "$(dirname "$(readlink -f "$0")")/../code"
export PYTHONDONTWRITEBYTECODE=1
fail=0; shape=$1; tag=$2; read r0 R N nq M <<< "$3"
f=../runs/gen4/${tag}_extra.npz; t=../runs/gen4/${tag}_traces.npz; log=../runs/audit/${tag}_extra.log
echo "$(date -u +%FT%TZ) start $tag $3" > $log
python3 gen_shape.py $shape $r0 $R $N $nq $f $4 >> $log 2>&1
r=$?; echo "$(date -u +%FT%TZ) gen_shape.py exit $r" >> $log; [ $r -ne 0 ] && fail=1
timeout 1200 python3 ../scratch/mk_traces.py $f $M $t >> $log 2>&1
r=$?; echo "$(date -u +%FT%TZ) ../scratch/mk_traces.py exit $r" >> $log; [ $r -ne 0 ] && fail=1
python3 ../scratch/cl_from_h.py $t >> $log 2>&1
r=$?; echo "$(date -u +%FT%TZ) ../scratch/cl_from_h.py exit $r" >> $log; [ $r -ne 0 ] && fail=1
timeout 1200 python3 vd14.py $f >> $log 2>&1
r=$?; echo "$(date -u +%FT%TZ) vd14.py exit $r" >> $log; [ $r -ne 0 ] && fail=1
timeout 1200 python3 vzeros.py $f $M ../runs/audit/${tag}_zeros.json >> $log 2>&1
r=$?; echo "$(date -u +%FT%TZ) vzeros.py exit $r" >> $log; [ $r -ne 0 ] && fail=1
echo "$(date -u +%FT%TZ) end $tag" >> $log
rm -f $f
# exit status 1 if any step failed (exit codes recorded in the log; fixed 2026-10-19)
exit $fail
