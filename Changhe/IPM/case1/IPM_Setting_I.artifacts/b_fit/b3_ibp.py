"""w-only finite-part B_3 in two algebraically equivalent forms (lead, analysis.md section 12).
  (orig) B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^(beta-1) dx                       needs w''' (through a2')
  (ibp)  B_3 = -((1-beta)/(3N)) f.p. int_0^{x*} (a2/g^3 - kappa) m^(beta-2) A_g/g dx    needs only w''
with m = -w/g, (w/g)' = A_g/g (this defines g from w, g ~ x^2 at 0), a2 = (g' - w'')/2, kappa = a2(x*)/g(x*)^3,
N = A^beta (g0 = 1), beta = 2/A, A = 2c_l - 1, p3 = 6 + beta. A_g = A gives the formula of analysis 7.3 / SPEC R10;
A_g(x) = A + (mu1 - A)(x/x*)^2 with mu1 = w'(x*) removes the pole of g'/g at x* that a trial with h(P) != 1 has
(a regularization of size (mu1 - A)/A ~ 1e-5).
Quadrature: [0, xc] even-polynomial least-squares fit of x^(5+beta) f (and x^beta f for the kappa part) on [x_lo, xc],
exact finite part; [xc, x*] Gauss-Jacobi with weight (x* - x)^(beta-1).
Usage: python3 b3_ibp.py test            (manufactured compatible data, exact orig = ibp check)
       python3 b3_ibp.py fields.npz      (export with axis_x, axis_w, axis_w_prime, c_l)"""
import sys
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
from scipy.special import roots_jacobi, roots_legendre


class WOnly:
    def __init__(self, w, wp, wpp, cl, xs, Ag='A', wppp=None):
        self.w, self.wp, self.wpp, self.cl, self.xs = w, wp, wpp, cl, xs
        A = 2 * cl - 1
        self.A, self.beta = A, 2 / A
        self.p3 = 6 + self.beta
        self.N = A ** self.beta
        mu1 = float(wp(xs))
        self.mu1 = mu1
        if Ag == 'A':
            self.Ag = lambda x: A + 0 * np.asarray(x, float)
        else:
            self.Ag = lambda x: A + (mu1 - A) * (np.asarray(x, float) / xs) ** 2
        # ln(g/x^2) = int_0^x e(t) dt, e = (w' - A_g)/w - 2/t (regular at 0; at x* regular only if A_g(x*) = w'(x*))
        xx = np.concatenate([np.geomspace(1e-4 * xs, 0.02 * xs, 60), np.linspace(0.02 * xs, xs, 3000)[1:]])
        if Ag == 'A':
            xx = xx[np.abs(xx - xs) > 2e-3 * xs]
        e = (wp(xx) - self.Ag(xx)) / w(xx) - 2 / xx
        Es = CubicSpline(xx ** 2, e / xx)                      # e odd: e = x E(x^2)
        Ei = Es.antiderivative()
        self.lg = lambda t: 0.5 * (Ei(np.asarray(t) ** 2) - Ei(0.0))
        self.g = lambda t: np.asarray(t) ** 2 * np.exp(self.lg(t))
        xg = xx[np.abs(xx - xs) > (2e-2 if Ag == 'A' else 1e-3) * xs]
        gp = self.g(xg) * (wp(xg) - self.Ag(xg)) / w(xg)
        gps = CubicSpline(xg ** 2, gp / xg)                    # g' odd
        self.gp = lambda t: np.asarray(t) * gps(np.asarray(t) ** 2)
        a2 = (self.gp(xx) - wpp(xx)) / 2
        self.a2s = CubicSpline(xx ** 2, a2 / xx)               # a2 odd
        self.a2 = lambda t: np.asarray(t) * self.a2s(np.asarray(t) ** 2)
        self.a2p = lambda t: self.a2s(np.asarray(t) ** 2) + 2 * np.asarray(t) ** 2 * self.a2s(np.asarray(t) ** 2, 1)
        if wppp is not None:                                   # exact data: a2' from w''' and g''
            def a2p_exact(t):
                t = np.asarray(t, float)
                W, W1, W2 = w(t), wp(t), wpp(t)
                G, G1 = self.g(t), self.gp(t)
                L = (W1 - self.Ag(t)) / W
                dAg = 2 * (mu1 - A) * t / xs ** 2 if Ag != 'A' else 0.0
                Lp = ((W2 - dAg) * W - (W1 - self.Ag(t)) * W1) / W ** 2
                G2 = G1 * L + G * Lp
                return (G2 - wppp(t)) / 2
            self.a2p = a2p_exact
            self.a2 = lambda t: (self.g(t) * (wp(t) - self.Ag(t)) / w(t) - wpp(t)) / 2
        # kappa = a2(x*)/g(x*)^3 with g'(x*) = g(x*) (w''(x*) - A_g'(x*)) / w'(x*) (limit of g (w' - A_g)/w)
        dAg_s = 0.0 if Ag == 'A' else 2 * (mu1 - A) / xs
        gp_s = float(self.g(xs)) * (float(wpp(xs)) - dAg_s) / mu1
        self.kappa = (gp_s - float(wpp(xs))) / 2 / float(self.g(xs)) ** 3

    def m(self, x):
        return -self.w(x) / self.g(x)

    def f_orig(self, x):
        g = self.g(x)
        q = self.a2p(x) / g ** 3 - 3 * self.a2(x) * self.gp(x) / g ** 4
        return q * self.m(x) ** (self.beta - 1)

    def f_ibp1(self, x):
        g = self.g(x)
        return self.a2(x) / g ** 3 * self.m(x) ** (self.beta - 2) * self.Ag(x) / g

    def f_ibp2(self, x):
        g = self.g(x)
        return self.m(x) ** (self.beta - 2) * self.Ag(x) / g


def fp_near0(f, expo, xlo, xc, K, n=300):
    """f.p. int_0^xc f, f = x^expo * (even polynomial of degree 2K) fitted on [xlo, xc]."""
    x = np.sqrt(np.linspace(xlo ** 2, xc ** 2, n))
    Q = f(x) / x ** expo
    s = (x / xc) ** 2
    c = np.polynomial.polynomial.polyfit(s, Q, K)
    fit = np.max(np.abs(np.polynomial.polynomial.polyval(s, c) - Q)) / np.max(np.abs(Q))
    e = expo + 2 * np.arange(K + 1) + 1
    return float(np.sum(c * xc ** (expo + 1) / e)), fit


def end_piece(S, xc, xs, beta, n):
    t, wt = roots_jacobi(n, beta - 1, 0.0)
    x = xc + (xs - xc) * (1 + t) / 2
    return float(((xs - xc) / 2) ** beta * np.sum(wt * S(x)))


def b3_both(d, xc, xlo, K, n):
    be, xs = d.beta, d.xs
    # orig
    I0, fit0 = fp_near0(d.f_orig, -5 - be, xlo, xc, K)
    S0 = lambda x: d.f_orig(x) / (xs - x) ** (be - 1)
    Bo = (I0 + end_piece(S0, xc, xs, be, n)) / (3 * d.N)
    # ibp
    J1, fit1 = fp_near0(d.f_ibp1, -5 - be, xlo, xc, K)
    J2, fit2 = fp_near0(d.f_ibp2, -be, xlo, xc, K)
    S1 = lambda x: (d.f_ibp1(x) - d.kappa * d.f_ibp2(x)) / (xs - x) ** (be - 1)
    J3 = end_piece(S1, xc, xs, be, n)
    Bi = -(1 - be) / (3 * d.N) * (J1 - d.kappa * J2 + J3)
    return Bo, Bi, max(fit0, fit1, fit2)


def run(d, label):
    xs = d.xs
    nat = xs ** (d.p3 - 2)
    print(f'{label}: c_l {d.cl:.10f} x* {xs:.8f} mu1 {d.mu1:.8f} (A {d.A:.8f}, (mu1-A)/A {(d.mu1 - d.A) / d.A:.2e}) '
          f'kappa {d.kappa:.6e}; B_3 in natural units (x B_3 x*^(p3-2))')
    rows = []
    for xc in (0.3, 0.4):
        for xlo in (0.03, 0.05):
            for K in (7, 9):
                for n in (40, 80):
                    Bo, Bi, fit = b3_both(d, xc * xs, xlo * xs, K, n)
                    rows.append((xc, xlo, K, n, Bo * nat, Bi * nat, fit))
                    print(f'  xc {xc} xlo {xlo} K {K} n {n}:  orig {Bo * nat: .5f}  ibp {Bi * nat: .5f}  near-0 fit {fit:.1e}')
    o = np.array([r[4] for r in rows]); i = np.array([r[5] for r in rows])
    print(f'  SUMMARY {label}: orig median {np.median(o):.4f} range [{o.min():.4f}, {o.max():.4f}];  '
          f'ibp median {np.median(i):.4f} range [{i.min():.4f}, {i.max():.4f}]')
    return rows


if __name__ == '__main__':
  if True:
    if sys.argv[1] == 'test':
        import sympy as sp
        X = sp.symbols('x')
        for cl in (2.2, 5.5763218720):
            A = 2 * cl - 1
            ws = -A * X * (1 - X ** 2) / (1 + X ** 2) * (1 + 0.3 * X ** 2 * (1 - X ** 2))
            wd = [sp.lambdify(X, sp.diff(ws, X, k), 'numpy') for k in range(4)]
            d = WOnly(wd[0], wd[1], wd[2], cl, 1.0, Ag='A', wppp=wd[3])
            run(d, f'manufactured c_l={cl} (exact derivatives)')
            d2 = WOnly(wd[0], wd[1], wd[2], cl, 1.0, Ag='A')
            run(d2, f'manufactured c_l={cl} (spline a2)')
    elif sys.argv[1].endswith('.txt'):
        # text axis file (x, w columns; header '# ... c_l = <value>; ...'): derivatives from the spline w = x S(x^2)
        import re
        cl = float(re.search(r'c_l = ([0-9.]+)', open(sys.argv[1]).readline()).group(1))
        zz = np.loadtxt(sys.argv[1]); x, wv = zz[:, 0], zz[:, 1]
        Ss = CubicSpline(x ** 2, wv / x)
        w = lambda t: np.asarray(t) * Ss(np.asarray(t) ** 2)
        wp = lambda t: Ss(np.asarray(t) ** 2) + 2 * np.asarray(t) ** 2 * Ss(np.asarray(t) ** 2, 1)
        wpp = lambda t: 6 * np.asarray(t) * Ss(np.asarray(t) ** 2, 1) + 4 * np.asarray(t) ** 3 * Ss(np.asarray(t) ** 2, 2)
        xs = brentq(w, 1.0, 0.99 * x[-1])
        run(WOnly(w, wp, wpp, cl, xs, Ag='mu1'), sys.argv[1].split('/')[-1] + ' A_g=mu1')
    else:
        z = np.load(sys.argv[1])
        cl = float(z['c_l'])
        x = z['axis_x']; sel = x < 40; x = x[sel]
        ws_ = CubicSpline(x ** 2, z['axis_w'][sel] / x)
        wps = CubicSpline(x ** 2, z['axis_w_prime'][sel])
        w = lambda t: np.asarray(t) * ws_(np.asarray(t) ** 2)
        wp = lambda t: wps(np.asarray(t) ** 2)
        wpp = lambda t: 2 * np.asarray(t) * wps(np.asarray(t) ** 2, 1)
        xs = brentq(w, 1.0, 30.0)
        for Ag in (('mu1',) if 'mu1only' in sys.argv else ('A', 'mu1')):
            run(WOnly(w, wp, wpp, cl, xs, Ag=Ag), f'{"/".join(sys.argv[1].split("/")[-2:])} A_g={Ag}')
