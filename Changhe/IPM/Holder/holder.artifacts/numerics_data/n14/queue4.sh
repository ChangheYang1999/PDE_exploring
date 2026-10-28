#!/bin/bash
# after queue3 finishes (ALLDONE in queue.log): refined 9/10 run with the repaired code (Lipschitz mixed cells), delta .007
cd ../numerics_code
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
P=python3
echo $$ > ../numerics_data/n14/queue4.pid
while ! grep -q ALLDONE ../numerics_data/n14/queue.log; do sleep 30; done
run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/n14/queue.log; $P -u certify_note14.py "$@" --nproc 3 --out ../numerics_data/n14/$tag.json > ../numerics_data/n14/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/n14/queue.log; }
run n14_a910_c30_f --alpha 9/10 --b 7/20 --c=-3/10 --lam 10/11 --delta 0.007 --delta_far0 0.007 --maxdepth 3 --rho_max 1e40
echo ALLDONE4 >> ../numerics_data/n14/queue.log
