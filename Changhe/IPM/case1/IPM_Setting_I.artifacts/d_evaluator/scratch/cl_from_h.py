# c_l determined by h(P) = 1 on a fixed sampled rho (Psi_1 fixed), from the verifier's traces (w computed with the identity c_l)
import sys, numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
for f in sys.argv[1:]:
    z = np.load(f)
    x, w, wp, cl = z['x'], z['w'], z['wp'], float(z['c_l'])
    u = np.log(x)
    Psi1 = cl * x - w
    sP = CubicSpline(u, Psi1 / x)          # Psi1/x smooth in u
    sPp = CubicSpline(u, cl - wp)          # Psi1'
    def hP(c):
        xs = brentq(lambda t: c - sP(np.log(t)), 5.0, 12.0)
        return c + float(sPp(np.log(xs))), xs
    h0, xs0 = hP(cl)
    hh = lambda c: hP(c)[0] - 1.0
    # h(P) = 2 c_l - mu1 = c + Psi1'(x*) ... check against 2 cl - wp(x*)
    c1 = brentq(hh, cl - 0.01, cl + 0.01, xtol=1e-14)
    dc = 1e-5
    slope = (hh(cl + dc) - hh(cl - dc)) / (2 * dc)
    print('%s: identity c_l %.9f  h(P) %.9f (x* %.7f)  c_l from h(P)=1: %.9f  diff %+.2e  dh/dc_l (fixed rho) %.4f' % (
        f.split('/')[-1], cl, h0, xs0, c1, c1 - cl, slope))
