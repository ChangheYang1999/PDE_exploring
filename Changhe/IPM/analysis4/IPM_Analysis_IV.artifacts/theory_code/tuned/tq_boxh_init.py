"""Box certificates for the tuned rational majorant at delta = 2h/Q, h >= 2, with the actual initial norms
d_j >= j ||f_j||_1 (j <= Q) in place of the Catalan bounds (theory Section 12.6, Remark 4), optionally with the reduced
bilinear constant kappa_* and the sharp Poisson constant L_Q = 3Q^2/(4(3Q-1)).  Independent of the certificate code that
first proposed these refinements: the root is enclosed by a sign change of O_Q in interval arithmetic (mpmath iv), the
initial fields f_1..f_Q are evaluated over that enclosure, and the box test is exact rational arithmetic (as tq_boxh.py).

usage: tq_boxh_init.py Q h profile b0 s [kappa=old|star] [L=half|sharp] [eps=1e-40]
  profile: 'two' (f_1 = sin + b sin 3, B = 4) or a JSON file {"density": {"1": a_1, "3": a_3, ...}} (exact rationals;
           normalized by a_1, sin 3 coefficient replaced by the root b; B = largest frequency + 1)
  b0: starting guess for the root of O_Q;  s: rational lower bound for inf_k |sigma_k| at that root (e.g. 1/536870912)
Prints the enclosure, d_1..d_Q, the smallest passing z0 = 2^-q in the box family 2 Y0 (and that 2^-(q-1) fails), and
the strict radius 2^(qQ/(2h)) of the normalized profile.
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


def make_phi_h(x, kap, L, s):
    """h >= 2; Y = (V_1..V_(Q-1), E, W); x[1..Q] are the initial norms (P = sum x_j z^j)"""
    Pz = x[:]
    hiP2 = pmul(Pz, Pz)[Q + 1:]
    Pdz = Pz[1:]
    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = [Fr(0)] * r + x[r:Q + 1]
        hiA[r] = pmul(pr, pr)[Q + r:]
        lowA[r] = pr[r:]

    def phi(z, Y):
        V, E, W = Y[0:Q - 1], Y[Q - 1], Y[Q]
        Pv = peval(Pz, z)

        def Ar(r):
            return peval(hiA[r], z) + 2 * z * peval(lowA[r], z) * W + z ** (Q + 2 - r) * W * W
        out = []
        for r in range(1, Q):
            out.append(kap * (L * Ar(r) + z ** (Q + 1 - r) * E * W + 2 * L * sum(x[sq] * V[r - sq - 1] for sq in range(1, r))))
        out.append(kap / s * (L * Ar(Q) + z * E * W + 2 * L * sum(x[sq] * V[Q - sq - 1] for sq in range(1, Q))))
        out.append(kap * L * peval(hiP2, z) + 2 * kap * L * Pv * W + kap * L * z ** (Q + 1) * W * W
                   + kap * E * (peval(Pdz, z) + z ** Q * W))
        return out
    return phi


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


PHI = make_phi_h(D, KAP, LC, S)
d = Q + 1
c0 = PHI(Fr(0), [Fr(0)] * d)
J = [[Fr(0)] * d for _ in range(d)]
for j in range(d):
    e = [Fr(0)] * d
    e[j] = Fr(1)
    col = PHI(Fr(0), e)
    for i in range(d):
        J[i][j] = col[i] - c0[i]
e2 = [Fr(i + 2) for i in range(d)]
assert PHI(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(d)) for i in range(d)]  # affine at z = 0
assert all(J[i][j] == 0 for i in range(d) for j in range(i, d))  # strictly lower triangular
Tm = [[Fr(int(i == j)) for j in range(d)] for i in range(d)]
Pw = [row[:] for row in Tm]
for _ in range(Q):
    Pw = [[sum(Pw[i][l] * J[l][j] for l in range(d)) for j in range(d)] for i in range(d)]
    Tm = [[Tm[i][j] + Pw[i][j] for j in range(d)] for i in range(d)]
Y0 = matvec(Tm, c0)
BX = [2 * y for y in Y0]


def ratio(q):
    z0 = Fr(1, 2 ** q)
    rest = [u - c - w for u, c, w in zip(PHI(z0, BX), c0, matvec(J, BX))]
    Gv = [y + w for y, w in zip(Y0, matvec(Tm, rest))]
    return max(g / bb for g, bb in zip(Gv, BX))


q = 1
while ratio(q) > 1:
    q += 1
r1, r0 = ratio(q), ratio(q - 1)
assert r0 > 1
print('smallest passing z0 = 2^-%d (max ratio %.5f); 2^-%d fails (max ratio %.4g); radius r > 2^%s |eps|^(%s)'
      % (q, float(r1), q - 1, float(r0), Fr(q * Q, 2 * H), Fr(Q, 2 * H)))
print('time %.1fs' % (time.time() - t0))
