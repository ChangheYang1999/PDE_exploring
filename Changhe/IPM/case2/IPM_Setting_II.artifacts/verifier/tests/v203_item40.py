"""V203: symbolic checks of item 40 (Proposition 2.3 / Section 9.20, working draft of the lead analyst, STAT23 1bca6723,
SEC920 ec47e7c8). Written independently of the lead's files. Each check prints its name and True/False."""
import sympy as sp
x, y, l, s, t = sp.symbols('x y l s t', real=True)
r, th = sp.symbols('r th', positive=True)
R = []
def ok(name, val):
    R.append(bool(val)); print('%-100s %s' % (name, bool(val)), flush=True)
a = sp.Rational(1, 2); beta = 2*l - a; d = beta - a
A = sp.diag(a, beta); M = sp.diag(a - l, l - a)
ok('S1 l I + M = A = diag(1/2, beta), tr A = 2l', sp.simplify(l*sp.eye(2) + M - A) == sp.zeros(2) and sp.simplify(A.trace() - 2*l) == 0)
W1, W2 = sp.symbols('W1 W2', real=True)
X = sp.Matrix([r*sp.cos(th), r*sp.sin(th)]); V = A*X + sp.Matrix([W1, W2])
rdot = (X.T*V)[0]/r; thdot = (X[0]*V[1] - X[1]*V[0])/r**2
er = (X[0]*W1 + X[1]*W2)/r**2; eth = (X[0]*W2 - X[1]*W1)/r**2
ok('S1 r\'/r = a + d sin^2 th + e_r', sp.simplify(rdot/r - (a + d*sp.sin(th)**2 + er)) == 0)
ok('S1 th\' = d sin th cos th + e_th', sp.simplify(thdot - (d*sp.sin(th)*sp.cos(th) + eth)) == 0)
ok('S1 |e_r|, |e_th| <= |W|/r (Cauchy-Schwarz: e_r^2 + e_th^2 = |W|^2/r^2)', sp.simplify(er**2 + eth**2 - (W1**2 + W2**2)/r**2) == 0)
# Step 1: r'/r >= 1/2 - 2 eta = 1/4 at eta = 1/8
ok('S1 a - 2*(1/8) = 1/4', a - 2*sp.Rational(1, 8) == sp.Rational(1, 4))
# Step 3: |th'| >= (d/2) sin 2eps - 2eta >= (d/4) sin 2eps... with 2 eta <= (d/4) sin 2eps: (d/2 - d/4) sin2eps = (d/4) sin 2eps
D_, S2e, eta = sp.symbols('D S2e eta', positive=True)
ok('S3 d sin th cos th = (d/2) sin 2th and (d/2)S - 2eta >= (d/4)S when 2eta <= (d/4)S',
   sp.simplify(d*sp.sin(th)*sp.cos(th) - d*sp.sin(2*th)/2) == 0 and sp.simplify((D_/2*S2e - D_/4*S2e).subs({}) - D_/4*S2e) == 0)
# kernel symmetry
X1, Y1 = sp.symbols('X1 Y1', real=True)
rr = X1**2 + Y1**2
K = sp.Matrix([-2*X1*Y1/rr, (X1**2 - Y1**2)/rr])/(2*sp.pi*rr)
Kpolar = sp.Matrix([-sp.sin(2*th), sp.cos(2*th)])/(2*sp.pi*r**2)
ok('S8 K = (-sin 2th, cos 2th)/(2 pi r^2) in Cartesian form', sp.simplify(K.subs({X1: r*sp.cos(th), Y1: r*sp.sin(th)}) - Kpolar) == sp.zeros(2, 1))
J = sp.diag(-1, 1)
KJ = K.subs({X1: -X1}, simultaneous=True)
ok('S8 K(JZ) = J K(Z)', sp.simplify(KJ - J*K) == sp.zeros(2, 1))
DK = K.jacobian([X1, Y1]); DKJ = DK.subs({X1: -X1}, simultaneous=True)
ok('S8 DK(JZ) J = J DK(Z)', sp.simplify(DKJ*J - J*DK) == sp.zeros(2))
ok('S8 div K = 0 away from 0 (so div of the combined kernel in X is 0)', sp.simplify(sp.diff(K[0], X1) + sp.diff(K[1], Y1)) == 0)
ok('S8 J A = A J, J e_2 = e_2', J*A == A*J and J*sp.Matrix([0, 1]) == sp.Matrix([0, 1]))
# Step 6: d(e^{at} z_1)/dt = -e^{at} N_1 when z' = -(a z_1 + N_1)
z1 = sp.Function('z1')(t); N1 = sp.Function('N1')(t)
ok('S6 d(e^(at) z1)/dt = -e^(at) N1 given z1\' = -a z1 - N1', sp.simplify(sp.diff(sp.exp(a*t)*z1, t).subs(sp.diff(z1, t), -a*z1 - N1) + sp.exp(a*t)*N1) == 0)
ok('S6 e^t |z|^3 with |z| <= C e^(-t/2) is C e^(-t/2); (e^(at) z1)^2 = e^t z1^2', sp.simplify(sp.exp(t)*sp.exp(-3*t/2) - sp.exp(-t/2)) == 0
   and sp.simplify((sp.exp(a*t)*z1)**2 - sp.exp(t)*z1**2) == 0)
# Step 6 propagator: int_0^t e^{-a(t-u)} e^{-2au} du = (e^{-at} - e^{-2at})/a <= e^{-at}/a
u = sp.Symbol('u', positive=True); tp = sp.Symbol('tp', positive=True)
I6 = sp.integrate(sp.exp(-a*(tp - u))*sp.exp(-2*a*u), (u, 0, tp))
ok('S6 variation of constants: int_0^t e^(-a(t-u)) e^(-2au) du = (e^(-at) - e^(-2at))/a', sp.simplify(I6 - (sp.exp(-a*tp) - sp.exp(-2*a*tp))/a) == 0)
# Step 5: X.AX >= a|X|^2 since beta > a
ok('S5 X.AX - a|X|^2 = d y^2 >= 0', sp.expand((sp.Matrix([x, y]).T*A*sp.Matrix([x, y]))[0] - a*(x**2 + y**2) - d*y**2) == 0)
# Step 2: q < 1/gamma achievable: gamma a < 1 for gamma < 2
g_ = sp.Symbol('g', positive=True)
ok('S2 gamma a < 1 for gamma < 2 (gamma a = gamma/2)', sp.solve_univariate_inequality(g_*a < 1, g_, relational=False).intersect(sp.Interval.open(0, sp.oo)) == sp.Interval.open(0, 2))
# Sharpness: at gamma = 2 the formal pair rho = x^2, V = AX (W_2 = 0) is x-even, transported, with V = 0 only at 0
rho = x**2; VV = A*sp.Matrix([x, y])
ok('Sharp rho = x^2, V = AX: V.grad rho = rho (gamma = 2, Step 2 needs gamma a < 1)', sp.expand(VV[0]*sp.diff(rho, x) + VV[1]*sp.diff(rho, y) - rho) == 0)
# l > 1/2 from beta > 1/2
ok('S5 beta > 1/2 iff l > 1/2', sp.solve(sp.Eq(2*l - a, a), l) == [a])
# Section 9.14 Step 7: beta >= 1/gamma iff l >= 1/4 + 1/(2 gamma)
ok('S1 beta >= 1/gamma iff l >= 1/4 + 1/(2gamma)', sp.simplify((1/g_ + a)/2 - (sp.Rational(1, 4) + 1/(2*g_))) == 0)
print('ALL', all(R), len(R), flush=True)
