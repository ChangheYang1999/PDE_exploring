"""Joint fit across P (verifier check of lead analysis 13.16 (c)): on [-W, -a] U [a, W] (physical xi = x - x*, y fixed),
  H = poly_D(xi) + J xi_+^3 / 6           (model S: one smooth function plus a third-derivative step at xi = 0)
  H = poly_D(xi)                          (model 0: no step)
J and the rms of both models. Legendre basis on xi / W. A |xi|^lam pair differs from the step only by |xi|^(-0.07)
in H_xxx, which this test does not separate (see pjump_win.py).
Usage: python3 pjump_joint.py shape.npz x_star y"""
import sys
import numpy as np
from numpy.polynomial import legendre as Lg
from pjump import H_pts
d = np.load(sys.argv[1], allow_pickle=True); xs = float(sys.argv[2]); y = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
W = 0.8
x = xs + np.linspace(-W, W, 3201); xi = x - xs
H = H_pts(d, x, np.full(len(x), y))
for D in (6, 8, 10, 12):
    row = []
    for a in (0.0, 0.03, 0.05, 0.1, 0.15, 0.2, 0.3):
        m = np.abs(xi) >= a
        V = Lg.legvander(xi[m] / W, D)
        c0, *_ = np.linalg.lstsq(V, H[m], rcond=None); r0 = np.sqrt(np.mean((V @ c0 - H[m]) ** 2))
        M = np.c_[V, np.where(xi[m] > 0, xi[m], 0) ** 3 / 6]
        c1, *_ = np.linalg.lstsq(M, H[m], rcond=None); r1 = np.sqrt(np.mean((M @ c1 - H[m]) ** 2))
        row.append('a %.2f J %+.4f rms %.1e/%.1e' % (a, c1[-1], r1, r0))
    print('y %.2f D %2d | ' % (y, D) + ' | '.join(row))
