#!/bin/bash
# waits for the running n14_a34_c30 job, then runs the remaining certified runs sequentially (3 workers each)
cd ../numerics_code
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
P=python3
echo $$ > ../numerics_data/n14/queue2.pid
while [ ! -f ../numerics_data/n14/n14_a34_c30.json ]; do sleep 20; done
run() { tag=$1; shift; echo "start $tag $(date -u +%FT%TZ)" >> ../numerics_data/n14/queue.log; $P -u certify_note14.py "$@" --nproc 3 --out ../numerics_data/n14/$tag.json > ../numerics_data/n14/$tag.log 2>&1; echo "end $tag $(date -u +%FT%TZ) exit $?" >> ../numerics_data/n14/queue.log; }
run n14_a12_c15    --alpha 1/2  --b 3/4  --c=-3/20 --lam 1000/1021 --delta 0.01 --delta_far0 0.01 --maxdepth 3 --rho_max 1e8
run n14_a310_c0    --alpha 3/10 --b 1/2  --c=0     --lam 1000/1007 --delta 0.01 --delta_far0 0.01 --maxdepth 3 --rho_max 1e6
run n14_a910_c30   --alpha 9/10 --b 7/20 --c=-3/10 --lam 10/11     --delta 0.01 --delta_far0 0.01 --maxdepth 3 --rho_max 1e40
run n14_a34_c30_f  --alpha 3/4  --b 3/4  --c=-3/10 --lam 50/53     --delta 0.005 --delta_far0 0.005 --maxdepth 3 --rho_max 1e16
echo ALLDONE >> ../numerics_data/n14/queue.log
