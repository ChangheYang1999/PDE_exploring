"""V195: independent symbolic checks of the displayed identities in referee result 40 (written without
reading the referee check script). Equations: -Lap psi = rho_x, l X.grad rho + {psi, rho} = rho, {f,g} = f_x g_y - f_y g_x,
V = (l x - psi_y, l y + psi_x), beta = 2 l - 1/2. Each check prints its name and True/False."""
import sympy as sp, itertools, random
x, y, u, v, l, t = sp.symbols('x y u v l t')
beta = 2 * l - sp.Rational(1, 2)
R = []
def ok(name, val):
    R.append(bool(val)); print('%-72s %s' % (name, bool(val)), flush=True)
def br(f, g, X=x, Y=y):
    return sp.expand(sp.diff(f, X) * sp.diff(g, Y) - sp.diff(f, Y) * sp.diff(g, X))
def lap(f):
    return sp.expand(sp.diff(f, x, 2) + sp.diff(f, y, 2))
def hom(name, k, X=x, Y=y):
    c = sp.symbols('%s0:%d' % (name, k + 1))
    return sum(c[p] * X**p * Y**(k - p) for p in range(k + 1)), list(c)
def cf(e, k, X=x, Y=y):
    P = sp.Poly(sp.expand(e), X, Y)
    return [P.coeff_monomial(X**p * Y**(k - p)) for p in range(k + 1)]

# Step 1: quadratic jet
a, b, c = sp.symbols('a b c')
psi2 = a * (x**2 - y**2) / 2 + b * x * y + c * (x**2 + y**2) / 2
ok('S1 -Lap psi2 = -2c', sp.expand(-lap(psi2) + 2 * c) == 0)
e2 = sp.expand(l * (x * 2 * x) + br(psi2, x**2) - x**2)
ok('S1 degree-2 transport = (2l-1-2b)x^2 + 2(a-c)xy', sp.expand(e2 - ((2*l - 1 - 2*b) * x**2 + 2*(a - c)*x*y)) == 0)
ok('S1 solve: c = a = 0, b = l - 1/2', sp.solve(cf(e2, 2) + [c], [a, b, c], dict=True) == [{a: 0, b: l - sp.Rational(1, 2), c: 0}])
rs, ps = x**2, -x**3 / 3 + (l - sp.Rational(1, 2)) * x * y
V = (l * x - sp.diff(ps, y), l * y + sp.diff(ps, x))
ok('S1 known solution: V = (x/2, beta y - x^2)', sp.expand(V[0] - x / 2) == 0 and sp.expand(V[1] - beta * y + x**2) == 0)
ok('S1 known solution: -Lap psi = rho_x and V.grad rho = rho',
   sp.expand(-lap(ps) - sp.diff(rs, x)) == 0 and sp.expand(V[0] * sp.diff(rs, x) + V[1] * sp.diff(rs, y) - rs) == 0)

# Step 2: diagonal operator, homogeneous recursion, particular solution of the Poisson equation
p2 = (l - sp.Rational(1, 2)) * x * y
good = True
for k in range(3, 10):
    for p in range(k + 1):
        q = k - p; m = x**p * y**q
        good &= sp.expand(br(p2, m) - (l - sp.Rational(1, 2)) * (q - p) * m) == 0
        good &= sp.expand((k * l - 1) * m + br(p2, m) - (sp.Rational(p, 2) + beta * q - 1) * m) == 0
ok('S2 {psi2, x^p y^q} = (l-1/2)(q-p) x^p y^q and D_k diagonal (k = 3..9)', good)
ok('S2 {-x^3/3, R} = -x^2 R_y (generic quartic R)', (lambda Rq: sp.expand(br(-x**3 / 3, Rq) + x**2 * sp.diff(Rq, y)) == 0)(hom('r', 4)[0]))
# homogeneous comparison: random polynomial rho, psi with the jets; degree-k part of the transport residual
random.seed(1)
def rpoly(lo, hi):
    return sum(sp.Rational(random.randint(-5, 5), random.randint(1, 4)) * x**p * y**(k - p) for k in range(lo, hi + 1) for p in range(k + 1))
good = True
for trial in range(3):
    rho = x**2 + rpoly(3, 5); psi = p2 + rpoly(3, 6)
    T = sp.expand(l * (x * sp.diff(rho, x) + y * sp.diff(rho, y)) + br(psi, rho) - rho)
    hp = lambda f, k: sum(cc * x**pp * y**(k - pp) for pp, cc in enumerate(cf(f, k)))
    for k in range(3, 10):
        rk = hp(rho, k); form = (k * l - 1) * rk + br(p2, rk) + br(hp(psi, k), x**2) \
            + sum(br(hp(psi, i), hp(rho, k + 2 - i)) for i in range(3, k))
        good &= sp.expand(hp(T, k) - form) == 0
ok('S2 degree-k transport = D_k rho_k + {psi_k,x^2} + sum_{i=3}^{k-1} {psi_i,rho_(k+2-i)}', good)
def Ix2(f):
    return sp.integrate(sp.integrate(f, (x, 0, x)), (x, 0, x))
good = True
for k in range(0, 8):
    S = hom('s', k)[0]; P = 0; j = 0
    while sp.diff(S, y, 2 * j) != 0:
        f = sp.diff(S, y, 2 * j)
        for _ in range(j + 1):
            f = Ix2(f)
        P += (-1)**j * f; j += 1
    good &= sp.expand(lap(P) - S) == 0
ok('S2 P = sum (-1)^j (I_x^2)^(j+1) d_y^(2j) S solves Lap P = S (k = 0..7)', good)
bb = sp.Rational(1, 3) + sp.Rational(1, 1000)
ok('S2 l > 5/12: p/2 + beta q - 1 > 0 for p+q >= 3 (beta = 1/3 + 1e-3, p+q <= 40)',
   all(sp.Rational(p, 2) + bb * (k - p) - 1 > 0 for k in range(3, 41) for p in range(k + 1)))

# Step 3: Euler identities and the power identity
good = True
for m, n in [(3, 4), (4, 5), (5, 3), (2, 6)]:
    f = hom('f', m)[0]; g = hom('g', n)[0]; J = br(f, g)
    good &= sp.expand(m * f * sp.diff(g, x) - n * g * sp.diff(f, x) + y * J) == 0
    good &= sp.expand(m * f * sp.diff(g, y) - n * g * sp.diff(f, y) - x * J) == 0
    for X in (x, y):
        good &= sp.simplify(sp.diff(g**m / f**n, X) - g**(m - 1) * f**(-n - 1) * (m * f * sp.diff(g, X) - n * g * sp.diff(f, X))) == 0
ok('S3 m f g_x - n g f_x = -y{f,g}, m f g_y - n g f_y = x{f,g}, d(g^m/f^n)', good)

# Step 4: highest parts
e1, e2_, mu, lam = sp.symbols('e1 e2 mu lam')
good = True
for N in range(2, 8):
    L = e1 * x + e2_ * y
    good &= sp.expand(lap(L**(N + 1)) - N * (N + 1) * (e1**2 + e2_**2) * L**(N - 1)) == 0
    good &= sp.expand(sp.diff(mu * L**N, x) - mu * N * e1 * L**(N - 1)) == 0
ok('S4 Lap (e.X)^(N+1) = N(N+1)|e|^2 (e.X)^(N-1), d_x mu (e.X)^N = mu N e1 (e.X)^(N-1)', good)
z = sp.symbols('z')
good = True
for M in range(3, 9):
    A = sp.Rational(random.randint(1, 9), 7) + sp.I * sp.Rational(random.randint(-9, 9), 5)
    pol = sp.Poly(A * z**M + sp.conjugate(A), z)
    good &= sp.degree(sp.gcd(pol, pol.diff(z))) == 0 and pol.eval(0) != 0
    hm = sp.expand(A * (x + sp.I * y)**M + sp.conjugate(A) * (x - sp.I * y)**M)
    good &= lap(hm) == 0
ok('S4 A t^M + conj(A) squarefree with nonzero roots; A z^M + conj(A) w^M harmonic (M = 3..8)', good)
ok('S4 M <= N: mu y^N, {psi_M, mu y^N} = mu N y^(N-1) psi_M,x (generic psi_5, N = 6)',
   (lambda P5: sp.expand(br(P5, mu * y**6) - mu * 6 * y**5 * sp.diff(P5, x)) == 0)(hom('w', 5)[0]))

# Step 5: N = 2
F = sp.Function('F')
Q5 = hom('q', 3)[0] + hom('qq', 2)[0]
ok('S5 transport for rho = x^2: (2l-1)x^2 - 2x psi_y', sp.expand(l * 2 * x**2 + br(Q5, x**2) - x**2 - ((2*l - 1)*x**2 - 2*x*sp.diff(Q5, y))) == 0)

# Step 6: N = 3
A_, B_, C_, D_ = sp.symbols('A B C D')
psi3 = A_ * x**3 + B_ * x**2 * y + C_ * x * y**2 + D_ * y**3
rho3 = mu * (x + t * y)**3
E1 = cf(-lap(psi3) - 2 * x, 1)
ok('S6 Poisson degree one: 6A + 2C = -2, 2B + 6D = 0', sp.expand(E1[1] + 6*A_ + 2*C_ + 2) == 0 and sp.expand(E1[0] + 2*B_ + 6*D_) == 0)
E3 = cf((3 * l - 1) * rho3 + br(p2, rho3) + br(psi3, x**2), 3)
target = [mu * t**3 * (3 * beta - 1), 3 * mu * t**2 * (2 * beta - sp.Rational(1, 2)) - 6 * D_, 3 * mu * t * beta - 4 * C_, mu / 2 - 2 * B_]
ok('S6 the four degree-3 transport equations', all(sp.expand(E3[i] - target[i]) == 0 for i in range(4)))
Bs, Ds = mu / 4, mu * t**2 * (2 * beta - sp.Rational(1, 2)) / 2
ok('S6 2B + 6D = (mu/2)(1 + 6 t^2 (2beta - 1/2))', sp.expand(2 * Bs + 6 * Ds - mu / 2 * (1 + 6 * t**2 * (2 * beta - sp.Rational(1, 2)))) == 0)
ok('S6 beta = 1/3 turns it into 1 + t^2', sp.expand((1 + 6 * t**2 * (2 * beta - sp.Rational(1, 2))).subs(l, (sp.Rational(1, 3) + sp.Rational(1, 2)) / 2) - (1 + t**2)) == 0)
w_ = sp.Symbol('w')
G = sp.groebner(E1 + E3 + [mu * w_ - 1], A_, B_, C_, D_, mu, w_, l, t, order='lex')
elim = [g for g in G.exprs if not g.has(A_, B_, C_, D_, mu, w_)]
print('   S6 elimination ideal in (l, t) with mu != 0:', elim, flush=True)
ok('S6 elimination ideal contains t^2 + 1 (no real t, any l)', any(sp.expand(g - (t**2 + 1)) == 0 for g in elim))

# Step 7: resonance list
good = True
for n in range(3, 30):
    bt = sp.Rational(1, n)
    res = [(p, k - p) for k in range(3, 80) for p in range(k + 1) if sp.Rational(p, 2) + bt * (k - p) - 1 == 0]
    want = [(0, n)] + ([(1, n // 2)] if n % 2 == 0 else [])
    good &= sorted(res) == sorted(want)
# nonresonant sample values
for bt in [sp.Rational(2, 7), sp.Rational(3, 10), sp.Rational(1, 3) + sp.Rational(1, 100), sp.Rational(5, 2)]:
    good &= not any(sp.Rational(p, 2) + bt * (k - p) - 1 == 0 for k in range(3, 80) for p in range(k + 1))
ok('S7 resonances for beta = 1/n are exactly y^n and (n even) x y^(n/2), degrees <= 79', good)
ok('S7 l = 1/4 + 1/(2n) <=> beta = 1/n; n = 3 -> l = 5/12; xy^2 (beta = 1/4) -> l = 3/8',
   sp.solve(sp.Eq(beta, sp.Rational(1, 3)), l) == [sp.Rational(5, 12)] and sp.solve(sp.Eq(beta, sp.Rational(1, 4)), l) == [sp.Rational(3, 8)])

# Step 8: div, curl, linear part; the formal eigenfunction h; rho = h^2 recursion operator
psiG = p2 + rpoly(3, 5)
VG = (l * x - sp.diff(psiG, y), l * y + sp.diff(psiG, x))
ok('S8 div V = 2l, curl V = Lap psi, V(0) = 0, V_1 = (x/2, beta y)',
   sp.expand(sp.diff(VG[0], x) + sp.diff(VG[1], y) - 2 * l) == 0 and sp.expand(sp.diff(VG[1], x) - sp.diff(VG[0], y) - lap(psiG)) == 0
   and VG[0].subs({x: 0, y: 0}) == 0 and VG[1].subs({x: 0, y: 0}) == 0
   and sp.expand(sum(cc * x**pp * y**(1 - pp) for pp, cc in enumerate(cf(VG[0], 1))) - x / 2) == 0
   and sp.expand(sum(cc * x**pp * y**(1 - pp) for pp, cc in enumerate(cf(VG[1], 1))) - beta * y) == 0)
good = True
for k in range(2, 9):
    for p in range(k + 1):
        m = x**p * y**(k - p)
        good &= sp.expand(x / 2 * sp.diff(m, x) + beta * y * sp.diff(m, y) - m / 2 - (sp.Rational(p, 2) + beta * (k - p) - sp.Rational(1, 2)) * m) == 0
        good &= sp.expand(x / 2 * sp.diff(m, x) + beta * y * sp.diff(m, y) - m - ((k * l - 1) * m + br(p2, m))) == 0
ok('S8 (V_1.grad - 1/2) diagonal p/2 + beta q - 1/2; V_1.grad - 1 = D_k', good)
# solve D h = h/2 to degree 8 for a polynomial V with the forced linear part at a nonresonant rational l
lv = sp.Rational(3, 2); bv = 2 * lv - sp.Rational(1, 2)
psiN = (lv - sp.Rational(1, 2)) * x * y + rpoly(3, 5)
VN = (lv * x - sp.diff(psiN, y), lv * y + sp.diff(psiN, x))
h = x; K = 9
for k in range(2, K):
    r = sp.expand(VN[0] * sp.diff(h, x) + VN[1] * sp.diff(h, y) - h / 2)
    rk = cf(r, k)
    h += sum(-rk[p] / (sp.Rational(p, 2) + bv * (k - p) - sp.Rational(1, 2)) * x**p * y**(k - p) for p in range(k + 1))
r = sp.expand(VN[0] * sp.diff(h, x) + VN[1] * sp.diff(h, y) - h / 2)
ok('S8 formal h = x + O(2), D h = h/2 solvable degree by degree (residual O(|X|^9), l = 3/2)',
   all(c_ == 0 for k in range(0, K) for c_ in cf(r, k)))
ok('S8 known solution: h = x (D x = x/2), rho = h^2',
   sp.expand(V[0] * 1 - x / 2) == 0)
# P^2 | rho from rho(f(y), y) = rho_x(f(y), y) = 0 when f is a root: algebra check on an example rho = (x + y^2)^2 (1 + y)
Pex = x + y**2; rex = sp.expand(Pex**2 * (1 + y))
ok('S8 example: common root of rho, rho_x along x = -y^2 and P^2 | rho',
   sp.expand(rex.subs(x, -y**2)) == 0 and sp.expand(sp.diff(rex, x).subs(x, -y**2)) == 0 and sp.rem(sp.Poly(rex, x), sp.Poly(Pex**2, x)).is_zero)
# 2 Q D P + P D Q = P Q from D(P^2 Q) = P^2 Q (derivation identity)
Pf, Qf, Vx, Vy = [sp.Function(n_)(x, y) for n_ in ('P', 'Q', 'Vx', 'Vy')]
Dop = lambda f: Vx * sp.diff(f, x) + Vy * sp.diff(f, y)
ok('S8 D(P^2 Q) - P^2 Q = P (2 Q DP + P DQ - P Q)', sp.expand(Dop(Pf**2 * Qf) - Pf**2 * Qf - Pf * (2 * Qf * Dop(Pf) + Pf * Dop(Qf) - Pf * Qf)) == 0)

# Step 9
A0, T0, F0 = [sp.Function(n_)(v) for n_ in ('A0', 'T0', 'F0')]
eqd = 2 * A0 * F0 + T0 * sp.diff(F0, v) - F0
eqv = A0 + sp.diff(T0, v) - 2 * l
ok('S9 eliminating A(0,v): T0 F\' - 2 (T0\' - beta) F = (density eq) - 2 F (divergence eq)',
   sp.expand(eqd - 2 * F0 * eqv - (T0 * sp.diff(F0, v) - 2 * (sp.diff(T0, v) - beta) * F0)) == 0)
# u-coordinates: density equation after cancelling u^2 restricted to u = 0
Au, Tu, Qu = [sp.Function(n_)(u, v) for n_ in ('Au', 'Tu', 'Qu')]
Duv = lambda f: u * Au * sp.diff(f, u) + Tu * sp.diff(f, v)
ok('S9 D(u^2 Q) - u^2 Q = u^2 (2 A Q + u A Q_u + T Q_v - Q)',
   sp.expand(Duv(u**2 * Qu) - u**2 * Qu - u**2 * (2 * Au * Qu + u * Au * sp.diff(Qu, u) + Tu * sp.diff(Qu, v) - Qu)) == 0)
# brute force: T0 of degree <= 6 with T0(0)=0, T0'(0)=beta, F of degree <= 3 with F(0)=1
good = True
for lv_ in [sp.Rational(3, 2), sp.Rational(3, 10), sp.Rational(7, 5)]:
    bv_ = 2 * lv_ - sp.Rational(1, 2)
    tc = sp.symbols('t2:7'); fc = sp.symbols('f1:4')
    T0p = bv_ * v + sum(tc[i] * v**(i + 2) for i in range(5)); F0p = 1 + sum(fc[i] * v**(i + 1) for i in range(3))
    eqs = sp.Poly(sp.expand(T0p * sp.diff(F0p, v) - 2 * (sp.diff(T0p, v) - bv_) * F0p), v).coeffs()
    sols = sp.solve(eqs, list(tc) + list(fc), dict=True)
    good &= sols == [{**{ti: 0 for ti in tc}, **{fi: 0 for fi in fc}}]
ok('S9 T0 F\' = 2(T0\' - beta) F with deg T0 <= 6, deg F <= 3 forces T0 = beta v, F = 1 (3 values of l)', good)
# the degree count d = 2m (leading coefficients) and an example with d = 2m: T0 = beta v + v^2, F = ?
tau, phi = sp.symbols('tau phi'); good = True
for m in range(2, 6):
    for d in range(0, 7):
        lo = sp.symbols('lo0:%d' % (m + d + 2))
        T0q = beta * v + sum(lo[i] * v**i for i in range(2, m)) + tau * v**m
        F0q = sum(lo[m + i] * v**i for i in range(0, d)) + phi * v**d
        ex = sp.Poly(sp.expand(T0q * sp.diff(F0q, v) - 2 * (sp.diff(T0q, v) - beta) * F0q), v)
        good &= ex.degree() <= m + d - 1 and sp.expand(ex.coeff_monomial(v**(m + d - 1)) - tau * phi * (d - 2 * m)) == 0
ok('S9 top coefficient of T0 F\' - 2(T0\' - beta)F is tau phi (d - 2m) for m >= 2 (m <= 5, d <= 6)', good)

# Step 10: Cauchy data and harmonic uniqueness
psiC = sp.Function('psiC')(x, y)
ok('S10 tangential velocity on x = 0: l y + psi_x(0,y) = beta y <=> psi_x(0,y) = (l - 1/2) y',
   sp.simplify((beta - l) - (l - sp.Rational(1, 2))) == 0)
good = True
for k in range(2, 9):
    H, hc = hom('h', k)
    eqs = cf(lap(H), k - 2) + [hc[0], hc[1]]   # H(0,y) = hc[0] y^k, H_x(0,y) = hc[1] y^(k-1)
    sol = sp.solve(eqs, hc, dict=True)
    good &= sol == [{hh: 0 for hh in hc}]
ok('S10 homogeneous harmonic H with H(0,y) = H_x(0,y) = 0 is zero (k = 2..8)', good)
ok('S10 psi_3 + x^3/3 harmonic with zero Cauchy data; {-x^3/3, x^2} = 0',
   sp.expand(-lap(-x**3 / 3) - 2 * x) == 0 and br(-x**3 / 3, x**2) == 0 and sp.diff(-x**3 / 3, x).subs(x, 0) == 0)

# Step 11: curl formula in (u, v) coordinates
aa, bb_, Cc, cc_ = sp.symbols('a b C c')
fF = sp.Function('f'); HF = sp.Function('H')
g = sp.diff(fF(v), v); T = beta * v + HF(u)
Vx_ = u / 2 - g * T; Vy_ = (T - aa * Vx_) / bb_
dx = lambda f: (1 + aa * g) * sp.diff(f, u) + aa * sp.diff(f, v)
dy = lambda f: bb_ * g * sp.diff(f, u) + bb_ * sp.diff(f, v)
Kk = aa**2 + bb_**2
curl = dx(Vy_) - dy(Vx_)
form = (1 + 2 * aa * g + Kk * g**2) * sp.diff(HF(u), u) + Kk * sp.diff(fF(v), v, 2) * HF(u) + Kk * beta * v * sp.diff(fF(v), v, 2) \
    + (beta - sp.Rational(1, 2)) * (aa + Kk * g)
ok('S11 b curl V = (1+2ag+Kg^2)H\' + K f\'\' H + K beta v f\'\' + (beta-1/2)(a+Kg)', sp.simplify(sp.expand(bb_ * curl - form)) == 0)
# the same in (x, y) with explicit f and H: derivative operators, Du = u/2, Dv = T, div V = 2l, Jacobian b
fe = Cc * v**2 + cc_ * v**3; He = sp.Symbol('r1') * u + sp.Symbol('r2') * u**2 + sp.Symbol('r3') * u**3
vxy = aa * x + bb_ * y; uxy = x + fe.subs(v, vxy)
Te = (beta * v + He).subs(u, uxy).subs(v, vxy)
Vxe = (u / 2).subs(u, uxy) - sp.diff(fe, v).subs(v, vxy) * Te
Vye = (Te - aa * Vxe) / bb_
Dxy = lambda f: Vxe * sp.diff(f, x) + Vye * sp.diff(f, y)
ok('S11 explicit f, H: D u = u/2, D v = beta v + H(u), div V = 2l, Jacobian(u,v) = b',
   sp.expand(Dxy(uxy) - uxy / 2) == 0 and sp.expand(Dxy(vxy) - Te) == 0
   and sp.expand(sp.diff(Vxe, x) + sp.diff(Vye, y) - 2 * l) == 0
   and sp.expand(sp.diff(uxy, x) * sp.diff(vxy, y) - sp.diff(uxy, y) * sp.diff(vxy, x) - bb_) == 0)
curl_xy = sp.diff(Vye, x) - sp.diff(Vxe, y)
form_e = form.subs({fF(v): fe}).doit().subs(HF(u), He).doit()
form_e = form.replace(fF, sp.Lambda(v, fe)).replace(HF, sp.Lambda(u, He)).doit()
ok('S11 explicit f, H: (x,y) curl agrees with the (u,v) formula', sp.expand(bb_ * curl_xy - form_e.subs(u, uxy).subs(v, vxy)) == 0)
# linear part of D v at the origin: H'(0) = a(1/2 - beta)
Vlin = (x / 2, beta * y)
Dv_lin = sp.expand(aa * Vlin[0] + bb_ * Vlin[1])
ulin, vlin = x, aa * x + bb_ * y
ok('S11 linear part: a x/2 + b beta y = beta v + a(1/2 - beta) u at first order', sp.expand(Dv_lin - (beta * vlin + aa * (sp.Rational(1, 2) - beta) * ulin)) == 0)
# coefficient of u^r for H of degree r >= 2 and of u^1 for H = r0 u
r0 = aa * (sp.Rational(1, 2) - beta)
formL = form.replace(HF, sp.Lambda(u, r0 * u)).doit()
c1 = sp.expand(sp.diff(formL, u).subs(u, 0))
ok('S11 H = r0 u: u-coefficient of b curl V is K r0 f\'\'', sp.simplify(c1 - Kk * r0 * sp.diff(fF(v), v, 2)) == 0)
ok('S11 u-coefficient of -2bu(1+ag) is -2b(1+a f\')', sp.expand(sp.diff(-2 * bb_ * u * (1 + aa * g), u) + 2 * bb_ * (1 + aa * g)) == 0)
# direct check: no H of degree <= 3 and f = C v^2 + c v^3 with (C, c) != 0 satisfies b curl V = -2 b u (1 + a g)
r1, r2, r3 = sp.symbols('r1 r2 r3')
diff_ = sp.expand(form.replace(fF, sp.Lambda(v, fe)).replace(HF, sp.Lambda(u, He)).doit() + 2 * bb_ * u * (1 + aa * sp.diff(fe, v)))
cs = sp.Poly(diff_, u, v).coeffs()
sol = sp.solve(cs + [r1 - r0], [r1, r2, r3, Cc, cc_], dict=True)
print('   S11 solutions (r1, r2, r3, C, c) at generic a, b, l:', sol, flush=True)
ok('S11 no solution with (C, c) != 0 (generic a, b != 0, l)', all(s.get(Cc, Cc) == 0 and s.get(cc_, cc_) == 0 for s in sol))

# Step 12: Q in (u, v) coordinates and the alpha identity
al1, ga1, ka = sp.symbols('alpha1 gamma1 kappa')
xs = u - Cc * v**2; ys = (v - aa * xs) / bb_
Q = 1 + al1 * x + ga1 * y + ka * (aa * x + bb_ * y)**2
Quv = sp.expand(Q.subs({x: xs, y: ys}, simultaneous=True))
mons = sp.Poly(Quv, u, v).monoms()
ok('S12 Q(u,v) has only the monomials 1, u, v, v^2', set(mons) <= {(0, 0), (1, 0), (0, 1), (0, 2)})
alp = sp.Symbol('alpha'); Duf = sp.Function('Du')(u, v)
ok('S12 D(u^2(1+alpha u)) - u^2(1+alpha u) = u((2+3alpha u)Du - u(1+alpha u))',
   sp.expand((2 * u + 3 * alp * u**2) * Duf - u**2 * (1 + alp * u) - u * ((2 + 3 * alp * u) * Duf - u * (1 + alp * u))) == 0)
ok('S12 u = -2/(3alpha): u(1+alpha u) = -2/(9alpha)', sp.simplify((u * (1 + alp * u)).subs(u, -2 / (3 * alp)) + 2 / (9 * alp)) == 0)

# Step 13: quadratic and rank-one identities
s11, s12, s22 = sp.symbols('s11 s12 s22'); Am = sp.Matrix(2, 2, sp.symbols('a11 a12 a21 a22'))
S_ = sp.Matrix([[s11, s12], [s12, s22]]); Z = sp.Matrix([x, y])
H2 = (Z.T * S_ * Z)[0] / 2
ok('S13 (AZ).grad H2 = Z^T (A^T S + S A) Z / 2', sp.expand((Am * Z).dot(sp.Matrix([sp.diff(H2, x), sp.diff(H2, y)])) - (Z.T * (Am.T * S_ + S_ * Am) * Z)[0] / 2) == 0)
ok('S13 tr(S^-1 (A^T S + S A)) = 2 tr A', sp.simplify((S_.inv() * (Am.T * S_ + S_ * Am)).trace() - 2 * Am.trace()) == 0)
ok('S13 D(grad P) = (1/2) grad P - (DV)^T grad P when V.grad P = P/2 (gradient of the identity)',
   (lambda Pp, W1, W2: sp.expand(sp.Matrix([sp.diff(W1 * sp.diff(Pp, x) + W2 * sp.diff(Pp, y) - Pp / 2, X_) for X_ in (x, y)])
     - (sp.Matrix([[sp.diff(Pp, x, x), sp.diff(Pp, x, y)], [sp.diff(Pp, x, y), sp.diff(Pp, y, y)]]) * sp.Matrix([W1, W2])
        + sp.Matrix([[sp.diff(W1, x), sp.diff(W2, x)], [sp.diff(W1, y), sp.diff(W2, y)]]) * sp.Matrix([sp.diff(Pp, x), sp.diff(Pp, y)])
        - sp.Matrix([sp.diff(Pp, x), sp.diff(Pp, y)]) / 2)) == sp.zeros(2, 1))(sp.Function('P')(x, y), sp.Function('W1')(x, y), sp.Function('W2')(x, y)))
# rank one: H2 = u^2, generic linear A, generic quadratic V2, cubic H3
au = sp.symbols('b11 b12 b21 b22'); V2u, _c2u = hom('pu', 2, u, v); V2v, _c2v = hom('pv', 2, u, v); H3, h3 = hom('hh', 3, u, v)
V1u = au[0] * u + au[1] * v; V1v = au[2] * u + au[3] * v
lin = sp.expand(V1u * sp.diff(u**2, u) + V1v * sp.diff(u**2, v) - u**2 / 2)
sl = sp.solve(cf(lin, 2, u, v), [au[0], au[1]], dict=True)
ok('S13 rank one: (AZ).grad u^2 = u^2/2 forces D_1 u = u/4', sl == [{au[0]: sp.Rational(1, 4), au[1]: 0}])
cub = sp.expand((V1u * sp.diff(H3, u) + V1v * sp.diff(H3, v) + V2u * sp.diff(u**2, u) + V2v * sp.diff(u**2, v) - H3 / 2).subs(sl[0]))
ok('S13 degree-3 equation at u = 0: (3 d0 - 1/2) h v^3', sp.expand(cub.subs(u, 0) - (3 * au[3] - sp.Rational(1, 2)) * h3[0] * v**3) == 0)
ok('S13 trace 1/4 + 1/6 = 5/12 = 2l -> l = 5/24 < 1/4; nondegenerate: l = 1/4',
   sp.Rational(1, 4) + sp.Rational(1, 6) == sp.Rational(5, 12) and sp.Rational(5, 24) < sp.Rational(1, 4))

# Step 14: critical points
A1, B1, C1, c1_ = sp.symbols('A1 B1 C1 c1')
P14 = x + A1 * x**2 + B1 * x * y + C1 * y**2 + c1_ * x**3
q1 = sp.expand(sp.diff(P14, x).subs(y, -B1 * x / (2 * C1)))
ok('S14 L ~ x, C != 0: P_x on P_y = 0 is quadratic in x with leading coefficient 3c',
   sp.expand(sp.diff(P14, y).subs(y, -B1 * x / (2 * C1))) == 0 and sp.Poly(q1, x).degree() == 2 and sp.Poly(q1, x).LC() == 3 * c1_)
ok('S14 C = 0, B != 0: (0, -1/B) critical', all(sp.simplify(sp.diff(P14.subs(C1, 0), X_).subs({x: 0, y: -1 / B1})) == 0 for X_ in (x, y)))
ok('S14 B = C = 0: x | P', sp.rem(sp.Poly(P14.subs({B1: 0, C1: 0}), x), sp.Poly(x, x)).is_zero)
tt = sp.Symbol('tt')
P14b = tt + A1 * tt**2 + B1 * tt * v + C1 * v**2 + c1_ * v**3
ts = sp.solve(sp.diff(P14b, tt), tt)[0]
q2 = sp.expand(sp.diff(P14b, v).subs(tt, ts))
ok('S14 b != 0, A != 0: P_v on P_t = 0 is quadratic in v with leading coefficient 3c', sp.Poly(q2, v).degree() == 2 and sp.simplify(sp.Poly(q2, v).LC() - 3 * c1_) == 0)
P14c = P14b.subs(A1, 0)
ok('S14 A = 0, B != 0: v = -1/B and t = -(2Cv + 3cv^2)/B is critical',
   all(sp.simplify(sp.diff(P14c, X_).subs(v, -1 / B1).subs(tt, -(2 * C1 * (-1 / B1) + 3 * c1_ / B1**2) / B1)) == 0 for X_ in (tt, v)))
# real irreducible cubic P = x + C L^2 + c L^3 has no critical point issue: Step 11 applies with f = C v^2 + c v^3 (checked above)
print('ALL', all(R), len(R), flush=True)
