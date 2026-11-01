#!/bin/bash
# Candidate-shaped roots 1..4 of Corollary T_{9,2}.C (B = 20) with tq_prefix_block.py, M = 3 (N = 27).
# Output: tq_prefix_block_cand.out.  Waits for the PID given as $1 (the two-mode batch) so that only one job runs.
cd "$(dirname "$0")"
if [ -n "$1" ]; then while kill -0 "$1" 2>/dev/null; do sleep 30; done; fi
PY=python3
CR=(-0.152635000561798 0.0420056861532581 0.0893795255904838 0.174059472087551)
CS=(1/16384 1/2097152 1/268435456 1/8388608)
for i in 0 1 2 3; do
  echo "== Candidate-shaped root $((i+1)) s=${CS[$i]} M=3 L=sharp"
  $PY tq_prefix_block.py 9 2 candidate007_leading_exact.json ${CR[$i]} ${CS[$i]} 3 L=sharp 2>&1 | grep -v pyenv
done
