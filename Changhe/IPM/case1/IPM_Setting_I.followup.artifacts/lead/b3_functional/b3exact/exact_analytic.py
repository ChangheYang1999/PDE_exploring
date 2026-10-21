"""Exact B_3^nat (R10 functional, natural units) on R12 axis data perturbed by w -> w (1 + eps b), b analytic near 0,
with the finite part at 0 from the Taylor series (radius ~ L) and quadrature beyond; b carries a C^infinity cutoff to 0 on
[0.8, 0.95] x* (source condition w'(x*) = A kept). Compares dB_3/deps (central, eps = +-e) with the b3core estimators.
Usage: python3 exact_analytic.py L 'sympy expression of b in t' [e]"""
import sys
import numpy as np
import sympy as sp
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'b3infl')); import b3core
A = 10.150725; L = float(sys.argv[1]); bexpr = sys.argv[2]; e0 = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-4
beta = 2 / A; N = A ** beta; p3 = 6 + beta; xs = L
t = sp.symbols('t', positive=True)
wS = -A * t * (1 - (t / L) ** 2) / (1 + (t / L) ** 2); gS = t ** 2 / (1 + (t / L) ** 2)
b_an = sp.sympify(bexpr, locals={'t': t})
_a, _b = 0.8 * L, 0.95 * L
_s = (_b - t) / (_b - _a)
_S = sp.exp(-1 / _s) / (sp.exp(-1 / _s) + sp.exp(-1 / (1 - _s)))
chi = sp.Piecewise((1, t <= _a), (_S, t < _b), (0, True))
xc0 = 0.5
GS, G1, G2 = [sp.lambdify(t, sp.diff(gS, t, k), 'numpy') for k in range(3)]
W2, W3 = [sp.lambdify(t, sp.diff(wS, t, k), 'numpy') for k in (2, 3)]
KORD = 18


def B3nat(eps):
    """exact functional for w_eps = w (1 + eps b chi)."""
    bb = b_an * chi
    we = wS * (1 + eps * bb)
    # g_eps = g (1 + eps b) exp(eps A K), K = int_0^x b/(w (1 + eps b)); near 0 use the analytic b (chi = 1 there)
    Kint_an = sp.series(b_an / (wS * (1 + eps * b_an)), t, 0, KORD + 2).removeO()
    K_an = sp.integrate(Kint_an, t)
    def Jexpr(bfun, Kfun):
        we_ = wS * (1 + eps * bfun)
        ge = gS * (1 + eps * bfun) * sp.exp(eps * A * Kfun)
        a2 = (sp.diff(ge, t) - sp.diff(we_, t, 2)) / 2
        q = sp.diff(a2, t) / ge ** 3 - 3 * a2 * sp.diff(ge, t) / ge ** 4
        return q, ge, we_
    # (1) [0, xc0]: series of x^(5+beta) J = x^(5+beta) q m^(beta-1), m = |w|/g = A (1-u^2)(1+eps b)/(x (...)) analytic * x^-1
    q, ge, we_ = Jexpr(b_an, K_an)
    mx = sp.simplify(-we_ / ge * t)          # m x, analytic and positive near 0
    E = sp.series(q * t ** 6 * mx ** (beta - 1), t, 0, KORD).removeO()
    cs = [float(E.coeff(t, k)) for k in range(KORD)]
    I = sum(cs[k] * xc0 ** (k - 4 - beta) / (k - 4 - beta) for k in range(KORD) if abs(cs[k]) > 0)
    # (2) [xc0, x*]: quadrature, K by cumulative quadrature from xc0 with K(xc0) from the series
    Kf = sp.Function('Kf')
    qK, geK, weK = Jexpr(bb, Kf(t))
    Kd = b_an * chi / (wS * (1 + eps * b_an * chi))
    # replace derivatives of Kf by Kd and its derivative
    qK = qK.subs(sp.Derivative(Kf(t), (t, 2)), sp.diff(Kd, t)).subs(sp.Derivative(Kf(t), t), Kd)
    Ksym = sp.symbols('Ksym')
    fJ = sp.lambdify((t, Ksym), (qK * (-weK / geK) ** (beta - 1)).subs(Kf(t), Ksym), 'numpy')
    Kdf = sp.lambdify(t, Kd, 'numpy')
    xx = np.geomspace(xc0, 0.999999 * xs, 400001)
    Kc = float(K_an.subs(t, xc0)) + cumulative_trapezoid(Kdf(xx), xx, initial=0.0)
    Ksp = CubicSpline(np.log(xx), Kc); Kinf = float(Kc[np.searchsorted(xx, 0.96 * xs)])
    Kx = lambda x: float(Ksp(np.log(x))) if x < 0.96 * xs else Kinf
    f = lambda x: fJ(x, Kx(x))
    pts = [xc0, 1.0, 2.0, 4.0, 0.8 * xs, 0.95 * xs]
    I += sum(quad(f, a, c, limit=400, epsabs=0, epsrel=1e-12)[0] for a, c in zip(pts[:-1], pts[1:]))
    D = xs - 0.95 * xs
    # tail [0.95 x*, x*]: b = 0 there, so g_eps = g E, E = exp(eps A K(x*)), w_eps = w; m = |w|/(g E) is written with
    # delta = x* - x as A delta (2L - delta)/(L^2 x E) (no cancellation); substitution delta = D tau^(1/beta)
    E_ = np.exp(eps * A * Kinf)
    def ftail(dl):
        x = xs - dl
        g1, g2, w2, w3 = G1(x), G2(x), W2(x), W3(x); g = GS(x)
        qq = (E_ * g2 - w3) / (2 * E_ ** 3 * g ** 3) - 3 * (E_ * g1 - w2) * E_ * g1 / (2 * E_ ** 4 * g ** 4)
        return qq * (A * dl * (2 * L - dl) / (L ** 2 * x * E_)) ** (beta - 1)
    I += quad(lambda tau: ftail(D * tau ** (1 / beta)) * D / beta * tau ** (1 / beta - 1) if tau > 0 else 0.0, 0, 1,
              limit=400, epsrel=1e-12)[0]
    return xs ** (p3 - 2) / (3 * N) * I


def traces(eps):
    z = np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'exclusion_certificates', 'reference_fit', 'data', 'c6g_traces.npz'), allow_pickle=True)
    xg = z['x'] * (L / 8.6000638)
    we = wS * (1 + eps * b_an * chi)
    F = [sp.lambdify(t, sp.diff(we, t, k), 'numpy') for k in range(3)]
    return xg, F[0](xg), F[1](xg), F[2](xg), (A + 1) / 2


b0 = B3nat(0.0)
SA = 6 * A * (4 * A - 3) / (8 * A - 1)
print('base exact %.8f (closed form %.8f)' % (b0, 0.530667 * (1 - SA / L ** 2)), flush=True)
bp, bm = B3nat(e0), B3nat(-e0)
tp, tm = traces(e0), traces(-e0)
sp_, sm = b3core.b3_median(*tp), b3core.b3_median(*tm)
o = (b3core.b3_one(*tp)[0] - b3core.b3_one(*tm)[0]) / (2 * e0)
print('b = %s, e %.0e: exact dB3nat/deps %.6e | med-orig %.6e med-ibp %.6e one %.6e | ranges(+) orig [%.4f, %.4f] ibp [%.4f, %.4f]' % (
    bexpr, e0, (bp - bm) / (2 * e0), (sp_['orig_median'] - sm['orig_median']) / (2 * e0),
    (sp_['ibp_median'] - sm['ibp_median']) / (2 * e0), o, sp_['orig_min'], sp_['orig_max'], sp_['ibp_min'], sp_['ibp_max']))
