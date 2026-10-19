"""Independent checks of referee result 39 SEC915 (Theorem 4.9, Corollary 4.10, Remark 4.11): scaling identities, Fourier
coefficients of g_p and Psi_p, the limit of (p/(1-p)) J_p[A], the Step 10 and Step 13 elementary bounds, and the
Fourier multiplier of the compact-source velocity. Written from the statements, not from the referee check script."""
import sympy as sp, itertools, random
x, y, p, th = sp.symbols('x y p theta', real=True)
out = []
def chk(name, cond):
    out.append((name, bool(cond))); print(name, bool(cond), flush=True)
# 1. chain-rule identities of Step 1 with generic rho, V
rho = sp.Function('rho'); V1 = sp.Function('V1'); V2 = sp.Function('V2')
X = (x / p, y / p)
f = p**2 * rho(*X)
b = (p**2 * V1(*X), p**2 * V2(*X))
gx, gy = sp.diff(f, x), sp.diff(f, y)
u, v = sp.symbols('u v')
sub = {u: x / p, v: y / p}
rho_u = sp.diff(rho(u, v), u).subs(sub); rho_v = sp.diff(rho(u, v), v).subs(sub)
V1u = sp.diff(V1(u, v), u).subs(sub); V1v = sp.diff(V1(u, v), v).subs(sub)
V2u = sp.diff(V2(u, v), u).subs(sub); V2v = sp.diff(V2(u, v), v).subs(sub)
chk('grad f_p = p grad rho', sp.simplify(gx - p * rho_u) == 0 and sp.simplify(gy - p * rho_v) == 0)
chk('b.grad f_p = p^3 V.grad rho', sp.simplify(b[0] * gx + b[1] * gy - p**3 * (V1(*X) * rho_u + V2(*X) * rho_v)) == 0)
chk('div b_p = p div V', sp.simplify(sp.diff(b[0], x) + sp.diff(b[1], y) - p * (V1u + V2v)) == 0)
chk('curl b_p = p curl V', sp.simplify(sp.diff(b[1], x) - sp.diff(b[0], y) - p * (V2u - V1v)) == 0)
# with div V = 2l = 2/p, curl V = -rho_x: div b = 2, curl b = -p rho_x = -d_x f_p
chk('p * (2/p) = 2 and -p rho_x = -d_x f_p', sp.simplify(p * (2 / p) - 2) == 0 and sp.simplify(-p * rho_u + gx) == 0)
# Db_p(0) = p diag(1/2, 2l - 1/2) with l = 1/p
chk('Db_p(0) = diag(p/2, 2 - p/2)', sp.simplify(p * (2 / p - sp.Rational(1, 2)) - (2 - p / 2)) == 0)
# D^2 f_p(0) = D^2 rho(0)
chk('D^2 f_p = D^2 rho(Z/p)', sp.simplify(sp.diff(f, x, 2) - sp.diff(rho(u, v), u, 2).subs(sub)) == 0)
# homogeneity: K(pZ) = p^-2 K(Z), phi(pZ) = p^-3 phi, grad phi(pZ) = p^-4 grad phi
r = sp.sqrt(x**2 + y**2)
K = sp.Matrix([-2 * x * y / r**2, (x**2 - y**2) / r**2]) / (2 * sp.pi * r**2)
phi = (3 * x**2 * y - y**3) / r**6       # r^-3 sin 3th
pp = sp.symbols('pp', positive=True)
Ks = K.subs({x: pp * x, y: pp * y}, simultaneous=True)
chk('K(pZ) = p^-2 K(Z)', sp.simplify(Ks - K / pp**2) == sp.zeros(2, 1))
chk('phi(pZ) = p^-3 phi(Z)', sp.simplify(phi.subs({x: pp * x, y: pp * y}, simultaneous=True) - phi / pp**3) == 0)
gphi = sp.Matrix([sp.diff(phi, x), sp.diff(phi, y)])
chk('grad phi(pZ) = p^-4 grad phi', sp.simplify(gphi.subs({x: pp * x, y: pp * y}, simultaneous=True) - gphi / pp**4) == sp.zeros(2, 1))
# c[f_p]: p^2 * p^-3 * p^2 (dZ) = p ; Q[f_p]: p^2 * p^2 * p^-4 * p^2 = p^2
l = 1 / p
c = l - sp.Rational(1, 2)
chk('c[f_p] = p c = 1 - p/2', sp.simplify(p * c - (1 - p / 2)) == 0)
Q = sp.pi * c * (c - sp.Rational(1, 2))
chk('Q[f_p] = p^2 Q = pi(1-p/2)(1-p)', sp.simplify(p**2 * Q - sp.pi * (1 - p / 2) * (1 - p)) == 0)
chk('kappa = (1-p)/(1-p/2) = 2(1-p)/(2-p)', sp.simplify(Q / (sp.pi * c**2) - (1 - p) / (1 - p / 2)) == 0
    and sp.simplify((1 - p) / (1 - p / 2) - 2 * (1 - p) / (2 - p)) == 0)
# 2. Theorem 3.16 RHS equals g_p
A = sp.Function('A')
rhs316 = sp.diff(sp.sin(th) * A(th), th) - (p + 1) * sp.cos(th) * A(th)
gp = sp.sin(th) * sp.diff(A(th), th) - p * sp.cos(th) * A(th)
chk('(sin A)\' - (p+1) cos A = sin A\' - p cos A', sp.simplify(rhs316 - gp) == 0)
# 3. Fourier coefficients for random trigonometric polynomials A with modes 0..4 (exact rationals). A function is a
# dict {m: complex Fourier coefficient of e^{i m th}}; products are convolutions, d/dth multiplies by i m. Exact in p.
def mul(F, G):
    H = {}
    for m, a in F.items():
        for n, c in G.items():
            H[m + n] = H.get(m + n, 0) + a * c
    return {k: sp.cancel(v) for k, v in H.items()}
def add(*Fs):
    H = {}
    for F in Fs:
        for m, a in F.items():
            H[m] = H.get(m, 0) + a
    return {k: sp.cancel(v) for k, v in H.items()}
def scl(c, F):
    return {m: sp.cancel(c * a) for m, a in F.items()}
def dth(F):
    return {m: sp.I * m * a for m, a in F.items()}
def cs(F, m):            # real cos and sin coefficients of mode m >= 1
    return sp.simplify(F.get(m, 0) + F.get(-m, 0)), sp.simplify(sp.I * (F.get(m, 0) - F.get(-m, 0)))
COS = {1: sp.Rational(1, 2), -1: sp.Rational(1, 2)}; SIN = {1: -sp.I / 2, -1: sp.I / 2}
random.seed(7)
for trial in range(6):
    co = [sp.Rational(random.randint(-9, 9), random.randint(1, 5)) for _ in range(9)]
    if trial == 5:
        co[3] = co[4] = 0            # a_2 = b_2 = 0
    Ath = {0: co[0]}
    for k in range(1, 5):
        Ath = add(Ath, scl(co[2 * k - 1], {k: sp.Rational(1, 2), -k: sp.Rational(1, 2)}), scl(co[2 * k], {k: -sp.I / 2, -k: sp.I / 2}))
    Abar = Ath[0]
    a2, b2 = cs(Ath, 2)
    ok0 = sp.simplify(a2 - co[3]) == 0 and sp.simplify(b2 - co[4]) == 0
    g = add(mul(SIN, dth(Ath)), scl(-p, mul(COS, Ath)))
    gc, gs = cs(g, 1)
    ok1 = sp.simplify(gc - (-p * Abar - (p + 2) * a2 / 2)) == 0 and sp.simplify(gs + (p + 2) * b2 / 2) == 0
    Psi = {m: sp.cancel(c / ((p + 1)**2 - m**2)) for m, c in g.items()}
    res = add(dth(dth(Psi)), scl((p + 1)**2, Psi), scl(-1, g))
    okr = all(sp.simplify(v) == 0 for v in res.values())
    Pc, Ps = cs(Psi, 1)
    ok2 = sp.simplify(Pc - (-Abar / (p + 2) - a2 / (2 * p))) == 0 and sp.simplify(Ps + b2 / (2 * p)) == 0
    J = add(scl(p + 1, mul(Psi, dth(Ath))), scl(-p, mul(dth(Psi), Ath)))
    P2 = add(scl(a2, COS), scl(b2, SIN))
    target = scl(-sp.Rational(1, 2), mul(P2, dth(Ath)))
    ok3 = True; ok4 = True
    for m in set(J) | set(target):
        cm = sp.cancel(p / (1 - p) * J.get(m, 0))
        ok3 = ok3 and sp.simplify(sp.limit(cm, p, 0) - target.get(m, 0)) == 0
        if trial == 5:
            ok4 = ok4 and sp.limit(J.get(m, 0), p, 0).is_finite
    chk('trial %d: a_2,b_2 readback %s, g_p first mode %s, ODE residual %s, Psi_p first mode %s, limit of p J/(1-p) %s%s'
        % (trial, ok0, ok1, okr, ok2, ok3, (', J_p bounded as p -> 0 (a_2 = b_2 = 0) %s' % ok4) if trial == 5 else ''),
        ok0 and ok1 and okr and ok2 and ok3 and ok4)
# 4. Step 10 elementary integrals
chk('int cos^2 sin3 = 0', sp.integrate(sp.cos(th)**2 * sp.sin(3 * th), (th, 0, 2 * sp.pi)) == 0)
chk('int |sin 3th| = 4 (numerical quadrature) and (1/pi)(R/2)*4 <= R', abs(float(sp.Integral(sp.Abs(sp.sin(3 * th)), (th, 0, 2 * sp.pi)).evalf(30)) - 4) < 1e-20 and float(2 / sp.pi) <= 1)
# 5. Step 13 multinomial: sum over |alpha| = N+1 of (N+1)!/alpha! |h|^alpha = (|h1|+|h2|)^(N+1)
h1, h2 = sp.symbols('h1 h2', positive=True)
ok = True
for N in range(0, 8):
    s = sum(sp.factorial(N + 1) / (sp.factorial(k) * sp.factorial(N + 1 - k)) * h1**k * h2**(N + 1 - k) for k in range(N + 2))
    ok = ok and sp.expand(s - (h1 + h2)**(N + 1)) == 0
chk('multinomial identity N = 0..7', ok)
# 6. Fourier multiplier of U = (d_xy G, -d_xx G) * rho, G^ = -1/|xi|^2
k1, k2 = sp.symbols('k1 k2', real=True)
G = -1 / (k1**2 + k2**2)
U1 = (sp.I * k1) * (sp.I * k2) * G; U2 = -(sp.I * k1)**2 * G
chk('multiplier (k1 k2, -k1^2)/|k|^2, norm |k1|/|k| <= 1',
    sp.simplify(U1 - k1 * k2 / (k1**2 + k2**2)) == 0 and sp.simplify(U2 + k1**2 / (k1**2 + k2**2)) == 0
    and sp.simplify(U1**2 + U2**2 - k1**2 / (k1**2 + k2**2)) == 0)
# curl and div of the multiplier field: i k1 U2 - i k2 U1 = -i k1 (curl = -rho_x), i k1 U1 + i k2 U2 = 0
chk('div U = 0, curl U = -rho_x in Fourier', sp.simplify(sp.I * k1 * U1 + sp.I * k2 * U2) == 0
    and sp.simplify(sp.I * k1 * U2 - sp.I * k2 * U1 + sp.I * k1) == 0)
print('ALL', all(o[1] for o in out), len(out))
