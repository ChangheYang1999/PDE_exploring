"""One-sided non-analytic content of the axis velocity w at x* on a trace: least-squares fit on |x - x*| < R of
  w = poly_deg(x - x*) + D- (x* - x)_+^(mu + 1) + D+ (x - x*)_+^(mu + 1),  mu = g*/A (lambda-mode of g),
and the same with mu + 1 replaced by 3 (a plain jump of w''' ) as a control. Also g from the w-only formula of R10.
Usage: python3 lamfit.py traces.npz"""
import sys
import numpy as np
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'dcode'))
from vb3ibp import build
from scipy.interpolate import CubicSpline

z = np.load(sys.argv[1], allow_pickle=True)
x, w, wp, wpp, cl = z['x'], z['w'], z['wp'], z['wpp_ode'], float(z['c_l'])
d = build(x, w, wp, wpp, cl)
xs, A = d['xs'], d['A']
gs = CubicSpline(d['u'], d['g'])
gst = float(gs(np.log(xs)))
mu = gst / A
print('%s: x* %.8f A %.6f g* %.5f mu = g*/A %.5f' % (sys.argv[1].split('/')[-1], xs, A, gst, mu))
for ex_name, ex in (('mu+1', mu + 1), ('3 (w\'\'\' jump)', 3.0), ('4', 4.0)):
    for R in (1.0, 2.0, 3.0):
        for deg in (6, 8, 10):
            sel = np.abs(x - xs) < R
            t = (x[sel] - xs) / R
            V = np.vander(t, deg + 1)
            Vm = np.clip(-t, 0, None) ** ex
            Vp = np.clip(t, 0, None) ** ex
            M = np.column_stack([V, Vm, Vp])
            c, *_ = np.linalg.lstsq(M, w[sel], rcond=None)
            res = np.abs(M @ c - w[sel]).max()
            c0, *_ = np.linalg.lstsq(V, w[sel], rcond=None)
            res0 = np.abs(V @ c0 - w[sel]).max()
            # coefficients of (x* - x)^ex in absolute units
            Dm, Dp = c[-2] / R ** ex, c[-1] / R ** ex
            print('  ex %-14s R %.0f deg %2d  D- %+.4e  D+ %+.4e  maxres %.2e (no singular terms %.2e)' % (ex_name, R, deg, Dm, Dp, res, res0))
