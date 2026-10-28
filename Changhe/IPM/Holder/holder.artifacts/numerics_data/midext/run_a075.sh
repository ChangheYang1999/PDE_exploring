#!/bin/bash
# completes the slack decomposition at alpha 3/4: C and D two-point LPs at three phase nodes (rho_max 1e8) and the near-cell calibration
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
nice -n 10 $PY -u ../../code/near_lp.py 0.75 0,np.pi/4 16 2 1e-8 > near_a075.log 2>&1
for b in 0 0.39269908 0.78539816; do
  nice -n 10 $PY -u ../../code/otlp.py --alpha 0.75 --beta $b --ident 0.5 --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e8 --ntheta_f 48 --h 0.04 --out fullD_a075_b$b.json > fullD_a075_b$b.log 2>&1
  nice -n 10 $PY -u ../../code/otlp.py --alpha 0.75 --beta $b --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e8 --ntheta_f 48 --h 0.04 --out full_a075_b$b.json > full_a075_b$b.log 2>&1
done
echo "done $(date -u +%FT%TZ)" > a075.done
