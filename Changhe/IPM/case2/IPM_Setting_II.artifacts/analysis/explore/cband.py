# Lead: band decomposition of c = l - m1 = (1/pi) int rho r^-3 sin 3th dX on a lead-format state (m1mom.py formula,
# no core term below lr[0]), split into upper / lower half-planes, plus the near-node coefficients G_up / G_lo = median of
# rho / x^2 over |cos th| > 0.5 in each half-plane at the given radii. Usage: python3 cband.py state.npz [state2 ...]
import sys, numpy as np
for f in sys.argv[1:]:
    s = np.load(f); g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p']); l = 1 / p
    w = np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]
    up = np.sin(th) > 0
    cu = 2 * np.where(up, w, 0).mean(axis=1); cl = 2 * np.where(~up, w, 0).mean(axis=1)
    tail = (cu[-1] + cl[-1]) / (1 - p)
    out = []
    for lo, hi in [(-14.1, -10), (-10, -6), (-6, -2), (-2, 2), (2, 10.1)]:
        m = (lr >= lo) & (lr <= hi)
        out.append('%g..%g up %+.3f lo %+.3f' % (lo, hi, np.trapz(cu[m], lr[m]), np.trapz(cl[m], lr[m])))
    c = np.trapz(cu + cl, lr) + tail
    Gs = []
    for t in [-13, -11, -9, -7]:
        i = np.argmin(abs(lr - t)); rr = np.exp(lr[i]); rho = rr ** p * g[i]; x2 = (rr * np.cos(th)) ** 2
        sel = np.abs(np.cos(th)) > 0.5
        Gu = np.median((rho / x2)[sel & up]); Gl = np.median((rho / x2)[sel & ~up]); Gs.append('lr %d G_up %.4g G_lo %.4g log(lo/up) %+.3f' % (t, Gu, Gl, np.log(Gl / Gu)))
    print(f, 'p %.4f l %.4f c %.4f m1(grid) %.5f tail %+.3f' % (p, l, c, l - c, tail))
    print('   ' + ' | '.join(out)); print('   ' + ' | '.join(Gs))
