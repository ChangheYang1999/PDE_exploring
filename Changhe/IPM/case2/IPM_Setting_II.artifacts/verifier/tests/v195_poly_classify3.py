"""V195: tests/v193_poly_classify2.py with resonances kept: at a zero diagonal entry beta q + p/2 - 1 of D_k (k <= N) the
coefficient of x^p y^q in rho_k is a free unknown r_k_p and the corresponding coefficient of the degree-k condition is
added to the equations; the real solutions are listed separately from the nonreal ones.
Based on V193 pre-work, faster variant of tests/v193_poly_classify.py (same equations): for N + 1 <= k <= M the degree-k
condition reads 2k x (a_k Im z^(k-1) - b_k Re z^(k-1)) + R_k(h_3..h_(k-1)) = 0, so its x^k and x^(k-1) y coefficients
give b_k and a_k as polynomials in the lower unknowns; they are substituted and the remaining coefficients kept. The
Groebner computation then runs on a_3, b_3, ..., a_N, b_N only. Usage: python3 v193_poly_classify2.py l N M [N M ...]"""
import sympy as sp, sys, time, itertools
x, y = sp.symbols('x y', real=True)
def br(f, g):
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
def coeffs(e, k):
    P = sp.Poly(e, x, y)
    return [P.coeff_monomial(x**p * y**(k - p)) for p in range(k + 1)]
def particular(F, j):
    c = sp.symbols('c0:%d' % (j + 1))
    psi = sum(c[p] * x**p * y**(j - p) for p in range(j - 1))
    eqs = coeffs(sp.expand(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - F), j - 2)
    sol = sp.solve(eqs, c[:j - 1], dict=True); assert len(sol) == 1
    return sp.expand(psi.subs(sol[0]).subs({ci: 0 for ci in c}))
def run(l, N, M):
    t0 = time.time()
    beta = 2 * l - sp.Rational(1, 2)
    psi = {2: (l - sp.Rational(1, 2)) * x * y}; rho = {2: x**2}
    ab = []; sub = {}; reseq = []
    for k in range(3, M + 1):
        a, b = sp.symbols('a%d b%d' % (k, k))
        zk = sp.expand((x + sp.I * y)**k)
        F = sp.expand(sp.diff(rho.get(k - 1, 0), x))
        psi[k] = sp.expand(particular(F, k) + a * sp.re(zk) + b * sp.im(zk))
        assert sp.expand(-sp.diff(psi[k], x, 2) - sp.diff(psi[k], y, 2) - F) == 0
        S = br(psi[k], x**2) + sum(br(psi[i], rho[k + 2 - i]) for i in range(3, k) if k + 2 - i in rho)
        S = sp.expand(S)
        if k <= N:
            ab += [a, b]
            rk = 0; resid = 0
            for p, cf in enumerate(coeffs(S, k)):
                dg = beta * (k - p) + sp.Rational(p, 2) - 1
                if dg != 0:
                    rk += -cf / dg * x**p * y**(k - p)
                else:
                    r = sp.Symbol('r%d_%d' % (k, p)); ab.append(r); reseq.append(sp.expand(cf)); rk += r * x**p * y**(k - p); resid += cf * x**p * y**(k - p)
                    print('   resonance at x^%d y^%d (k = %d): free coefficient %s, condition %s' % (p, k - p, k, r, sp.expand(cf)), flush=True)
            rho[k] = sp.expand(rk)
            assert sp.expand((k * l - 1) * rho[k] + br(psi[2], rho[k]) + S - resid) == 0
        else:
            cf = coeffs(S, k)
            # coefficient of x^k is -2k b + ..., of x^(k-1) y is 2k(k-1) a + ...
            assert sp.expand(sp.diff(cf[k], b)) == -2 * k and sp.expand(sp.diff(cf[k - 1], a)) == 2 * k * (k - 1)
            sb = sp.solve(cf[k], b)[0]; sa = sp.solve(cf[k - 1].subs(b, sb), a)[0]
            psi[k] = sp.expand(psi[k].subs({b: sb}).subs({a: sa}))
            sub[a] = sa; sub[b] = sb
    eqs = [e for e in reseq if e != 0]
    for k in range(N + 1, N + M - 1):
        S = sp.expand(sum(br(psi[i], rho[j]) for i in psi for j in rho if i + j == k + 2))
        eqs += [e for e in coeffs(S, k) if e != 0] if S != 0 else []
    t1 = time.time()
    G = sp.groebner(eqs, *ab, order='grevlex', domain='QQ')
    print('l = %s, N = %d, M = %d: %d unknowns after elimination, %d equations (%.1f s); grevlex basis %d elements, '
          'zero-dimensional %s (%.1f s)' % (l, N, M, len(ab), len(eqs), t1 - t0, len(G), G.is_zero_dimensional, time.time() - t1), flush=True)
    if not G.is_zero_dimensional:
        print('   NOT zero-dimensional: basis', G.exprs, flush=True); return
    GL = G.fglm('lex'); sols = sp.solve(list(GL), ab, dict=True)
    LM = [sp.Poly(g, *ab).monoms(order='grevlex')[0] for g in G.exprs]
    pure = [max(m[i] for m in LM if sum(m) == m[i]) for i in range(len(ab))]
    dim = len([e for e in itertools.product(*[range(pp) for pp in pure]) if not any(all(e[i] >= m[i] for i in range(len(ab))) for m in LM)])
    print('   solutions %s; quotient dimension %d' % (sols, dim), flush=True)
    real = [s_ for s_ in sols if all(sp.im(sp.nsimplify(val)) == 0 for val in s_.values())]
    print('   real solutions: %d of %d' % (len(real), len(sols)), flush=True)
    if len(sols) == 1:
        ok = all(G.contains((v - sols[0][v])**dim) for v in ab)
        print('   (v - v*)^%d in the ideal for every unknown: %s -> the only complex solution' % (dim, ok), flush=True)
    for s in sols:
        full = dict(s); full.update({v: sp.expand(e.subs(s)) for v, e in sub.items()})
        r = sp.expand(sum(rho.values()).subs(full)); q = sp.expand(sum(psi.values()).subs(full))
        P1 = sp.expand(-sp.diff(q, x, 2) - sp.diff(q, y, 2) - sp.diff(r, x))
        T1 = sp.expand(l * (x * sp.diff(r, x) + y * sp.diff(r, y)) + br(q, r) - r)
        print('   rho =', r, '  psi =', q, '  PDE residuals zero:', P1 == 0 and T1 == 0, '(%.1f s)' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    l = sp.Rational(sys.argv[1]); a = [int(v) for v in sys.argv[2:]]
    for i in range(0, len(a), 2):
        run(l, a[i], a[i + 1])
