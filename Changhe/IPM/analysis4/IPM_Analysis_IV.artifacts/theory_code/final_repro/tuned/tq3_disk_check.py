"""Independent check of the larger compatible shape disks at c = 3 (three-mode profiles
f_1 = sin(theta) + b sin(3 theta) + tau sin(5 theta), B = 6), using the Fourier code tq_sym3.py for O_6(b,tau) and the
responses sigma_k(b,tau), and the Step 4 majorant system of theory Section 12.5 at Q = 3, B = 6 (kappa = 14, L = 3/2).

For each real root of P6 (= O_6(b,0) up to a constant) with own isolating interval [l,u], m = (l+u)/2, and the
parameters (t0, h, s, a, q) under test:
 (1) circle:   sum_{(i,j) != (1,0)} |c_ij| h^i t0^j < |A| h,  O(m+x,tau) = sum c_ij x^i tau^j, A = c_10;  (u-l)/2 < h.
 (2) k=2..9:   |d_00| - sum_{(i,j) != (0,0)} |d_ij| h^i t0^j > s for sigma_k(m+x,tau) = sum d_ij x^i tau^j.
 (3) k>=10:    sigma_k = N(k,b,tau)/D(k); with k = 10+w: D(10+w) has coefficients >= 0 and D_0 > 0 (after a common sign),
               and for every ell: e*n_(ell,0,0) - sum_{(i,j) != (0,0)} |n_(ell,i,j)| h^i t0^j - s D_ell >= 0 (> 0 for
               ell = 0), with e = sign of the limit at the center.
 (4) radius:   a >= 1 + |m| + h + t0, and G(z0, 2 Y0) <= 2 Y0 for the Step 4 system with (a, s), z0 = 2^-q;
               then R > z0^(-3/2) = 2^(3q/2).
"""
import sys, time
from fractions import Fraction as Fr
from math import comb
sys.argv = [sys.argv[0], '3', '14']
import tq_sym3 as T
from sympy import Poly, symbols, sympify, together, fraction, Rational

t0_ = time.time()
b, tau, k, x, w = symbols('b tau k x w')
out = []


def log(*a):
    s = ' '.join(str(v) for v in a)
    print(s, flush=True)
    out.append(s)


def fr(v):
    v = Rational(v)
    return Fr(int(v.p), int(v.q))


F, G = T.low_orders(6)
O = sympify(F[6].get(1, T.R.zero).as_expr())
P6 = Poly(O.subs(tau, 0), b)
ivs = Poly(P6.primitive()[1], b).intervals(eps=Rational(1, 10 ** 30))
log('real roots of O_6(b,0):', len(ivs))
sm = {}
for kv in range(2, 10):
    s_, _ = T.sigma(kv, F, G)
    sm[kv] = sympify(s_.as_expr())
sg, _ = T.sigma(None, F, G)
num, den = fraction(together(sympify(sg.as_expr())))
Dw = Poly(Poly(den, k).as_expr().subs(k, 10 + w), w)
sgnD = 1 if Dw.LC() > 0 else -1
Dl = [fr(c) * sgnD for c in Dw.all_coeffs()[::-1]]
assert all(c >= 0 for c in Dl) and Dl[0] > 0
Nw = Poly(sgnD * num.subs(k, 10 + w), w, b, tau)
log('D(10+w): %d coefficients, all >= 0 after sign normalization, D_0 > 0' % len(Dl))


def coeffs2(expr):
    """exact coefficients c_ij of a polynomial in (x, tau)"""
    p = Poly(expr, x, tau)
    return {mon: fr(c) for mon, c in p.terms()}


def check(ir, t0, h, s):
    (l, u), mult = ivs[ir]
    l, u = fr(l), fr(u)
    m = (l + u) / 2
    ms = Rational(m.numerator, m.denominator)
    ok = (u - l) / 2 < h
    # (1)
    c = coeffs2(O.subs(b, ms + x).expand())
    A = c.get((1, 0), Fr(0))
    rest = sum(abs(v) * h ** i * t0 ** j for (i, j), v in c.items() if (i, j) != (1, 0))
    circ = rest / (abs(A) * h)
    ok1 = rest < abs(A) * h
    # (2)
    marg2 = []
    for kv in range(2, 10):
        d = coeffs2(sm[kv].subs(b, ms + x).expand())
        d00 = d.get((0, 0), Fr(0))
        mg = abs(d00) - sum(abs(v) * h ** i * t0 ** j for (i, j), v in d.items() if (i, j) != (0, 0))
        marg2.append(mg - s)
    ok2 = all(v > 0 for v in marg2)
    # (3) tail
    byell = {}
    for (el, i, j), cf in Nw.terms():
        byell.setdefault(el, {})[(i, j)] = byell.setdefault(el, {}).get((i, j), 0) + cf
    # sign of the limit at the center: leading w coefficient (when deg N = deg D)
    ok3 = True
    minm = None
    e = None
    for el in range(max(len(Dl), max(byell) + 1)):
        pe = sum(cf * b ** i * tau ** j for (i, j), cf in byell.get(el, {}).items())
        cxy = coeffs2(sympify(pe).subs(b, ms + x).expand()) if pe != 0 else {}
        n00 = cxy.get((0, 0), Fr(0))
        if e is None and el == len(Dl) - 1:
            pass
        restn = sum(abs(v) * h ** i * t0 ** j for (i, j), v in cxy.items() if (i, j) != (0, 0))
        byell[el] = (n00, restn)
    lead = byell[len(Dl) - 1][0]
    e = 1 if lead > 0 else -1
    for el in range(len(Dl)):
        n00, restn = byell.get(el, (Fr(0), Fr(0)))
        mg = e * n00 - restn - s * Dl[el]
        ok3 &= (mg > 0) if el == 0 else (mg >= 0)
        minm = mg if minm is None or mg < minm else minm
    assert max(byell) <= len(Dl) - 1
    return dict(m=m, ok=ok, ok1=ok1, circ=float(circ), ok2=ok2, min2=float(min(marg2)), ok3=ok3, e=e)


# Step 4 system at Q = 3, B = 6 (as in tq_bounds_radius.py, with B as a parameter)
Q, B = 3, 6


def pmul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, xx in enumerate(p):
        if xx:
            for j, yy in enumerate(q):
                r[i + j] += xx * yy
    return r


def peval(p, z):
    v = Fr(0)
    for cc in reversed(p):
        v = v * z + cc
    return v


def make_phi(a, s):
    kap = Fr(Q - 2) * (3 - Fr(2, Q)) * B
    L = Fr(Q, 2)
    cat = [comb(2 * mm, mm) // (mm + 1) for mm in range(Q)]
    xx = [Fr(0)] + [cat[j - 1] * (kap * L) ** (j - 1) * a ** j for j in range(1, Q + 1)]
    Pz = [Fr(0)] + xx[1:]
    hiP2 = pmul(Pz, Pz)[Q + 1:]
    hiA, lowA = {}, {}
    for r in range(1, Q + 1):
        pr = [Fr(0)] * r + xx[r:Q + 1]
        hiA[r] = pmul(pr, pr)[Q + r + 1:]
        lowA[r] = pr[r:]

    def phi(z, Y):
        W, V, E = Y[0], Y[1:Q], Y[Q]
        Pv = peval(Pz, z)
        o = [kap * L * peval(hiP2, z) + 2 * kap * L * Pv * W + kap * L * z ** (Q + 1) * W * W
             + kap * E * (Pv + z ** (Q + 1) * W)]

        def Ar(r):
            return peval(hiA[r], z) + 2 * peval(lowA[r], z) * W + z ** (Q + 1 - r) * W * W
        for r in range(1, Q):
            o.append(kap * (L * Ar(r) + z ** (Q + 1 - r) * E * W + Q * sum(xx[sq] * V[r - sq - 1] for sq in range(1, r))))
        o.append(kap / s * (L * Ar(Q) + z * E * W + Q * sum(xx[sq] * V[Q - sq - 1] for sq in range(1, Q))))
        return o
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
    e2 = [Fr(i + 2) for i in range(d)]
    assert phi(Fr(0), e2) == [c0[i] + sum(J[i][j] * e2[j] for j in range(d)) for i in range(d)]
    assert all(J[i][j] == 0 for i in range(d) for j in range(i, d))
    Tm = [[Fr(int(i == j)) for j in range(d)] for i in range(d)]
    Pw = [row[:] for row in Tm]
    for _ in range(Q):
        Pw = [[sum(Pw[i][l] * J[l][j] for l in range(d)) for j in range(d)] for i in range(d)]
        Tm = [[Tm[i][j] + Pw[i][j] for j in range(d)] for i in range(d)]
    Y0 = matvec(Tm, c0)
    bx = [2 * y for y in Y0]
    z0 = Fr(1, 2 ** q)
    rest = [u_ - c_ - w_ for u_, c_, w_ in zip(phi(z0, bx), c0, matvec(J, bx))]
    Gv = [y + w_ for y, w_ in zip(Y0, matvec(Tm, rest))]
    ratio = max(g / bb for g, bb in zip(Gv, bx))
    return ratio <= 1, ratio, kap


# Q = 3, B = 4 specialization sanity: kappa must be 28/3 (Section 12.4)
B = 4
assert make_phi(Fr(2), Fr(1, 100000))[1] == Fr(28, 3)
B = 6
cases = [(0, Fr(1, 512), Fr(1, 256), Fr(1, 100000), Fr(1287, 1000), 42),
         (1, Fr(1, 128), Fr(1, 64), Fr(1, 2000), Fr(167, 100), 38)]
allok = True
for ir, t0, h, s, a, q in cases:
    r = check(ir, t0, h, s)
    okA = a >= 1 + abs(r['m']) + h + t0
    okB, ratio, kap = certificate(a, s, q)
    okB1, ratio1, _ = certificate(a, s, q - 1)
    log('root %d: m = %.15f, t0 = %s, h = %s, s = %s: width < h %s; circle ratio %.10f (%s); k=2..9 min margin over s '
        '%.3e (%s); tail k>=10 (sign %+d): %s' % (ir + 1, float(r['m']), t0, h, s, r['ok'], r['circ'], r['ok1'], r['min2'],
                                                 r['ok2'], r['e'], r['ok3']))
    log('   a = %s >= 1+|m|+h+t0: %s; kappa = %s; z0 = 2^-%d: %s (max ratio %.5f); z0 = 2^-%d: %s (%.3g); R > 2^%s'
        % (a, okA, kap, q, okB, float(ratio), q - 1, okB1, float(ratio1), Fr(3 * q, 2)))
    allok &= r['ok'] and r['ok1'] and r['ok2'] and r['ok3'] and okA and okB
log('ALL PASS' if allok else 'FAIL')
log('time %.1fs' % (time.time() - t0_))
open('tq3_disk_check.out', 'w').write('\n'.join(out) + '\n')
