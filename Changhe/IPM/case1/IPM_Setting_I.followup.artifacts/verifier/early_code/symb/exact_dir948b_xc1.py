"""verifier: exact_dir948b, second quadrature for exact_dir948.py: composite Gauss-Legendre panels on [x_c, 0.95 L]
(graded towards the cutoff breaks), ln(g/x^2) at the nodes by Gauss-Legendre on [panel start, node], no nested
adaptive quadrature. Otherwise as exact_dir948.py:
exact (fit-free) first-order response of the w-only B_3 functional on R12 data (A = 10.150725,
L = x* = 8.6) along w -> w (1 + eps b chi), b = x^2 exp(-x^2/8), chi the C^infinity cutoff (1 on x <= 0.8 L, 0 on
x >= 0.95 L, e^(-1/t)/(e^(-1/t) + e^(-1/(1-t))), t = (0.95 L - x)/(0.15 L) in between). Lead request (k2), 2026-10-20.
B_3 = (1/(3 A^beta)) f.p. int_0^L Q' m^(beta-1) dx, Q = (g' - w'')/(2 g^3), m = -w/g, g rebuilt from w with g/x^2 -> 1.
 [0, x_c]: exact power series of x^(5+beta) Q' m^(beta-1) (truncated power-series arithmetic, no fit), finite part
           term by term.
 [x_c, 0.95 L]: tanh-sinh quadrature; ln(g/x^2) = series value at x_c + int_{x_c}^x [(w' - A)/w - 2/t] dt.
 [0.95 L, L]: chi = 0, so w = w_R12 and g = K g_R12 with the constant K = (g/g_R12)(0.95 L); exact rational Q' in x and
           K, m = A tau (L + x)/(K L^2 x) with tau = L - x, and tau = sigma^(1/beta) removes the endpoint singularity.
Response by central differences at two eps (30 digits)."""
import sys
import time
import mpmath as mp
import sympy as sp

mp.mp.dps = 34
N = 64
A = mp.mpf('10.150725')
L = mp.mpf('8.6')
be = 2 / A
xc = mp.mpf('1.0')
out = []
P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))


# ---- truncated power series (coefficient lists of length N + 1) ----
def mul(a, b):
    return [mp.fsum(a[i] * b[n - i] for i in range(n + 1)) for n in range(N + 1)]


def inv(a):
    c = [1 / a[0]]
    for n in range(1, N + 1):
        c.append(-mp.fsum(a[i] * c[n - i] for i in range(1, n + 1)) / a[0])
    return c


def sexp(a):                       # a[0] = 0
    f = [mp.mpf(1)]
    for n in range(1, N + 1):
        f.append(mp.fsum(k * a[k] * f[n - k] for k in range(1, n + 1)) / n)
    return f


def spow(a, p):                    # a[0] > 0
    f = [a[0]**p]
    for n in range(1, N + 1):
        f.append(mp.fsum((k * p - n + k) * a[k] * f[n - k] for k in range(1, n + 1)) / (n * a[0]))
    return f


der = lambda a: [n * a[n] for n in range(1, N + 1)] + [mp.mpf(0)]
integ = lambda a: [mp.mpf(0)] + [a[n] / (n + 1) for n in range(N)]
down = lambda a: a[1:] + [mp.mpf(0)]          # divide by x (a[0] = 0)
up = lambda a: [mp.mpf(0)] + a[:N]             # multiply by x
add = lambda a, b: [u + v for u, v in zip(a, b)]
scal = lambda c, a: [c * u for u in a]
ev = lambda a, x: mp.fsum(a[n] * x**n for n in range(N + 1))


def zeros():
    return [mp.mpf(0)] * (N + 1)


def origin(eps):
    """fp int_0^xc Q' m^(beta-1) (exact series) and ln(g/x^2) at xc."""
    num, den = zeros(), zeros()
    num[1], num[3] = -A, A / L**2               # -A x (1 - u^2)
    den[0], den[2] = mp.mpf(1), 1 / L**2        # 1 + u^2
    wR = mul(num, inv(den))
    bq = zeros()
    bq[2] = mp.mpf(-1) / 8
    b = up(up(sexp(bq)))                         # x^2 exp(-x^2/8)
    one = zeros()
    one[0] = mp.mpf(1)
    w = mul(wR, add(one, scal(eps, b)))
    wt = down(w)                                 # w/x, wt(0) = -A
    wp = der(w)
    r = mul(add(wp, scal(-A, one)), inv(wt))     # (w' - A)/(w/x), r(0) = 2
    assert abs(r[0] - 2) < mp.mpf(10)**(-25)
    r[0] = mp.mpf(0)
    e = down(r)                                  # (w' - A)/w - 2/x
    lg = integ(e)
    gh = sexp(lg)                                # g/x^2
    g = up(up(gh))
    nm = add(der(g), scal(-1, der(der(w))))      # g' - w'' (odd)
    qt = mul(down(nm), inv(scal(2, mul(gh, mul(gh, gh)))))   # Q = x^-5 qt
    ph1 = [(n - 5) * qt[n] for n in range(N + 1)]            # x^6 Q'
    mm = mul(scal(-1, wt), inv(gh))                          # x m
    ph = mul(ph1, spow(mm, be - 1))                          # x^(5+beta) Q' m^(beta-1)
    fp = mp.fsum(ph[n] * xc**(n - 4 - be) / (n - 4 - be) for n in range(N + 1))
    tail = abs(ph[N] * xc**N) + abs(ph[N - 1] * xc**(N - 1))
    return fp, ev(lg, xc), tail


# ---- pointwise data on [xc, 0.95 L] ----
x, ep = sp.symbols('x eps', positive=True)
As, Ls = sp.Rational('10.150725'), sp.Rational('8.6')
u = x / Ls
wRs = -As * x * (1 - u**2) / (1 + u**2)
bs = x**2 * sp.exp(-x**2 / 8)
tt = (sp.Rational(95, 100) * Ls - x) / (sp.Rational(15, 100) * Ls)
chis = sp.exp(-1 / tt) / (sp.exp(-1 / tt) + sp.exp(-1 / (1 - tt)))
WD = {}
for reg, ch in [(1, sp.Integer(1)), (2, chis)]:
    ws = wRs * (1 + ep * bs * ch)
    WD[reg] = [sp.lambdify((x, ep), sp.diff(ws, x, k), 'mpmath') for k in range(4)]
a1, a2 = mp.mpf('0.8') * L, mp.mpf('0.95') * L


def reg_of(t):
    return 1 if t <= a1 else 2


def efun(t, eps):
    W = WD[reg_of(t)]
    return (W[1](t, eps) - A) / W[0](t, eps) - 2 / t


def integrand(t, lgh, eps):
    W = WD[reg_of(t)]
    w0, w1, w2, w3 = [W[k](t, eps) for k in range(4)]
    g = t**2 * mp.exp(lgh)
    g1 = (w1 - A) * g / w0
    g2 = ((w2 * g + (w1 - A) * g1) * w0 - (w1 - A) * g * w1) / w0**2
    Qp = (g2 - w3) / (2 * g**3) - 3 * (g1 - w2) * g1 / (2 * g**4)
    m = -w0 / g
    return Qp * m**(be - 1)


# ---- [0.95 L, L]: exact R12 rational structure with constant K ----
Ks = sp.symbols('K', positive=True)
gRs = x**2 / (1 + u**2)
Qs = (Ks * sp.diff(gRs, x) - sp.diff(wRs, x, 2)) / (2 * Ks**3 * gRs**3)
Qps = sp.lambdify((x, Ks), sp.cancel(sp.diff(Qs, x)), 'mpmath')


def end_part(K):
    s1 = (L - a2)**be

    def f(sg):
        tau = sg**(1 / be)
        xx = L - tau
        return Qps(xx, K) * (A * (L + xx) / (K * L**2 * xx))**(be - 1) / be
    return mp.quad(f, [0, s1 / 4, s1])



NG = 24


def gl_nodes(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        z = mp.cos(mp.pi * (i - mp.mpf(1) / 4) / (n + mp.mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.mpf(1), z
            for k in range(2, n + 1):
                p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
            dp = n * (z * p1 - p0) / (z**2 - 1)
            dz = p1 / dp
            z -= dz
            if abs(dz) < mp.mpf(10)**(-40):
                break
        p0, p1 = mp.mpf(1), z
        for k in range(2, n + 1):
            p0, p1 = p1, ((2 * k - 1) * z * p1 - (k - 1) * p0) / k
        dp = n * (z * p1 - p0) / (z**2 - 1)
        xs.append(z)
        ws.append(2 / ((1 - z**2) * dp**2))
    return xs, ws


GX, GW = gl_nodes(NG)
assert abs(mp.fsum(GW) - 2) < mp.mpf(10)**(-30) and abs(mp.fsum(w * z**6 for z, w in zip(GX, GW)) - mp.mpf(2) / 7) < mp.mpf(10)**(-30)


def gl(f, a, b):
    h = (b - a) / 2
    return h * mp.fsum(w * f(a + h * (z + 1)) for z, w in zip(GX, GW))


tb = [mp.mpf(s) for s in ['0', '1/80', '1/40', '1/20', '1/10', '1/5', '0.35', '0.5', '0.65', '0.8', '0.9', '0.95', '0.975', '0.9875', '1']]
br1 = [xc + mp.mpf(k) / 4 for k in range(int((a1 - xc) * 4) + 1)]
if a1 - br1[-1] > mp.mpf('1e-20'):
    br1.append(a1)
br2 = sorted(a2 - t * (a2 - a1) for t in tb)
BR = br1 + br2[1:]


def B3(eps):
    eps = mp.mpf(eps)
    fp0, lgc, tail = origin(eps)
    lg0, I = lgc, mp.mpf(0)
    for a, b in zip(BR[:-1], BR[1:]):
        h = (b - a) / 2
        for z, w in zip(GX, GW):
            t = a + h * (z + 1)
            lgt = lg0 + gl(lambda s: efun(s, eps), a, t)
            I += h * w * integrand(t, lgt, eps)
        lg0 += gl(lambda s: efun(s, eps), a, b)
    K = mp.exp(lg0) * (1 + (a2 / L)**2)
    I3 = end_part(K)
    pref = 1 / (3 * A**be)
    return pref * (fp0 + I + I3), tail, K


nat = L**(6 + 2 / A - 2)
t0 = time.time()
B0, tail0, K0 = B3(0)
P('[GL panels, %d nodes, %d panels] eps = 0: B_3^nat = %s (C4 series value 0.325791726307172), K - 1 = %s, %.0f s' % (
    NG, len(BR) - 1, mp.nstr(B0 * nat, 20), mp.nstr(K0 - 1, 3), time.time() - t0))
for e in ['1e-8', '1e-10']:
    Bp, _, Kp = B3(e)
    Bm, _, Km = B3('-' + e)
    d = (Bp - Bm) / (2 * mp.mpf(e)) * nat
    P('[GL] eps = %s: dB_3^nat/deps = %s (central difference), K(+eps) - 1 = %s, %.0f s' % (e, mp.nstr(d, 16), mp.nstr(Kp - 1, 3), time.time() - t0))
open('verifier/early_runs/exact_dir948b_xc1.log', 'w').write('\n'.join(out) + '\n')
