# V166: checks of the formulas changed by item 26 (ref6 corrections). Own code.
import sympy as sp, mpmath as mp
ok = []
def chk(name, cond, info=''):
    ok.append(bool(cond)); print(('OK  ' if cond else 'FAIL'), name, info)
p, eps, r, th, l = sp.symbols('p epsilon r theta l', positive=True)
# R1: kappa c = l - 1 with c = 1/p - 1/2, kappa = 2(1-p)/(2-p); kappa/(1-p) -> 2 as p -> 1
kap = 2*(1-p)/(2-p); c = 1/p - sp.Rational(1, 2)
chk('R1 kappa*c = 1/p - 1', sp.simplify(kap*c - (1/p - 1)) == 0)
chk('R1 kappa/(1-p) -> 2', sp.limit(kap/(1-p), p, 1) == 2)
# R1 two-sided bound: f_n -> f uniformly, ||f|| > 0 => ||f||/2 <= ||f_n|| <= 2||f|| eventually (triangle inequality)
# (no computation needed; recorded)
# R1 limit equation: Psi'' + (p+1)^2 Psi = sin A' - p cos A at p = 1
A = sp.Function('A')(th); Ps = sp.Function('Psi')(th)
lhs = sp.diff(Ps, th, 2) + (p+1)**2*Ps - (sp.sin(th)*sp.diff(A, th) - p*sp.cos(th)*A)
chk('R1 limit equation at p = 1', sp.simplify(lhs.subs(p, 1) - (sp.diff(Ps, th, 2) + 4*Ps - sp.sin(th)*sp.diff(A, th) + sp.cos(th)*A)) == 0)
# Proposition 4.7 proof constants: Psi = C A^2 near a zero beta, A = a t^2 + b t^3 + ...
t, a, b, C, be = sp.symbols('t a b C beta', real=True)
Aser = a*t**2 + b*t**3
Pser = C*Aser**2
res = sp.diff(Pser, t, 2) + 4*Pser - (sp.sin(be+t)*sp.diff(Aser, t) - sp.cos(be+t)*Aser)
ser = sp.series(res, t, 0, 3).removeO()
c1 = sp.simplify(ser.coeff(t, 1)); c2 = sp.simplify(ser.coeff(t, 2).subs(sp.sin(be), 0))
chk('4.7 order t: -2a sin(beta)', sp.simplify(c1 + 2*a*sp.sin(be)) == 0, str(c1))
sol = sp.solve(sp.Eq(c2.subs(be, 0), 0), C); sol2 = sp.solve(sp.Eq(c2.subs(be, sp.pi), 0), C)
chk('4.7 C = cos(beta)/(12a) at 0 and pi', sol == [1/(12*a)] and sol2 == [-1/(12*a)], str((sol, sol2)))
# R3a: crossover scale and counterexample
Rs = eps**(-2/eps)
chk('R3a eps^-2 R_*^-eps = 1', sp.simplify(eps**-2*Rs**(-eps) - 1) == 0)
val = sp.simplify(eps**-2*(Rs/eps)**(-eps))
chk('R3a r = R_*/eps gives eps^eps', sp.simplify(val - eps**eps) == 0, str(val))
chk('R3a eps^eps -> 1', sp.limit(eps**eps, eps, 0, '+') == 1)
chk('R3a r/R_* = 1/eps -> infinity, eps log r - 2 log(1/eps) = eps log(1/eps) -> 0',
    sp.limit(eps*sp.log(Rs/eps) - 2*sp.log(1/eps), eps, 0, '+') == 0)
for cl, ref in [(2, 16), (sp.Rational(3, 2), 7e2), (sp.Rational(5, 4), 1e7), (sp.Rational(11, 10), 8e22)]:
    e = 1 - 1/sp.Integer(1)/cl
    v = float(e**(-2/e))
    chk('R3a R_* at c_l = %s' % cl, abs(v/ref - 1) < 0.08 or (ref == 16 and v == 16), '%.6g' % v)
# O3: div(rho phi V) = (1 - l) rho phi + rho W.grad phi given V.grad rho = rho, div V = 2l, V = lX + W
x, y = sp.symbols('x y', real=True)
rho = sp.Function('rho')(x, y); W1 = sp.Function('W1')(x, y); W2 = sp.Function('W2')(x, y)
phi = (3*x**2*y - y**3)/(x**2 + y**2)**3   # r^{-3} sin 3 th
chk('O3 phi = r^-3 sin 3th', sp.simplify(phi.subs({x: r*sp.cos(th), y: r*sp.sin(th)}) - sp.sin(3*th)/r**3) == 0)
chk('O3 X.grad phi = -3 phi', sp.simplify(x*sp.diff(phi, x) + y*sp.diff(phi, y) + 3*phi) == 0)
V1 = l*x + W1; V2 = l*y + W2
div = sp.diff(rho*phi*V1, x) + sp.diff(rho*phi*V2, y)
Vgr = V1*sp.diff(rho, x) + V2*sp.diff(rho, y); divV = sp.diff(V1, x) + sp.diff(V2, y)
expr = div - ((1 - l)*rho*phi + rho*(W1*sp.diff(phi, x) + W2*sp.diff(phi, y))) - phi*(Vgr - rho) - rho*phi*(divV - 2*l)
chk('O3 identity (exact, modulo the two equations)', sp.simplify(sp.expand(expr)) == 0)
# O3 boundary term: int_{eps<r<R} div(F) = R G(R) - eps G(eps), G(s) = int F_r(s, th) dth; for F = rho phi V,
# s G(s) = s^{-2} int rho V_r sin 3th dth, so the inner term is B_eps and N_eps + B_eps = (l - 1) I_eps
mp.mp.dps = 20
lv = mp.mpf('1.3')
def rhof(X, Y): return X*X*mp.exp(-(X-0.3)**2 - (Y+0.2)**2) + 0.1*Y*X*mp.exp(-X*X-Y*Y)
def Wf(X, Y): return (mp.sin(Y)*mp.exp(-X*X-Y*Y), X*Y*mp.exp(-X*X-2*Y*Y))
def F(X, Y):
    rh = rhof(X, Y); R2 = X*X + Y*Y; ph = (3*X*X*Y - Y**3)/R2**3; w = Wf(X, Y)
    return (rh*ph*(lv*X + w[0]), rh*ph*(lv*Y + w[1]))
def divF(X, Y, h=mp.mpf('1e-6')):
    return (F(X+h, Y)[0] - F(X-h, Y)[0])/(2*h) + (F(X, Y+h)[1] - F(X, Y-h)[1])/(2*h)
e0, R0 = mp.mpf('0.5'), mp.mpf('3')
bulk = mp.quad(lambda s, a: s*divF(s*mp.cos(a), s*mp.sin(a)), [e0, R0], [0, 2*mp.pi])
def bnd(s):
    return mp.quad(lambda a: s*(F(s*mp.cos(a), s*mp.sin(a))[0]*mp.cos(a) + F(s*mp.cos(a), s*mp.sin(a))[1]*mp.sin(a)), [0, 2*mp.pi])
Beps = mp.quad(lambda a: e0**-2*rhof(e0*mp.cos(a), e0*mp.sin(a))*((lv*e0*mp.cos(a) + Wf(e0*mp.cos(a), e0*mp.sin(a))[0])*mp.cos(a)
       + (lv*e0*mp.sin(a) + Wf(e0*mp.cos(a), e0*mp.sin(a))[1])*mp.sin(a))*mp.sin(3*a), [0, 2*mp.pi])
chk('O3 inner boundary term equals B_eps', abs(bnd(e0) - Beps) < 1e-12, mp.nstr(Beps, 12))
chk('O3 divergence theorem: bulk = outer - B_eps', abs(bulk - (bnd(R0) - Beps)) < 1e-6, mp.nstr(bulk - (bnd(R0) - Beps), 3))
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
