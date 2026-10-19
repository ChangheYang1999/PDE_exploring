# Usage: python3 ana_resmap.py tag shape.npz   (reads runs/audit/<tag>_resmap.npz)
import sys, numpy as np
tag, shp = sys.argv[1], sys.argv[2]
d = np.load('runs/audit/%s_resmap.npz' % tag)
r, th, R, Nf = d['r'], d['th'], d['R'], d['Nf']
xs = float(d['x_star']); ok = (th > 1e-3) & (th < np.pi/2 - 1e-3)
th, R, Nf = th[ok], R[:, ok], Nf[:, ok]; q = np.abs(R) / Nf
i, j = np.unravel_index(np.argmax(q), q.shape)
print('max %.3e at r %.4f th %.4f  (x %.3f y %.3f)' % (q[i, j], r[i], th[j], r[i]*np.cos(th[j]), r[i]*np.sin(th[j])))
for lo, hi, tl, thh in [(6, 8.2, 0, 1.6), (8.2, 9.4, 0, 0.5), (8.2, 9.4, 0.5, 1.6), (9.4, 9.7, 0, 1.6), (9.7, 11, 0, 1.6), (11, 14, 0, 1.6)]:
    m = (r >= lo) & (r <= hi); n = (th >= tl) & (th <= thh)
    if m.any() and n.any():
        s = q[np.ix_(m, n)]; a, b = np.unravel_index(np.argmax(s), s.shape)
        print('  r %5.2f-%5.2f th %.1f-%.1f  max %.3e at r %.3f th %.3f  rms %.3e' % (lo, hi, tl, thh, s.max(), r[m][a], th[n][b], np.sqrt((s**2).mean())))
k = np.load(shp, allow_pickle=True)
kn = np.unique(k['spline_knots']); L = float(k['L']); kk = float(k['k'])
# knots are in q = 1 - (1+rr^2)^(-(1-k)/2), rr = r/L
qq = kn[(kn > 0) & (kn < 1)]; rr = np.sqrt((1 - qq) ** (-2 / (1 - kk)) - 1); rk = rr * L
for lo, hi in [(6, 8.2), (8.2, 9.4), (9.4, 9.7), (9.7, 11), (11, 14)]:
    s = rk[(rk >= lo) & (rk <= hi)]
    if len(s) > 1: print('  knot spacing r %5.2f-%5.2f: %.4f (n %d)' % (lo, hi, np.median(np.diff(s)), len(s)))
# sign changes along r at the angle of the global max
col = R[:, j]; m = (r >= max(r[i] - 1.5, 6)) & (r <= r[i] + 1.5); rc = r[m]; cc = col[m]
z = rc[1:][np.sign(cc[1:]) != np.sign(cc[:-1])]
print('  sign changes along r at th %.3f in [%.2f, %.2f]: %d, median spacing %.4f' % (th[j], rc[0], rc[-1], len(z), np.median(np.diff(z)) if len(z) > 2 else np.nan))
print('  r grid spacing near max %.4f' % np.median(np.diff(rc)))
