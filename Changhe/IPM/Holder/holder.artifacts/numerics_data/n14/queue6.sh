#!/bin/bash
# optional refinement with idle cores: alpha 3/4 at delta .0035 (start-hashed code, sidecar); expected ~2 h
cd ../numerics_code
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
P=python3
echo $$ > ../numerics_data/n14/queue6.pid
run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/n14/queue.log; $P -u certify_note14.py "$@" --nproc 3 --out ../numerics_data/n14/$tag.json > ../numerics_data/n14/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/n14/queue.log; }
run n14_a34_c30_ff --alpha 3/4 --b 3/4 --c=-3/10 --lam 50/53 --delta 0.0035 --delta_far0 0.0035 --maxdepth 3 --rho_max 1e16
echo ALLDONE6 >> ../numerics_data/n14/queue.log
