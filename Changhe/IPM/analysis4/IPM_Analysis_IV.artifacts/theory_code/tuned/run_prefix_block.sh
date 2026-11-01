#!/bin/bash
# Batch for tq_prefix_block.py at delta = 4/9 (theory Section 12.6, Remark 5(a), general M).  Output: tq_prefix_block_Q9h2.out
cd "$(dirname "$0")"
PY=python3
ROOTS=(0.0634372744551 0.1524299875186 0.2698308393969 0.4223764827872 1.8566753384149)
SNEW=(211/25000000000 87/200000000 47/200000000 99/250000 4114)
for i in 3 0 1 2 4; do
  for m in ${MLIST:-4}; do
    echo "== two-mode root $((i+1)) s=${SNEW[$i]} M=$m L=sharp"
    $PY tq_prefix_block.py 9 2 two ${ROOTS[$i]} ${SNEW[$i]} $m L=sharp 2>&1 | grep -v pyenv
  done
done
