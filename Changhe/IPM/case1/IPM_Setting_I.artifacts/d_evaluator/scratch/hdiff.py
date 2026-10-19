# Difference of the trial exponents H of two shapes near the x-axis (regular part only; verifier, verifier).
# Usage: python3 hdiff.py shapeA.npz shapeB.npz [mcut]; prints H_B - H_A (modes m >= mcut only if mcut given) at fixed r, theta.
import sys, numpy as np
from scipy.interpolate import BSpline
def prof(path, rs):
    d = np.load(path, allow_pickle=True)
    z = d['z']; k = float(z[0]); coef = z[1:]; L = float(d['L'])
    deg, ang, order, r_or = int(d['degree']), int(d['angular']), int(d['spline_order']), float(d['origin_radius'])
    rr = rs / L; q = 1 - np.exp(-(1 - k) / 2 * np.log1p(rr ** 2))
    Bv = BSpline(np.asarray(d['spline_knots'], float), np.eye(deg + 1), order, extrapolate=False)(q)[:, 1:]
    chi = rr ** 2 / (rr ** 2 + r_or ** 2)
    P = np.zeros((len(rs), ang + 1))
    for m in range(ang + 1):
        p = Bv @ coef[m * deg:(m + 1) * deg]
        if r_or > 0 and m > 1: p = p * chi ** (m - 1)
        P[:, m] = p
    return P
rs = np.array([7.6, 7.8, 8.0, 8.1, 8.2, 8.3, 8.4, 8.47, 8.52, 8.56, 8.59, 8.62, 8.66, 8.7])
mcut = int(sys.argv[3]) if len(sys.argv) > 3 else 0
PA, PB = prof(sys.argv[1], rs), prof(sys.argv[2], rs)
n = max(PA.shape[1], PB.shape[1])
PA = np.pad(PA, ((0, 0), (0, n - PA.shape[1]))); PB = np.pad(PB, ((0, 0), (0, n - PB.shape[1])))
D = (PB - PA)[:, mcut:]
ths = np.array([0, .0025, .005, .01, .015, .02, .03, .05, .08, .12, .2, .3])
C = np.cos(2 * np.outer(np.arange(mcut, n), ths))
V = D @ C
print('H_B - H_A, modes m >=', mcut, '; columns theta')
print('   r    ' + ' '.join('%9.4f' % t for t in ths))
for i, r in enumerate(rs):
    print('  %5.2f ' % r + ' '.join('%9.2e' % v for v in V[i]))
