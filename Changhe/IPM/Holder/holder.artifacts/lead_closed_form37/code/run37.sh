#!/bin/bash
# Theorem 3.7 node certificates for the closed-form bound on [0, 7/20] (groups 0 and 1 of the uniform comparison, plus
# the exponent 0). Sequential and single-threaded; every chunk is bounded by 590 seconds.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
ALPHAS="0 1/200 13/2000 17/2000 11/1000 29/2000 19/1000 1/40 4/125 1/25 13/250 13/200 2/25 1/10 3/25 7/50 33/200 19/100 11/50 1/4 11/40 3/10 13/40 7/20"
for r in "0 64" "64 128" "128 192" "192 256"; do
  set -- $r
  [ -f local/r$1.done ] || { nice -n 5 timeout 590 python3 code/local_nodes.py --alphas $ALPHAS --start $1 --stop $2 --out-stem local/r$1_$2 > local/r$1.log 2>&1 && echo ok > local/r$1.done; }
done
G="1/20:0,1/200,13/2000,17/2000,11/1000,29/2000,19/1000,1/40,4/125,1/25,13/250,13/200,2/25,1/10,3/25,7/50,33/200,19/100;27/100:19/100,11/50,1/4,11/40,3/10,13/40,7/20"
for s in $(seq 0 32 480); do
  e=$((s+32))
  [ -f mid/n512_$s.json ] || nice -n 5 timeout 590 python3 code/mid_nodes.py --angles 512 --radial 512 --phases 16 --groups "$G" --start $s --stop $e --out mid/n512_$s.json > mid/n512_$s.log 2>&1
done
echo DONE > run37.done
