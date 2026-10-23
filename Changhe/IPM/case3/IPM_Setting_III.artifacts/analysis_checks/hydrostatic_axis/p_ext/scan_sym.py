# Symmetric reduction of the Case II system of NOTES.md (same necessary conditions as scan_exc.py).
# The nonzero poles v_1..v_{e+1} are grouped by weight A = 2 mu; a group of size n_g is described by its
# elementary symmetric functions sigma_1..sigma_{n_g} (real when the configuration is conjugation invariant,
# since conjugate poles have equal weights). Power sums come from Newton's identities. The moment equation of
# order l is linear in sigma_l of the largest group (coefficient (-1)^{l-1} l a), so sigma_1..sigma_{n*} of that
# group are eliminated triangularly. The remaining variables are eliminated by a lex Groebner basis (vs last);
# when no variable other than vs remains after one more linear solve, a resultant is used instead.
# A solution needs a real root vs = (2n+m)/(2n+m-1), n >= 1, in particular a real root in (1, (m+2)/(m+1)].
import sys, signal, time
from collections import Counter
import sympy as sp

def multisets(total, parts):
    def rec(t, p, mx):
        if p == 0:
            if t == 0: yield ()
            return
        for a in range(min(mx, t - (p - 1)), 0, -1):
            for rest in rec(t - a, p - 1, a): yield (a,) + rest
    yield from rec(total, parts, total)

def power_sums(sig, L):
    # sig = [s1..sn]; returns p_1..p_L via Newton: p_l = sum_{i=1}^{l-1} (-1)^{i-1} s_i p_{l-i} + (-1)^{l-1} l s_l
    n = len(sig); p = [None]
    for l in range(1, L + 1):
        val = sum((-1)**(i - 1) * sig[i - 1] * p[l - i] for i in range(1, min(l - 1, n) + 1))
        if l <= n: val += (-1)**(l - 1) * l * sig[l - 1]
        p.append(sp.expand(val))
    return p

class TO(Exception): pass
def handler(s, f): raise TO()
signal.signal(signal.SIGALRM, handler)

def case(m, e, A0, mu, tlim):
    vs = sp.Symbol('vs'); v = sp.Symbol('v')
    groups = sorted(Counter(mu).items(), key=lambda kv: -kv[1])   # (mu value, size), largest group first
    sig = []; allvars = []
    for gi, (mv, ng) in enumerate(groups):
        ss = list(sp.symbols('s%d_1:%d' % (gi, ng + 1))); sig.append(ss); allvars += ss
    P = [power_sums(ss, e + 1) for ss in sig]
    a = [2 * mv for mv, ng in groups]
    M = [None] + [sp.expand(A0 + sum(a[g] * P[g][l] for g in range(len(groups)))) for l in range(1, e + 2)]
    # triangular elimination of sigma_1..sigma_{n*} of group 0
    sub = {}
    n0 = groups[0][1]
    for l in range(1, n0 + 1):
        eq = sp.expand(M[l].subs(sub))
        x = sig[0][l - 1]
        sol = sp.solve(eq, x)
        assert len(sol) == 1
        sub[x] = sp.expand(sol[0])
        for k in list(sub): sub[k] = sp.expand(sub[k].subs(x, sub[x]))
    rest = [x for x in allvars if x not in sub]
    eqs = [sp.expand(M[l].subs(sub)) for l in range(n0 + 1, e + 1)]
    prodv = sp.prod([(-1)**0 * ss[-1] for ss in sig])            # prod of all v_k = prod of sigma_{n_g}
    eqs.append(sp.expand((M[e + 1] * vs - (-1)**e * m * prodv).subs(sub)))
    pi = sp.prod([sum((-1)**i * (ss[i - 1] if i else 1) * v**(len(ss) - i) for i in range(len(ss) + 1)) for ss in sig])
    eqs.append(sp.expand(sp.diff(pi, v).subs(v, vs).subs(sub)))
    eqs = [q for q in eqs if q != 0]
    signal.alarm(tlim)
    try:
        if len(rest) == 0:
            uni = [sp.Poly(q, vs) for q in eqs]
            p = uni[0]
            for q in uni[1:]: p = sp.gcd(p, q)
            how = 'direct'
        elif len(rest) == 1 and len(eqs) == 2:
            p = sp.Poly(sp.resultant(eqs[0], eqs[1], rest[0]), vs)
            how = 'resultant'
        else:
            G = sp.groebner(eqs, *rest, vs, order='lex')
            last = [g for g in G.exprs if g.free_symbols <= {vs}]
            if not last: return 'no univariate eliminant', None
            p = sp.Poly(last[-1], vs); how = 'groebner'
    finally:
        signal.alarm(0)
    if p.is_zero:
        return '%s: ZERO ELIMINANT (common factor; not excluded)' % how, None
    if p.degree() <= 0:
        return '%s: inconsistent (eliminant constant)' % how, []
    sqf = sp.Poly(sp.sqf_part(p.as_expr()), vs)
    global LASTPOLY; LASTPOLY = sqf
    real = sp.real_roots(sqf)
    inint = [r for r in real if 1 < r <= sp.Rational(m + 2, m + 1)]
    lin = [f for f, k in sp.factor_list(sqf.as_expr())[1] if sp.Poly(f, vs).degree() == 1]
    rat = [sp.solve(f, vs)[0] for f in lin]
    adm = [r for r in rat if r > 1 and ((1 / (r - 1) + 1 - m) % 2 == 0) and (1 / (r - 1) + 1 - m) >= 2] if rat else []
    return '%s: deg %d (sqf %d), real roots %s, in (1,(m+2)/(m+1)]: %s, rational roots %s, admissible %s' % (
        how, p.degree(), sqf.degree(), ['%.6g' % float(r) for r in real], ['%.6g' % float(r) for r in inint],
        rat, adm), adm

if __name__ == '__main__':
    ms = [int(x) for x in sys.argv[1].split(',')]
    tlim = int(sys.argv[2]) if len(sys.argv) > 2 else 600
    emin = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    for m in ms:
        for e in range(emin, (m - 3) // 2 + 1):
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
