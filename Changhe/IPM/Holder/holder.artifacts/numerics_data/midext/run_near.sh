#!/bin/bash
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f mphi.done ]; do sleep 10; done
nice -n 10 $PY -u ../../code/near_lp.py 0.5 0,np.pi/4 16 2 1e-8 > near_a05.log 2>&1
nice -n 10 $PY -u ../../code/near_lp.py 0.5 0,np.pi/4 64 1.5 1e-8 > near_a05_fine.log 2>&1
echo "done $(date -u +%FT%TZ)" > near.done
