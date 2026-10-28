#!/bin/bash
# after phipi.done: full two-point D LP (otlp --ident 0.5) at the five phase nodes, alpha 1/2, same discretisation as the C runs
cd ../numerics_data/midext
export OMP_NUM_THREADS=1
PY=python3
while [ ! -f phipi.done ]; do sleep 10; done
for b in 0 0.19634954 0.39269908 0.58904862 0.78539816; do
  nice -n 10 $PY -u ../../code/otlp.py --alpha 0.5 --beta $b --ident 0.5 --ntheta 16 --q 2 --rho_min 1e-8 --qf 1.5 --rho_max 1e6 --ntheta_f 48 --h 0.04 --out fullD_a05_b$b.json > fullD_a05_b$b.log 2>&1
done
echo "done $(date -u +%FT%TZ)" > fullD.done
