"""Symbolic (in k) top-degree cycle of the edge-1 recurrence at delta = 2/3, signed offsets o around m = 2k-2:
  2(n-1) a_r = P_(n-1) h_(r-1) f_1' - p_1 h_(r-1)' f_1 + P_1 g_1 a_(r-1)' - p_(n-1) g_1' a_(r-1),  n = 3k + r,
  h_r = nonresonant Poisson inverse of a_r at n = 3k + r; f_1 = sin, g_1 = -3/20 sin 2.  Checks
  [offset +1] a_3 = -2k R(k) identically in k (valid for k >= 3, where no reflected frequency meets m+1)."""
import sympy as sp
k = sp.symbols('k')
m = 2 * k - 2
p = lambda n: 1 - sp.Rational(2, 3) * n
P = lambda n: 2 - sp.Rational(2, 3) * n


def mul_sin_cos(S, mu_off, C):
    """S: {offset: coeff} for sin((m+o)theta) times C: {nu: coeff} cos(nu theta) (nu fixed small)"""
    out = {}
    for o, x in S.items():
        for nu, y in C.items():
            for oo in (o + nu, o - nu):
                out[oo] = out.get(oo, 0) + x * y / 2
    return out


def low_sin_times_high_cos(lowS, H):
    """sum_nu lowS[nu] sin(nu theta) * sum_o H[o] cos((m+o) theta)"""
    out = {}
    for nu, x in lowS.items():
        for o, y in H.items():
            out[o + nu] = out.get(o + nu, 0) + x * y / 2   # sin(a)cos(b) = [sin(a+b) + sin(a-b)]/2, a - b = -(m+o-nu)
            out[o - nu] = out.get(o - nu, 0) - x * y / 2
    return out


def addd(a, b, cf=1):
    for o, v in b.items():
        a[o] = a.get(o, 0) + cf * v
    return a


def step_density(n, h_prev, a_prev):
    acc = {}
    # P_(n-1) h f_1' : h sin(m+o) * cos(theta)
    addd(acc, mul_sin_cos(h_prev, None, {1: 1}), P(n - 1))
    # - p_1 h' f_1 : h' = (m+o) cos(m+o) ; times sin(theta)
    hd = {o: (m + o) * v for o, v in h_prev.items()}
    addd(acc, low_sin_times_high_cos({1: 1}, hd), -p(1))
    if a_prev:
        # P_1 g_1 a' : g_1 = -3/20 sin 2 ; a' = (m+o) cos(m+o)
        ad = {o: (m + o) * v for o, v in a_prev.items()}
        addd(acc, low_sin_times_high_cos({2: sp.Rational(-3, 20)}, ad), P(1))
        # - p_(n-1) g_1' a : g_1' = -3/10 cos 2
        addd(acc, mul_sin_cos(a_prev, None, {2: sp.Rational(-3, 10)}), -p(n - 1))
    return {o: sp.factor(v / (2 * (n - 1))) for o, v in acc.items()}


def step_poisson(n, a):
    out = {}
    for o, A in a.items():
        K = m + o
        out[o + 1] = out.get(o + 1, 0) - A / (2 * (K + 1 + P(n)))
        out[o - 1] = out.get(o - 1, 0) + A / (2 * (K - 1 - P(n)))
    return {o: sp.factor(v) for o, v in out.items()}


h0 = {0: sp.Integer(1)}
a1 = step_density(3 * k + 1, h0, None)
print('a_1 =', a1)
h1 = step_poisson(3 * k + 1, a1)
a2 = step_density(3 * k + 2, h1, a1)
h2 = step_poisson(3 * k + 2, a2)
a3 = step_density(3 * k + 3, h2, a2)
Pk = 6480 * k**5 - 3132 * k**4 - 23454 * k**3 + 29472 * k**2 - 10791 * k + 880
Rk = (k - 1) * (2 * k - 1) * Pk / (14400 * k**2 * (3 * k - 4) * (3 * k - 2) * (3 * k + 1) * (3 * k + 2) * (6 * k - 5) * (6 * k - 1))
print('supports a_1, a_2, a_3:', sorted(a1), sorted(a2), sorted(a3))
print('[offset +1] a_3 + 2k R(k) simplifies to:', sp.simplify(a3[1] + 2 * k * Rk))
print('nonzero limits: a1[+1] %s, a2[+1] %s, a3[+1] %s, h1[+2] %s, h2[+2] %s' % tuple(
    sp.limit(d[o], k, sp.oo) for d, o in ((a1, 1), (a2, 1), (a3, 1), (h1, 2), (h2, 2))))
