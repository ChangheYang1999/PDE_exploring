"""Oscillation scale of the normalized residual near the stem maximum (lead diagnostic).
Counts sign changes of R/den along the ray theta = t0 for r in (8.0, 9.6), and along the arc r = r0 for theta in
(0, 0.5), and compares with the radial knot count and the angular Nyquist count of the shape.
Usage: python3 scale.py fields.npz shape.npz [t0 r0]"""
import sys
import numpy as np
d = np.load(sys.argv[1]); s = np.load(sys.argv[2])
t0 = float(sys.argv[3]) if len(sys.argv) > 3 else 0.228
r0 = float(sys.argv[4]) if len(sys.argv) > 4 else 8.71
r, th = d['r'], d['theta']
R, den = d['residual'], d['denominator']
k, L = float(s['k']), float(s['L'])
kn = np.unique(s['spline_knots'])
rk = L*np.sqrt(np.clip((1-kn)**(-2/(1-k))-1, 0, None))
ang = int(s['angular'])
for t in (t0-0.06, t0, t0+0.06):
    j = np.argmin(abs(th - t)); m = (r > 8.0) & (r < 9.6)
    v = R[m, j]/den[m, j]
    sc = int(np.sum(np.diff(np.sign(v)) != 0))
    nk = int(np.sum((rk > 8.0) & (rk < 9.6)))
    print(f'ray theta {th[j]:.4f}: {m.sum()} pts in 8.0<r<9.6, sign changes {sc}, knots inside {nk}, max|v| {abs(v).max():.2e}')
i = np.argmin(abs(r - r0)); m = (th > 0.0) & (th < 0.5)
v = R[i, m]/den[i, m]
sc = int(np.sum(np.diff(np.sign(v)) != 0))
print(f'arc r {r[i]:.4f}: {m.sum()} pts in 0<theta<0.5, sign changes {sc}, angular half-periods of mode 2*{ang} in 0.5 rad: {0.5/(np.pi/(2*ang)):.0f}, max|v| {abs(v).max():.2e}')
idx = np.linspace(0, m.sum()-1, 30).astype(int)
print('   ', ' '.join(f'{th[m][q]:.3f}:{v[q]*1e6:+.1f}' for q in idx))
