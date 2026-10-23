# Exceptional case P = n + m/2 of the polynomial axis problem, Case II (see NOTES.md).
# For each odd m, each e >= 2 with 2e+3 <= m, each odd A0 >= 1 and each multiset mu_1..mu_{e+1} >= 1
# (not all equal; the equal case is excluded analytically) with A0 + 2 sum(mu) = m, the necessary conditions
#   A0 + sum_k 2 mu_k v_k^l = 0 (l = 1..e),
#   (A0 + sum_k 2 mu_k v_k^{e+1}) vs = (-1)^e m prod_k v_k,
#   pi'(vs) = 0, pi(v) = prod_k (v - v_k),
# are eliminated (lex Groebner basis) to a univariate polynomial in vs; a solution needs a real root
# vs = (2n+m)/(2n+m-1) for an integer n >= 1, in particular a real root in (1, (m+2)/(m+1)].
import sys, signal, itertools, time
import sympy as sp

def multisets(total, parts):
    def rec(t, p, mx):
        if p == 0:
            if t == 0: yield ()
            return
        for a in range(min(mx, t - (p - 1)), 0, -1):
            for rest in rec(t - a, p - 1, a): yield (a,) + rest
    yield from rec(total, parts, total)

class TO(Exception): pass
def handler(s, f): raise TO()
signal.signal(signal.SIGALRM, handler)

def case(m, e, A0, mu, tlim):
    vs = sp.Symbol('vs'); v = sp.Symbol('v')
    V = sp.symbols('v1:%d' % (e + 2))
    A = [2 * x for x in mu]
    eqs = [A0 + sum(a * x**l for a, x in zip(A, V)) for l in range(1, e + 1)]
    eqs.append(sp.expand((A0 + sum(a * x**(e + 1) for a, x in zip(A, V))) * vs - (-1)**e * m * sp.prod(V)))
    pi = sp.prod([v - x for x in V])
    eqs.append(sp.expand(sp.diff(pi, v).subs(v, vs)))
    signal.alarm(tlim)
    try:
        G = sp.groebner(eqs, *V, vs, order='lex')
    finally:
        signal.alarm(0)
    last = [g for g in G.exprs if g.free_symbols <= {vs}]
    if not last: return 'no univariate eliminant', None
    p = sp.Poly(last[-1], vs)
    if p.degree() <= 0: return 'inconsistent (basis [1])', []
    real = [r for r in sp.real_roots(p)]
    inint = [r for r in real if 1 < r <= sp.Rational(m + 2, m + 1)]
    hits = []
    for n in range(1, 200):
        val = sp.Rational(2 * n + m, 2 * n + m - 1)
        if p.eval(val) == 0: hits.append(n)
    return 'deg %d, real roots %s, in (1,(m+2)/(m+1)]: %s, admissible n: %s' % (
        p.degree(), [float(r) for r in real], [float(r) for r in inint], hits), hits

if __name__ == '__main__':
    ms = [int(x) for x in sys.argv[1].split(',')]
    tlim = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    for m in ms:
        for e in range(2, (m - 3) // 2 + 1):
            for A0 in range(1, m + 1, 2):
                tot = (m - A0) // 2
                if tot < e + 1: continue
                for mu in multisets(tot, e + 1):
                    if len(set(mu)) == 1:
                        print(m, e, A0, mu, 'equal multiplicities: excluded analytically', flush=True); continue
                    t0 = time.time()
                    try:
                        res, hits = case(m, e, A0, mu, tlim)
                    except TO:
                        res = 'TIMEOUT %d s' % tlim
                    print(m, e, A0, mu, res, '(%.1f s)' % (time.time() - t0), flush=True)
