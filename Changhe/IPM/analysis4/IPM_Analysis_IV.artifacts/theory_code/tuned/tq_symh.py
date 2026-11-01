"""Exact first obstruction and response coefficients sigma_k at delta = 2h/Q (gcd(h,Q) = 1, 2h < Q) for a two-mode
profile; h = 1 reproduces tq_sym.py.  Every rational delta = a/b in (0,1) in lowest terms has this form: Q = b, h = a/2
for even a, and Q = 2b, h = a for odd a (Q is the resonance period n_r of the theory, Section 14.2).

delta = 2h/Q, c = Q/(Q-2h), p_n = 1-n delta, P_n = 2-n delta, lambda_n = 2h(n-1)/(Q-2h).  Stream resonances at n = kQ
with stream mode q_k = 2hk-2 (k >= 1 if h >= 2, k >= 2 if h = 1); the obstruction at n = kQ is the density coefficient
at mode q_k - 1 = 2hk-3.  The first obstruction is O_Q (h >= 2) or O_2Q (h = 1).  A unit multipole e = sin(q_k theta) at
stream order n = kQ changes f_(n+r), r = 1..Q, by phi_r (linear), and sigma_k is the coefficient of
sin((q_(k+1) - 1) theta) = sin((2hk+2h-3) theta) in phi_Q.

f_1 = sin(theta) + b sin(M theta).  Coefficients live in QQ(k)[b] (sympy sparse polynomial rings), so the symbolic-k
computation is exact.  Modes: an int (absolute frequency, numeric k) or ('q', j) meaning q_k + j (symbolic k, valid
when every q_k + j that occurs is >= 1 and every density input to a Poisson inverse is >= 3).

usage: python3 tq_symh.py Q h M [kmax]
"""
import sys
from sympy import QQ, Rational, factor_list, Poly, symbols, real_roots, gcd, factor, sympify, nsimplify
from sympy.polys.fields import field
from sympy.polys.rings import ring

Q = int(sys.argv[1]) if len(sys.argv) > 1 else 9
HH = int(sys.argv[2]) if len(sys.argv) > 2 else 2
MM = int(sys.argv[3]) if len(sys.argv) > 3 else 3
KMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 12
from math import gcd as igcd
assert igcd(HH, Q) == 1 and 2 * HH < Q
KFIRST = 1 if HH >= 2 else 2  # first resonance index
NFIRST = KFIRST * Q  # order of the first obstruction

Fk, K = field('k', QQ)
R, B = ring('b', Fk)
one = R.one
dl = Rational(2 * HH, Q)


def p_(n):  # n may be an Fk element (symbolic order)
    return 1 - n * Fk(dl)


def P_(n):
    return 2 - n * Fk(dl)


def lam(n):
    return (n - 1) * Fk(Rational(2 * HH, Q - 2 * HH))


def addm(d, m, v):
    if v == 0:
        return
    if isinstance(m, tuple):
        d[m] = d.get(m, R.zero) + v
        return
    if m == 0:
        return
    if m < 0:
        m, v = -m, -v
    d[m] = d.get(m, R.zero) + v


def clean(d):
    return {m: v for m, v in d.items() if v != 0}


def modeval(m):
    """value of a mode as an Fk element"""
    if isinstance(m, tuple):
        return 2 * HH * K - 2 + m[1]
    return Fk(m)


def mplus(l, m):
    if isinstance(l, tuple) and isinstance(m, tuple):
        raise ValueError
    if isinstance(l, tuple):
        return ('q', l[1] + m)
    if isinstance(m, tuple):
        return ('q', m[1] + l)
    return l + m


def mminus(m, l):
    """m - l, returning (mode, sign) with folding to a positive mode"""
    if isinstance(m, tuple) and not isinstance(l, tuple):
        return ('q', m[1] - l), 1
    if isinstance(l, tuple) and not isinstance(m, tuple):
        return ('q', l[1] - m), -1  # m - (q+j) < 0 for large k: fold
    return m - l, 1


def T(gs, Pi, fs, pj):
    """sine coefficients of P_i g f' - p_j g' f for sine series g (stream) and f (density)."""
    out = {}
    for l, bb in gs.items():
        lv = modeval(l)
        for m, a in fs.items():
            mv = modeval(m)
            addm(out, mplus(l, m), R(Fk(Rational(1, 2)) * (Pi * mv - pj * lv)) * bb * a)
            md, sg = mminus(m, l)
            addm(out, md, R(Fk(Rational(1, 2)) * (-pj * lv - Pi * mv)) * sg * bb * a)
    return clean(out)


def pois(fs, n, drop=None):
    """non-resonant Poisson inverse at order n: density mode M -> stream modes M+1 and M-1."""
    out = {}
    Pn = P_(n)
    for M, a in fs.items():
        Mv = modeval(M)
        up = mplus(M, 1)
        if up != drop:
            addm(out, up, -a * R(1 / (2 * (Mv + 1 + Pn))))
        if isinstance(M, tuple) or M != 1:
            dn = ('q', M[1] - 1) if isinstance(M, tuple) else M - 1
            if dn != drop:
                addm(out, dn, a * R(1 / (2 * (Mv - 1 - Pn))))
    return clean(out)


def lin(*terms):
    out = {}
    for t in terms:
        for m, v in t.items():
            out[m] = out.get(m, R.zero) + v
    return clean(out)


def scale(d, s):
    return clean({m: v * R(s) for m, v in d.items()})


def low_orders(nmax):
    F = {1: {1: one, MM: B}}
    G = {1: pois(F[1], 1)}
    for n in range(2, nmax + 1):
        acc = lin(*[T(G[i], P_(i), F[n - i], p_(n - i)) for i in range(1, n)])
        F[n] = scale(acc, 1 / lam(Fk(n)))
        if n % Q == 0 and n >= NFIRST:
            break  # resonant stream not needed here
        G[n] = pois(F[n], n)
    return F, G


def sigma(kval, F, G):
    """kval: int (absolute modes) or None (symbolic k)"""
    if kval is None:
        n = Q * K
        e = {('q', 0): one}
        key = ('q', 2 * HH - 1)
    else:
        n = Fk(Q * kval)
        e = {2 * HH * kval - 2: one}
        key = 2 * HH * kval + 2 * HH - 3
    Pn = P_(n)
    phi, psi = {}, {}
    for r in range(1, Q + 1):
        terms = [T(e, Pn, F[r], p_(Fk(r)))]
        for s in range(1, r):
            terms.append(T(G[r - s], P_(Fk(r - s)), phi[s], p_(n + s)))
            terms.append(T(psi[s], P_(n + s), F[r - s], p_(Fk(r - s))))
        phi[r] = scale(lin(*terms), 1 / lam(n + r))
        if r < Q:
            psi[r] = pois(phi[r], n + r)
    return phi[Q].get(key, R.zero), phi


def topoly(v):
    """R element -> sympy Poly in b over QQ(k) expression form"""
    return v.as_expr()


if __name__ == '__main__':
    import time
    t0 = time.time()
    F, G = low_orders(NFIRST)
    O = F[NFIRST].get(2 * HH * KFIRST - 3, R.zero)
    bs, ks = symbols('b k')
    Oe = sympify(O.as_expr())
    Op = Poly(Oe, bs)
    print('Q=%d h=%d M=%d  O_%d(b) = %s' % (Q, HH, MM, NFIRST, Op.as_expr()))
    num = Poly(Op.as_expr() * Op.LC() ** -1, bs)
    print('monic O:', num.as_expr())
    print('factor_list:', factor_list(Op.as_expr()))
    rr = real_roots(Poly(nsimplify(Op.as_expr()), bs))
    print('real roots:', [r.evalf(30) for r in rr])
    print('time low orders %.1fs' % (time.time() - t0), flush=True)
    sg, _ = sigma(None, F, G)
    print('generic sigma(k) =', factor(sg.as_expr()), flush=True)
    print('time generic %.1fs' % (time.time() - t0), flush=True)
    for kv in range(KFIRST, KMAX + 1):
        s, _ = sigma(kv, F, G)
        print('k=%d sigma=%s' % (kv, factor(s.as_expr())), flush=True)
