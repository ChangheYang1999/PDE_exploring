"""Lead check of an exported construct1 candidate: B_3 by the finite-part formula (b3_diag.py) from the exported axis
traces, plus the axis identities of SPEC D9. Usage: python b3_construct1.py fields.npz [xstar]"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from b3_diag import AxisData

z = np.load(sys.argv[1])
x = z['axis_x']
cl = float(z['c_l'])
A = 2 * cl - 1
w = z['axis_w']
sel = x < 40
x = x[sel]


def odd(f, p=1):
    """f = x^p S(x^2) for p = 1 (odd); spline S in s = x^2."""
    S = CubicSpline(x ** 2, f[sel] / x ** p)
    return lambda t: np.sign(t) ** p * np.abs(t) ** p * S(np.asarray(t) ** 2) if p % 2 else np.abs(t) ** p * S(np.asarray(t) ** 2)


def even(f, p=0):
    S = CubicSpline(x ** 2, f[sel] / x ** p)
    return lambda t: np.asarray(t) ** p * S(np.asarray(t) ** 2)


wf = odd(w, 1)
xs = brentq(wf, 1.0, 30.0) if len(sys.argv) < 3 else float(sys.argv[2])
hf = even(z['axis_h'])
g1 = even(z['axis_G1'], 2)
g1p = odd(z['axis_G1_prime'], 1)
out = {}
for name in ('', '_finite_difference'):
    a2 = odd(z['axis_A2' + name], 1)
    b3 = even(z['axis_B3W' + name])
    for nch in (64, 96, 128):
        d = AxisData(wf, hf, a2, b3, g1, g1p, cl, xs, ncheb=nch)
        for delta in (0.3, 0.4, 0.5):
            val, info = d.b3_fp(delta=delta)
            out[(name or 'solver', nch, delta)] = (val, info['odd_rel'], info['fft_tail'])
print(f"c_l = {cl:.12f}, A = {A:.9f}, p3 = {6 + 2 / A:.9f}, x* (root of w) = {xs:.10f}")
for k, v in out.items():
    print(f"  a2/b3 {k[0]:>18s} ncheb {k[1]:3d} delta {k[2]:.1f}:  B3 = {v[0]: .6e}  odd/even {v[1]:.1e}  fft tail {v[2]:.1e}")
# axis identities (SPEC D9): (w/g)' = A/g  and  int_0^{x*} (1/g - 1/(g0 x^2)) dx = 1/(g0 x*), g0 = a(0)
from scipy.integrate import quad
g0 = float(g1(1e-3) / 1e-6)
I, err = quad(lambda t: 1 / g1(t) - 1 / (g0 * t * t), 0, xs, limit=400, points=[1.0])
print(f"g0 = {g0:.10f};  int_0^x* (1/g - 1/(g0 x^2)) = {I:.10f}  vs 1/(g0 x*) = {1 / (g0 * xs):.10f}  rel defect {I * g0 * xs - 1:.2e}")
tt = np.linspace(0.05, 0.98 * xs, 9)
hh = 1e-4
lhs = (wf(tt + hh) / g1(tt + hh) - wf(tt - hh) / g1(tt - hh)) / (2 * hh)
print("  (w/g)' g / A - 1 at", np.round(tt, 2), ":", np.array2string(lhs * g1(tt) / A - 1, precision=2))
# G1 equation w g' = (1 - h) g, normalized by |w g'| + |(1 - h) g|
r1 = (wf(tt) * g1p(tt) - (1 - hf(tt)) * g1(tt)) / (np.abs(wf(tt) * g1p(tt)) + np.abs((1 - hf(tt)) * g1(tt)))
print("  G1 equation normalized defect:", np.array2string(r1, precision=2))
# a2 = (g' - w'')/2 consistency (E1)
wpp = (wf(tt + hh) - 2 * wf(tt) + wf(tt - hh)) / hh ** 2
a2s = odd(z['axis_A2'], 1)
print("  a2 - (g' - w'')/2, relative:", np.array2string((a2s(tt) - (g1p(tt) - wpp) / 2) / np.abs(a2s(tt)), precision=2))
# h(P), w'(P)
print(f"  h(x*) = {float(hf(xs)):.9f}, w'(x*) = {float((wf(xs + hh) - wf(xs - hh)) / (2 * hh)):.9f} (A = {A:.9f})")
# w-only B3 at A = 2 not applicable; report g(P), w''(P)
print(f"  g(P) = {float(g1(xs)):.6f}, w''(P) = {float((wf(xs + hh) - 2 * wf(xs) + wf(xs - hh)) / hh ** 2):.6f}")
