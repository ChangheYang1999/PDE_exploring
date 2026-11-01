"""Box certificates G(z0, 2 Y0) <= 2 Y0 for the tuned majorant at delta = 2h/Q, B = 4, from given rational inputs
(a_i, s_i): a_i >= ||f_1||_1, s_i <= inf_k |sigma_k(b_i)|.  Part (B) of tq_radiush.py without the response
computation, so that boxes from any source of (a_i, s_i) can be replayed.
usage: tq_boxh.py Q h [B=bandwidth] a_1 s_1 a_2 s_2 ...   (rationals such as 133/125 or 2**-29 given as 1/536870912;
B defaults to 4, i.e. f_1 = sin + b sin 3)
For each pair: the smallest q with G(2^-q, 2 Y0) <= 2 Y0, a check that q - 1 fails, and the strict radius
2^(qQ/(2h)) |eps|^(Q/(2h)).  Then the common certificate with max a_i and min s_i.
h = 1: Theorem T_Q, Step 4 (Y = (W, V_1..V_(Q-1), E)); h >= 2: Theorem T_{Q,h}, Step 3 (Y = (V_1..V_(Q-1), E, W)).
"""
import sys, time
from fractions import Fraction as Fr
from math import comb

Q, H = int(sys.argv[1]), int(sys.argv[2])
args = sys.argv[3:]
B = 4
if args and args[0].startswith('B='):  # optional bandwidth (even; frequencies of f_1 below B)
    B = int(args[0][2:])
    args = args[1:]
vals = [Fr(v) for v in args]
PAIRS = list(zip(vals[0::2], vals[1::2]))
t0 = time.time()


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


def lowfields(a, kap):
    L = Fr(Q, 2)
    cat = [comb(2 * m, m) // (m + 1) for m in range(Q)]
    x = [Fr(0)] + [cat[j - 1] * (kap * L) ** (j - 1) * a ** j for j in range(1, Q + 1)]
    return L, x, [Fr(0)] + x[1:]


def make_phi(a, s):
    """h = 1; Y = (W, V_1..V_(Q-1), E)"""
    kap = Fr(Q - 2) * (3 - Fr(2, Q)) * B
    L, x, Pz = lowfields(a, kap)
    hiP2 = pmul(Pz, Pz)[Q + 1:]
    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = [Fr(0)] * r + x[r:Q + 1]
        hiA[r] = pmul(pr, pr)[Q + r + 1:]
        lowA[r] = pr[r:]

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
    L, x, Pz = lowfields(a, kap)
    hiP2 = pmul(Pz, Pz)[Q + 1:]  # [P^2]_(>=Q+1) / z^(Q+1)
    Pdz = Pz[1:]  # P / z
    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = [Fr(0)] * r + x[r:Q + 1]
        hiA[r] = pmul(pr, pr)[Q + r:]  # [P_r^2]_(>=Q+r) / z^(Q+r)
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
    c0 = phi(Fr(0), [Fr(0)] * d)
    J = [[Fr(0)] * d for _ in range(d)]
    for j in range(d):
        e = [Fr(0)] * d
        e[j] = Fr(1)
        col = phi(Fr(0), e)
        for i in range(d):
            J[i][j] = col[i] - c0[i]
    e2 = [Fr(i + 2) for i in range(d)]
    assert phi(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(d)) for i in range(d)]  # affine at z = 0
    assert all(J[i][j] == 0 for i in range(d) for j in range(i, d))  # strictly lower triangular
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


def smallest(a, s):
    q = 1
    while not certificate(a, s, q)[0]:
        q += 1
    ok, ratio, kap = certificate(a, s, q)
    ok1, ratio1, _ = certificate(a, s, q - 1)
    return q, ratio, ok1, ratio1, kap


res = []
for i, (a, s) in enumerate(PAIRS):
    q, ratio, ok1, ratio1, kap = smallest(a, s)
    res.append(not ok1)
    print('pair %d: a=%s, s=%s: smallest passing z0=2^-%d (max ratio %.5f); at 2^-%d: %s (max ratio %.3g); '
          'radius r > 2^%s |eps|^(%s)' % (i + 1, a, s, q, float(ratio), q - 1, ok1, float(ratio1), Fr(q * Q, 2 * H),
                                          Fr(Q, 2 * H)), flush=True)
ac, sc = max(a for a, _ in PAIRS), min(s for _, s in PAIRS)
q, ratio, ok1, ratio1, kap = smallest(ac, sc)
print('common: a=%s, s=%s: z0=2^-%d (max ratio %.5f); radius r > 2^%s |eps|^(%s)' % (ac, sc, q, float(ratio),
                                                                                 Fr(q * Q, 2 * H), Fr(Q, 2 * H)))
print('B =', B, '; kappa =', kap, '; all preceding dyadic z0 fail:', all(res))
print('time %.1fs' % (time.time() - t0))
