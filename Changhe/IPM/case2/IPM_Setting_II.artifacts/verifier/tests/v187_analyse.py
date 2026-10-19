"""V187 analysis of runs/v187_cells.npz: per-cell odd parts of the core finite-difference product and its split into
travel-time and angular factors; offsets delta of the core exit angles from the moving Gamma angle."""
import numpy as np, sys
d = np.load('runs/v187_cells.npz'); ers = d['ers'][:len(d['th1'])]; lr = d['lr']; sc = d['scale']; nu = float(d['nu'])
fl = d['flip']; v = d['v']
bands = [(-14, -12), (-12, -10), (-10, -8)]
def odd(a):
    return 0.5 * (a - a[..., fl])
Tg0 = d['Tg0']; TH0 = d['TH0']; A0 = d['A0']; ok = A0 > 0; Tt0 = np.where(ok, d['Tt0'], 0.0)  # the axis cells th = 90, 270 deg (A0 = 0) contribute 0 to the odd part
th10 = np.radians(float(d['th10'])); th20 = np.radians(float(d['th20']))
wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
def offs(TH, t1, t2):
    d1 = wrap(TH - t1); d2 = wrap(TH - t2)
    return np.where(np.abs(d1) < np.abs(d2), d1, d2)
dl0 = offs(TH0, th10, th20)
print('|u| %.4e; core rows %d; base th12 %.6f %.6f deg' % (nu, len(lr), np.degrees(th10), np.degrees(th20)))
for (a, b) in bands:
    m = np.broadcast_to(((lr >= a) & (lr < b))[:, None], ok.shape)
    print('band [%d,%d): median |delta0| %.3e rad, median Tt0 %.3f, median Tg0/scale %.3e' % (a, b, np.median(np.abs(dl0[m])), np.median(Tt0[m & ok]), np.median((Tg0 / sc[:, None])[m])))
print('per eps: band |C| (odd part of (Tg - Tg0)/scale / e), |C_Tt| = |odd(T0 (-dTt))/e|, |C_A| = |odd(T0 dlogA)/e|, |C_rest|, frac of cells with sign(delta) != sign(delta0), med |delta - delta0| / |delta0|')
for k, er in enumerate(ers):
    e = er * nu
    t1 = np.radians(d['th1'][k]); t2 = np.radians(d['th2'][k])
    dT = (d['Tg'][k] - Tg0) / sc[:, None]
    C = odd(dT) / e
    T0s = Tg0 / sc[:, None]
    CTt = odd(np.where(ok, T0s * (-(d['Tt'][k] - Tt0)), 0.0)) / e
    CA = odd(np.where(ok, T0s * (np.log(np.maximum(d['A'][k], 1e-300)) - np.log(np.maximum(A0, 1e-300))), 0.0)) / e
    rest = C - CTt - CA
    dl = offs(d['TH'][k], t1, t2)
    row = []
    for (a, b) in bands:
        m = np.broadcast_to(((lr >= a) & (lr < b))[:, None], ok.shape)
        flip_frac = float((np.sign(dl[m & ok]) != np.sign(dl0[m & ok])).mean())
        rel = float(np.median(np.abs(dl[m & ok] - dl0[m & ok]) / np.abs(dl0[m & ok])))
        row.append('%.3e %.3e %.3e %.3e f%.4f r%.2e' % (np.linalg.norm(C[m]), np.linalg.norm(CTt[m]), np.linalg.norm(CA[m]), np.linalg.norm(rest[m]), flip_frac, rel))
    print('eps_rel %.2e | dth1 %.3e rad | %s' % (er, t1 - th10, ' | '.join(row)))
