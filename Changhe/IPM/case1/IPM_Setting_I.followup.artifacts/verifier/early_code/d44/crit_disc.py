"""verifier D44: the critical-order discontinuity of B_3 among compatible axis data (fred5 (1b), equations (8)-(10);
FINAL_REPORT 6.4 'Conditioning', 'not checked by the verifier').  Own code.
Reference: R12, A = 10.150725, L = x* = 8.6, w0 = -A x (1-u^2)/(1+u^2), g0 = x^2/(1+u^2), u = x/L.
B_3 = (1/(3 A^beta)) f.p. int_0^L Q' m^(beta-1) dx, Q = (g' - w'')/(2 g^3), m = -w/g, g rebuilt by w g' = (w' - A) g
with g/x^2 -> 1 at 0.  (This equals the convergent form of 6.3.1 (i) after one integration by parts; the boundary term
at L vanishes for w smooth near L.)
(a) origin bumps h_eps = t eps^(7+beta) phi(x/eps), phi = exp(-1/((u-1)(2-u))) on (1, 2): the exact difference
    D(eps) = B_3[w0 + h_eps] - B_3[w0] (an ordinary integral over [eps, L], since nothing changes on (0, eps)) against
    the claimed limit kappa_A t int_1^2 phi u^(-8-beta) du, kappa_A = (1-beta)(6+beta)(7+beta)/(6A), and the C^m norms
    of h_eps (m = 0..7) to show they tend to 0.
(b) endpoint bumps h_eps = t eps^(3-beta) phi((L-x)/eps): D(eps) against the claimed limit
    (beta-1)(3-beta)/(6 A g_P^(beta+2)) (g_P/A - (2-beta)) t int_1^2 phi u^(beta-4) du, g_P = g0(L) = L^2/2.
"""
import sys, time
import mpmath as mp

mp.mp.dps = 40
A, L = mp.mpf('10.150725'), mp.mpf('8.6')
be = 2 / A
pref = 1 / (3 * A**be)
t0 = time.time()
out = []


def P(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


# jets [f, f', ..., f^(n-1)] (mp.taylor returns f^(k)/k!, so rescale by k!)
def jet(f, x, n):
    return [c * mp.factorial(k) for k, c in enumerate(mp.taylor(f, x, n - 1))]


def w0d(x, n=4):
    return jet(lambda y: -A * y * (1 - (y / L)**2) / (1 + (y / L)**2), x, n)


def g0d(x, n=3):
    return jet(lambda y: y**2 / (1 + (y / L)**2), x, n)


def phid(u, n=4):
    # derivatives of exp(-1/((u-1)(2-u))) at u in (1, 2)
    return jet(lambda v: mp.exp(-1 / ((v - 1) * (2 - v))), u, n)


def fint(w, g):
    """Q' m^(beta-1) from jets w = (w, w', w'', w'''), g = (g, g', g'')."""
    w0, w1, w2, w3 = w
    g0, g1, g2 = g
    Qp = (g2 - w3) / (2 * g0**3) - 3 * (g1 - w2) * g1 / (2 * g0**4)
    return Qp * (-w0 / g0)**(be - 1)


def gjet(w, lg):
    w0, w1, w2 = w[:3]
    gg = mp.exp(lg)
    g1 = (w1 - A) * gg / w0
    g2 = ((w2 * gg + (w1 - A) * g1) * w0 - (w1 - A) * gg * w1) / w0**2
    return (gg, g1, g2)


NG = 20
GX, GW = [], []
for i in range(NG):
    pass
_x, _w = mp.gauss_quadrature(NG, 'legendre') if hasattr(mp, 'gauss_quadrature') else (None, None)
if _x is None:
    # own Gauss-Legendre nodes
    for i in range(1, NG + 1):
        z = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (NG + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), z
            for k in range(2, NG + 1):
                p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
            dp = NG * (z * p1 - p0) / (z**2 - 1)
            dz = p1 / dp
            z -= dz
            if abs(dz) < mp.mpf(10)**(-45):
                break
        p0, p1 = mp.mpf(1), z
        for k in range(2, NG + 1):
            p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
        dp = NG * (z * p1 - p0) / (z**2 - 1)
        GX.append(z)
        GW.append(2 / ((1 - z**2) * dp**2))
else:
    GX, GW = list(_x), list(_w)


def gl(f, a, b):
    h = (b - a) / 2
    return h * mp.fsum(wt * f(a + h * (z + 1)) for z, wt in zip(GX, GW))


def bump_region(a, b, wfun, npan):
    """int_a^b (f[w] - f[w0]) dx with g rebuilt from g0(a) along w = wfun(x) (jets); returns (integral, K = g(b)/g0(b))."""
    efun = lambda x: (lambda W: (W[1] - A) / W[0])(wfun(x))
    br = [a + (b - a) * mp.mpf(j) / npan for j in range(npan + 1)]
    lg = mp.log(g0d(a, 1)[0])
    I = mp.mpf(0)
    for p, q in zip(br[:-1], br[1:]):
        h = (q - p) / 2
        for z, wt in zip(GX, GW):
            x = p + h * (z + 1)
            W = wfun(x)
            gp = gjet(W, lg + gl(efun, p, x))
            I += h * wt * (fint(W, gp) - fint(w0d(x), g0d(x)))
        lg += gl(efun, p, q)
    return I, mp.exp(lg) / g0d(b, 1)[0]


def outer_diff(a, b, K, endpoint):
    """int_a^b (f_K - f_0) dx with w = w0, g = K g0; if endpoint, b = L and the s^(beta-1) singularity is removed
    by sigma = (L - x)^beta."""
    def d(x):
        W, G = w0d(x), g0d(x)
        return fint(W, [K * c for c in G]) - fint(W, G)
    if not endpoint:
        # geometric panels from a
        br = [a]
        while br[-1] * 2 < b:
            br.append(br[-1] * 2)
        br.append(b)
        fine = []
        for p, q in zip(br[:-1], br[1:]):
            fine += [p + (q - p) * mp.mpf(j) / 4 for j in range(4)]
        fine.append(b)
        return mp.fsum(gl(d, p, q) for p, q in zip(fine[:-1], fine[1:]))
    s1 = (L - a)**be

    def ds(sg):
        tau = sg**(1 / be)
        x = L - tau
        return d(x) * tau**(1 - be) / be
    br = [s1 * mp.mpf(j) / 8 for j in range(9)]
    return mp.fsum(gl(ds, p, q) for p, q in zip(br[:-1], br[1:]))


_x = mp.mpf('1.3')
_u = _x / L
_w1 = -A * ((1 - _u**2) / (1 + _u**2) - 4 * _u**2 / (1 + _u**2)**2)
_g1 = _x**2 / (1 + _u**2) * 2 / (_x * (1 + _u**2))
P('jet self-test: w0\' %s, g0\' %s, (w0\' - A)/w0 - g0\'/g0 = %s' % (mp.nstr(w0d(_x)[1] - _w1, 3), mp.nstr(g0d(_x)[1] - _g1, 3),
  mp.nstr((w0d(_x)[1] - A) / w0d(_x)[0] - g0d(_x)[1] / g0d(_x)[0], 3)))
phiint = lambda e: mp.quad(lambda u: mp.exp(-1 / ((u - 1) * (2 - u))) * u**e, [1, 1.5, 2])
kapA = (1 - be) * (6 + be) * (7 + be) / (6 * A)
part = sys.argv[1] if len(sys.argv) > 1 else 'ab'

if 'a' in part:
    lim1 = kapA * phiint(-8 - be)
    P('(a) beta = %s, kappa_A = %s, int phi u^(-8-beta) = %s, claimed limit per unit t = %s' % (
        mp.nstr(be, 12), mp.nstr(kapA, 15), mp.nstr(phiint(-8 - be), 15), mp.nstr(lim1, 15)))
    for t in [mp.mpf(1), mp.mpf(-1)]:
        for eps in ['0.4', '0.2', '0.1', '0.05', '0.025', '0.0125']:
            eps = mp.mpf(eps)

            def wfun(x, eps=eps, t=t):
                W = w0d(x)
                ph = phid(x / eps)
                return [W[k] + t * eps**(7 + be - k) * ph[k] for k in range(4)]
            I1, K = bump_region(eps, 2 * eps, wfun, 8)
            I2 = outer_diff(2 * eps, L / 2, K, False) + outer_diff(L / 2, L, K, True)
            D = pref * (I1 + I2)
            P('(a) t = %+d eps = %-7s D = %s  D/limit = %s  (D/limit - 1)/eps^2 = %s  K - 1 = %s  (%.0f s)' % (
                int(t), mp.nstr(eps, 4), mp.nstr(D, 15), mp.nstr(D / (t * lim1), 15),
                mp.nstr((D / (t * lim1) - 1) / eps**2, 6), mp.nstr(K - 1, 4), time.time() - t0))
    # C^m norms of h_eps: sup |h^(m)| = eps^(7+beta-m) sup |phi^(m)|
    sups = []
    for m_ in range(8):
        us = [1 + mp.mpf(j) / 400 for j in range(1, 400)]
        sups.append(max(abs(mp.diff(lambda v: mp.exp(-1 / ((v - 1) * (2 - v))), u, m_)) for u in us[::4]))
    P('(a) sup|phi^(m)|, m = 0..7 (sampled): %s; so ||h_eps||_{C^m} <= C eps^(7.197 - m) -> 0 for m <= 7' % (
        [mp.nstr(s, 4) for s in sups]))

if 'b' in part:
    gP = L**2 / 2
    lim2 = (be - 1) * (3 - be) / (6 * A * gP**(be + 2)) * (gP / A - (2 - be)) * phiint(be - 4)
    P('(b) g_P = %s, claimed limit per unit t = %s' % (mp.nstr(gP, 10), mp.nstr(lim2, 15)))
    for t in [mp.mpf(1), mp.mpf(-1)]:
        for eps in ['0.2', '0.1', '0.05', '0.025', '0.0125', '0.00625']:
            eps = mp.mpf(eps)

            def wfun(x, eps=eps, t=t):
                W = w0d(x)
                ph = phid((L - x) / eps)
                return [W[k] + t * eps**(3 - be - k) * (-1)**k * ph[k] for k in range(4)]
            # g unchanged on [0, L - 2 eps]
            I1, K = bump_region(L - 2 * eps, L - eps, wfun, 8)
            I2 = outer_diff(L - eps, L, K, True)
            D = pref * (I1 + I2)
            P('(b) t = %+d eps = %-8s D = %s  D/limit = %s  (D/limit - 1)/eps = %s  K - 1 = %s  (%.0f s)' % (
                int(t), mp.nstr(eps, 4), mp.nstr(D, 15), mp.nstr(D / (t * lim2), 15),
                mp.nstr((D / (t * lim2) - 1) / eps, 6), mp.nstr(K - 1, 4), time.time() - t0))
