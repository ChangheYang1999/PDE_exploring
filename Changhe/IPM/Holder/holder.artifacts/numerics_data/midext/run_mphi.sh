#!/bin/bash
# after tail.done: LP of the whole remaining density m_phi (cross disks + middle + exterior) at alpha 1/2 and 3/4, compared with W_j + X_j + E_j
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f tail.done ]; do sleep 10; done
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.193410 mphi > midext_a05_mphi.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.75 0,np.pi/8,np.pi/4 48 0.04 1e8 2.638768 mphi > midext_a075_mphi.log 2>&1
echo "done $(date -u +%FT%TZ)" > mphi.done
