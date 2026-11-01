"""Exact global response minima and explicit exterior radii at delta = 2h/Q (gcd(h,Q) = 1, 2h < Q, c = Q/(Q-2h)),
f_1 = sin + b_i sin 3, for the real roots b_i of the first obstruction.  h = 1 reproduces tq_minima.py.
usage: tq_radiush.py Q h k_1[:KT_1] ... k_m[:KT_m]   (k_i = proposed unique minimizing index for the i-th real root,
increasing order; k_i = 0: the infimum is |sigma_inf(b_i)| and is not attained; KT_i >= K0 = ceil((4Q+2)/(2h)) is the
start of the tail test, default K0).  k1 = 1 if h >= 2 else 2.
(A) as in tq_minima.py, over k >= k1: finite gaps for k1 <= k < KT_i by interval evaluation (direct responses for
    k < K0, exact values of the generic formula for K0 <= k < KT_i); the tail k >= KT_i by the t-coefficient test on
    k = KT_i + t.  The certified lower bound s_i <= min_k |sigma_k(b_i)| has 3 significant digits.  The exact generic
    sigma is cached in tq_sigma_Q<Q>h<h>.cache.json and reused by later runs.
(B) the generating system of the majorant.  h = 1: Theorem T_Q, Step 4 (Y = (W, V_1..V_{Q-1}, E)).  h >= 2: the
    first constant sits at order Q, so E = sum_{n>=Q} eta_n z^(n-Q), V_r = sum_{n>=Q} u_(n,r) z^(n-Q), X = P + z^(Q+1) W,
      W   = kL z^-(Q+1)[P^2]_(>=Q+1) + 2kL P W + kL z^(Q+1) W^2 + k E (z^-1 P + z^Q W),
      V_r = k[L A_r + z^(Q+1-r) E W + Q sum_(s<r) x_s V_(r-s)]  (1 <= r <= Q-1),
      E   = (k/sigma_*)[L A_Q + z E W + Q sum_(s<Q) x_s V_(Q-s)],
      A_r = z^-(Q+r)[P_r^2]_(>=Q+r) + 2 z^(1-r) P_r W + z^(Q+2-r) W^2,
    with k = kappa = ((Q-2h)/h)(3-2h/Q)B, L = Q/2, x_j = Cat_(j-1)(kL)^(j-1) a^j (j <= Q).  In the order
    (V_1..V_(Q-1), E, W) the linear part at z = 0 is strictly lower triangular (W depends on E through k x_1 E).
    Box test G(z0, 2 Y0) <= 2 Y0 exactly as for h = 1; then the tuned series converges for r > z0^(-Q/(2h)) (times
    |epsilon|^(Q/(2h))).
"""
import sys, time
from fractions import Fraction as Fr
from math import comb
QQ_ = int(sys.argv[1]) if len(sys.argv) > 1 else 9
HH_ = int(sys.argv[2]) if len(sys.argv) > 2 else 2
KMIN, KTAIL = [], []
for v_ in sys.argv[3:]:
    kk_, _, kt_ = v_.partition(':')
    KMIN.append(int(kk_))
    KTAIL.append(int(kt_) if kt_ else None)
K0 = -(-(4 * QQ_ + 2) // (2 * HH_))
KTAIL = [kt_ if kt_ else K0 for kt_ in KTAIL]
assert all(kt_ >= K0 for kt_ in KTAIL)
sys.argv = [sys.argv[0], str(QQ_), str(HH_), '3', str(K0 + 5)]
import tq_symh as T
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


Q, B, H = QQ_, 4, HH_
k1, N1 = T.KFIRST, T.NFIRST
F, G = T.low_orders(N1)
O = sympify(F[N1].get(2 * H * k1 - 3, T.R.zero).as_expr())
P10 = Poly(Poly(O, b).primitive()[1], b)
ivs = P10.intervals(eps=Rational(1, 10 ** 30))
roots = [(fr(lo), fr(hi)) for (lo, hi), m in ivs]
assert all(m == 1 for _, m in ivs)
log('Q = %d, h = %d, %d real roots; k1 = %d, K0 = %d' % (Q, H, len(roots), k1, K0))
assert len(KMIN) == len(roots)
# ---------------- (A) response lower bounds
small = {}
for kv in range(k1, K0):
    s, _ = T.sigma(kv, F, G)
    small[kv] = [fr(c) for c in Poly(sympify(s.as_expr()), b).all_coeffs()]
import os, json
cache = 'tq_sigma_Q%dh%d.cache.json' % (Q, H)
if os.path.exists(cache):  # exact generic sigma = num(k, b) / den(k) from an earlier run of this script
    cj = json.load(open(cache))
    num = Poly.from_dict({(i, j): Rational(p, q) for i, j, p, q in cj['num']}, b, k).as_expr()
    den = Poly.from_dict({(j,): Rational(p, q) for j, p, q in cj['den']}, k).as_expr()
    log('generic sigma read from', cache)
else:
    sg, _ = T.sigma(None, F, G)
    num, den = fraction(together(sympify(sg.as_expr())))
    json.dump({'num': [[i, j, str(Rational(c).p), str(Rational(c).q)] for (i, j), c in Poly(num, b, k).as_dict().items()],
               'den': [[j, str(Rational(c).p), str(Rational(c).q)] for (j,), c in Poly(den, k).as_dict().items()]},
              open(cache, 'w'))
Nb = Poly(num, b)
Dk = Poly(den, k)
# K0 <= k < max tail start: exact values of the generic formula (valid for k >= K0)
for kv in range(K0, max(KTAIL)):
    dv = fr(Dk.eval(kv))
    small[kv] = [fr(Poly(c, k).eval(kv)) / dv for c in Nb.all_coeffs()]


def tailcoeffs(KT):
    """ascending t-coefficients of D(KT+t) (sign-normalized) and of N(KT+t, b) (as b-polynomials, descending)"""
    dD = Dk.shift(KT).all_coeffs()[::-1]
    sgnD = 1 if dD[-1] > 0 else -1
    dD = [fr(c) * sgnD for c in dD]
    assert all(c > 0 for c in dD), 'D(KT+t) coefficients not of one sign'
    nb = Nb.degree()
    colsb = []
    for i in range(nb + 1):
        ci = Nb.coeff_monomial(b ** i)
        colsb.append([fr(c) * sgnD for c in Poly(ci, k).shift(KT).all_coeffs()[::-1]] if ci != 0 else [])
    nT = max(len(c) for c in colsb)
    tco = [[colsb[i][ell] if ell < len(colsb[i]) else Fr(0) for i in range(nb, -1, -1)] for ell in range(nT)]
    log('KT = %d: D(KT+t): %d coefficients, all positive after sign normalization; N(KT+t,b): degree %d in b, %d '
        't-coefficients' % (KT, len(dD), nb, nT))
    return dD, tco, nT


TAIL = {KT: tailcoeffs(KT) for KT in sorted(set(KTAIL))}
# sigma_inf for the sign
dn = Poly(num, k).degree()
dd = Poly(den, k).degree()
lead = Poly(num, k).coeff_monomial(k ** dd) if dn == dd else 0
sinf = [fr(c) for c in Poly(sympify(lead) / Poly(den, k).LC(), b).all_coeffs()]
resA = []
A_, S_ = [], []
for i, I in enumerate(roots):
    ki = KMIN[i]
    KT = KTAIL[i]
    dD, tco, nT = TAIL[KT]
    tpoly = small[ki] if ki else sinf
    vmin = ihorner(tpoly, I)
    assert vmin[0] > 0 or vmin[1] < 0
    ei = 1 if vmin[0] > 0 else -1
    lo_i, hi_i = (vmin[0], vmin[1]) if ei > 0 else (-vmin[1], -vmin[0])  # interval of |sigma_(k_i)(b_i)|
    vi = ihorner(sinf, I)
    assert vi[0] > 0 or vi[1] < 0
    eps = 1 if vi[0] > 0 else -1
    gaps = []
    for kv in range(k1, KT):
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
    log('root %d: k_i = %s, sign %+d, |sigma_(k_i)| in [%.16g, %.16g]; finite gaps k=%d..%d positive: %s (min gap %.3e); '
        'tail k>=%d strictly above the target: %s (min coefficient margin / D_ell %.3e); certified s_i = %s'
        % (i + 1, ki if ki else 'inf (not attained)', ei, float(lo_i), float(hi_i), k1, KT - 1, ok_small, float(min(gaps)), KT, ok_tail, float(minc), si))
assert all(resA)
log('(A) PASS: for all %d roots, inf_{k>=%d} |sigma_k(b_i)| is attained only at the listed k_i; where k_i = inf it equals |sigma_inf(b_i)| and is attained at no finite k' % (len(roots), k1))


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


def make_phi_h(a, s):
    """h >= 2; Y = (V_1..V_(Q-1), E, W)"""
    kap = Fr(Q - 2 * H, H) * (3 - Fr(2 * H, Q)) * B
    L = Fr(Q, 2)
    cat = [comb(2 * m, m) // (m + 1) for m in range(Q)]
    x = [Fr(0)] + [cat[j - 1] * (kap * L) ** (j - 1) * a ** j for j in range(1, Q + 1)]
    Pz = [Fr(0)] + x[1:]
    P2 = pmul(Pz, Pz)
    hiP2 = P2[Q + 1:]  # [P^2]_(>=Q+1) / z^(Q+1)
    Pdz = Pz[1:]  # P / z

    def Pr(r):
        return [Fr(0)] * r + x[r:Q + 1]

    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = Pr(r)
        hiA[r] = pmul(pr, pr)[Q + r:]  # [P_r^2]_(>=Q+r)/z^(Q+r)
        lowA[r] = pr[r:]  # P_r / z^r

    def phi(z, Y):
        V, E, W = Y[0:Q - 1], Y[Q - 1], Y[Q]
        Pv = peval(Pz, z)

        def Ar(r):
            return peval(hiA[r], z) + 2 * z * peval(lowA[r], z) * W + z ** (Q + 2 - r) * W * W
        out = []
        for r in range(1, Q):
            out.append(kap * (L * Ar(r) + z ** (Q + 1 - r) * E * W + Q * sum(x[sq] * V[r - sq - 1] for sq in range(1, r))))
        out.append(kap / s * (L * Ar(Q) + z * E * W + Q * sum(x[sq] * V[Q - sq - 1] for sq in range(1, Q))))
        out.append(kap * L * peval(hiP2, z) + 2 * kap * L * Pv * W + kap * L * z ** (Q + 1) * W * W
                   + kap * E * (peval(Pdz, z) + z ** Q * W))
        return out
    return phi, kap


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def certificate(a, s, q):
    phi, kap = make_phi(a, s) if H == 1 else make_phi_h(a, s)
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
        '(max ratio %.3g); radius r > 2^%s |eps|^(%s)' % (i + 1, A_[i], S_[i], q, ok, float(ratio), q - 1, ok1,
                                                       float(ratio1), Fr(q * Q, 2 * H), Fr(Q, 2 * H)))
ac = max(A_)
sc = min(S_)
q = 1
while not certificate(ac, sc, q)[0]:
    q += 1
okc, ratioc, _ = certificate(ac, sc, q)
log('common: a=%s, s=%s, z0=2^-%d: %s (max ratio %.5f); radius r > 2^%s |eps|^(%s)'
    % (ac, sc, q, okc, float(ratioc), Fr(q * Q, 2 * H), Fr(Q, 2 * H)))
log('kappa =', kap)
assert all(resB) and okc
log('(B) PASS')
log('time %.1fs' % (time.time() - t0))
open('tq_radiush_Q%dh%d.out' % (Q, H), 'w').write('\n'.join(out) + '\n')
