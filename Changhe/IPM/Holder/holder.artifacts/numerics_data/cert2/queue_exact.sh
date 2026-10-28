#!/bin/bash
# exact-zero-curve witness (lead N9): cheap settings; to be launched when the polygon sweep is done.
cd ../numerics_code
export OMP_NUM_THREADS=1
P=python3
while pgrep -f "cert2/queue[5][.]sh" > /dev/null; do sleep 60; done
run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/cert2/queue.log; $P certify_lb.py "$@" --nproc 6 --out ../numerics_data/cert2/$tag.json > ../numerics_data/cert2/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/cert2/queue.log; }
D=0.02
run ex_a12  --alpha 1/2  --a 1/2 --zmode exact --delta $D --delta_cross 0.1 --delta_far0 $D --rho_min 1e-6 --rho_max 1e8  --maxdepth 2
run ex_a110 --alpha 1/10 --a 1/2 --zmode exact --delta $D --delta_cross 0.1 --delta_far0 $D --rho_min 1e-6 --rho_max 1e6  --maxdepth 2
run ex_a910 --alpha 9/10 --a 1/2 --zmode exact --delta $D --delta_cross 0.1 --delta_far0 $D --rho_min 1e-6 --rho_max 1e40 --maxdepth 2
run ex_a310 --alpha 3/10 --a 1/2 --zmode exact --delta $D --delta_cross 0.1 --delta_far0 $D --rho_min 1e-6 --rho_max 1e6  --maxdepth 2
run ex_a34  --alpha 3/4  --a 1/2 --zmode exact --delta $D --delta_cross 0.1 --delta_far0 $D --rho_min 1e-6 --rho_max 1e16 --maxdepth 2
echo EXACTDONE >> ../numerics_data/cert2/queue.log
