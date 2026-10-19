"""R/N_f maxima of vresmap npz maps by bands of pi/2 - theta (2026-10-18; band rows off the y-axis columns).
Usage: python3 scratch/band_look.py tagA [tagB]"""
import sys, warnings, numpy as np
warnings.simplefilter('ignore')
for t in sys.argv[1:]:
    D = np.load('runs/audit/%s_resmap.npz' % t); r, th = D['r'], D['th']
    q = np.where(D['Nf'] > 0, D['R'] / D['Nf'], 0.0); ya = np.pi / 2 - th
    print(t, len(r), 'radii in [%.4g, %.4g],' % (r.min(), r.max()), len(th), 'angles')
    for c in (0.006, 0.012, 0.05, 0.1, 0.2, 0.57):
        mt = (ya >= c); a = np.abs(q[:, mt]); i, j = np.unravel_index(np.argmax(a), a.shape)
        print('  pi/2-theta >= %.3f: %.3e at r %.4g theta %.4f' % (c, a[i, j], r[i], th[mt][j]))
    for lo, hi in ((0, 0.006), (0.006, 0.05), (0.05, 0.2)):
        mt = (ya >= lo) & (ya < hi) & (ya > 1e-12); a = np.abs(q[:, mt]); i, j = np.unravel_index(np.argmax(a), a.shape)
        print('  pi/2-theta in [%.3f, %.3f): %.3e at r %.4g theta %.4f' % (lo, hi, a[i, j], r[i], th[mt][j]))
