"""V193 pre-work (written independently of the check script for referee result 40): polynomial solutions of
    -Lap psi = rho_x,   l X.grad rho + {psi, rho} = rho,   rho = x^2 + O(|X|^3),   psi = O(|X|^2),
with deg rho <= N and deg psi <= M, at fixed rational l. Degree 2 forces psi_2 = (l - 1/2) x y. For k >= 3 the degree-k
part of the transport equation is D_k rho_k + {psi_k, x^2} + sum_{i=3}^{k-1} {psi_i, rho_{k+2-i}} = 0, where D_k is
diagonal on x^p y^q with entries beta q + p/2 - 1 (checked below), and psi_k = particular(rho_{k-1}) + a_k Re z^k
+ b_k Im z^k. Unknowns: a_k, b_k (3 <= k <= M). Conditions: rho_k = 0 for N < k (i.e. the bracket sum vanishes) up to
degree N + M - 2. Groebner basis over QQ. Usage: python3 v193_poly_classify.py l N M [N M ...]"""
import sympy as sp, sys, time
x, y = sp.symbols('x y', real=True)
def br(f, g):
    return sp.expand(sp.diff(f, x) * sp.diff(g, y) - sp.diff(f, y) * sp.diff(g, x))
def coeffs(e, k):
    P = sp.Poly(e, x, y)
    return [P.coeff_monomial(x**p * y**(k - p)) for p in range(k + 1)]
def particular(F, j):
    # -Lap psi = F (homogeneous of degree j - 2); psi with zero coefficients of x^j and x^(j-1) y
    c = sp.symbols('c0:%d' % (j + 1))
    psi = sum(c[p] * x**p * y**(j - p) for p in range(j - 1))
    eqs = coeffs(sp.expand(-sp.diff(psi, x, 2) - sp.diff(psi, y, 2) - F), j - 2) if j >= 2 else []
    sol = sp.solve(eqs, c[:j - 1], dict=True)
    assert len(sol) == 1
    return sp.expand(psi.subs(sol[0]).subs({ci: 0 for ci in c}))
def run(l, N, M):
    t0 = time.time()
    beta = 2 * l - sp.Rational(1, 2)
    c2 = l - sp.Rational(1, 2)
    psi = {2: c2 * x * y}; rho = {2: x**2}
    # check degree 2 and the diagonal of D_k
    assert sp.expand((2 * l - 1) * x**2 + br(psi[2], x**2)) == 0
    for k in range(3, 9):
        for p in range(k + 1):
            m = x**p * y**(k - p)
            assert sp.expand((k * l - 1) * m + br(psi[2], m) - (beta * (k - p) + sp.Rational(p, 2) - 1) * m) == 0
    ab = []
    for k in range(3, M + 1):
        a, b = sp.symbols('a%d b%d' % (k, k)); ab += [a, b]
        zk = sp.expand((x + sp.I * y)**k)
        F = sp.diff(rho.get(k - 1, 0), x)
        psi[k] = particular(sp.expand(F), k) + a * sp.re(zk) + b * sp.im(zk)
        psi[k] = sp.expand(psi[k])
        assert sp.expand(-sp.diff(psi[k], x, 2) - sp.diff(psi[k], y, 2) - F) == 0
        if k <= N:
            S = br(psi[k], x**2) + sum(br(psi[i], rho[k + 2 - i]) for i in range(3, k))
            rk = 0
            for p, cf in enumerate(coeffs(S, k)):
                rk += -cf / (beta * (k - p) + sp.Rational(p, 2) - 1) * x**p * y**(k - p)
            rho[k] = sp.expand(rk)
            assert sp.expand((k * l - 1) * rho[k] + br(psi[2], rho[k]) + S) == 0
    eqs = []
    for k in range(3, N + M - 1):
        S = sum(br(psi[i], rho[j]) for i in psi for j in rho if i + j == k + 2 and not (i == 2 and j == k)) \
            + (k * l - 1) * rho.get(k, 0) + br(psi[2], rho.get(k, 0))
        S = sp.expand(S)
        if S != 0:
            eqs += [e for e in coeffs(S, k) if e != 0]
    G = sp.groebner(eqs, *ab, order='grevlex', domain='QQ') if eqs else None
    print('   grevlex basis: %d elements, zero-dimensional %s (%.1f s)' % (len(G), G.is_zero_dimensional, time.time() - t0), flush=True)
    Gg = G
    G = G.fglm('lex') if G.is_zero_dimensional else sp.groebner(eqs, *ab, order='lex', domain='QQ')
    sols = sp.solve(list(G), ab, dict=True) if G is not None else 'free'
    print('l = %s, N = %d, M = %d: %d unknowns, %d equations; Groebner basis %s; solutions %s (%.1f s)' %
          (l, N, M, len(ab), len(eqs), list(G) if G is not None and len(G) < 12 else ('len %d' % len(G) if G is not None else None),
           sols, time.time() - t0), flush=True)
    if Gg.is_zero_dimensional and isinstance(sols, list) and len(sols) == 1:
        # quotient dimension from the grevlex leading monomials; then (v - v*)^dim in I for every unknown proves that the
        # complex variety is the single point
        LM = [sp.Poly(g, *ab).monoms(order='grevlex')[0] for g in Gg.exprs]
        pure = [max(m[i] for m in LM if sum(m) == m[i]) for i in range(len(ab))]
        import itertools
        std = [e for e in itertools.product(*[range(pp) for pp in pure]) if not any(all(e[i] >= m[i] for i in range(len(ab))) for m in LM)]
        dim = len(std)
        ok = all(Gg.contains((v - sols[0][v])**dim) for v in ab)
        print('   quotient dimension %d; (v - v*)^%d in the ideal for every unknown: %s -> the only complex solution' % (dim, dim, ok), flush=True)
    for s in (sols if isinstance(sols, list) else []):
        r = sp.expand(sum(rho.values()).subs(s)); q = sp.expand(sum(psi.values()).subs(s))
        P1 = sp.expand(-sp.diff(q, x, 2) - sp.diff(q, y, 2) - sp.diff(r, x))
        T1 = sp.expand(l * (x * sp.diff(r, x) + y * sp.diff(r, y)) + br(q, r) - r)
        print('   rho =', r, '  psi =', q, '  PDE residuals zero:', P1 == 0 and T1 == 0, flush=True)
if __name__ == '__main__':
    l = sp.Rational(sys.argv[1]); a = [int(v) for v in sys.argv[2:]]
    for i in range(0, len(a), 2):
        run(l, a[i], a[i + 1])
