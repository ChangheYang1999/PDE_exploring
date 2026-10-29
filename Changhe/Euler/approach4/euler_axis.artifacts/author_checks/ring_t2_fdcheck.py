# Finite-difference check of the analytic F', F'' used by seeds/ring_t2.py (lead, 2026-10-28).
import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'seeds'))
import numpy as np
from ring_t2 import F_all
for (c, Finf, b, rho1, n) in [(0.6, 0.5, 1.3, 0.8, 4), (0.72, 0.9, 0.5, 0.94, 3), (0.56, 0.2, 8.0, 0.8, 8)]:
    rho = np.array([0.0, 0.1, 0.7, 1.0, 2.5, 30.0]); h = 1e-5
    F, F1, F2 = F_all(rho, c, Finf, b, rho1, n)
    Fp, F1p, _ = F_all(rho + h, c, Finf, b, rho1, n); Fm, F1m, _ = F_all(np.abs(rho - h), c, Finf, b, rho1, n)
    print('c=%.2f n=%d  max|F1 - FD| = %.1e  max|F2 - FD| = %.1e  F1(0) = %g  F2(0) = %g'
          % (c, n, np.max(np.abs(F1[1:] - (Fp - Fm)[1:]/(2*h))), np.max(np.abs(F2[1:] - (F1p - F1m)[1:]/(2*h))), F1[0], F2[0]))
