#!/bin/bash
# Two-mode root 5 at delta = 4/9 with tq_prefix_block.py, M = 4, at higher precision (at 90 digits the response interval
# at n = 27 contains 0).  Output: tq_prefix_block_root5.out.  Waits for the PID given as $1.
cd "$(dirname "$0")"
if [ -n "$1" ]; then while kill -0 "$1" 2>/dev/null; do sleep 30; done; fi
for m in 2 4; do
  echo "== two-mode root 5 s=4114 M=$m L=sharp dps=200 eps=1e-150"
  python3 tq_prefix_block.py 9 2 two 1.8566753384149 4114 $m L=sharp dps=200 eps=1e-150 2>&1 | grep -v pyenv
done
