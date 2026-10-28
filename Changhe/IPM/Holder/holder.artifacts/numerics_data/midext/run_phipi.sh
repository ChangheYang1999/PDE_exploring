#!/bin/bash
# after near.done: Q + atom LP at phi = pi (negative lobes along the increment; lead reports a gain of 0.016 there) and 3pi/4, exact masses
cd ../numerics_data/qatom
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f ../midext/near.done ]; do sleep 10; done
nice -n 10 $PY -u ../../code/qatom_ot.py 0.5 np.pi,3*np.pi/4,21*np.pi/32 32 8 1e-4 > qatom_a05_phipi.log 2>&1
echo "done $(date -u +%FT%TZ)" > ../midext/phipi.done
