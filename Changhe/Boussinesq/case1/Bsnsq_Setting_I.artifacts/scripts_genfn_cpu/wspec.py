"""Angular (w) Chebyshev content of H(t, w) = sum_n c_nk T_n(.) T_k(2w - 1) at fixed radial t (diagnostic):
prints max |coefficient of T_k(2w - 1)| in k-bands at several t, and the physical r range of that t-ring.
Usage: python3 wspec.py state.npz"""
import sys, math, numpy as np
d = np.load(sys.argv[1]); J, K = int(d['J']), int(d['Kw']); c = d['c'].reshape(J + 1, K + 1); al = float(d['alpha'])
def zeta_of_t(t):
    return 1 - (np.log((1 - t) * (math.exp(al) - 1) + 1) / al if al > 0 else 1 - t)   # basis variable (1 - zeta), cf. model.py
for t in [0.01, 0.03, 0.1, 0.3, 0.6, 0.9, 0.99, 0.999, 0.9999]:
    s = 2 * zeta_of_t(t) - 1
    Tn = np.cos(np.arange(J + 1) * np.arccos(np.clip(s, -1, 1)))
    hk = Tn @ c          # coefficients of T_k(2w - 1) at this t
    E = t ** -6.0; wmax = (1 - t ** 6) ** (1 / 3)
    bands = [(0, 8), (8, 16), (16, 24), (24, K + 1)]
    print('t %-7g E^(1/2) %-9.3g wmax %.4f  ' % (t, E ** 0.5, wmax) + '  '.join('k%d-%d %.1e' % (a, b - 1, np.abs(hk[a:b]).max()) for a, b in bands if a <= K))
