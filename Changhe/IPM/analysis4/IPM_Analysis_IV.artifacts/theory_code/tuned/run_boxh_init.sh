#!/bin/bash
# Batch for tq_boxh_init.py at delta = 4/9 (theory Section 12.6, Remark 4).  Output: tq_boxh_init_Q9h2.out
cd "$(dirname "$0")"
PY=python3
ROOTS=(0.0634372744551 0.1524299875186 0.2698308393969 0.4223764827872 1.8566753384149)
SOLD=(1/536870912 1/16777216 1/33554432 1/16384 1)
SNEW=(211/25000000000 87/200000000 47/200000000 99/250000 4114)
for i in 0 1 2 3 4; do
  for cfg in "kappa=old L=half" "kappa=star L=half" "kappa=star L=sharp"; do
    for sv in "${SOLD[$i]}" "${SNEW[$i]}"; do
      echo "== two-mode root $((i+1)) s=$sv $cfg"
      $PY tq_boxh_init.py 9 2 two ${ROOTS[$i]} $sv $cfg 2>&1 | grep -v pyenv
    done
  done
done
CR=(0.0420056861532581 0.0893795255904838)
CS=(1/2097152 1/268435456)
for i in 0 1; do
  for cfg in "kappa=old L=half" "kappa=star L=half" "kappa=star L=sharp"; do
    echo "== Candidate-shaped root $((i+2)) s=${CS[$i]} $cfg"
    $PY tq_boxh_init.py 9 2 candidate007_leading_exact.json ${CR[$i]} ${CS[$i]} $cfg 2>&1 | grep -v pyenv
  done
done
