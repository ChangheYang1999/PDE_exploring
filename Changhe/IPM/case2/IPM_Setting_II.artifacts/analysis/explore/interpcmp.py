# Lead: one semi-Lagrangian step on a lead stationary state with the SAME feet (lead velocity, RK2), interpolated four
# ways: lead prefiltered cubic B-spline +- hull limiter, numerics local cubic Lagrange (their PFwdB.interp, read-only import) +-
# limiter. Prints the relative one-step change (gn - g)/(ds g) by lr band and angle window: where each interpolant drifts.
# Usage: python3 withpf2.py interpcmp.py state.npz
import sys, numpy as np, torch
sys.path.insert(0, '../numerics/code')
sys.path.insert(0, 'explore')
torch.set_default_dtype(torch.float64)
from pfwd_batch import PFwdB
import pforward as PF, p0_forward2 as P2
from scipy.ndimage import map_coordinates
d = np.load(sys.argv[1]); g, lr, th, p = d['g'], d['lr'], d['th'], float(d['p']); Nr, Nth = g.shape; r = np.exp(lr); l = 1 / p
ds = 0.02; drho = lr[1] - lr[0]; dth = 2 * np.pi / Nth
wr, wt = PF.velocity_p((r ** p)[:, None] * g, lr, th, p)
ar = l + wr / r[:, None]; at = wt / r[:, None]; src = p * wr / r[:, None]
ci0 = np.arange(Nr)[:, None] + 0.5 * ds * ar / drho; cj0 = np.arange(Nth)[None, :] + 0.5 * ds * at / dth
arm = P2.interp_qm(ar, ci0, cj0, Nth); atm = P2.interp_qm(at, ci0, cj0, Nth); srm = P2.interp_qm(src, ci0, cj0, Nth)
ci = np.arange(Nr)[:, None] + ds * arm / drho; cj = np.arange(Nth)[None, :] + ds * atm / dth
fac = np.exp(ds * srm); inside = ci <= Nr - 1
def bs(lim):
    Pd = 24; gp = np.concatenate([g[:, -Pd:], g, g[:, :Pd]], axis=1); cic = np.clip(ci, 0, Nr - 1); cjp = np.mod(cj, Nth) + Pd
    v = map_coordinates(gp, [cic, cjp], order=3, mode='nearest')
    if lim:
        i0 = np.clip(np.floor(cic).astype(int), 0, Nr - 2); j0 = np.floor(cjp).astype(int)
        c = [gp[i0, j0], gp[i0, j0 + 1], gp[i0 + 1, j0], gp[i0 + 1, j0 + 1]]
        v = np.clip(v, np.minimum.reduce(c), np.maximum.reduce(c))
    return v
def lag(lim):
    S = PFwdB.__new__(PFwdB); S.Nr, S.Nth, S.dev, S.limiter = Nr, Nth, torch.device('cpu'), lim
    G = torch.tensor(g)[None]; top = torch.tensor(g[-1:]).expand(2, -1)[None]
    return S.interp(G, torch.tensor(ci)[None], torch.tensor(cj)[None], top)[0].numpy()
res = {'bspline+lim': bs(True), 'bspline': bs(False), 'lagrange+lim': lag(True), 'lagrange': lag(False)}
deg = np.degrees(th)
wins = [('|th-90|<3', np.abs(deg - 90) < 3), ('3-15 deg from 90', (np.abs(deg - 90) >= 3) & (np.abs(deg - 90) < 15)),
        ('15-60 from 90', (np.abs(deg - 90) >= 15) & (np.abs(deg - 90) < 60)), ('|th-270|<3', np.abs(deg - 270) < 3),
        ('3-15 from 270', (np.abs(deg - 270) >= 3) & (np.abs(deg - 270) < 15))]
print('state', sys.argv[1], 'Nth', Nth, ': max over band of |gn - g| / (ds g), same feet')
print('%-14s %-18s' % ('scheme', 'window') + ''.join('%12s' % ('[%g,%g]' % b) for b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2)]))
for k, gn in res.items():
    gn = np.where(inside, gn * fac, g)
    rel = (gn - g) / (ds * np.maximum(g, 1e-300))
    for wn, wm in wins:
        row = []
        for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -2), (-2, 2)]:
            i = (lr >= a) & (lr < b); x = rel[np.ix_(i, wm)]; x = x[np.isfinite(x) & (g[np.ix_(i, wm)] > 0)]
            row.append('%12.2e' % (x[np.argmax(np.abs(x))] if x.size else np.nan))
        print('%-14s %-18s' % (k, wn) + ''.join(row))
