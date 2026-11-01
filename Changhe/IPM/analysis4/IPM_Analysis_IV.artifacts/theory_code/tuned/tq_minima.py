"""Exact global response minima at delta = 2/Q (default Q = 5), f_1 = sin + b_i sin 3, and radii from them.
usage: tq_minima.py Q k_1 ... k_m   (k_i = proposed unique minimizing index for the i-th real root, increasing order)
For each root b_i (isolating interval I_i of width <= 1e-30): e_i = sign sigma_(k_i)(b_i) (interval excludes 0).
 finite gaps: for 2 <= k < K0, k != k_i:  lower bound of |sigma_k| on I_i  >  upper bound of e_i sigma_(k_i) on I_i.
 tail k >= K0 = 2Q+1, k = K0 + t: every t-coefficient of eps_inf N(K0+t,b) - e_i sigma_(k_i)(b) D(K0+t), a polynomial
 in b, has a strictly positive interval lower bound on I_i (D(K0+t) has positive coefficients). Then
 |sigma_k(b_i)| > |sigma_(k_i)(b_i)| for all k >= 2, k != k_i.  The certified lower bound s_i is the largest
 n/10^(d) below the interval of e_i sigma_(k_i) with 3 significant digits; then (B) of tq_bounds_radius.py is run with s_i.
 k_i = 0 means: the infimum is |sigma_inf(b_i)| and is not attained. Then the finite gaps are taken against the interval
 of |sigma_inf|, and in the tail the target is eps_inf sigma_inf(b) D(K0+t): its top t-coefficient cancels exactly (it
 is checked to vanish identically in b) and every other t-coefficient must have a strictly positive lower bound, so
 |sigma_k(b_i)| > |sigma_inf(b_i)| for every k >= 2 while sigma_k -> sigma_inf.
"""
import sys, time
from fractions import Fraction as Fr
from math import comb
QQ_ = int(sys.argv[1]) if len(sys.argv) > 1 else 5
KMIN = [int(v) for v in sys.argv[2:]] or [5, 8, 5, 6, 5, 5]
K0 = 2 * QQ_ + 1
sys.argv = [sys.argv[0], str(QQ_), '3', str(K0 + 5)]
import tq_sym as T
from sympy import Poly, symbols, sympify, together, fraction, Rational

t0 = time.time()
b, k = symbols('b k')
out = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s, flush=True)
    out.append(s)


def fr(x):
    x = Rational(x)
    return Fr(int(x.p), int(x.q))


# interval arithmetic on Fractions
def imul(x, y):
    p = [x[0] * y[0], x[0] * y[1], x[1] * y[0], x[1] * y[1]]
    return (min(p), max(p))


def ihorner(coeffs_desc, I):
    v = (Fr(0), Fr(0))
    for c in coeffs_desc:
        v = imul(v, I)
        v = (v[0] + c, v[1] + c)
    return v


Q, B = QQ_, 4
F, G = T.low_orders(2 * Q)
O = sympify(F[2 * Q].get(1, T.R.zero).as_expr())
P10 = Poly(Poly(O, b).primitive()[1], b)
ivs = P10.intervals(eps=Rational(1, 10 ** 30))
roots = [(fr(lo), fr(hi)) for (lo, hi), m in ivs]
assert all(m == 1 for _, m in ivs)
log('Q = %d, %d real roots' % (Q, len(roots)))
# ---------------- (A) response lower bounds
small = {}
for kv in range(2, K0):
    s, _ = T.sigma(kv, F, G)
    small[kv] = [fr(c) for c in Poly(sympify(s.as_expr()), b).all_coeffs()]
sg, _ = T.sigma(None, F, G)
num, den = fraction(together(sympify(sg.as_expr())))
Nb = Poly(num, b)
dD = Poly(den, k).shift(K0).all_coeffs()[::-1]  # ascending in t
sgnD = 1 if dD[-1] > 0 else -1
dD = [fr(c) * sgnD for c in dD]
assert all(c > 0 for c in dD), 'D(11+t) coefficients not of one sign'
log('D(K0+t): %d coefficients, all positive after sign normalization' % len(dD))
# t-coefficients of N(11+t, b): list over ell of b-polynomials (descending in b)
nb = Nb.degree()
colsb = []  # colsb[i] = ascending t-coefficients of the coefficient of b^i
for i in range(nb + 1):
    ci = Nb.coeff_monomial(b ** i)
    colsb.append([fr(c) * sgnD for c in Poly(ci, k).shift(K0).all_coeffs()[::-1]] if ci != 0 else [])
nT = max(len(c) for c in colsb)
tco = []
for ell in range(nT):
    tco.append([colsb[i][ell] if ell < len(colsb[i]) else Fr(0) for i in range(nb, -1, -1)])  # descending in b
log('N(K0+t,b): degree %d in b, %d t-coefficients' % (nb, nT))
# sigma_inf for the sign
dn = Poly(num, k).degree()
dd = Poly(den, k).degree()
lead = Poly(num, k).coeff_monomial(k ** dd) if dn == dd else 0
sinf = [fr(c) for c in Poly(sympify(lead) / Poly(den, k).LC(), b).all_coeffs()]
resA = []
A_, S_ = [], []
for i, I in enumerate(roots):
    ki = KMIN[i]
    tpoly = small[ki] if ki else sinf
    vmin = ihorner(tpoly, I)
    assert vmin[0] > 0 or vmin[1] < 0
    ei = 1 if vmin[0] > 0 else -1
    lo_i, hi_i = (vmin[0], vmin[1]) if ei > 0 else (-vmin[1], -vmin[0])  # interval of |sigma_(k_i)(b_i)|
    vi = ihorner(sinf, I)
    assert vi[0] > 0 or vi[1] < 0
    eps = 1 if vi[0] > 0 else -1
    gaps = []
    for kv in range(2, K0):
        if kv == ki:
            continue
        v = ihorner(small[kv], I)
        lowabs = v[0] if v[0] > 0 else (-v[1] if v[1] < 0 else Fr(0))
        gaps.append(lowabs - hi_i)
    ok_small = all(g > 0 for g in gaps)
    target = [ei * c for c in tpoly]  # descending in b
    ok_tail = True
    minc = None
    for ell in range(max(nT, len(dD))):
        cN = tco[ell] if ell < nT else [Fr(0)]
        Dl = dD[ell] if ell < len(dD) else Fr(0)
        nb_ = max(len(cN), len(target))
        cN2 = [Fr(0)] * (nb_ - len(cN)) + [eps * c for c in cN]
        tg2 = [Fr(0)] * (nb_ - len(target)) + [c * Dl for c in target]
        diff = [p_ - q_ for p_, q_ in zip(cN2, tg2)]
        v = ihorner(diff, I)
        if ki == 0 and ell == max(nT, len(dD)) - 1:
            ok_tail &= all(c == 0 for c in diff)  # exact cancellation of the top coefficient
            continue
        ok_tail &= v[0] > 0
        r = v[0] / Dl if Dl else v[0]
        minc = r if minc is None or r < minc else minc
    d_ = 0
    while Fr(1, 10 ** d_) > lo_i:
        d_ += 1
    sc = Fr(10 ** (d_ + 2))
    si = Fr(int(lo_i * sc), sc)
    assert 0 < si <= lo_i
    S_.append(si)
    hi = 1 + max(abs(I[0]), abs(I[1]))
    A_.append(Fr(-((-hi * 100) // 1), 100))
    resA.append(ok_small and ok_tail)
    log('root %d: k_i = %s, sign %+d, |sigma_(k_i)| in [%.16g, %.16g]; finite gaps k=2..%d positive: %s (min gap %.3e); '
        'tail k>=%d strictly above the target: %s (min coefficient margin / D_ell %.3e); certified s_i = %s'
        % (i + 1, ki if ki else 'inf (not attained)', ei, float(lo_i), float(hi_i), K0 - 1, ok_small, float(min(gaps)), K0, ok_tail, float(minc), si))
assert all(resA)
log('(A) PASS: for all %d roots, inf_{k>=2} |sigma_k(b_i)| is attained only at the listed k_i; where k_i = inf it equals |sigma_inf(b_i)| and is attained at no finite k' % len(roots))


# ---------------- (B) generating-system certificate
def pmul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        if x:
            for j, y in enumerate(q):
                r[i + j] += x * y
    return r


def peval(p, z):
    v = Fr(0)
    for c in reversed(p):
        v = v * z + c
    return v


def make_phi(a, s):
    kap = Fr(Q - 2) * (3 - Fr(2, Q)) * B
    L = Fr(Q, 2)
    cat = [comb(2 * m, m) // (m + 1) for m in range(Q)]
    x = [Fr(0)] + [cat[j - 1] * (kap * L) ** (j - 1) * a ** j for j in range(1, Q + 1)]
    Pz = [Fr(0)] + x[1:]  # P(z) coefficients, degree Q
    P2 = pmul(Pz, Pz)
    hiP2 = P2[Q + 1:]  # [P^2]_(>=Q+1) / z^(Q+1)

    def Pr(r):
        return [Fr(0)] * r + x[r:Q + 1]

    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = Pr(r)
        hiA[r] = pmul(pr, pr)[Q + r + 1:]  # [P_r^2]_(>=Q+r+1)/z^(Q+r+1)
        lowA[r] = pr[r:]  # P_r / z^r

    def phi(z, Y):
        W, V, E = Y[0], Y[1:Q], Y[Q]
        Pv = peval(Pz, z)
        out = [kap * L * peval(hiP2, z) + 2 * kap * L * Pv * W + kap * L * z ** (Q + 1) * W * W
               + kap * E * (Pv + z ** (Q + 1) * W)]

        def Ar(r):
            return peval(hiA[r], z) + 2 * peval(lowA[r], z) * W + z ** (Q + 1 - r) * W * W
        for r in range(1, Q):
            out.append(kap * (L * Ar(r) + z ** (Q + 1 - r) * E * W + Q * sum(x[sq] * V[r - sq - 1] for sq in range(1, r))))
        out.append(kap / s * (L * Ar(Q) + z * E * W + Q * sum(x[sq] * V[Q - sq - 1] for sq in range(1, Q))))
        return out
    return phi, kap


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def certificate(a, s, q):
    phi, kap = make_phi(a, s)
    d = Q + 1
    zero = [Fr(0)] * d
    c0 = phi(Fr(0), zero)
    J = [[Fr(0)] * d for _ in range(d)]
    for j in range(d):
        e = [Fr(0)] * d
        e[j] = Fr(1)
        col = phi(Fr(0), e)
        for i in range(d):
            J[i][j] = col[i] - c0[i]
    # affine check at z = 0 and strict lower triangularity
    e2 = [Fr(i + 2) for i in range(d)]
    assert phi(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(d)) for i in range(d)]
    assert all(J[i][j] == 0 for i in range(d) for j in range(i, d))
    # T = sum J^i
    Tm = [[Fr(int(i == j)) for j in range(d)] for i in range(d)]
    Pw = [row[:] for row in Tm]
    for _ in range(Q):
        Pw = [[sum(Pw[i][l] * J[l][j] for l in range(d)) for j in range(d)] for i in range(d)]
        Tm = [[Tm[i][j] + Pw[i][j] for j in range(d)] for i in range(d)]
    Y0 = matvec(Tm, c0)
    bx = [2 * y for y in Y0]
    z0 = Fr(1, 2 ** q)
    rest = [u - c - w for u, c, w in zip(phi(z0, bx), c0, matvec(J, bx))]
    Gv = [y + w for y, w in zip(Y0, matvec(Tm, rest))]
    ratio = max(g / bb for g, bb in zip(Gv, bx))
    return ratio <= 1, ratio, kap


resB = []
Z_ = []
for i, I in enumerate(roots):
    assert 1 + max(abs(I[0]), abs(I[1])) <= A_[i]  # ||f_1||_1 = 1 + |b_i| <= a_i
    q = 1
    while True:
        ok, ratio, kap = certificate(A_[i], S_[i], q)
        if ok:
            break
        q += 1
    ok1, ratio1, _ = certificate(A_[i], S_[i], q - 1)
    Z_.append(q)
    resB.append(ok and not ok1)
    log('root %d: a=%s, s=%s, smallest passing q: z0=2^-%d: G(z0,2Y0) <= 2Y0: %s (max ratio %.5f); at z0=2^-%d: %s '
        '(max ratio %.3g); radius r > 2^%s |eps|^(%d/2)' % (i + 1, A_[i], S_[i], q, ok, float(ratio), q - 1, ok1,
                                                         float(ratio1), Fr(q * Q, 2), Q))
ac = max(A_)
sc = min(S_)
q = 1
while not certificate(ac, sc, q)[0]:
    q += 1
okc, ratioc, _ = certificate(ac, sc, q)
log('common: a=%s, s=%s, z0=2^-%d: %s (max ratio %.5f); radius r > 2^%s |eps|^(%d/2)'
    % (ac, sc, q, okc, float(ratioc), Fr(q * Q, 2), Q))
log('kappa =', kap)
assert all(resB) and okc
log('(B) PASS')
log('time %.1fs' % (time.time() - t0))
open('tq_minima_Q%d.out' % Q, 'w').write('\n'.join(out) + '\n')
