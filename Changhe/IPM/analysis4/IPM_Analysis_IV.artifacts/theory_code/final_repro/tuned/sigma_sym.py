"""Exact response coefficient sigma_k at delta=2/3 (c=3) for f_1 = sin(th) + b sin(M th).

n = 3k (k >= 2) is resonant with stream mode q = 2k-2; a unit multipole e = r^{P_n} sin(q th) added to g_n changes
f_{n+1}, f_{n+2}, f_{n+3} by phi_1, phi_2, phi_3 (linear in the unit), and sigma_k is the coefficient of sin((q+1)th)
in phi_3, i.e. of the obstruction mode at the next resonance n+3.
Generic k (symbolic, no folding of modes) and numeric k (absolute modes with folding) are both supported.
"""
import sys
import sympy as sp
b, kk = sp.symbols('b k')
dl = sp.Rational(2, 3)
c = 1 / (1 - dl)
def p(n): return 1 - n * dl
def P(n): return 2 - n * dl
def lam(n): return (n - 1) * (c - 1)

def clean(d):
    out = {}
    for m, v in d.items():
        v = sp.cancel(sp.together(v))
        if v != 0:
            out[m] = v
    return out

def add(d, m, v):
    if m.is_number:
        m = sp.Integer(m)
        if m == 0:
            return
        if m < 0:
            m, v = -m, -v
    else:
        m = sp.expand(m)
        if sp.Poly(m, kk).LC() < 0:  # generic k: the mode is negative for large k, fold it
            m, v = sp.expand(-m), -v
    d[m] = d.get(m, 0) + v

def T(gs, Pi, fs, pj):
    """sine coefficients of -p_j g' f + P_i g f' for sine series g (stream) and f (density)."""
    out = {}
    for l, bb in gs.items():
        for m, a in fs.items():
            add(out, l + m, sp.Rational(1, 2) * (Pi * m - pj * l) * bb * a)
            add(out, m - l, sp.Rational(1, 2) * (-pj * l - Pi * m) * bb * a)
    return out

def pois(fs, n):
    """non-resonant Poisson inverse at order n: density mode M -> stream modes M+1 and M-1."""
    out = {}
    Pn = P(n)
    for M, a in fs.items():
        add(out, M + 1, -a / (2 * (M + 1 + Pn)))
        if not (M.is_number and M == 1):
            add(out, M - 1, a / (2 * (M - 1 - Pn)))
    return out

def lin(*terms):
    out = {}
    for t in terms:
        for m, v in t.items():
            out[m] = out.get(m, 0) + v
    return out

def scale(d, s):
    return {m: v * s for m, v in d.items()}

def low_orders(M):
    F = {1: {sp.Integer(1): sp.Integer(1), sp.Integer(M): b}}
    G = {1: clean(pois(F[1], 1))}
    for n in (2, 3):
        acc = lin(*[T(G[i], P(i), F[n - i], p(n - i)) for i in range(1, n)])
        F[n] = clean(scale(acc, 1 / lam(n)))
        G[n] = clean(pois(F[n], n))
    return F, G

def sigma(k, F, G):
    n = 3 * k
    q = 2 * k - 2
    e = {sp.sympify(q): sp.Integer(1)}
    Pn = P(n)
    phi1 = clean(scale(T(e, Pn, F[1], p(1)), 1 / lam(n + 1)))
    ps1 = clean(pois(phi1, n + 1))
    phi2 = clean(scale(lin(T(e, Pn, F[2], p(2)), T(G[1], P(1), phi1, p(n + 1)), T(ps1, P(n + 1), F[1], p(1))),
                       1 / lam(n + 2)))
    ps2 = clean(pois(phi2, n + 2))
    phi3 = clean(scale(lin(T(e, Pn, F[3], p(3)), T(G[1], P(1), phi2, p(n + 2)), T(ps2, P(n + 2), F[1], p(1)),
                           T(G[2], P(2), phi1, p(n + 1)), T(ps1, P(n + 1), F[2], p(2))), 1 / lam(n + 3)))
    key = sp.expand(sp.sympify(q + 1))
    val = 0
    for m, v in phi3.items():
        if sp.expand(m - key) == 0:
            val += v
    return sp.factor(sp.cancel(val)), phi3

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    F, G = low_orders(M)
    bval = sp.Float(sys.argv[2], 30) if len(sys.argv) > 2 else None
    gen, _ = sigma(kk, F, G)
    print('generic sigma(k) =', gen)
    for k in range(2, 12):
        s, _ = sigma(k, F, G)
        g = sp.factor(gen.subs(kk, k))
        line = 'k=%d sigma=%s' % (k, s)
        if bval is not None:
            line += '  value=%s generic=%s' % (sp.N(s.subs(b, bval), 12), sp.N(g.subs(b, bval), 12))
        print(line)
