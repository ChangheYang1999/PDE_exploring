"""Independent check of the edge-1 highest-log cycle at delta = 2/3 (review of the edge-top-chain derivation).
Exact polynomial-log edge-1 recurrence: only ordered pairs (1, n-1), (n-1, 1) (once if equal), F_1 = sin, c = 3,
  (lambda_n - c D) F_n = sum T(G_i, F_j),  T(G, F) = (P_i + D) G F' - G' (p_j + D) F,  lambda_n = 2(n-1),
  stream mode j from density mode m = j-1: -(1/2)(D + P_n + j)^(-1), from m = j+1: -(1/2)(D + P_n - j)^(-1);
  zero shift: integration from zero, then the whole t^0 coefficient of the resonant mode is deleted.
Fields are dicts {(q, m): Fraction} for t^q sin(m theta).  Computes b_k = [t^(k-1) sin((2k-2) theta)] G_(3k) directly
and compares with the claimed b_2, b_3 and b_(k+1) = R(k) b_k; then checks P(x+3) > 0, lim k R(k) and the order-250
coefficient bound |v| < 2^-1075 from the product formula.
usage: edge_top_check.py N  (orders 1..N directly)"""
import sys
from fractions import Fraction as Fr
from collections import defaultdict

N = int(sys.argv[1])
dl, c = Fr(2, 3), Fr(3)


def p_(n):
    return 1 - n * dl


def P_(n):
    return 2 - n * dl


def lam(n):
    return (n - 1) * (c - 1)


def add(d, q, m, v):
    if m == 0 or v == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[(q, m)] += v


def dth(F):
    """theta derivative: returns cosine dict {(q, m): coeff of t^q cos(m theta)}"""
    return {(q, m): m * v for (q, m), v in F.items()}


def Dt(F):
    out = defaultdict(Fr)
    for (q, m), v in F.items():
        if q > 0:
            out[(q - 1, m)] += q * v
    return out


def lin(F, a, G=None, b=1):
    out = defaultdict(Fr)
    for k, v in F.items():
        out[k] += a * v
    if G is not None:
        for k, v in G.items():
            out[k] += b * v
    return out


def prod_sc(S, C):
    """(sum t^q sin mu)(sum t^l cos nu) as sine dict"""
    out = defaultdict(Fr)
    for (q, mu), x in S.items():
        for (l, nu), y in C.items():
            add(out, q + l, mu + nu, x * y / 2)
            add(out, q + l, mu - nu, x * y / 2)
    return out


def T(G, Pi, F, pj):
    A = prod_sc(lin(G, Pi, Dt(G)), dth(F))  # (P_i + D)G * F'
    Bm = prod_sc(lin(F, pj, Dt(F)), dth(G))  # (p_j + D)F * G'
    return lin(A, 1, Bm, -1)


def shift_inv(poly, alpha):
    """(D + alpha)^(-1) on {q: coeff}; alpha = 0: integration from zero"""
    if not poly:
        return {}
    top = max(poly)
    out = {}
    if alpha == 0:
        for q in range(top, -1, -1):
            out[q + 1] = poly.get(q, 0) / (q + 1)
        return out
    nxt = Fr(0)
    for q in range(top, -1, -1):
        v = (poly.get(q, 0) - (q + 1) * nxt) / alpha
        out[q] = v
        nxt = v
    return out


def density_inv(R, n):
    out = defaultdict(Fr)
    modes = defaultdict(dict)
    for (q, m), v in R.items():
        modes[m][q] = v
    L = lam(n)
    for m, poly in modes.items():
        top = max(poly)
        nxt = Fr(0)
        for q in range(top, -1, -1):  # L F_q - c (q+1) F_(q+1) = R_q
            v = (poly.get(q, 0) + c * (q + 1) * nxt) / L
            if v:
                out[(q, m)] = v
            nxt = v
    return out


def poisson(F, n):
    Pn = P_(n)
    modes = defaultdict(dict)
    for (q, m), v in F.items():
        modes[m][q] = v
    out = defaultdict(Fr)
    res = set()
    for m, poly in modes.items():
        for j, alpha in ((m + 1, Pn + m + 1), (m - 1, Pn - (m - 1))):
            if j <= 0:
                continue
            if alpha == 0:
                res.add(j)
            for q, v in shift_inv(poly, alpha).items():
                out[(q, j)] += -v / 2
    for j in res:
        out[(0, j)] = Fr(0)
    return {k: v for k, v in out.items() if v != 0}, res


F = {1: {(0, 1): Fr(1)}}
G = {}
G[1], _ = poisson(F[1], 1)
print('g_1 =', dict(G[1]))
b = {}
for n in range(2, N + 1):
    acc = T(G[1], P_(1), F[n - 1], p_(n - 1))
    if n - 1 != 1:
        acc = lin(acc, 1, T(G[n - 1], P_(n - 1), F[1], p_(1)), 1)
    F[n] = density_inv(acc, n)
    G[n], res = poisson(F[n], n)
    degF = max([q for q, _ in F[n]] + [0])
    degG = max([q for q, _ in G[n]] + [0])
    dn, en = max(0, (n - 1) // 3 - 1), max(0, n // 3 - 1)
    assert degF <= dn and degG <= en, (n, degF, degG)
    if n % 3 == 0 and n >= 6:
        k = n // 3
        b[k] = G[n].get((k - 1, 2 * k - 2), 0)
        assert res == {2 * k - 2}, (n, res)
        top = {m for (q, m) in G[n] if q == k - 1}
        assert top == {2 * k - 2}, (n, top)


def R(k):
    Pk = 6480 * k**5 - 3132 * k**4 - 23454 * k**3 + 29472 * k**2 - 10791 * k + 880
    return Fr((k - 1) * (2 * k - 1) * Pk, 14400 * k**2 * (3 * k - 4) * (3 * k - 2) * (3 * k + 1) * (3 * k + 2) * (6 * k - 5) * (6 * k - 1))


print('degree bounds d_n, e_n hold for n <= %d; top stream column at 3k is exactly sin((2k-2) theta)' % N)
print('b_2 =', b[2], ' claimed -9589/73728000000:', b[2] == Fr(-9589, 73728000000))
print('b_3 =', b[3], ' claimed -37847783/8138627481600000000:', b[3] == Fr(-37847783, 8138627481600000000))
for k in sorted(b):
    if k + 1 in b and k >= 3:
        print('k = %d: b_(k+1)/b_k == R(k): %s' % (k, b[k + 1] / b[k] == R(k)))
# top-degree density coefficient checks: a_1 at 3k+1
for k in sorted(b):
    n = 3 * k + 1
    if n <= N:
        m = 2 * k - 2
        a1p = F[n].get((k - 1, m + 1), 0) / b[k]
        a1m = F[n].get((k - 1, m - 1), 0) / b[k]
        ok = a1p == Fr(-2 * (k - 1), 9 * k) and (k < 3 or a1m == Fr(-(k - 1), 9 * k))
        print('k = %d: a_1 profile (offsets +1, -1) as claimed: %s' % (k, ok))
# polynomial positivity and limit
import sympy as sp
x, kk = sp.symbols('x k')
Pk = 6480 * kk**5 - 3132 * kk**4 - 23454 * kk**3 + 29472 * kk**2 - 10791 * kk + 880
print('P(x+3) =', sp.expand(Pk.subs(kk, x + 3)))
Rk = (kk - 1) * (2 * kk - 1) * Pk / (14400 * kk**2 * (3 * kk - 4) * (3 * kk - 2) * (3 * kk + 1) * (3 * kk + 2) * (6 * kk - 5) * (6 * kk - 1))
print('lim k R(k) =', sp.limit(kk * Rk, kk, sp.oo))
# order 250: k = 83, r = 1, degree 82, mode 165
bb = Fr(-37847783, 8138627481600000000)
for k in range(3, 83):
    bb *= R(k)
v = bb * Fr(-2 * 82, 9 * 83)
print('v = [t^82 sin 165] F_250: nonzero %s, |v| < 2^-1075: %s, log10|v| = %.9f' % (
    v != 0, abs(v.numerator) * 2**1075 < v.denominator,
    (len(str(abs(v.numerator))) - len(str(v.denominator))) + __import__('math').log10(
        int(str(abs(v.numerator))[:17]) / int(str(v.denominator)[:17]))))
