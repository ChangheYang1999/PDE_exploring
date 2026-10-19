# Where in theta the high angular modes of H live at fixed r (verifier, verifier).
import sys, numpy as np
from scipy.interpolate import BSpline
path = sys.argv[1]; mcut = int(sys.argv[2]) if len(sys.argv) > 2 else 40
d = np.load(path, allow_pickle=True)
z = d['z']; k = float(z[0]); coef = z[1:]; L = float(d['L'])
deg, ang, order, r_or = int(d['degree']), int(d['angular']), int(d['spline_order']), float(d['origin_radius'])
knots = np.asarray(d['spline_knots'], float)
rs = np.array([7.5, 8.0, 8.2, 8.3, 8.4, 8.47, 8.55, 8.6, 8.65, 8.75, 9.0])
rr = rs / L; q = 1 - np.exp(-(1 - k) / 2 * np.log1p(rr ** 2))
Bv = BSpline(knots, np.eye(deg + 1), order, extrapolate=False)(q)[:, 1:]
chi = rr ** 2 / (rr ** 2 + r_or ** 2)
P = np.zeros((len(rs), ang + 1))
for m in range(ang + 1):
    prof = Bv @ coef[m * deg:(m + 1) * deg]
    if r_or > 0 and m > 1: prof = prof * chi ** (m - 1)
    P[:, m] = prof
th = np.linspace(0, np.pi / 2, 4001)
C = np.cos(2 * np.outer(np.arange(ang + 1), th))
Hhi = P[:, mcut:] @ C[mcut:]
tb = [0, .01, .02, .05, .1, .2, .3, .5, .8, 1.2, 1.5708]
print(path.split('/')[-1], 'high part m >=', mcut, ': max |H_hi| per theta band')
print('   r    ' + ' '.join('%7.2f-' % tb[i] for i in range(len(tb) - 1)) + '  argmax th')
for i, r in enumerate(rs):
    v = [np.abs(Hhi[i, (th >= tb[j]) & (th <= tb[j + 1])]).max() for j in range(len(tb) - 1)]
    print('  %5.2f ' % r + ' '.join('%8.1e' % x for x in v) + '   %.4f' % th[np.argmax(np.abs(Hhi[i]))])
