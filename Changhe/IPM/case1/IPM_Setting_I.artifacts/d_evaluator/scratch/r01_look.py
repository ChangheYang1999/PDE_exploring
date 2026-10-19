"""Residual R/N_f of one vresmap npz on r <= 0.1 by bands of pi/2 - theta and of r (2026-10-18, lead NOTES 17:30:05Z item 2)."""
import sys, numpy as np
D = np.load('runs/audit/%s_resmap.npz' % sys.argv[1]); r, th = D['r'], D['th']
q = np.where(D['Nf'] > 0, D['R'] / D['Nf'], 0.0); ya = np.pi / 2 - th[None, :] + 0 * r[:, None]; R2 = r[:, None] + 0 * th[None, :]
print('grid', len(r), 'radii in', r.min(), r.max(), len(th), 'angles, step', th[1] - th[0])
for lo, hi in ((0, 0.003), (0.003, 0.006), (0.006, 0.012), (0.012, 0.05), (0.05, 0.2), (0.2, 0.6), (0.6, 1.0), (1.0, 1.6)):
    m = (ya >= lo) & (ya < hi)
    if not m.any(): continue
    a = np.abs(q) * m; i, j = np.unravel_index(np.argmax(a), a.shape)
    print('pi/2-theta [%.3f, %.3f): max %.3e at r %.4g theta %.4f' % (lo, hi, a[i, j], r[i], th[j]))
for lo, hi in ((0, 0.003), (0.003, 0.01), (0.01, 0.03), (0.03, 0.1001)):
    for cut in (0.0, 0.006, 0.05):
        m = (R2 >= lo) & (R2 < hi) & (ya >= cut)
        a = np.abs(q) * m; i, j = np.unravel_index(np.argmax(a), a.shape)
        print('r [%.3f, %.3f) pi/2-theta >= %.3f: max %.3e at r %.4g theta %.4f' % (lo, hi, cut, a[i, j], r[i], th[j]))
