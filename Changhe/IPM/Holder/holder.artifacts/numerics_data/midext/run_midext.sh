#!/bin/bash
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
../rot/with_pause.sh bash -c "nice -n 10 python3 -u ../../code/midext_lp.py 0.5 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.193410 > midext_a05.log 2>&1; nice -n 10 python3 -u ../../code/midext_lp.py 0.75 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e8 2.638768 > midext_a075.log 2>&1; nice -n 10 python3 -u ../../code/midext_lp.py 0.3 0,np.pi/16,np.pi/8,3*np.pi/16,np.pi/4 48 0.04 1e6 2.772659 > midext_a03.log 2>&1"
echo "done $(date -u +%FT%TZ)" > midext.done
