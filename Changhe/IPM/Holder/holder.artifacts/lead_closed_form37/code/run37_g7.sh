#!/bin/bash
# Theorem 3.7 node certificates for group 7 of the uniform comparison ([9/10, 199/200], plans at 24/25), same grids as
# run37.sh. Sequential and single-threaded; every chunk is bounded by 590 seconds.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
ALPHAS="9/10 183/200 93/100 943/1000 191/200 963/1000 97/100 122/125 49/50 123/125 987/1000 1979/2000 124/125 1987/2000 199/200"
for r in "0 64" "64 128" "128 192" "192 256"; do
  set -- $r
  [ -f local7/r$1.done ] || { nice -n 5 timeout 590 python3 code/local_nodes.py --alphas $ALPHAS --start $1 --stop $2 --out-stem local7/r$1_$2 > local7/r$1.log 2>&1 && echo ok > local7/r$1.done; }
done
G="24/25:9/10,183/200,93/100,943/1000,191/200,963/1000,97/100,122/125,49/50,123/125,987/1000,1979/2000,124/125,1987/2000,199/200"
for s in $(seq 0 32 480); do
  e=$((s+32))
  [ -f mid7/n512_$s.json ] || nice -n 5 timeout 590 python3 code/mid_nodes.py --angles 512 --radial 512 --phases 16 --groups "$G" --start $s --stop $e --out mid7/n512_$s.json > mid7/n512_$s.log 2>&1
done
echo DONE > run37_g7.done
