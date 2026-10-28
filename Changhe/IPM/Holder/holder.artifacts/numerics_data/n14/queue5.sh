#!/bin/bash
# optional refinement with idle cores: alpha 1/2 at delta .0035 (start-hashed code, sidecar); expected ~2 h
cd ../numerics_code
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
P=python3
echo $$ > ../numerics_data/n14/queue5.pid
run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/n14/queue.log; $P -u certify_note14.py "$@" --nproc 3 --out ../numerics_data/n14/$tag.json > ../numerics_data/n14/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/n14/queue.log; }
run n14_a12_c15_ff --alpha 1/2 --b 3/4 --c=-3/20 --lam 1000/1021 --delta 0.0035 --delta_far0 0.0035 --maxdepth 3 --rho_max 1e8 --rho_min 1e-8
echo ALLDONE5 >> ../numerics_data/n14/queue.log
