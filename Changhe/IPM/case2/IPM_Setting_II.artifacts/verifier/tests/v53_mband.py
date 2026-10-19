"""V53: strain integral M = int rho r^-3 sin 3th dX (m1 = l - M/pi) of own-format states by t = log r band and by angular sector
(within 10 deg of the weak axis 90 / 270 deg, rest), for pairs of states (increments). Used to locate where the lead's a_3 +- 0.03
states (imported, tests/v52_import.py) differ from mine. Usage: python3 tests/v53_mband.py BASE1 PERT1 [BASE2 PERT2 ...]."""
import sys, math, json, numpy as np
bands = [(-99, -10), (-10, -8), (-8, -6), (-6, -4), (-4, -2), (-2, 0), (0, 99)]
def parts(fn):
    d = np.load(fn, allow_pickle=True)
    rr = d['rho']; r0 = d['r']; th0 = d['th']; p = float(d['p']); nt = len(th0); t = np.log(r0)
    w = np.zeros_like(t); dt = np.diff(t); w[:-1] += dt/2; w[1:] += dt/2
    c = (w/r0)[:, None]*rr*np.sin(3*th0)[None, :]*(2*math.pi/nt)
    tail = r0[-1]**(p - 1)/(1 - p)*float((rr[-1]/r0[-1]**p*np.sin(3*th0)).sum())*2*math.pi/nt
    deg = np.degrees(th0) % 360
    win = (np.abs(deg - 90) < 10) | (np.abs(deg - 270) < 10)
    out = {}
    for lo, hi in bands:
        m = (t >= lo) & (t < hi)
        out['%g..%g' % (lo, hi)] = (float(c[m][:, win].sum()/math.pi), float(c[m][:, ~win].sum()/math.pi))
    out['tail'] = (0.0, tail/math.pi)
    return out, (float(c.sum()) + tail)/math.pi, p
args = sys.argv[1:]
for i in range(0, len(args), 2):
    b, bm, p = parts(args[i]); q, qm, _ = parts(args[i + 1])
    print('pair', args[i].split('/')[-1], args[i + 1].split('/')[-1], 'M/pi base %.6f pert %.6f  dm1 = -dM/pi = %+.6f' % (bm, qm, -(qm - bm)))
    print('  band      d(M/pi) windows(+-10deg)  rest      (base windows, rest)')
    for k in b:
        print('  %-9s %+.6f          %+.6f   (%.5f, %.5f)' % (k, q[k][0] - b[k][0], q[k][1] - b[k][1], b[k][0], b[k][1]))
