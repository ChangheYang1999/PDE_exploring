"""Check of the formal local-jet construction (generating function G, Theta = a0 eta).
Builds Psi = beta x G_x + b eta G_eta - 2 beta G in the variables (x, eta), the physical derivatives
Dx = d_x - (B/A) d_eta, Dy = A^-1 d_eta (A = G_x eta, B = G_xx), and the residuals of both transport equations,
truncated by total degree via a scaling parameter t.  Checks: (i) temperature residual vanishes identically;
(ii) the degree N-2 vorticity residual is affine in H_N with linear part T_N H = -(L+1) Lap (L - 2 beta) H + a0 H_xx;
(iii) the selected square block is triangular with nonzero diagonal (solvability with x^(N-1) eta coefficient free)."""
import sympy as sp, random
x, e, t = sp.symbols('x eta t')
beta = sp.Rational(random.randint(21, 60), 10); a0 = sp.Rational(random.randint(-90, 90), 7) or sp.Integer(5)
al, b = beta + 2, beta - 2
print('beta', beta, 'a0', a0)
def trunc(expr, deg):
    s = sp.expand(expr.subs({x: t * x, e: t * e}))
    s = sp.series(s, t, 0, deg + 1).removeO()
    return sp.expand(s.subs(t, 1))
def run(N, lower):
    hs = sp.symbols('h0:%d' % (N // 2))
    HN = sum(hs[k] * x ** (2 * k + 1) * e ** (N - 2 * k - 1) for k in range(N // 2))
    G = x * e + lower + HN
    A = sp.diff(G, x, e); B = sp.diff(G, x, 2)
    D = N + 2
    Ainv = trunc(sum((1 - A) ** k for k in range(D)), D)
    Dx = lambda f: trunc(sp.diff(f, x) - B * Ainv * sp.diff(f, e), D)
    Dy = lambda f: trunc(Ainv * sp.diff(f, e), D)
    Psi = sp.expand(beta * x * sp.diff(G, x) + b * e * sp.diff(G, e) - 2 * beta * G)
    W1 = trunc(beta * x - Dy(Psi), D); W2 = trunc(beta * sp.diff(G, x) + Dx(Psi), D)
    Th = a0 * e
    RT = trunc(W1 * Dx(Th) + W2 * Dy(Th) - b * Th, N)
    Om = trunc(-(Dx(Dx(Psi)) + Dy(Dy(Psi))), N)
    RO = trunc(W1 * Dx(Om) + W2 * Dy(Om) + Om - Dx(Th), N - 2)
    return hs, HN, RT, RO
# lower terms: random H4 when N = 6
for N, lower in [(4, 0), (6, sp.Rational(3, 7) * x ** 3 * e - sp.Rational(5, 11) * x * e ** 3)]:
    hs, HN, RT, RO = run(N, lower)
    print('N', N, 'temperature residual through degree', N, ':', sp.simplify(RT))
    P = sp.Poly(RO, x, e)
    top = sum(c * x ** m[0] * e ** m[1] for m, c in zip(P.monoms(), P.coeffs()) if sum(m) == N - 2)
    lin = sp.expand(top - top.subs({h: 0 for h in hs}))
    L = lambda f: sp.expand(al * x * sp.diff(f, x) + b * e * sp.diff(f, e))
    Lap = lambda f: sp.expand(sp.diff(f, x, 2) + sp.diff(f, e, 2))
    pred = sp.expand(-(L(Lap(L(HN) - 2 * beta * HN)) + Lap(L(HN) - 2 * beta * HN)) + a0 * sp.diff(HN, x, 2))
    print('   linear part minus T_N H:', sp.simplify(lin - pred))
    rows = [x ** (2 * k + 1) * e ** (N - 2 - 2 * k - 1) for k in range(N // 2 - 1)]
    Mx = sp.Matrix([[sp.Poly(lin, x, e).coeff_monomial(r).coeff(hs[j]) for j in range(N // 2 - 1)] for r in rows])
    print('   selected block:', Mx.tolist(), ' det', sp.factor(Mx.det()))
