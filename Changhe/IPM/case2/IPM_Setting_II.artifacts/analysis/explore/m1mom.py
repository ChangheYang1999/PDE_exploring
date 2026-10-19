# Lead: moment m1 = 1/p - c, c = (1/pi) int rho sin3th r^-3 dX on the grid (trapezoid in lr), + far tail (g frozen at r_max) + core estimate (jet x^2 below r_min).
import sys, numpy as np
for f in sys.argv[1:]:
    s = np.load(f); g, lr, th, p = s['g'], s['lr'], s['th'], float(s['p'])
    w = np.exp((p - 1) * lr)[:, None] * g * np.sin(3 * th)[None, :]
    ang = w.mean(axis=1) * 2 * np.pi / np.pi
    c_grid = np.trapz(ang, lr)
    c_tail = ang[-1] / (1 - p)
    # core: rho = x^2 below r_min contributes 0 (cos^2 sin3 integrates to 0 over the circle); report the r^(p-1) g share of the first 2 units instead
    i2 = lr < lr[0] + 2
    c_in2 = np.trapz(ang[i2], lr[i2])
    print(f, 'Nth', len(th), 'p %.6f' % p, 'c_grid %.5f c_tail %.5f m1_mom %.5f' % (c_grid, c_tail, 1 / p - c_grid - c_tail), 'c(first 2 lr units) %.5f' % c_in2,
          'm1_saved', float(s['m1']) if 'm1' in s else None)
