"""Exact first-order response of the R10 functional B_3 (natural units) on the R12 axis data
   w = -A x (1-u^2)/(1+u^2), g = x^2/(1+u^2), u = x/L (compatible: w g' = (w' - A) g, x* = L)
to w -> w (1 + eps b), b(x) = exp(-(ln(x/x0)/sig)^2). b is flat at 0, so the finite part at 0 is untouched and the
response is an ordinary integral of the linearized integrand:
   d ln g = b + A K,  K(x) = int_0^x b/w,   d m/m = -A K,   m = |w|/g,
   J = (a2/g^3)' m^(beta-1),  a2 = (g' - w'')/2,   B_3^nat = x*^(p3-2)/(3N) f.p. int_0^x* J.
Closed-form r = g'/g (no cancellation at x*). Compared with the numerical estimators (b3core) on sampled traces.
Usage: python3 lin_r12.py L x0,x0,... [sig]  (b is multiplied by a smooth cutoff, 1 on x < 0.8 x*, 0 on x > 0.95 x*)"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b3infl')); import b3core
A = 10.150725; L = float(sys.argv[1]); x0s = [float(v) for v in sys.argv[2].split(',')]
sig = float(sys.argv[3]) if len(sys.argv) > 3 else 0.3
beta = 2 / A; N = A ** beta; p3 = 6 + beta; xs = L
t, X0 = sp.symbols('t X0', positive=True)
wS = -A * t * (1 - (t / L) ** 2) / (1 + (t / L) ** 2); gS = t ** 2 / (1 + (t / L) ** 2)
rS = sp.simplify(sp.diff(gS, t) / gS)
_c = sp.lambdify(t, wS * sp.diff(gS, t) - (sp.diff(wS, t) - A) * gS, 'numpy')
assert max(abs(_c(v)) for v in (0.3, 2.0, 7.9)) < 1e-10
bS = sp.exp(-(sp.log(t / X0) / sig) ** 2)
# C^infinity cutoff chi = 1 on x < 0.8 x*, 0 on x > 0.95 x*, so that w'(x*) = A is preserved (an incompatible
# perturbation, b(x*) != 0, makes the exact functional infinite: K ~ log|x* - x|)
_a, _b = 0.8 * L, 0.95 * L
_s = (_b - t) / (_b - _a)
_S = sp.exp(-1 / _s) / (sp.exp(-1 / _s) + sp.exp(-1 / (1 - _s)))
bS = bS * sp.Piecewise((1, t <= _a), (_S, t < _b), (0, True))
W = [sp.lambdify(t, sp.diff(wS, t, k), 'numpy') for k in range(4)]
G = [sp.lambdify(t, sp.diff(gS, t, k), 'numpy') for k in range(3)]
R = [sp.lambdify(t, sp.diff(rS, t, k), 'numpy') for k in range(2)]
Bf = [sp.lambdify((t, X0), sp.diff(bS, t, k), 'numpy') for k in range(4)]


def dJ(x, x0, K):
    w, w1, w2, w3 = [f(x) for f in W]; g, g1, g2 = [f(x) for f in G]; r, rp = [f(x) for f in R]
    b, b1, b2, b3 = [f(x, x0) for f in Bf]
    a2 = (g1 - w2) / 2; a2p = (g2 - w3) / 2
    dg = g * (b + A * K)
    dg1 = dg * r + g * (b1 + A * b / w)
    dg2 = dg1 * r + dg * rp + g1 * (b1 + A * b / w) + g * (b2 + A * (b1 * w - b * w1) / w ** 2)
    dw2 = w2 * b + 2 * w1 * b1 + w * b2
    dw3 = w3 * b + 3 * w2 * b1 + 3 * w1 * b2 + w * b3
    da2 = (dg1 - dw2) / 2; da2p = (dg2 - dw3) / 2
    q = a2p / g ** 3 - 3 * a2 * g1 / g ** 4
    dq = da2p / g ** 3 - 3 * a2p * dg / g ** 4 - 3 * da2 * g1 / g ** 4 - 3 * a2 * dg1 / g ** 4 + 12 * a2 * g1 * dg / g ** 5
    m = np.abs(w) / g
    return dq * m ** (beta - 1) + q * m ** (beta - 1) * (beta - 1) * (-A * K)


z = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'exclusion_certificates', 'reference_fit', 'data', 'c6g_traces.npz'), allow_pickle=True)
xg = z['x'] * (L / 8.6000638)          # same relative sampling as the c6g traces
for x0 in x0s:
    lo, hi = x0 * np.exp(-9 * sig), 0.95 * xs
    xx = np.geomspace(lo, hi, 200001)
    Kc = cumulative_trapezoid(Bf[0](xx, x0) / W[0](xx), xx, initial=0.0)
    Ks = CubicSpline(np.log(xx), Kc); Kinf = Kc[-1]
    Kf = lambda x: float(Ks(np.log(x))) if x < hi else Kinf
    f = lambda x: dJ(x, x0, Kf(x))
    pts = sorted(set([lo, x0 * np.exp(-sig), x0, min(x0 * np.exp(sig), 0.79 * xs), 0.8 * xs, hi]))
    I = sum(quad(f, a, b, limit=400, epsabs=0, epsrel=1e-11)[0] for a, b in zip(pts[:-1], pts[1:]))
    if hi < xs:   # tail [hi, x*]: integrand ~ (x* - x)^(beta-1) S(x)
        D = xs - hi   # x = x* - D tau^(1/beta): the integrand becomes smooth in tau
        I += quad(lambda tau: f(xs - D * tau ** (1 / beta)) * D / beta * tau ** (1 / beta - 1), 0, 1, limit=400,
                  epsrel=1e-10)[0]
    exact = xs ** (p3 - 2) / (3 * N) * I

    def tr(e):
        bb, b1, b2 = Bf[0](xg, x0), Bf[1](xg, x0), Bf[2](xg, x0)
        w0, w1, w2 = W[0](xg), W[1](xg), W[2](xg)
        return xg, w0 * (1 + e * bb), w1 * (1 + e * bb) + w0 * e * b1, w2 * (1 + e * bb) + 2 * w1 * e * b1 + w0 * e * b2, (A + 1) / 2
    res = []
    for e in (1e-7, 1e-5):
        p, m_ = tr(e), tr(-e)
        sp_, sm = b3core.b3_median(*p), b3core.b3_median(*m_)
        o = (b3core.b3_one(*p)[0] - b3core.b3_one(*m_)[0]) / (2 * e)
        res.append(((sp_['orig_median'] - sm['orig_median']) / (2 * e), (sp_['ibp_median'] - sm['ibp_median']) / (2 * e), o,
                    sp_['orig_min'], sp_['orig_max']))
    b0 = b3core.b3_median(*tr(0.0))
    print('L %.3f x0 %.2f sig %.2f | exact %.5e | eps 1e-7: med-orig %.5e med-ibp %.5e one %.5e | eps 1e-5: med-orig %.5e '
          'med-ibp %.5e one %.5e | base %.6f range(+1e-5) [%.4f, %.4f]' % (L, x0, sig, exact, *res[0][:3], *res[1][:3],
                                                                          b0['orig_median'], res[1][3], res[1][4]), flush=True)
