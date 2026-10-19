# V135: symbolic checks of draft FR 9.7 (Proposition 3.15 uniqueness), independent of the lead's prop315_check.py.
import sympy as sp
ok = []
def chk(name, cond):
    ok.append(bool(cond)); print(('OK  ' if cond else 'FAIL ') + name)
x, y = sp.symbols('x y', real=True)
l = sp.symbols('l', positive=True)
beta = 2*l - sp.Rational(1, 2)
f = sp.Function('f'); s = sp.Function('s')
rho = x**2*f(y); psi = x*s(y)
W = sp.Matrix([-sp.diff(psi, y), sp.diff(psi, x)])
V = sp.Matrix([l*x, l*y]) + W
lap = sp.diff(psi, x, 2) + sp.diff(psi, y, 2)
chk('Step 1: -Lap psi - rho_x = -x (s\'\' + 2 f)', sp.simplify(-lap - sp.diff(rho, x) + x*(sp.diff(s(y), y, 2) + 2*f(y))) == 0)
b = l*y + s(y)
tr = V[0]*sp.diff(rho, x) + V[1]*sp.diff(rho, y) - rho
chk('Step 1: V1 = x(2l - b\'), V2 = b', sp.simplify(V[0] - x*(2*l - sp.diff(b, y))) == 0 and sp.simplify(V[1] - b) == 0)
chk('Step 1: V.grad rho - rho = x^2 [b f\' - 2(b\' - beta) f]', sp.simplify(tr - x**2*(b*sp.diff(f(y), y) - 2*(sp.diff(b, y) - beta)*f(y))) == 0)
chk('beta - l = l - 1/2 and 2l - beta = 1/2', sp.simplify(beta - l - (l - sp.Rational(1, 2))) == 0 and sp.simplify(2*l - beta) == sp.Rational(1, 2))
# b-equation with f = -b''/2
B = sp.Function('B')(y)
b1, b2, b3 = [sp.diff(B, y, k) for k in (1, 2, 3)]
fe = -b2/2
teq = B*sp.diff(fe, y) - 2*(b1 - beta)*fe
chk('transport with f = -b\'\'/2 is -(1/2)[b b\'\'\' - 2(b\' - beta) b\'\']', sp.simplify(teq + (B*b3 - 2*(b1 - beta)*b2)/2) == 0)
E = B*b2 - (3*b1**2 - 4*beta*b1)/2
Ep = sp.diff(E, y).subs(sp.Derivative(B, (y, 3)), 2*(b1 - beta)*b2/B)
chk('Step 2: E\' = 0 on solutions', sp.simplify(Ep) == 0)
chk('Step 2: E(0) = beta^2/2 with b(0) = 0, b\'(0) = beta', sp.simplify((0 - (3*beta**2 - 4*beta*beta)/2) - beta**2/2) == 0)
p1 = sp.symbols('p1')
chk('Step 2: beta^2/2 + (3p^2 - 4 beta p)/2 = (3p - beta)(p - beta)/2', sp.expand(beta**2/2 + (3*p1**2 - 4*beta*p1)/2 - (3*p1 - beta)*(p1 - beta)/2) == 0)
vv = sp.symbols('v')
chk('Step 2: (3b\' - beta)(b\' - beta)/2 = (beta + 3v/2) v with v = b\' - beta', sp.expand(((3*(vv + beta) - beta)*vv)/2 - (beta + 3*vv/2)*vv) == 0)
chk('Step 3: partial fractions', sp.simplify((beta + vv)/(vv*(beta + 3*vv/2)) - (1/vv - sp.Rational(1, 2)/(beta + 3*vv/2))) == 0)
chk('Step 3: d/dv[log v - log(beta + 3v/2)/3] = (beta + v)/(v (beta + 3v/2))', sp.simplify(sp.diff(sp.log(vv) - sp.log(beta + 3*vv/2)/3, vv) - (beta + vv)/(vv*(beta + 3*vv/2))) == 0)
G = vv*(beta + 3*vv/2)**sp.Rational(-1, 3)
chk('Step 3: G\'(v) = (beta + v)(beta + 3v/2)^(-4/3)', sp.simplify(sp.diff(G, vv) - (beta + vv)*(beta + 3*vv/2)**sp.Rational(-4, 3)) == 0)
chk('Step 3: G\'(0) = beta^(-1/3)', sp.simplify(sp.diff(G, vv).subs(vv, 0) - beta**sp.Rational(-1, 3)) == 0)
chk('Step 3: K = (2/beta) beta^(-1/3) = 2 beta^(-4/3)', sp.simplify(2/beta*beta**sp.Rational(-1, 3) - 2*beta**sp.Rational(-4, 3)) == 0)
# explicit solution, y > -beta
yy = sp.symbols('yy', positive=True)   # yy = beta + y > 0
bs = beta*yy/3 - beta**4/(3*yy**2)
fs = (beta/yy)**4
d = lambda e, k=1: sp.diff(e, yy, k)
chk('explicit: b(0) = 0 (yy = beta)', sp.simplify(bs.subs(yy, beta)) == 0)
chk('explicit: b\'(0) = beta', sp.simplify(d(bs).subs(yy, beta) - beta) == 0)
chk('explicit: f = -b\'\'/2', sp.simplify(fs + d(bs, 2)/2) == 0)
chk('explicit: f(0) = 1', sp.simplify(fs.subs(yy, beta) - 1) == 0)
chk('explicit: transport b f\' = 2(b\' - beta) f', sp.simplify(bs*d(fs) - 2*(d(bs) - beta)*fs) == 0)
chk('explicit: b b\'\' = (3b\' - beta)(b\' - beta)/2', sp.simplify(bs*d(bs, 2) - (3*d(bs) - beta)*(d(bs) - beta)/2) == 0)
t = beta/yy
vs = d(bs) - beta
chk('explicit: v = (2 beta/3)(t^3 - 1)', sp.simplify(vs - 2*beta/3*(t**3 - 1)) == 0)
chk('explicit: beta + 3v/2 = beta t^3', sp.simplify(beta + 3*vs/2 - beta*t**3) == 0)
chk('explicit: b = (beta^2/3)(1/t - t^2)', sp.simplify(bs - beta**2/3*(1/t - t**2)) == 0)
# (beta t^3)^(-1/3) = beta^(-1/3)/t for beta, t > 0; check with a positive symbol in place of beta, then at sample values
Bp, tp = sp.symbols('Bp tp', positive=True)
Gt = (2*Bp/3)*(tp**3 - 1)*(Bp*tp**3)**sp.Rational(-1, 3)
bt = Bp**2/3*(1/tp - tp**2)
chk('explicit: G(v) = -2 beta^(-4/3) b (beta, t > 0)', sp.simplify(Gt + 2*Bp**sp.Rational(-4, 3)*bt) == 0)
Gs = vs*(beta + 3*vs/2)**sp.Rational(-1, 3)
chk('explicit: G(v_*(y)) + 2 beta^(-4/3) b_*(y) = 0 at sample (l, y)', all(abs(sp.N((Gs + 2*beta**sp.Rational(-4, 3)*bs).subs({l: lv, yy: beta.subs(l, lv) + yv}))) < 1e-12 for lv in (sp.Rational(11, 10), 2, 5) for yv in (-sp.Rational(1, 2), sp.Rational(1, 3), 4)))
# remark: (G(v)/b)' = 0 using b v' = (beta + 3v/2) v and b' = beta + v
bb, vp = sp.symbols('bb vp')
num = sp.diff(G, vv)*vp*bb - G*(beta + vv)
chk('remark: G\'(v) v\' b - G(v) b\' = 0 when b v\' = (beta + 3v/2) v', sp.simplify(num.subs(vp, (beta + 3*vv/2)*vv/bb)) == 0)
# zeros of b_*: only yy = beta (y = 0) on yy > 0
chk('b_* = 0 iff (beta + y)^3 = beta^3', sp.simplify(sp.factor(sp.together(bs*3*yy**2/beta)) - (yy**3 - beta**3)) == 0)
# limit at -beta
chk('b_* -> -inf and f_* -> inf as y -> -beta+', sp.limit(bs.subs(l, 1), yy, 0, '+') == -sp.oo and sp.limit(fs.subs(l, 1), yy, 0, '+') == sp.oo)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
