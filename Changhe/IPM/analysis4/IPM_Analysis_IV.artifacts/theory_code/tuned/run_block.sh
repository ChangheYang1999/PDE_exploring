#!/bin/bash
# Batch for tq_block.py at delta = 4/9 (theory Section 12.6, Remark 5).  Output: tq_block_Q9h2.out
cd "$(dirname "$0")"
PY=python3
ROOTS=(0.0634372744551 0.1524299875186 0.2698308393969 0.4223764827872 1.8566753384149)
SOLD=(1/536870912 1/16777216 1/33554432 1/16384 1)
SNEW=(211/25000000000 87/200000000 47/200000000 99/250000 4114)
for i in 0 1 2 3 4; do
  for sv in "${SOLD[$i]}" "${SNEW[$i]}"; do
    echo "== two-mode root $((i+1)) s=$sv kappa=star L=sharp"
    $PY tq_block.py 9 2 two ${ROOTS[$i]} $sv kappa=star L=sharp 2>&1 | grep -v pyenv
  done
done
CR=(0.0420056861532581 0.0893795255904838 0.174059472087551)
CN=(2 3 4)
CS=(1/2097152 1/268435456 1/8388608)
for i in 0 1 2; do
  echo "== Candidate-shaped root ${CN[$i]} s=${CS[$i]} kappa=star L=sharp"
  $PY tq_block.py 9 2 candidate007_leading_exact.json ${CR[$i]} ${CS[$i]} kappa=star L=sharp 2>&1 | grep -v pyenv
done
