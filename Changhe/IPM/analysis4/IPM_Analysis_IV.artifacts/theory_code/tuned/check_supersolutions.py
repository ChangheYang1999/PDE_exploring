"""Independent check of supplied rational supersolutions Phi(z0, Y) <= Y for the generating system of theory
Section 12.5 Step 4 (Theorem T_Q), with Phi built here from the displayed formulas (same construction as
tq_bounds_radius.py). Input: a JSON file with rows {a, response_lower, z0, box, display_radius}; the root intervals and
response bounds are re-derived independently (tq_cert.py / tq_minima.py). Checks, exactly in rationals:
 (1) a >= 1 + |b_i| on the isolating interval of the i-th real root (increasing order);
 (2) response_lower equals the certified bound of tq_minima.py for that root;
 (3) every component of Phi(z0, Y) is strictly below Y;
 (4) R^2 z0^Q > 1 for the displayed radius R (so R > z0^(-Q/2)).
usage: python3 check_supersolutions.py Q checks.json bounds(comma separated fractions) [B]
"""
import sys, json, time, math
from fractions import Fraction as Fr
from math import comb
Q = int(sys.argv[1])
rows = json.load(open(sys.argv[2]))['rows']
S_cert = [Fr(x) for x in sys.argv[3].split(',')]
B = int(sys.argv[4]) if len(sys.argv) > 4 else 4
t0 = time.time()
sys.argv = [sys.argv[0], str(Q), '3', str(2 * Q + 6)]
import tq_sym as T
from sympy import Poly, symbols, sympify, Rational
b = symbols('b')
F, G = T.low_orders(2 * Q)
O = sympify(F[2 * Q].get(1, T.R.zero).as_expr())
P = Poly(Poly(O, b).primitive()[1], b)
iv = P.intervals(eps=Rational(1, 10 ** 30))
roots = [(Fr(int(Rational(lo).p), int(Rational(lo).q)), Fr(int(Rational(hi).p), int(Rational(hi).q))) for (lo, hi), m in iv]


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


ok_all = len(rows) == len(roots) == len(S_cert)
print('Q = %d, B = %d, %d rows, %d real roots' % (Q, B, len(rows), len(roots)))
for i, row in enumerate(rows):
    a, s, z0 = Fr(row['a']), Fr(row['response_lower']), Fr(row['z0'])
    Y = [Fr(x) for x in row['box']]
    R = Fr(row['display_radius'])
    lo, hi = roots[i]
    c1 = 1 + max(abs(lo), abs(hi)) <= a
    c2 = s == S_cert[i]
    phi, kap = make_phi(a, s)
    PY = phi(z0, Y)
    c3 = all(p < y for p, y in zip(PY, Y)) and all(y > 0 for y in Y)
    c4 = R * R * z0 ** Q > 1
    ratio = max(p / y for p, y in zip(PY, Y))
    ok_all &= c1 and c2 and c3 and c4
    print('root %d: a=%s (>= 1+|b|: %s), s=%s (= certified bound: %s), Phi(z0,Y) < Y: %s (max ratio %.6f), '
          'R = %.4e, R^2 z0^%d > 1: %s, log2 R = %.3f' % (i + 1, a, c1, s, c2, c3, float(ratio), float(R), Q, c4,
                                                           math.log2(float(R))))
print('kappa =', kap)
print('ALL PASS' if ok_all else 'FAIL')
print('time %.1fs' % (time.time() - t0))
sys.exit(0 if ok_all else 1)
