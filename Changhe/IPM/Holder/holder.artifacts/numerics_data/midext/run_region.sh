#!/bin/bash
# after full.done: exterior-only and middle-only LPs at alpha 1/2 (same discretisation), then a finer both-region run at the worst phase node j=12
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f full.done ]; do sleep 10; done
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.193410 far > midext_a05_far.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.193410 mid > midext_a05_mid.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 3*np.pi/16 96 0.02 1e6 2.193410 both > midext_a05_fine_j12.log 2>&1
echo "done $(date -u +%FT%TZ)" > region.done
