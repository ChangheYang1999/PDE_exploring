"""angular_spectrum.py -- cos(2j th) coefficients of q = rho/(a0 y) at fixed small radii (lead 00:08Z item 6): geometric versus algebraic decay in j.
q(r, th) is even about th = 0 and th = pi/2, so q = sum_j c_j(r) cos 2j th; coefficients by the exact discrete cosine transform on 2J equispaced angles
in [0, pi/2] (J = 48, exact for j < 48 if q is band-limited; the model has M <= 48 modes).  usage: python3 src/angular_spectrum.py states... [radii]"""
import sys, math, numpy as np
import os as _os; sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__))); import qdiag
J = 64; th = (np.arange(J) + 0.5) * (math.pi / 2) / J
radii = [0.01, 0.03, 0.1, 0.3]
for f in [a for a in sys.argv[1:] if '=' not in a]:
    S = qdiag.State(f); print(f"{f.split('/')[-1]} (N={S.N}, M={S.M}, a0={S.a0:.5f}): |c_j| of q = sum_j c_j cos 2j th")
    for r in radii:
        o = S.ev(np.full_like(th, r), th); q = o['w'] * o['b'] / S.a0
        c = np.array([np.mean(q * np.cos(2 * j * th)) * (1 if j == 0 else 2) for j in range(J)])
        line = f"  r = {r:5.2f}: " + " ".join(f"{abs(c[j]):.1e}" for j in [0, 1, 2, 3, 4, 6, 8, 12, 16, 24, 32])
        # local decay rate between j = 4 and 12, and 12 and 24 (algebraic exponent)
        def ex(j1, j2): return math.log(abs(c[j2]) / abs(c[j1])) / math.log(j2 / j1) if c[j1] != 0 and c[j2] != 0 else float('nan')
        print(line + f"   algebraic exponent j^p: p(4->12) = {ex(4,12):+.2f}, p(12->24) = {ex(12,24):+.2f}; ratio c_24/c_12 = {abs(c[24])/abs(c[12]):.2e}")
