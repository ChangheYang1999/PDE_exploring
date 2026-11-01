"""Box certificates for the resonance-block majorant at delta = 2h/Q, h >= 2 (theory Section 12.6, Remark 5): harmonic
bounds only at n = kQ, residue series X_1..X_Q, E, V_1..V_(Q-1) in w = z^Q (2Q components).  Inputs as tq_boxh_init.py
(root enclosure by an interval sign change of O_Q, initial norms d_j over the enclosure, kappa and L options).  Before the
box test the formal solution of the block system is compared, coefficient by coefficient, with the direct scalar
recursion indexed by the total order (eta_n = 0 unless Q | n), for the first KCHK coefficients of every component.

usage: tq_block.py Q h profile b0 s [kappa=old|star] [L=half|sharp] [eps=1e-40] [kchk=3]
  profile: 'two' (f_1 = sin + b sin 3, B = 4) or a JSON file {"density": {"1": a_1, "3": a_3, ...}} (exact rationals;
           normalized by a_1, sin 3 coefficient replaced by the root b; B = largest frequency + 1)
  b0: starting guess for the root of O_Q;  s: rational lower bound for inf_k |sigma_k| at that root (e.g. 1/536870912)
Prints the enclosure, d_1..d_Q, the smallest passing z0 = 2^-q in the box family 2 Y0 (and that 2^-(q-1) fails), and
the strict radius 2^(q/(2h)) of the normalized profile (w0 = 2^-q).
"""
import sys, json, time
from fractions import Fraction as Fr
import mpmath as mp

Q, H = int(sys.argv[1]), int(sys.argv[2])
PROF, B0, S = sys.argv[3], sys.argv[4], Fr(sys.argv[5])
opts = dict(a.split('=') for a in sys.argv[6:])
KMODE, LMODE, EPS = opts.get('kappa', 'old'), opts.get('L', 'half'), mp.mpf(opts.get('eps', '1e-40'))
assert H >= 2
mp.mp.dps = 90
mp.iv.dps = 90
iv = mp.iv
t0 = time.time()
DL = Fr(2 * H, Q)

if PROF == 'two':
    HIGHER, BW = {}, 4
else:
    dens = {int(j): Fr(v) for j, v in json.load(open(PROF))['density'].items()}
    HIGHER = {j: v / dens[1] for j, v in dens.items() if j >= 5}
    BW = max(dens) + 1
assert BW % 2 == 0


def p_(n):
    return 1 - n * DL


def P_(n):
    return 2 - n * DL


def lam(n):
    return DL * (n - 1) / (1 - DL)


def addm(d, m, v):
    if m == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[m] = d[m] + v if m in d else v


def T(g, Pi, f, pj, cv):
    """T(g_i, f_j) = -p_j g' f + P_i g f' for sine dicts; cv converts rationals to the working number type"""
    out = {}
    for mu, x in g.items():
        for nu, y in f.items():
            xy = x * y / 2
            addm(out, mu + nu, cv(-pj * mu + Pi * nu) * xy)
            addm(out, nu - mu, cv(-pj * mu - Pi * nu) * xy)
    return out


def poisson(f, n, cv):
    pn, Pn = p_(n), P_(n)
    g = {}
    modes = set()
    for m in f:
        modes.add(m + 1)
        if m > 1:
            modes.add(m - 1)
    for j in modes:
        den = j * j - Pn * Pn
        assert den != 0, (n, j)  # exact: no resonance before order Q
        num = 0
        if j - 1 in f:
            num = num + cv((pn - (j - 1)) / 2) * f[j - 1]
        if j + 1 in f:
            num = num + cv((pn + (j + 1)) / 2) * f[j + 1]
        g[j] = num / cv(den)
    return g


def low_fields(b, cv):
    f1 = {1: cv(Fr(1)), 3: b}
    for j, v in HIGHER.items():
        f1[j] = cv(v)
    F, G = {1: f1}, {1: poisson(f1, 1, cv)}
    for n in range(2, Q + 1):
        acc = {}
        for i in range(1, n):
            for m, v in T(G[i], P_(i), F[n - i], p_(n - i), cv).items():
                acc[m] = acc[m] + v if m in acc else v
        F[n] = {m: v / cv(lam(n)) for m, v in acc.items()}
        if n < Q:
            G[n] = poisson(F[n], n, cv)
    return F


def cv_mp(x):
    return mp.mpf(x.numerator) / x.denominator


def cv_iv(x):
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def O_mp(b):
    return low_fields(b, cv_mp)[Q].get(2 * H - 3, 0)


def exact(x):
    """exact Fraction of an mpmath mpf"""
    sign, man, ex, _ = mp.mpf(x)._mpf_  # value (-1)^sign man 2^ex (mpf.man_exp drops the sign)
    return (-1) ** sign * Fr(man) * Fr(2) ** ex


def hi(x):
    return exact(mp.mp.make_mpf(x._mpi_[1]))


def lo(x):
    return exact(mp.mp.make_mpf(x._mpi_[0]))


# 1. root enclosure by a sign change of O_Q in interval arithmetic
broot = mp.findroot(O_mp, (mp.mpf(B0), mp.mpf(B0) * (1 + mp.mpf(10) ** -6)), solver='secant', tol=mp.mpf(10) ** -80)
bl, bh = exact(broot - EPS), exact(broot + EPS)
Ol = low_fields(cv_iv(bl), cv_iv)[Q][2 * H - 3]
Oh = low_fields(cv_iv(bh), cv_iv)[Q][2 * H - 3]
assert (hi(Ol) < 0 < lo(Oh)) or (hi(Oh) < 0 < lo(Ol)), 'no certified sign change'
print('root of O_%d enclosed in [%s, %s] (width %.1e); B = %d' % (Q, mp.nstr(cv_mp(bl), 25), mp.nstr(cv_mp(bh), 25),
                                                                 float(bh - bl), BW))

# 2. initial norms over the enclosure, rounded up to 10 significant digits
bI = iv.mpf([cv_mp(bl), cv_mp(bh)])
F = low_fields(bI, cv_iv)
D = [Fr(0)]
for j in range(1, Q + 1):
    nrm = 0
    for v in F[j].values():
        nrm = nrm + abs(v)
    u = hi(j * nrm)
    e = 0
    while u * 10 ** e < 10 ** 9:
        e += 1
    while u * 10 ** e >= 10 ** 10:
        e -= 1
    num = -((-u * 10 ** e).__floor__())  # ceiling
    D.append(Fr(num) / Fr(10) ** e)
print('d_j >= j||f_j||_1:', ' '.join('%.4g' % float(d) for d in D[1:]))

# 3. constants
if KMODE == 'old':
    KAP = Fr(Q - 2 * H, H) * (3 - DL) * BW
else:
    KAP = BW * (2 - DL + max(DL, 1 - DL)) * (1 - DL) / DL * Fr(Q + 1, Q)
LC = Fr(Q, 2) if LMODE == 'half' else Fr(3 * Q * Q, 4 * (3 * Q - 1))
print('kappa =', KAP, '; L =', LC, '; s =', S)


class Poly:
    """truncated power series in w with rational coefficients (degree < KCHK)"""
    def __init__(self, c):
        self.c = (list(c) + [Fr(0)] * KCHK)[:KCHK]

    def __add__(self, o):
        o = o if isinstance(o, Poly) else Poly([o])
        return Poly([a + b for a, b in zip(self.c, o.c)])
    __radd__ = __add__

    def __mul__(self, o):
        if not isinstance(o, Poly):
            return Poly([a * o for a in self.c])
        r = [Fr(0)] * KCHK
        for i, a in enumerate(self.c):
            if a:
                for j in range(KCHK - i):
                    r[i + j] += a * o.c[j]
        return Poly(r)
    __rmul__ = __mul__

    def __truediv__(self, o):
        return Poly([a / o for a in self.c])


KCHK = int(opts.get('kchk', '3'))


def make_block(d, kap, L, s):
    """171 map; Y = (V_1..V_(Q-1), E, X_1..X_Q); d[1..Q] initial norms; generic in the number type of w and Y"""
    rng = range(1, Q + 1)
    a = {r: sum(d[i] * d[Q + r - i] for i in rng if Q + r - i in rng and i >= r and Q + r - i >= r) for r in rng}
    b = {r: sum(d[i] * d[Q + r - i] for i in rng if Q + r - i in rng) for r in rng}

    def phi(w, Y):
        V = {r: Y[r - 1] for r in range(1, Q)}
        E = Y[Q - 1]
        X = {r: Y[Q - 1 + r] for r in rng}
        out = []

        def DC(r):
            D = sum((X[i] * X[r - i] for i in rng if r - i in rng), Fr(0))
            C = sum((X[i] * X[Q + r - i] for i in rng if Q + r - i in rng), Fr(0))
            return w * D + w * w * C
        cross_w = {r: 2 * w * sum((d[i] * X[Q + r - i] for i in rng if Q + r - i in rng and i >= r), Fr(0)) for r in rng}
        A = {r: a[r] + cross_w[r] + DC(r) for r in rng}
        Bv = {r: b[r] + 2 * sum((d[i] * X[r - i] for i in rng if r - i in rng), Fr(0)) + cross_w[r] + DC(r) for r in rng}
        for r in range(1, Q):
            out.append(kap * (L * A[r] + w * E * X[r] + 2 * L * sum((d[j] * V[r - j] for j in range(1, r)), Fr(0))))
        out.append(kap / s * (L * A[Q] + w * E * X[Q] + 2 * L * sum((d[j] * V[Q - j] for j in range(1, Q)), Fr(0))))
        for r in rng:
            out.append(kap * (L * Bv[r] + E * d[r] + w * E * X[r]))
        return out
    return phi


def direct(d, kap, L, s, K):
    """total-order scalar recursion of 171 Section 1 through order (K+1)Q + Q"""
    x = {j: d[j] for j in range(1, Q + 1)}
    eta, u = {}, {}
    for k in range(1, K + 1):
        n = k * Q
        for r in range(1, Q + 1):
            t = sum(x[i] * x[n + r - i] for i in range(r, n + 1))  # i, j >= r (so i, j <= n)
            hsum = sum(e * x[n + r - i] for i, e in eta.items() if n + r - i >= Q + 1)  # known harmonics, i <= n - Q
            look = sum(d[j] * u[(n, r - j)] for j in range(1, r))
            val = (L * t + hsum + 2 * L * look)
            if r < Q:
                u[(n, r)] = kap * val
            else:
                eta[n] = kap / s * val
        for m in range(n + 1, n + Q + 1):
            x[m] = kap * sum((L * x[i] + eta.get(i, 0)) * x[m - i] for i in range(1, m))
    return x, eta, u


def check_block(d, kap, L, s):
    phi = make_block(d, kap, L, s)
    w = Poly([0, 1])
    Y = [Poly([0])] * (2 * Q)
    for _ in range(2 * Q * (KCHK + 1)):
        Y = phi(w, Y)
    x, eta, u = direct(d, kap, L, s, KCHK)
    nid = 0
    for k in range(1, KCHK + 1):
        n = k * Q
        for r in range(1, Q):
            assert Y[r - 1].c[k - 1] == u[(n, r)], ('V', r, k)
            nid += 1
        assert Y[Q - 1].c[k - 1] == eta[n], ('E', k)
        nid += 1
        for r in range(1, Q + 1):
            assert Y[Q - 1 + r].c[k - 1] == x[n + r], ('X', r, k)
            nid += 1
    return nid


nid = check_block(D, KAP, LC, S)
print('block system = direct total-order recursion: %d exact coefficient identities' % nid)
PHI = make_block(D, KAP, LC, S)
d = 2 * Q
c0 = PHI(Fr(0), [Fr(0)] * d)
J = [[Fr(0)] * d for _ in range(d)]
for j in range(d):
    e = [Fr(0)] * d
    e[j] = Fr(1)
    col = PHI(Fr(0), e)
    for i in range(d):
        J[i][j] = col[i] - c0[i]
e2 = [Fr(i + 2) for i in range(d)]
assert PHI(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(d)) for i in range(d)]  # affine at w = 0
assert all(J[i][j] == 0 for i in range(d) for j in range(i, d))  # strictly lower triangular


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


Tm = [[Fr(int(i == j)) for j in range(d)] for i in range(d)]
Pw = [row[:] for row in Tm]
for _ in range(d - 1):
    Pw = [[sum(Pw[i][l] * J[l][j] for l in range(d)) for j in range(d)] for i in range(d)]
    Tm = [[Tm[i][j] + Pw[i][j] for j in range(d)] for i in range(d)]
Y0 = matvec(Tm, c0)
BX = [2 * y for y in Y0]


def ratio(q):
    w0 = Fr(1, 2 ** q)
    rest = [u - c - wv for u, c, wv in zip(PHI(w0, BX), c0, matvec(J, BX))]
    Gv = [y + wv for y, wv in zip(Y0, matvec(Tm, rest))]
    return max(g / bb for g, bb in zip(Gv, BX))


q = 1
while ratio(q) > 1:
    q += 1
r1, r0 = ratio(q), ratio(q - 1)
assert r0 > 1
print('smallest passing w0 = 2^-%d (max ratio %.5f); 2^-%d fails (max ratio %.4g); radius r > 2^%s |eps|^(%s)'
      % (q, float(r1), q - 1, float(r0), Fr(q, 2 * H), Fr(Q, 2 * H)))
print('time %.1fs' % (time.time() - t0))
