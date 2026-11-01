"""Independent reproduction, at delta = 2/5 (Q = 5, B = 4), f_1 = sin(theta) + b_i sin(3 theta), of
 (A) the all-k response lower bounds |sigma_k(b_i)| >= s_i for k >= 2, and
 (B) the explicit exterior radii from the generating system of Theorem T_Q (theory Section 12.5, Step 4),
for the six real roots b_i of P10, with the constants (a_i, s_i, z0_i) proposed by the independent review.

(A) k = 2..10: rational interval Horner evaluation of the exact sigma_k on an isolating interval of width <= 1e-30.
    k >= 11: generic sigma = N(k,b)/D(k) from tq_sym (unreduced). With k = 11 + t, D(11+t) has coefficients of one sign
    (normalized positive); every t-coefficient of eps*N(11+t,b) - s*D(11+t) (eps = sign sigma_inf(b_i)) is checked
    >= 0 on the interval, the constant one > 0. Then eps*sigma_k >= s for every real t >= 0, so for every k >= 11.
(B) Phi(z,Y), Y = (W, V_1..V_4, E), exactly as displayed in Section 12.5 Step 4 with kappa = (Q-2)(3-2/Q)B, L = Q/2,
    sigma_* = s_i, xbar_j = Cat_(j-1) (kappa L)^(j-1) a^j (j <= Q). c0 = Phi(0,0), J = Phi(0,e_j) - c0 (Phi(0,.) is affine),
    T = sum_(i<=Q) J^i, Y0 = T c0, G(z,Y) = Y0 + T[Phi(z,Y) - c0 - J Y]; box b = 2 Y0; check G(z0,b) <= b exactly.
    Then the tuned series converges for r > z0^(-Q/2) (times |epsilon|^(Q/2)).
"""
import sys, time
from fractions import Fraction as Fr
from math import comb
sys.argv = [sys.argv[0], '5', '3', '16']
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


Q, B = 5, 4
F, G = T.low_orders(10)
O = sympify(F[10].get(1, T.R.zero).as_expr())
P10 = Poly(Poly(O, b).primitive()[1], b)
ivs = P10.intervals(eps=Rational(1, 10 ** 30))
roots = [(fr(lo), fr(hi)) for (lo, hi), m in ivs]
assert len(roots) == 6 and all(m == 1 for _, m in ivs)
# the proposed constants (norm bound a_i, response bound s_i, z0_i) in increasing root order
A_ = [Fr(149, 100), Fr(1049, 1000), Fr(563, 500), Fr(1213, 1000), Fr(329, 250), Fr(39, 25)]
S_ = [Fr(1, 32), Fr(1, 8388608), Fr(1, 65536), Fr(1, 32768), Fr(1, 16384), Fr(1, 2048)]
Z_ = [56, 70, 64, 64, 64, 62]

# ---------------- (A) response lower bounds
small = {}
for kv in range(2, 11):
    s, _ = T.sigma(kv, F, G)
    small[kv] = [fr(c) for c in Poly(sympify(s.as_expr()), b).all_coeffs()]
sg, _ = T.sigma(None, F, G)
num, den = fraction(together(sympify(sg.as_expr())))
Nb = Poly(num, b)
dD = Poly(den, k).shift(11).all_coeffs()[::-1]  # ascending in t
sgnD = 1 if dD[-1] > 0 else -1
dD = [fr(c) * sgnD for c in dD]
assert all(c > 0 for c in dD), 'D(11+t) coefficients not of one sign'
log('D(11+t): %d coefficients, all positive after sign normalization' % len(dD))
# t-coefficients of N(11+t, b): list over ell of b-polynomials (descending in b)
nb = Nb.degree()
colsb = []  # colsb[i] = ascending t-coefficients of the coefficient of b^i
for i in range(nb + 1):
    ci = Nb.coeff_monomial(b ** i)
    colsb.append([fr(c) * sgnD for c in Poly(ci, k).shift(11).all_coeffs()[::-1]] if ci != 0 else [])
nT = max(len(c) for c in colsb)
tco = []
for ell in range(nT):
    tco.append([colsb[i][ell] if ell < len(colsb[i]) else Fr(0) for i in range(nb, -1, -1)])  # descending in b
log('N(11+t,b): degree %d in b, %d t-coefficients' % (nb, nT))
# sigma_inf for the sign
dn = Poly(num, k).degree()
dd = Poly(den, k).degree()
lead = Poly(num, k).coeff_monomial(k ** dd) if dn == dd else 0
sinf = [fr(c) for c in Poly(sympify(lead) / Poly(den, k).LC(), b).all_coeffs()]
resA = []
for i, I in enumerate(roots):
    s = S_[i]
    vi = ihorner(sinf, I)
    assert vi[0] > 0 or vi[1] < 0
    eps = 1 if vi[0] > 0 else -1
    ok_small = []
    for kv in range(2, 11):
        v = ihorner(small[kv], I)
        lowabs = v[0] if v[0] > 0 else (-v[1] if v[1] < 0 else Fr(0))
        ok_small.append(lowabs > s)
    minc = None
    ok_tail = True
    for ell in range(max(nT, len(dD))):
        cN = tco[ell] if ell < nT else [Fr(0)]
        v = ihorner(cN, I)
        lo = (eps * v[0] if eps > 0 else -v[1]) - s * (dD[ell] if ell < len(dD) else 0)
        if ell == 0:
            ok_tail &= lo > 0
        else:
            ok_tail &= lo >= 0
        r = lo / (dD[ell] if ell < len(dD) and dD[ell] != 0 else 1)
        minc = r if minc is None or r < minc else minc
    resA.append(all(ok_small) and ok_tail)
    log('root %d: sign(sigma_inf)=%+d; k=2..10 |sigma_k| > s: %s; tail certificate k>=11: %s; s = 1/%d; '
        'min over ell of coefficient margin / D_ell = %.3e' % (i + 1, eps, all(ok_small), ok_tail, 1 / s, float(minc)))
assert all(resA)
log('(A) PASS: |sigma_k(b_i)| >= s_i for all k >= 2, all six roots')


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
for i, I in enumerate(roots):
    assert 1 + max(abs(I[0]), abs(I[1])) <= A_[i]  # ||f_1||_1 = 1 + |b_i| <= a_i
    ok, ratio, kap = certificate(A_[i], S_[i], Z_[i])
    ok2, ratio2, _ = certificate(A_[i], S_[i], Z_[i] - 2)
    resB.append(ok)
    log('root %d: a=%s, s=1/%d, z0=2^-%d: G(z0,2Y0) <= 2Y0: %s (max ratio %.5f); at z0=2^-%d: %s (max ratio %.3g);'
        ' radius r > 2^%d |eps|^(5/2)' % (i + 1, A_[i], 1 / S_[i], Z_[i], ok, float(ratio), Z_[i] - 2, ok2,
                                          float(ratio2), Z_[i] * Q // 2))
okc, ratioc, _ = certificate(Fr(8, 5), Fr(1, 8388608), 74)
okc2, ratioc2, _ = certificate(Fr(8, 5), Fr(1, 8388608), 72)
log('common: a=8/5, s=1/8388608, z0=2^-74: %s (max ratio %.5f); at 2^-72: %s; radius r > 2^185 |eps|^(5/2)'
    % (okc, float(ratioc), okc2))
log('kappa =', kap)
assert all(resB) and okc
log('(B) PASS')
log('time %.1fs' % (time.time() - t0))
open('tq5_bounds_radius.out', 'w').write('\n'.join(out) + '\n')
