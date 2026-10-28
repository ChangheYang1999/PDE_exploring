#!/bin/bash
# after region.done: per-circle-restricted exterior LPs (farpc) vs unrestricted (far) at alpha 1/2, then the exact-mass qatom reruns
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f region.done ]; do sleep 10; done
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.193410 farpc > midext_a05_farpc.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.75 0,np.pi/8,np.pi/4 48 0.04 1e8 2.638768 far > midext_a075_far.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.75 0,np.pi/8,np.pi/4 48 0.04 1e8 2.638768 farpc > midext_a075_farpc.log 2>&1
cd ../qatom
nice -n 10 $PY -u ../../code/qatom_ot.py 0.5 np.pi/2,0 40 10 1e-4 > qatom_a05_exact.log 2>&1
echo "done $(date -u +%FT%TZ)" > ../midext/tail.done
