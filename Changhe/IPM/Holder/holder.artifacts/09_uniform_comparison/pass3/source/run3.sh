#!/bin/bash
# Pass 3 node certificates (Theorem 3.7 version of the uniform comparison), sequential and single-threaded.
cd the lead work/scratch/uniform3
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
mkdir -p local mid
ALPHAS="7/20 3/8 2/5 17/40 9/20 19/40 1/2 21/40 11/20 23/40 3/5 5/8 13/20 27/40 7/10 29/40 3/4 31/40 4/5 33/40 17/20 7/8 9/10 3/10"
for r in "0 128" "128 256"; do
  set -- $r
  [ -f local/r$1.done ] || { nice -n 5 timeout 590 python3 local_nodes.py --alphas $ALPHAS --start $1 --stop $2 --out-stem local/r$1_$2 > local/r$1.log 2>&1 && echo ok > local/r$1.done; }
done
G="17/40:7/20,3/8,2/5,17/40,9/20,19/40,1/2;11/20:1/2,21/40,11/20,23/40,3/5;13/20:3/5,5/8,13/20,27/40,7/10;3/4:7/10,29/40,3/4,31/40,4/5;17/20:4/5,33/40,17/20,7/8,9/10"
for s in $(seq 0 32 480); do
  e=$((s+32))
  [ -f mid/n512_$s.json ] || nice -n 5 timeout 590 python3 mid_nodes.py --angles 512 --radial 512 --phases 16 --groups "$G" --start $s --stop $e --out mid/n512_$s.json > mid/n512_$s.log 2>&1
done
echo DONE > run3.done
