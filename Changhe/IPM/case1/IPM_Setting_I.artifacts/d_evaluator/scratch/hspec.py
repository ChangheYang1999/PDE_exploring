# Angular spectrum of the trial exponent H at fixed radii: |H_m(r)| for the cos(2 m theta) profiles (verifier, verifier).
import sys, numpy as np
from scipy.interpolate import BSpline
for path in sys.argv[1:]:
    d = np.load(path, allow_pickle=True)
    z = d['z']; k = float(z[0]); coef = z[1:]; L = float(d['L'])
    deg, ang, order, r_or = int(d['degree']), int(d['angular']), int(d['spline_order']), float(d['origin_radius'])
    knots = np.asarray(d['spline_knots'], float)
    rs = np.array([6.0, 8.0, 8.3, 8.47, 8.6, 8.75, 9.0, 12.0, 30.0, 100.0])
    rr = rs / L; q = 1 - np.exp(-(1 - k) / 2 * np.log1p(rr ** 2))
    Bv = BSpline(knots, np.eye(deg + 1), order, extrapolate=False)(q)[:, 1:]
    chi = rr ** 2 / (rr ** 2 + r_or ** 2)
    P = np.zeros((len(rs), ang + 1))
    for m in range(ang + 1):
        prof = Bv @ coef[m * deg:(m + 1) * deg]
        if r_or > 0 and m > 1: prof = prof * chi ** (m - 1)
        P[:, m] = prof
    print(path.split('/')[-1], 'angular', ang, 'degree', deg)
    ms = [0, 1, 2, 5, 10, 20, 40, 60, 80, 90, 95, 100, 110, 120, 130, 140, 145, 150]
    ms = [m for m in ms if m <= ang]
    print('   r     ' + ' '.join('%8s' % ('m%d' % m) for m in ms))
    for i, r in enumerate(rs):
        # rms over blocks of 5 modes around m to smooth sign changes
        vals = []
        for m in ms:
            a, b = max(0, m - 2), min(ang, m + 2)
            vals.append(np.sqrt(np.mean(P[i, a:b + 1] ** 2)))
        print('  %6.2f ' % r + ' '.join('%8.1e' % v for v in vals))
