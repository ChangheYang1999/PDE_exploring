#!/bin/bash
# v2 polygon sweep, delta=0.01, maxdepth 3, alpha=1/10 first.
cd ../numerics_code
export OMP_NUM_THREADS=1
P=python3

run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/cert2/queue.log; $P -u certify_lb.py "$@" --nproc 6 --out ../numerics_data/cert2/$tag.json > ../numerics_data/cert2/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/cert2/queue.log; }
D=0.01
run a110_a35  --alpha 1/10 --a 3/5  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e6  --maxdepth 3
run a12_a12   --alpha 1/2  --a 1/2  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e8  --maxdepth 3
run a310_a12  --alpha 3/10 --a 1/2  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e6  --maxdepth 3
run a34_a310  --alpha 3/4  --a 3/10 --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e16 --maxdepth 3
run a910_a15  --alpha 9/10 --a 1/5  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e40 --maxdepth 3
run a15_a12   --alpha 1/5  --a 1/2  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e6  --maxdepth 3
run a120_a35  --alpha 1/20 --a 3/5  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e6  --maxdepth 3
run a25_a12   --alpha 2/5  --a 1/2  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e6  --maxdepth 3
run a35_a25   --alpha 3/5  --a 2/5  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e9  --maxdepth 3
run a710_a25  --alpha 7/10 --a 2/5  --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e12 --maxdepth 3
run a45_a310  --alpha 4/5  --a 3/10 --delta $D --delta_cross 0.05 --delta_far0 $D --rho_max 1e19 --maxdepth 3
echo ALLDONE >> ../numerics_data/cert2/queue.log
