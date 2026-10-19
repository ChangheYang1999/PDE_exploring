"""Verifier's own evaluation of the integrated-by-parts w-only B_3 (lead analysis.md section 12), verifier.

  B_3 = -((1 - beta)/(3N)) f.p. int_0^{x*} (a2/g^3 - kappa) m^(beta - 2) (A_g/g) dx,
  m = -w/g, g'/g = (w' - A_g)/w, g ~ x^2 at 0, a2 = (g' - w'')/2, kappa = a2(x*)/g(x*)^3, beta = 2/A, N = A^beta,
  A_g = A + (mu1 - A)(x/x*)^2 (mu1 = w'(x*)).
Independent of the lead's notes/b3_ibp/b3_ibp.py: data stay on the verifier's log grid (traces from code/vb3w.py's inverse,
saved by scratch/mk_traces.py); g by cumulative integration in u = log x of a spline of e = (w' - A_g)/w - 2/x;
near 0: least-squares fit of x^(5+beta) J1 and x^beta J2 by Legendre polynomials in (x/xc)^2 on grid points, exact finite
parts; middle: Gauss-Legendre in u of a spline of x J; end: J = (x* - x)^(beta - 1) S, S fitted by a low-degree polynomial
(or splined) on grid points left of x*, integrated after the substitution s = (x* - x)^beta (Gauss-Legendre in s).
Also evaluates the original form (1/(3N)) f.p. int (a2/g^3)' m^(beta - 1) with the same machinery (a2' from the spline).
Usage: python3 vb3ibp.py traces.npz [out.json]    |    python3 vb3ibp.py test
"""
import sys, json, itertools, warnings
warnings.simplefilter("ignore")
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq


def build(x, w, wp, wpp, cl, delta=1e-3):
    A = 2 * cl - 1
    be = 2 / A
    u = np.log(x)
    ws = CubicSpline(u, w / x)
    jz = np.where((x[:-1] > 0.5) & (np.sign(w[:-1]) != np.sign(w[1:])))[0][0]      # first sign change of w past 0.5
    xs = brentq(lambda t: ws(np.log(t)), x[jz], x[jz + 1])
    wps = CubicSpline(u, wp)
    mu1 = float(wps(np.log(xs)))
    Ag = lambda t: A + (mu1 - A) * (t / xs) ** 2
    keep = np.abs(x - xs) > delta * xs
    e = (wp - Ag(x)) / w - 2 / x
    es = CubicSpline(u[keep], (e * x)[keep])               # e x as a function of u (d x = x d u)
    cum = es.antiderivative()
    lg = lambda t: cum(np.log(t)) - cum(u[0]) + 0.5 * e[0] * x[0]   # int_0^x e, e = O(x) below x[0]
    g = x ** 2 * np.exp(lg(x))
    gp = np.where(keep, g * (wp - Ag(x)) / w, np.nan)
    gps = CubicSpline(u[keep], gp[keep])
    gp = gps(u)
    a2 = (gp - wpp) / 2
    a2s = CubicSpline(u, a2)
    gs = CubicSpline(u, g)
    kappa = float(a2s(np.log(xs)) / gs(np.log(xs)) ** 3)
    a2p = a2s(u, 1) / x
    m = -w / g
    J1 = a2 / g ** 3 * np.abs(m) ** (be - 2) * Ag(x) / g
    J2 = np.abs(m) ** (be - 2) * Ag(x) / g
    qd = a2p / g ** 3 - 3 * a2 * gp / g ** 4
    Jo = qd * np.abs(m) ** (be - 1)
    return dict(x=x, u=u, A=A, be=be, xs=xs, mu1=mu1, kappa=kappa, J1=J1, J2=J2, Jo=Jo, N=A ** be, p3=6 + be,
                g=g, a2=a2, keep=keep)


def fp0(x, f, expo, xlo, xc, K):
    sel = (x >= xlo) & (x <= xc)
    s = (x[sel] / xc) ** 2
    Q = f[sel] / x[sel] ** expo
    V = np.polynomial.legendre.legvander(2 * s - 1, K)
    cL, *_ = np.linalg.lstsq(V, Q, rcond=None)
    fit = float(np.abs(V @ cL - Q).max() / np.abs(Q).max())
    cm = np.polynomial.polynomial.Polynomial(np.polynomial.legendre.leg2poly(cL)).convert()  # in z = 2s - 1
    cs = np.polynomial.polynomial.Polynomial([-1.0, 2.0])
    P = np.polynomial.polynomial.Polynomial(cm.coef)(cs)                 # polynomial in s
    c = P.coef
    j = np.arange(len(c))
    val = float(np.sum(c * xc ** (expo + 1) / (expo + 2 * j + 1)))      # int_0^xc x^expo (x/xc)^(2j) dx
    return val, fit


def mid(d, f, xc, xe, nq=200):
    sel = d['keep'] & (d['x'] > xc / 1.15) & (d['x'] < xe * 1.03)      # keep the x* singularity out of the spline
    sp = CubicSpline(d['u'][sel], (f * d['x'])[sel])
    gx, gw = np.polynomial.legendre.leggauss(nq)
    a, b = np.log(xc), np.log(xe)
    uq = 0.5 * (a + b) + 0.5 * (b - a) * gx
    return float(np.sum(sp(uq) * gw) * 0.5 * (b - a))


def endp(d, f, xe, expo_end, mode, deg=6, nq=80):
    """int_xe^x* f, f = (x* - x)^expo_end S(x), S smooth up to x*."""
    x, xs = d['x'], d['xs']
    sel = (x > xe - 0.03 * xs) & (x < xs) & d['keep']
    S = f[sel] * (xs - x[sel]) ** (-expo_end)
    q = expo_end + 1
    D = xs - xe
    gx, gw = np.polynomial.legendre.leggauss(nq)
    sq = 0.5 * D ** q * (gx + 1)
    xq = xs - sq ** (1 / q)
    if mode == 'poly':
        pc = np.polyfit(x[sel] - xs, S, deg)
        Sq = np.polyval(pc, xq - xs)
        S1 = float(pc[-1])
    else:
        sp = CubicSpline(x[sel], S)
        Sq = sp(xq)
        S1 = float(sp(xs))
    return float(np.sum(Sq * gw) * 0.5 * D ** q / q), S1


def b3_variants(d, label=''):
    xs, be = d['xs'], d['be']
    nat = xs ** (d['p3'] - 2)
    rows = []
    for xcf, xlof, K, xef, mode in itertools.product((0.25, 0.35), (0.02, 0.04), (6, 8), (0.85, 0.92), ('poly', 'spline')):
        xc, xlo, xe = xcf * xs, xlof * xs, xef * xs
        J = d['J1'] - d['kappa'] * d['J2']
        a1, f1 = fp0(d['x'], d['J1'], -5 - be, xlo, xc, K)
        a2, f2 = fp0(d['x'], d['J2'], -be, xlo, xc, K)
        mi = mid(d, J, xc, xe)
        en, S1 = endp(d, J, xe, be - 1, mode)
        Bi = -(1 - be) / (3 * d['N']) * (a1 - d['kappa'] * a2 + mi + en)
        o0, fo = fp0(d['x'], d['Jo'], -5 - be, xlo, xc, K)
        mo = mid(d, d['Jo'], xc, xe)
        eo, _ = endp(d, d['Jo'], xe, be - 1, mode)
        Bo = (o0 + mo + eo) / (3 * d['N'])
        rows.append(dict(xc=xcf, xlo=xlof, K=K, xe=xef, end=mode, ibp=Bi * nat, orig=Bo * nat, fit=max(f1, f2), fit_orig=fo,
                         parts_ibp=[x_ * nat * -(1 - be) / (3 * d['N']) for x_ in (a1 - d['kappa'] * a2, mi, en)]))
    bi = np.array([r['ibp'] for r in rows])
    bo = np.array([r['orig'] for r in rows])
    summ = dict(label=label, x_star=xs, mu1=d['mu1'], A=d['A'], rel_mu1_A=(d['mu1'] - d['A']) / d['A'], kappa=d['kappa'],
                ibp_median=float(np.median(bi)), ibp_min=float(bi.min()), ibp_max=float(bi.max()),
                orig_median=float(np.median(bo)), orig_min=float(bo.min()), orig_max=float(bo.max()),
                worst_fit=float(max(r['fit'] for r in rows)))
    return summ, rows


def test():
    import sympy as sp
    X = sp.symbols('x')
    out = []
    for cl in (2.2, 5.5763218720):
        A = 2 * cl - 1
        ws = -A * X * (1 - X ** 2) / (1 + X ** 2) * (1 + 0.3 * X ** 2 * (1 - X ** 2))
        f = [sp.lambdify(X, sp.diff(ws, X, k), 'numpy') for k in range(3)]
        for N in (1500, 3000):
            x = np.exp(np.linspace(np.log(1e-4), np.log(1.6), N))
            d = build(x, f[0](x), f[1](x), f[2](x), cl)
            s, _ = b3_variants(d, 'manufactured c_l=%g N=%d' % (cl, N))
            out.append(s)
            print(json.dumps(s))
    return out


if __name__ == '__main__':
    if sys.argv[1] == 'test':
        test()
    else:
        z = np.load(sys.argv[1], allow_pickle=True)
        res = {}
        for key in ('wpp_ode', 'wpp_fd'):
            d = build(z['x'], z['w'], z['wp'], z[key], float(z['c_l']))
            s, rows = b3_variants(d, sys.argv[1] + ' ' + key)
            res[key] = dict(summary=s, rows=rows)
            print(json.dumps(s))
        if len(sys.argv) > 2:
            json.dump(res, open(sys.argv[2], 'w'), indent=1, default=float)
