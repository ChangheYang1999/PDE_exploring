"""V178: independent parity split of the numerics PL512 v1 b1 linear response (read only; numpy only).
dg = (g_j - g)/h on the (lr, th) grid of DR512_a2-1.000_it0.npz; reflection x -> -x is th -> pi - th, j -> (N/2 - j) mod N
on th_j = 2 pi j/N (checked on the grid below). Norms: plain l2 over grid points, physical (dg) and scaled (dg/scale),
scale = (r^2/(1+r^2))^(1-p/2) as in code/pfwd_parity.py line 51."""
import numpy as np
base = np.load('runs/pfwd/bn/DR512_a2-1.000_it0.npz', allow_pickle=True)
z = np.load('runs/pfwd/par/PL512_v1_resp_b1.npz', allow_pickle=False)
lr, th, g = base['lr'], base['th'], base['g']; N = th.size; p = 0.337335
assert np.allclose(th, 2 * np.pi * np.arange(N) / N)
fl = np.remainder(N // 2 - np.arange(N), N)
assert np.allclose(np.remainder(np.pi - th, 2 * np.pi), th[fl])
print('base g parity: |g - g o R|/|g| =', np.linalg.norm(g - g[:, fl]) / np.linalg.norm(g))
dg = z['dg'].astype(np.float64); r = np.exp(lr)[:, None]
scale = (r ** 2 / (1 + r ** 2)) ** (1 - p / 2)
def split(v, name, w=None):
    ve, vo = 0.5 * (v + v[:, fl]), 0.5 * (v - v[:, fl])
    n, ne, no = (np.linalg.norm(a) for a in (v, ve, vo))
    print('%-22s |v| %.6g  |P_even v| %.6g  |P_odd v| %.6g  even/|v| %.4f  even^2/|v|^2 %.4f' % (name, n, ne, no, ne / n, (ne / n) ** 2))
    return ve, vo
split(dg, 'physical dg')
u = dg / scale
ve, vo = split(u, 'scaled dg/scale')
# where is the even part (scaled)? fraction of |ve|^2 by lr band
e2 = (ve ** 2).sum(1); o2 = (vo ** 2).sum(1)
for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)]:
    m = (lr >= a) & (lr < b) if b < 10 else (lr >= a)
    print('lr [%3d,%3d): even %.3e  odd %.3e  share of even^2 %.3f' % (a, b, np.sqrt(e2[m].sum()), np.sqrt(o2[m].sum()), e2[m].sum() / e2.sum()))
# the h*dg added to g: clipping check (negative values of g + h dg before clip are not recoverable: dg saved after clip?)
h = float(z['h']); gj = g + h * dg
print('min(g + h dg) =', gj.min(), ' cells with g + h dg < 0:', int((gj < -1e-300).sum()))
# physical split by band, and angular location of the even part
ve_p, vo_p = 0.5 * (dg + dg[:, fl]), 0.5 * (dg - dg[:, fl])
e2p = (ve_p ** 2).sum(1); o2p = (vo_p ** 2).sum(1)
for a, b in [(-14, -8), (-8, -4), (-4, -2), (-2, 0), (0, 2), (2, 4), (4, 10)]:
    m = (lr >= a) & (lr < b) if b < 10 else (lr >= a)
    print('phys lr [%3d,%3d): even %.3e  odd %.3e  share of even^2 %.3f  share of odd^2 %.3f' % (a, b, np.sqrt(e2p[m].sum()), np.sqrt(o2p[m].sum()), e2p[m].sum() / e2p.sum(), o2p[m].sum() / o2p.sum()))
thd = np.degrees(th); ea = (ve_p ** 2).sum(0)
for c in [0, 30, 60, 80, 85, 88, 89, 90, 91, 92, 95, 100, 120, 150, 180]:
    k = int(np.argmin(np.abs(thd - c)))
    print('th %5.1f  even^2 share %.4f' % (thd[k], ea[k] / ea.sum()))
win = (np.abs(thd - 90) < 5) | (np.abs(thd - 270) < 5)
print('even^2 share within 5 deg of the axis: %.4f (angular measure share %.4f)' % (ea[win].sum() / ea.sum(), win.mean()))
# radial decay of the response at the core: max over th of |odd part| and |even part| vs lr, and local exponents
print('core decay: lr, max|g|, max|dg_odd|, max|dg_even|, slope_odd, slope_even (d log max / d lr over 1 unit)')
mo = np.abs(vo_p).max(1); me = np.abs(ve_p).max(1); mg = np.abs(g).max(1)
for L in [-14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2]:
    i = int(np.argmin(np.abs(lr - L))); i1 = int(np.argmin(np.abs(lr - (L + 1))))
    print('%5.1f  %.3e  %.3e  %.3e   %.3f  %.3f' % (lr[i], mg[i], mo[i], me[i], np.log(mo[i1] / mo[i]), np.log(me[i1] / me[i])))
# angular content of the odd part at lr = -12, -10: low cos modes
for L in [-12, -10, -6]:
    i = int(np.argmin(np.abs(lr - L))); c = np.fft.rfft(vo_p[i]) / N * 2
    print('lr %.1f odd part |cos/sin mode| m=1..7:' % lr[i], ' '.join('%.2e' % abs(c[m]) for m in range(1, 8)))
# per-band norms of the base u = g/scale and the relative response |dg|/|g| per band (scale-independent within a band)
ub = g / scale
print('band: |u_base| |u_resp_odd| |u_resp_even| rel_odd=|dg_odd|/|g| rel_even=|dg_even|/|g| (per unit b_1)')
for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)]:
    m = (lr >= a) & (lr < b) if b < 10 else (lr >= a)
    print('lr [%3d,%3d): %.3e %.3e %.3e  %.3e %.3e' % (a, b, np.linalg.norm(ub[m]), np.linalg.norm(vo[m]), np.linalg.norm(ve[m]),
          np.linalg.norm(vo_p[m]) / np.linalg.norm(g[m]), np.linalg.norm(ve_p[m]) / np.linalg.norm(g[m])))
print('|u_base| total %.4e; share of |u_base|^2 at lr < -8: %.4f' % (np.linalg.norm(ub), (ub[lr < -8] ** 2).sum() / (ub ** 2).sum()))
# FD step rule of linear_column: e = eps_rel |u| / |v| (global l2). Local relative perturbation of a unit direction living in one band:
print('band: |u|/|u_band|, and eps_rel*|u|/|u_band| for eps_rel 1e-3 (local relative size of e v for a unit v supported in that band)')
nu = np.linalg.norm(ub)
for a, b in [(-14, -12), (-12, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 4), (4, 10)]:
    m = (lr >= a) & (lr < b) if b < 10 else (lr >= a)
    print('lr [%3d,%3d): %.3e  %.3e' % (a, b, nu / np.linalg.norm(ub[m]), 1e-3 * nu / np.linalg.norm(ub[m])))
