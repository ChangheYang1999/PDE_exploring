"""Three-mode version of tq_sym.py: f_1 = sin(theta) + b sin(3 theta) + tau sin(5 theta) (B = 6), coefficients in QQ(k)[b,tau].
usage: python3 tq_sym3.py Q [kmax]

Original description: exact first obstruction O_(2Q) and response coefficients sigma_k at delta=2/Q, for a two-mode profile.

delta = 2/Q, c = Q/(Q-2), p_n = 1-2n/Q, P_n = 2-2n/Q, lambda_n = 2(n-1)/(Q-2).  Stream resonances at n = kQ (k>=2),
stream mode q_k = 2k-2; the obstruction at n = kQ is the density coefficient at mode 2k-3.  A unit multipole
e = sin(q_k theta) at stream order n = kQ changes f_(n+r), r = 1..Q, by phi_r (linear), and sigma_k is the coefficient
of sin((2k-1) theta) in phi_Q.

f_1 = sin(theta) + b sin(M theta).  Coefficients live in QQ(k)[b] (sympy sparse polynomial rings), so the symbolic-k
computation is exact.  Modes: an int (absolute frequency, numeric k) or ('q', j) meaning q_k + j (symbolic k, valid
when every q_k + j that occurs is >= 1 and every density input to a Poisson inverse is >= 3).

usage: python3 tq_sym.py Q M [kmax]
"""
import sys
from sympy import QQ, Rational, factor_list, Poly, symbols, real_roots, gcd, factor, sympify, nsimplify
from sympy.polys.fields import field
from sympy.polys.rings import ring

Q = int(sys.argv[1]) if len(sys.argv) > 1 else 5
MM = 3
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 12

Fk, K = field('k', QQ)
R, B, TAU = ring('b,tau', Fk)
one = R.one
dl = Rational(2, Q)


def p_(n):  # n may be an Fk element (symbolic order)
    return 1 - n * Fk(dl)


def P_(n):
    return 2 - n * Fk(dl)


def lam(n):
    return (n - 1) * Fk(Rational(2, Q - 2))


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
        return 2 * K - 2 + m[1]
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
    F = {1: {1: one, 3: B, 5: TAU}}
    G = {1: pois(F[1], 1)}
    for n in range(2, nmax + 1):
        acc = lin(*[T(G[i], P_(i), F[n - i], p_(n - i)) for i in range(1, n)])
        F[n] = scale(acc, 1 / lam(Fk(n)))
        if n % Q == 0 and n >= 2 * Q:
            break  # resonant stream not needed here
        G[n] = pois(F[n], n)
    return F, G


def sigma(kval, F, G):
    """kval: int (absolute modes) or None (symbolic k)"""
    if kval is None:
        n = Q * K
        e = {('q', 0): one}
        key = ('q', 1)
    else:
        n = Fk(Q * kval)
        e = {2 * kval - 2: one}
        key = 2 * kval - 1
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
    from sympy import resultant, Poly, together, fraction, LC
    t0 = time.time()
    F, G = low_orders(2 * Q)
    O = F[2 * Q].get(1, R.zero)
    bs, ts, ks = symbols('b tau k')
    Oe = sympify(O.as_expr())
    print('Q=%d three-mode  O_%d(b,tau) = %s' % (Q, 2 * Q, Oe), flush=True)
    sg, _ = sigma(None, F, G)
    ge = sympify(sg.as_expr())
    pb = Poly(ge, bs, ts)
    lim = 0
    for mon, cf in pb.terms():
        nu, de = fraction(together(cf))
        nu, de = Poly(nu, ks), Poly(de, ks)
        assert nu.degree() <= de.degree()
        if nu.degree() == de.degree():
            lim += (nu.LC() / de.LC()) * bs ** mon[0] * ts ** mon[1]
    print('sigma_inf(b,tau) =', factor(lim), flush=True)
    print('time generic %.1fs' % (time.time() - t0), flush=True)
    for kv in range(10, KMAX + 1):
        s, _ = sigma(kv, F, G)
        d = sympify(s.as_expr()) - ge.subs(ks, kv)
        print('k=%d direct minus generic = %s' % (kv, together(d)), flush=True)
    for kv in range(2, 10):
        s, _ = sigma(kv, F, G)
        print('k=%d sigma=%s' % (kv, sympify(s.as_expr()).expand()), flush=True)
    res = resultant(Poly(Oe, bs), Poly(lim, bs))
    rp = Poly(res, ts)
    print('resultant degree in tau:', rp.degree())
    from sympy import real_roots
    rr = real_roots(Poly(rp.as_expr() * rp.LC() ** -1, ts).clear_denoms()[1])
    print('real roots of resultant:', [r.evalf(20) for r in rr])
    print('time %.1fs' % (time.time() - t0))
