"""verifier: fred11 04-adjoint checks (lead request (l), item F5), own code.
 (1) sympy: delta Q formula (2) and DB_3 integrand (3) for a general variation v (function symbols).
 (2) R12, A = 10.150725, L = 8.6: the weight lambda of (5) (local terms by sympy, the Volterra term by quadrature);
     DB_3[v] = int lambda v for the compact bump v = exp(-1/((x-2)(5-x))) on (2, 5), against central differences of
     B_3[w_R12 + eps v] (eps = +-1e-10, 34 digits; v = 0 near 0 so the finite part at 0 does not move, g rebuilt on
     (2, 5), g = K g_R12 beyond 5).
 (3) lambda x^(8+beta) / kappa_A as x -> 0 (6); lambda s^(4-beta) against the coefficient of (7) as s = L - x -> 0.
 (4) the Poisson identity behind (12): (1/2) d_u (P_v * sgn|x|^(-a))(u) = (1/pi) Gamma(1-a) cos(pi a/2) Gamma(1+a)
     Re (v - i u)^(-1-a), checked by quadrature at a = 0.5 (ordinary integral), and the constant of (12) from it at
     a = 8 + beta (analytic continuation in a).
"""
import time
import mpmath as mp
import sympy as sp

out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
t0 = time.time()

# (1)
x, A_, b_, J = sp.symbols('x A b J')
w, g, v = [sp.Function(n)(x) for n in ('w', 'g', 'v')]
gp = (sp.diff(w, x) - A_) * g / w                       # axis law g'/g = (w' - A)/w
Q = (sp.diff(g, x) - sp.diff(w, x, 2)) / (2 * g**3)
z = v / w + J                                            # delta g / g, J' = A v / w^2
zp = sp.diff(v / w, x) + A_ * v / w**2
dg, dgp = z * g, zp * g + z * sp.diff(g, x)
dQ = (dgp - sp.diff(v, x, 2)) / (2 * g**3) - 3 * Q * z
D = sp.diff(g, x) / (2 * g**3) - 3 * Q
dQ2 = -sp.diff(v, x, 2) / (2 * g**3) + sp.diff(v, x) / (2 * g**2 * w) - 3 * Q * v / w + D * J
res = sp.simplify((dQ - dQ2).subs(sp.Derivative(g, x), gp))
P('(1) delta Q - formula (2), with g\' = (w\' - A) g/w:', res)
P('(1) delta(g\'/g) - delta((w\' - A)/w) with z = v/w + J:', sp.simplify(zp - (sp.diff(v, x) / w - (sp.diff(w, x) - A_) * v / w**2)))
m = -w / g
dm_over_m = v / w - z
P('(1) delta m / m + J =', sp.simplify(dm_over_m + J), '; delta(Q\' m^(b-1)) = M[(dQ)\' - (b-1) Q\' J] since delta M = (b-1) M delta m/m')

# (2)
mp.mp.dps = 34
As, Ls = sp.Rational('10.150725'), sp.Rational('8.6')
A, L = mp.mpf('10.150725'), mp.mpf('8.6')
be = 2 / A
bs = sp.Symbol('b', positive=True)     # beta kept symbolic (exact rational exponent overflows sympy printing)
u = x / Ls
wR = -As * x * (1 - u**2) / (1 + u**2)
gR = x**2 / (1 + u**2)
mR = sp.cancel(-wR / gR)
QR = sp.cancel((sp.diff(gR, x) - sp.diff(wR, x, 2)) / (2 * gR**3))
M = mR**(bs - 1)
Mp = sp.diff(M, x)
DR = sp.diff(gR, x) / (2 * gR**3) - 3 * QR
ER = sp.cancel(sp.diff(sp.diff(gR, x) / (2 * gR**3), x) - (bs + 2) * sp.diff(QR, x))
loc = sp.diff(Mp / (2 * gR**3), x, 2) + sp.diff(Mp / (2 * gR**2 * wR), x) + 3 * Mp * QR / wR + As * M * DR / wR**2
locf0 = sp.lambdify((x, bs), loc, 'mpmath')
Ef0 = sp.lambdify((x, bs), ER, 'mpmath')
locf = lambda t: locf0(t, be)
Ef = lambda t: Ef0(t, be)
wRf = sp.lambdify(x, wR, 'mpmath')
pref = 1 / (3 * A**be)


def Mtau(xx, tau):
    return (A * tau * (L + xx) / (L**2 * xx))**(be - 1)


def int_ME2(x0):
    s1 = (L - x0)**be

    def f(s):
        tau = s**(1 / be)
        xx = L - tau
        # M dt = (A (L+x)/(L^2 x))^(beta-1) tau^(beta-1) dtau, tau^(beta-1) dtau = ds/beta
        return (A * (L + xx) / (L**2 * xx))**(be - 1) * Ef(xx) / be
    return mp.quad(f, [0, s1 / 2, s1])


def lam(xx, IME):
    return pref * (locf(xx) + A / wRf(xx)**2 * IME)


NG = 24


def gl_nodes(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        zz = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), zz
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * zz * p1 - (k - 1) * p0) / k
            dp = n * (zz * p1 - p0) / (zz**2 - 1)
            dz = p1 / dp
            zz -= dz
            if abs(dz) < mp.mpf(10)**(-40):
                break
        p0, p1 = mp.mpf(1), zz
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * zz * p1 - (k - 1) * p0) / k
        dp = n * (zz * p1 - p0) / (zz**2 - 1)
        xs.append(zz)
        ws.append(2 / ((1 - zz**2) * dp**2))
    return xs, ws


GX, GW = gl_nodes(NG)


def gl(f, a, b):
    h = (b - a) / 2
    return h * mp.fsum(wt * f(a + h * (zz + 1)) for zz, wt in zip(GX, GW))


x1, x2 = mp.mpf(2), mp.mpf(5)
BR = sorted(set([x1 + mp.mpf('0.25') * mp.mpf(2)**-k for k in range(1, 12)] + [x2 - mp.mpf('0.25') * mp.mpf(2)**-k for k in range(1, 12)]
                + [x1 + mp.mpf(j) / 4 for j in range(13)]))
vs = sp.exp(-1 / ((x - 2) * (5 - x)))
vf = [sp.lambdify(x, sp.diff(vs, x, k), 'mpmath') for k in range(4)]
wRd = [sp.lambdify(x, sp.diff(wR, x, k), 'mpmath') for k in range(4)]
gRd = [sp.lambdify(x, sp.diff(gR, x, k), 'mpmath') for k in range(3)]
mRf = sp.lambdify(x, mR, 'mpmath')

# lambda side
I5 = int_ME2(x2)
P('(2) int_5^L M E dt = %s' % mp.nstr(I5, 20))
cum = [mp.mpf(0)] * len(BR)                 # int_{BR[i]}^5 M E
for i in range(len(BR) - 2, -1, -1):
    cum[i] = cum[i + 1] + gl(lambda t: mRf(t)**(be - 1) * Ef(t), BR[i], BR[i + 1])
DBl = mp.mpf(0)
for i in range(len(BR) - 1):
    a, b = BR[i], BR[i + 1]
    h = (b - a) / 2
    for zz, wt in zip(GX, GW):
        t = a + h * (zz + 1)
        IME = I5 + cum[i + 1] + gl(lambda s: mRf(s)**(be - 1) * Ef(s), t, b)
        DBl += h * wt * lam(t, IME) * vf[0](t)
P('(2) DB_3[v] = int lambda v = %s  (%.0f s)' % (mp.nstr(DBl, 20), time.time() - t0))


# direct side
def F(eps):
    eps = mp.mpf(eps)

    def W(t):
        return [wRd[k](t) + eps * vf[k](t) for k in range(4)]

    def efun(t):
        w0, w1 = W(t)[:2]
        return (w1 - A) / w0

    def integrand(t, lg):
        w0, w1, w2, w3 = W(t)
        gg = mp.exp(lg)
        g1 = (w1 - A) * gg / w0
        g2 = ((w2 * gg + (w1 - A) * g1) * w0 - (w1 - A) * gg * w1) / w0**2
        Qp = (g2 - w3) / (2 * gg**3) - 3 * (g1 - w2) * g1 / (2 * gg**4)
        return Qp * (-w0 / gg)**(be - 1)
    lg0, I = mp.log(gRd[0](x1)), mp.mpf(0)
    for a, b in zip(BR[:-1], BR[1:]):
        h = (b - a) / 2
        for zz, wt in zip(GX, GW):
            t = a + h * (zz + 1)
            I += h * wt * integrand(t, lg0 + gl(efun, a, t))
        lg0 += gl(efun, a, b)
    K = mp.exp(lg0) / gRd[0](x2)
    s1 = (L - x2)**be

    def fend(s):
        tau = s**(1 / be)
        xx = L - tau
        g0, g1, g2 = [K * gRd[k](xx) for k in range(3)]
        w2, w3 = wRd[2](xx), wRd[3](xx)
        Qp = (g2 - w3) / (2 * g0**3) - 3 * (g1 - w2) * g1 / (2 * g0**4)
        return Qp * (A * (L + xx) / (K * L**2 * xx))**(be - 1) / be
    return pref * (I + mp.quad(fend, [0, s1 / 2, s1])), K


for e in ['1e-10', '1e-12']:
    Fp, Kp = F(e)
    Fm, Km = F('-' + e)
    DBd = (Fp - Fm) / (2 * mp.mpf(e))
    P('(2) eps = %s: central difference %s, K(+eps) - 1 = %s; minus int lambda v: %s (rel %s)  (%.0f s)' % (
        e, mp.nstr(DBd, 20), mp.nstr(Kp - 1, 4), mp.nstr(DBd - DBl, 3), mp.nstr(abs(DBd - DBl) / abs(DBl), 3), time.time() - t0))

# (3)
kap = (1 - be) * (6 + be) * (7 + be) / (6 * A)
P('(3) kappa_A = %s' % mp.nstr(kap, 15))
for xx in ['0.04', '0.02', '0.01', '0.005']:
    xx = mp.mpf(xx)
    r = lam(xx, int_ME2(xx)) * xx**(8 + be) / kap
    P('(3) x = %s: lambda x^(8+beta)/kappa_A = %s, (ratio - 1)/x^2 = %s' % (mp.nstr(xx, 3), mp.nstr(r, 15), mp.nstr((r - 1) / xx**2, 8)))
gs = L**2 / 2
k = A / gs
c7 = -(be - 1) * (be - 3) * k**(be - 1) / (6 * A**be * gs**3) * (be - 2 + gs / A)
for s in ['1e-2', '1e-3', '1e-4', '1e-5']:
    s = mp.mpf(s)
    xx = L - s
    r = lam(xx, int_ME2(xx)) * s**(4 - be) / c7
    P('(3) s = L - x = %s: lambda s^(4-beta) / c7 = %s, (ratio - 1)/s = %s   (c7 = %s)' % (mp.nstr(s, 3), mp.nstr(r, 15), mp.nstr((r - 1) / s, 8), mp.nstr(c7, 10)))

# (4)
mp.mp.dps = 25
a = mp.mpf('0.5')
for uu, vv in [('0.7', '0.4'), ('-1.3', '0.25'), ('2', '1.5')]:
    uu, vv = mp.mpf(uu), mp.mpf(vv)
    # (1/2) d_u int P_v(u - x) sgn(x)|x|^(-a) dx = (1/2) int d_u P_v(u - x) sgn(x)|x|^(-a) dx
    dP = lambda X: -2 * (uu - X) * vv / (mp.pi * ((uu - X)**2 + vv**2)**2)
    f = lambda X: dP(X) * mp.sign(X) * abs(X)**(-a) / 2
    lhs = mp.quad(f, [-mp.inf, -1, 0, 1, mp.inf]) if abs(uu) > 1 else mp.quad(f, [-mp.inf, -1, 0, uu, 1, mp.inf])
    rhs = mp.gamma(1 - a) * mp.cos(mp.pi * a / 2) * mp.gamma(1 + a) / mp.pi * mp.re((vv - 1j * uu)**(-1 - a))
    P('(4) a = 0.5, (u, v) = (%s, %s): quadrature %s, formula %s, diff %s' % (uu, vv, mp.nstr(lhs, 15), mp.nstr(rhs, 15), mp.nstr(lhs - rhs, 3)))
mp.mp.dps = 34
a = 8 + be
c12 = mp.gamma(1 - a) * mp.cos(mp.pi * a / 2) * mp.gamma(1 + a) / mp.pi * kap / 2
P('(4) constant of (12) from the identity at a = 8 + beta, times kappa_A/2: %s; fred11 kappa_A (8+beta)/(4 sin(pi beta/2)): %s' % (
    mp.nstr(c12, 15), mp.nstr(kap * (8 + be) / (4 * mp.sin(mp.pi * be / 2)), 15)))
open('verifier/early_runs/check_fred11c.log', 'w').write('\n'.join(out) + '\n')
