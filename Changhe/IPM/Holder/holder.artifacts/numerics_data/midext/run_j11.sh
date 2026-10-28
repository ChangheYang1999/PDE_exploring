#!/bin/bash
# the certified D bracket peaks at phase j = 11 (phi = 11 pi/32, beta = 11 pi/64): remainder LP and D two-point LP exactly there (alpha 1/2)
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 11*np.pi/64 48 0.04 1e6 2.193410 mphi > midext_a05_mphi_j11.log 2>&1
nice -n 10 $PY -u ../../code/midext_lp.py 0.5 11*np.pi/64 48 0.04 1e6 2.193410 both > midext_a05_both_j11.log 2>&1
nice -n 10 $PY -u ../../code/otlp.py --alpha 0.5 --beta 0.53996 --ident 0.5 --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e6 --ntheta_f 48 --h 0.04 --out fullD_a05_j11.json > fullD_a05_j11.log 2>&1
echo "done $(date -u +%FT%TZ)" > j11.done
