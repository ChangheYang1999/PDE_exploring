#!/bin/bash
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
cd numerics/artifacts/research_copy/analysis1/IPM_Analysis_I.artifacts/numerics
date -u
echo '== c2_fminus M16 s16 Mout40 ppc4'
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 16 16 40 runs/c2/c2f_M16_s16_p4_repro.json 4 runs/c2/c2raw_M16_s16_p4_repro.npz
date -u
echo '== c2_gram2 H1m NJ1 rowsH1q'
python3 src/c2_gram2.py runs/c2/c2raw_M16_s16_p4_repro.npz runs/c2/c2gram2_M16_s16_p4_repro_H1m_NJ1_rowsH1q.json 1e-10 1 H1m two H1q
date -u
echo '== c2_gram2 H1m NJ0 rowsL2'
python3 src/c2_gram2.py runs/c2/c2raw_M16_s16_p4_repro.npz runs/c2/c2gram2_M16_s16_p4_repro_H1m_NJ0_rowsL2.json 1e-10 0 H1m two L2
date -u; echo DONE
