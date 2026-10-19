# Lead exploratory: scan (FE, alpha, beta) of the fan seed for (c, kappa); see seed_P0_kappa.py.
import numpy as np, sys
sys.argv = [sys.argv[0], sys.argv[1]]
sys.path.insert(0, 'explore')
import seed_P0_kappa as S
for FE in [0.25, 0.5, 1.0]:
    for alpha in [0.0, 0.5, 2.0]:
        for beta in [2.0, 4.0, 8.0, 16.0]:
            c, cm, k = S.ev(FE, alpha, beta)
            print('FE %.2f alpha %.2f beta %5.1f : c = %.4f kappa = %.4f' % (FE, alpha, beta, c, k), flush=True)
