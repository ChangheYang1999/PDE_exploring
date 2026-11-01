"""Certified-prefix resonance-block majorant at delta = 2h/Q, h >= 2 (theory Section 12.6, Remark 5(a), general M).
Independent of the certificate code that first proposed it.  Steps:
 1. the root of O_Q is enclosed by an interval sign change (mpmath iv, 90 digits by default), as in tq_boxh_init.py;
 2. the uniquely tuned prefix f_1..f_N, N = MQ, is computed over that enclosure in interval arithmetic (Fourier form of
    the recurrence, as cand_sigma.py): at n = kQ < N the obstruction mode 2hk-3 of f_n is checked to contain 0 and set to
    0 (it vanishes exactly: k = 1 by the root, k > 1 by the tuning of H_(n-Q)), the resonant stream mode 2hk-2 is left
    free, and H_n is the interval -R0/(R1-R0) from two provisional continuations to n+Q (H_n = 0 and H_n = 1), which is
    exact because the obstruction at n+Q is affine in H_n; the interval R1-R0 must exclude 0;
 3. d_j >= j||f_j||_1 (j <= N) and e_a >= aQ|H_aQ| (a < M) are interval upper bounds rounded up (10 digits);
 4. the 2Q-component block map of Remark 5(a) with kappa_N and L_Q; its formal solution is compared coefficient by
    coefficient with the direct scalar recursion indexed by the total order (KCHK coefficients per component);
 5. affine form and strict triangularity at w = 0, Y0 = (I-J)^(-1) c0, and two box families at w0 = 2^-q: the box 2 Y0,
    and an adaptive box (floating fixed-point iteration of G at w0 from Y0, scaled by 1 + 10^-6 and rounded to
    rationals, then checked exactly: b >= Y0 and G(w0, b) <= b).  Prints the smallest passing q of each family.

usage: tq_prefix_block.py Q h profile b0 s M [L=sharp|half] [eps=1e-40] [kchk=2] [dps=90]
  profile: 'two' (f_1 = sin + b sin 3, B = 4) or a JSON file as in tq_boxh_init.py; s: rational lower bound for
  inf_k |sigma_k|.  kappa is always kappa_N of Remark 5(a).
"""
import sys, json, time
from fractions import Fraction as Fr
import mpmath as mp

Q, H = int(sys.argv[1]), int(sys.argv[2])
PROF, B0, S, M = sys.argv[3], sys.argv[4], Fr(sys.argv[5]), int(sys.argv[6])
opts = dict(a.split('=') for a in sys.argv[7:])
LMODE, EPS = opts.get('L', 'sharp'), mp.mpf(opts.get('eps', '1e-40'))
KCHK = int(opts.get('kchk', '2'))
DPS = int(opts.get('dps', '90'))
assert H >= 2 and M >= 1
N = M * Q
mp.mp.dps = DPS
mp.iv.dps = DPS
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
    """T(g_i, f_j) = -p_j g' f + P_i g f' for sine dicts"""
    out = {}
    for mu, x in g.items():
        for nu, y in f.items():
            xy = x * y / 2
            addm(out, mu + nu, cv(-pj * mu + Pi * nu) * xy)
            addm(out, nu - mu, cv(-pj * mu - Pi * nu) * xy)
    return out


def poisson(f, n, cv, skip=None):
    pn, Pn = p_(n), P_(n)
    g = {}
    modes = set()
    for m in f:
        modes.add(m + 1)
        if m > 1:
            modes.add(m - 1)
    for j in modes:
        if j == skip:
            continue
        den = j * j - Pn * Pn
        assert den != 0, (n, j)
        num = 0
        if j - 1 in f:
            num = num + cv((pn - (j - 1)) / 2) * f[j - 1]
        if j + 1 in f:
            num = num + cv((pn + (j + 1)) / 2) * f[j + 1]
        g[j] = num / cv(den)
    return g


def cv_mp(x):
    return mp.mpf(x.numerator) / x.denominator


def cv_iv(x):
    return iv.mpf(x.numerator) / iv.mpf(x.denominator)


def density(F, G, m, cv):
    acc = {}
    for i in range(1, m):
        for k, v in T(G[i], P_(i), F[m - i], p_(m - i), cv).items():
            acc[k] = acc[k] + v if k in acc else v
    return {k: v / cv(lam(m)) for k, v in acc.items()}


def f1_of(b, cv):
    f1 = {1: cv(Fr(1)), 3: b}
    for j, v in HIGHER.items():
        f1[j] = cv(v)
    return f1


def O_mp(b):
    F, G = {1: f1_of(b, cv_mp)}, {}
    G[1] = poisson(F[1], 1, cv_mp)
    for n in range(2, Q + 1):
        F[n] = density(F, G, n, cv_mp)
        if n < Q:
            G[n] = poisson(F[n], n, cv_mp)
    return F[Q].get(2 * H - 3, 0)


def exact(x):
    sign, man, ex, _ = mp.mpf(x)._mpf_
    return (-1) ** sign * Fr(man) * Fr(2) ** ex


def hi(x):
    return exact(mp.mp.make_mpf(x._mpi_[1]))


def lo(x):
    return exact(mp.mp.make_mpf(x._mpi_[0]))


def contains0(x):
    return lo(x) <= 0 <= hi(x)


def up10(u):
    e = 0
    while u * 10 ** e < 10 ** 9:
        e += 1
    while u * 10 ** e >= 10 ** 10:
        e -= 1
    return Fr(-((-u * 10 ** e).__floor__())) / Fr(10) ** e


# 1. root enclosure
broot = mp.findroot(O_mp, (mp.mpf(B0), mp.mpf(B0) * (1 + mp.mpf(10) ** -6)), solver='secant', tol=mp.mpf(10) ** -(DPS - 10))
bl, bh = exact(broot - EPS), exact(broot + EPS)


def O_iv(b):
    F, G = {1: f1_of(b, cv_iv)}, {}
    G[1] = poisson(F[1], 1, cv_iv)
    for n in range(2, Q + 1):
        F[n] = density(F, G, n, cv_iv)
        if n < Q:
            G[n] = poisson(F[n], n, cv_iv)
    return F[Q][2 * H - 3]


Ol, Oh = O_iv(cv_iv(bl)), O_iv(cv_iv(bh))
assert (hi(Ol) < 0 < lo(Oh)) or (hi(Oh) < 0 < lo(Ol)), 'no certified sign change'
print('root of O_%d enclosed in [%s, %s] (width %.1e); B = %d; N = %d (M = %d)'
      % (Q, mp.nstr(cv_mp(bl), 25), mp.nstr(cv_mp(bh), 25), float(bh - bl), BW, N, M), flush=True)

# 2. tuned prefix over the enclosure
bI = iv.mpf([cv_mp(bl), cv_mp(bh)])
F, G, HARM = {1: f1_of(bI, cv_iv)}, {}, {}
G[1] = poisson(F[1], 1, cv_iv)


def resonant_stream(Fn, n, Hn):
    k = n // Q
    qm = 2 * H * k - 2
    g = poisson(Fn, n, cv_iv, skip=qm)
    g[qm] = Hn
    return g


for m in range(2, N + 1):
    F[m] = density(F, G, m, cv_iv)
    if m % Q == 0:
        k = m // Q
        ob = 2 * H * k - 3
        assert contains0(F[m].get(ob, iv.mpf(0))), ('obstruction interval excludes 0', m)
        F[m][ob] = iv.mpf(0)  # exact value 0
        if m == N:
            break
        Rv = []
        for hv in (iv.mpf(0), iv.mpf(1)):
            F2, G2 = dict(F), dict(G)
            G2[m] = resonant_stream(F[m], m, hv)
            for mm in range(m + 1, m + Q + 1):
                F2[mm] = density(F2, G2, mm, cv_iv)
                if mm < m + Q:
                    G2[mm] = poisson(F2[mm], mm, cv_iv)
            Rv.append(F2[m + Q].get(2 * H * (k + 1) - 3, iv.mpf(0)))
        Sv = Rv[1] - Rv[0]
        assert not contains0(Sv), ('response interval contains 0', m)
        HARM[m] = -Rv[0] / Sv
        G[m] = resonant_stream(F[m], m, HARM[m])
        print('  n = %d: response %s, H_n = %s' % (m, mp.nstr(cv_mp(lo(Sv)), 8), mp.nstr(cv_mp(lo(HARM[m])), 10)),
              flush=True)
    else:
        G[m] = poisson(F[m], m, cv_iv)

D = [Fr(0)]
for j in range(1, N + 1):
    nrm = iv.mpf(0)
    for v in F[j].values():
        nrm = nrm + abs(v)
    D.append(up10(hi(j * nrm)))
EA = {a: up10(hi(a * Q * abs(HARM[a * Q]))) for a in range(1, M)}
print('d_j >= j||f_j||_1:', ' '.join('%.4g' % float(d) for d in D[1:]))
print('e_a >= aQ|H_aQ|:', ' '.join('%.4g' % float(EA[a]) for a in range(1, M)))
print('prefix time %.1fs' % (time.time() - t0), flush=True)

# 3. constants
KAP = BW * (2 - DL + max(DL, 1 - DL)) * (1 - DL) / DL * Fr(N + 1, N)
LC = Fr(Q, 2) if LMODE == 'half' else Fr(3 * Q * Q, 4 * (3 * Q - 1))
print('kappa_N =', KAP, '; L =', LC, '; s =', S)


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


def zmul(A, B):
    out = {}
    for i, x in A.items():
        for j, y in B.items():
            out[i + j] = out.get(i + j, Fr(0)) + x * y
    return out


def Kproj(Fz, r):
    """[z^(N+r+kQ)] F, k >= 0"""
    top = max(Fz) if Fz else 0
    return [Fz.get(N + r + k * Q, Fr(0)) for k in range(max(0, (top - N - r) // Q + 1))]


def make_block(d, e, kap, L, s):
    rng = range(1, Q + 1)
    Pz = {i: d[i] for i in range(1, N + 1)}
    Hz = {a * Q: e[a] for a in range(1, M)}
    P2 = zmul(Pz, Pz)
    KP2 = {r: Kproj(P2, r) for r in rng}
    KPr2 = {}
    for r in rng:
        Pr = {i: v for i, v in Pz.items() if i >= r}
        KPr2[r] = Kproj(zmul(Pr, Pr), r)
    KHP = {}
    for b in (1, Q + 1):
        Pb = {i: v for i, v in Pz.items() if i >= b}
        HP = zmul(Hz, Pb)
        KHP[b] = {r: Kproj(HP, r) for r in rng}
    Sl = {}
    for r in rng:
        for b in (1, r):
            Sl[(r, b)] = [(i, t, (i + t - r) // Q) for i in range(b, N + 1) for t in rng
                          if i + t - r >= 0 and (i + t - r) % Q == 0]
    Tl = {(r, b): [(a, d[a * Q + r]) for a in range(0, N // Q + 1) if b <= a * Q + r <= N] for r in rng for b in (1, Q + 1)}
    maxk = 2 * M + 4

    def phi(w, Y):
        wp = [Fr(1), w]
        for _ in range(maxk + 2 * N // Q):
            wp.append(wp[-1] * w)

        def val(cs):
            return sum((c * wp[k] for k, c in enumerate(cs) if c), Fr(0))
        V = {r: Y[r - 1] for r in range(1, Q)}
        E = Y[Q - 1]
        X = {r: Y[Q - 1 + r] for r in rng}
        Hs = sum((e[a] * wp[a] for a in range(1, M)), Fr(0))
        DC = {}
        for r in rng:
            Dr = sum((X[i] * X[r - i] for i in rng if r - i in rng), Fr(0))
            Cr = sum((X[i] * X[Q + r - i] for i in rng if Q + r - i in rng), Fr(0))
            DC[r] = wp[M] * Dr + wp[M + 1] * Cr

        def Sv(r, b):
            return sum((d[i] * X[t] * wp[k] for i, t, k in Sl[(r, b)]), Fr(0))

        def Tv(r, b):
            return sum((c * wp[a] for a, c in Tl[(r, b)]), Fr(0))

        def Z(r, b):
            return val(KHP[b][r]) + Hs * X[r] + E * Tv(r, b) + wp[M] * E * X[r]
        out = []
        for r in range(1, Q):
            A = val(KPr2[r]) + 2 * Sv(r, r) + DC[r]
            out.append(kap * (L * A + Z(r, Q + 1) + 2 * L * sum((d[j] * V[r - j] for j in range(1, r)), Fr(0))))
        A = val(KPr2[Q]) + 2 * Sv(Q, Q) + DC[Q]
        out.append(kap / s * (L * A + Z(Q, Q + 1) + 2 * L * sum((d[j] * V[Q - j] for j in range(1, Q)), Fr(0))))
        for r in rng:
            B = val(KP2[r]) + 2 * Sv(r, 1) + DC[r]
            out.append(kap * (L * B + Z(r, 1)))
        return out
    return phi


def direct(d, e, kap, L, s, K):
    """scalar recursion of Remark 5(a) indexed by the total order, from the prefix, through order N + KQ"""
    x = {j: d[j] for j in range(1, N + 1)}
    eta = {a * Q: e[a] for a in range(1, M)}
    u = {}
    for k in range(K):
        n = N + k * Q
        for r in range(1, Q + 1):
            t = sum(x[i] * x[n + r - i] for i in range(r, n + 1))
            hsum = sum(ev * x[n + r - i] for i, ev in eta.items() if n + r - i >= Q + 1)
            look = sum(d[j] * u[(n, r - j)] for j in range(1, r))
            v = L * t + hsum + 2 * L * look
            if r < Q:
                u[(n, r)] = kap * v
            else:
                eta[n] = kap / s * v
        for m in range(n + 1, n + Q + 1):
            x[m] = kap * sum((L * x[i] + eta.get(i, 0)) * x[m - i] for i in range(1, m))
    return x, eta, u


PHI = make_block(D, EA, KAP, LC, S)
wpoly = Poly([0, 1])
Yp = [Poly([0])] * (2 * Q)
for _ in range(2 * Q * (KCHK + 1)):
    Yp = PHI(wpoly, Yp)
xd, etad, ud = direct(D, EA, KAP, LC, S, KCHK)
nid = 0
for k in range(KCHK):
    n = N + k * Q
    for r in range(1, Q):
        assert Yp[r - 1].c[k] == ud[(n, r)], ('V', r, k)
        nid += 1
    assert Yp[Q - 1].c[k] == etad[n], ('E', k)
    nid += 1
    for r in range(1, Q + 1):
        assert Yp[Q - 1 + r].c[k] == xd[n + r], ('X', r, k)
        nid += 1
print('block system = direct total-order recursion: %d exact coefficient identities' % nid, flush=True)

dim = 2 * Q
c0 = PHI(Fr(0), [Fr(0)] * dim)
J = [[Fr(0)] * dim for _ in range(dim)]
for j in range(dim):
    ev = [Fr(0)] * dim
    ev[j] = Fr(1)
    col = PHI(Fr(0), ev)
    for i in range(dim):
        J[i][j] = col[i] - c0[i]
e2 = [Fr(i + 2) for i in range(dim)]
assert PHI(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(dim)) for i in range(dim)]
assert all(J[i][j] == 0 for i in range(dim) for j in range(i, dim))


def matvec(Mx, v):
    return [sum(Mx[i][j] * v[j] for j in range(len(v))) for i in range(len(Mx))]


Tm = [[Fr(int(i == j)) for j in range(dim)] for i in range(dim)]
Pw = [row[:] for row in Tm]
for _ in range(dim - 1):
    Pw = [[sum(Pw[i][l] * J[l][j] for l in range(dim)) for j in range(dim)] for i in range(dim)]
    Tm = [[Tm[i][j] + Pw[i][j] for j in range(dim)] for i in range(dim)]
Y0 = matvec(Tm, c0)


def Gmap(w0, b):
    rest = [u - c - wv for u, c, wv in zip(PHI(w0, b), c0, matvec(J, b))]
    return [y + wv for y, wv in zip(Y0, matvec(Tm, rest))]


def ratio_2Y0(q):
    b = [2 * y for y in Y0]
    return max(g / bb for g, bb in zip(Gmap(Fr(1, 2 ** q), b), b))


def adaptive(q):
    """floating iteration of G at w0 = 2^-q from Y0; returns the exact max ratio of the rounded box, or None"""
    w0 = Fr(1, 2 ** q)
    Tf = [[float(v) for v in row] for row in Tm]
    Y0f = [float(v) for v in Y0]
    Jf = [[float(v) for v in row] for row in J]
    c0f = [float(v) for v in c0]
    PHf = make_block([float(v) for v in D], {a: float(v) for a, v in EA.items()}, float(KAP), float(LC), float(S))
    b = Y0f[:]
    wf = float(w0)
    for it in range(2000):
        ph = PHf(wf, b)
        rest = [u - c - sum(Jf[i][j] * b[j] for j in range(dim)) for i, (u, c) in enumerate(zip(ph, c0f))]
        nb = [Y0f[i] + sum(Tf[i][j] * rest[j] for j in range(dim)) for i in range(dim)]
        if any(v != v or v > 1e300 for v in nb):
            return None
        done = max(abs(x - y) / y for x, y in zip(nb, b)) < 1e-13
        b = nb
        if done:
            break
    else:
        return None
    best = None
    for t in (Fr(1, 10 ** 9), Fr(1, 10 ** 6), Fr(1, 10 ** 4), Fr(1, 100), Fr(1, 10)):
        bx = [max(Fr(v) * (1 + t), y) for v, y in zip(b, Y0)]
        rt = max(g / bb for g, bb in zip(Gmap(w0, bx), bx))
        best = rt if best is None else min(best, rt)
        if rt <= 1:
            return rt
    return best


q = 1
while ratio_2Y0(q) > 1:
    q += 1
r1, r0 = ratio_2Y0(q), ratio_2Y0(q - 1)
assert r0 > 1
print('box 2Y0: smallest passing w0 = 2^-%d (max ratio %.5f); 2^-%d fails (max ratio %.4g); radius r > 2^%s |eps|^(%s)'
      % (q, float(r1), q - 1, float(r0), Fr(q, 2 * H), Fr(Q, 2 * H)), flush=True)
qa = q
while True:
    ra = adaptive(qa - 1)
    if ra is None or ra > 1:
        break
    qa -= 1
ra = adaptive(qa)
if ra is not None and ra <= 1:
    print('adaptive box: smallest passing w0 = 2^-%d (exact max ratio %.8f; at 2^-%d the floating iteration diverges '
          'or every rounded box fails); radius r > 2^%s |eps|^(%s)' % (qa, float(ra), qa - 1, Fr(qa, 2 * H), Fr(Q, 2 * H)))
else:
    print('adaptive box: no improvement on the box 2Y0')
print('time %.1fs' % (time.time() - t0))
