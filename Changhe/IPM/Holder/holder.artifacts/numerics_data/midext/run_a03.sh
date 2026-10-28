#!/bin/bash
# slack decomposition at alpha 3/10: m_phi LP at three phase nodes, near calibration, C and D two-point LPs (rho_max 1e6)
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
nice -n 10 $PY -u ../../code/midext_lp.py 0.3 0,np.pi/8,np.pi/4 48 0.04 1e6 2.772659 mphi > midext_a03_mphi.log 2>&1
nice -n 10 $PY -u ../../code/near_lp.py 0.3 0,np.pi/4 16 2 1e-8 > near_a03.log 2>&1
for b in 0 0.39269908 0.78539816; do
  nice -n 10 $PY -u ../../code/otlp.py --alpha 0.3 --beta $b --ident 0.5 --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e6 --ntheta_f 48 --h 0.04 --out fullD_a03_b$b.json > fullD_a03_b$b.log 2>&1
  nice -n 10 $PY -u ../../code/otlp.py --alpha 0.3 --beta $b --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e6 --ntheta_f 48 --h 0.04 --out full_a03_b$b.json > full_a03_b$b.log 2>&1
done
echo "done $(date -u +%FT%TZ)" > a03.done
