#!/bin/bash
# Theorem 3.7 certificates for C at six exponents of Table 1, with middle and exterior plans chosen at the exponent
# itself. Same grids as the nodal certificates of the closed form: local circles 512 x 256, middle circles 512 x 512,
# exterior circles 512 x 128, m = 16 phases, delta = 1/64. Sequential, single-threaded; every chunk is bounded by 590 s.
cd "$(dirname "$0")/.."
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
ALPHAS="1/1000 1/100 1/20 1/10 1/5 99/100"
for a in $ALPHAS; do
  n=$(echo $a | tr / _)
  [ -f far/far_$n.json ] || nice -n 5 timeout 590 python3 code/far_nodes.py --angles 512 --radial 128 --alphas $a --ref $a --out far/far_$n.json > far/far_$n.log 2>&1
done
for r in "0 64" "64 128" "128 192" "192 256"; do
  set -- $r
  [ -f local/r$1.done ] || { nice -n 5 timeout 590 python3 code/local_nodes.py --alphas $ALPHAS --start $1 --stop $2 --out-stem local/r$1_$2 > local/r$1.log 2>&1 && echo ok > local/r$1.done; }
done
G="1/1000:1/1000;1/100:1/100;1/20:1/20;1/10:1/10;1/5:1/5;99/100:99/100"
for s in $(seq 0 32 480); do
  e=$((s+32))
  [ -f mid/n512_$s.json ] || nice -n 5 timeout 590 python3 code/mid_nodes.py --angles 512 --radial 512 --phases 16 --groups "$G" --start $s --stop $e --out mid/n512_$s.json > mid/n512_$s.log 2>&1
done
echo DONE > run_table37.done
