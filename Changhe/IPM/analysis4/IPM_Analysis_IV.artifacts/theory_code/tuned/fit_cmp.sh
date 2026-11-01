#!/bin/bash
# Same-window comparison of block-maximum fits (NUMERICAL EVIDENCE only), as in fit_hhf_Q8_N600_cmp.out.
# usage: fit_cmp.sh Q NEW OLD ROOTS...   e.g. fit_cmp.sh 10 N600 N300 1 2 3
# Prints, per root, A_f on n>=100,150,200 for the NEW and OLD runs and on n>=100,200,300,400 for the NEW run.
# Override a baseline file name with OLDFILE_<root>=name in the environment (e.g. a different amplitude).
P=python3
Q=$1; NEW=$2; OLD=$3; shift 3
for r in "$@"; do
  f=hhf_Q${Q}h1_root${r}_${NEW}_f64.out
  v=OLDFILE_$r; o=${!v:-hhf_Q${Q}h1_root${r}_${OLD}_f64.out}
  grep -q "^# done" "$f" 2>/dev/null || { echo "root$r incomplete"; continue; }
  a=$($P fit_hhf.py "$f" | grep -o "A_f=[0-9.e+-]*" | tr '\n' ' ')
  b=$($P fit_hhf.py "$o" | grep -o "A_f=[0-9.e+-]*" | tr '\n' ' ')
  c=$($P fit_hhf.py --lo=100,200,300,400 "$f" | grep -o "A_f=[0-9.e+-]*" | tr '\n' ' ')
  echo "root$r $NEW(100,150,200): $a | $OLD: $b | $NEW(100..400): $c"
done
