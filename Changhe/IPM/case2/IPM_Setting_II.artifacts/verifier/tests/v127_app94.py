# Symbolic checks for the FR 9.4 draft (26e952bd): exponent identities, A'' and B' at a zero, the chart (xi, y) at 0,
# the axis reduction, the log-derivative of h |y|^(2-p), (b h)' and the S_1 bounds; own code, sympy.
import sympy as sp
ok = 0
def chk(name, e):
    global ok
    e = sp.simplify(e)
    print(name, 'OK' if e == 0 else 'FAIL ' + str(e)); ok += (e == 0)
l = sp.symbols('l', positive=True); p = 1/l; lam = l - 1; b0 = 2*l - sp.Rational(1, 2)
chk('(1-p)/lam = p', (1 - p)/lam - p)
chk('lam/(1-p) = l', lam/(1 - p) - l)
chk('(1-p) l = lam', (1 - p)*l - lam)
chk('l(p-2) = 1-2l', l*(p - 2) - (1 - 2*l))
chk('b - l = l - 1/2', b0 - l - (l - sp.Rational(1, 2)))
chk('-l s + l p s = -lam s', sp.Symbol('s')*(-l + l*p + lam))
# Step 2: (A o Theta)'' at a zero of q; B = L^(-p/2) q o Theta^-1
a = sp.symbols('a'); q = sp.Function('q')(a); L = sp.Function('L')(a); Th = sp.Function('Theta')(a)
A2, A1 = sp.symbols('A2 A1')
lhs = sp.diff(L**(-p)*q**2, a, 2)          # = A''(Th) Th'^2 + A'(Th) Th''
Q1, Q2 = sp.symbols('Q1 Q2')
def atzero(e): return e.subs(q.diff(a, 2), Q2).subs(q.diff(a), Q1).subs(q, 0)
A2val = atzero(lhs)/Th.diff(a)**2          # A'(theta_j) = 0
chk("A''(theta_j) = 2 L^-p q'^2/Theta'^2", A2val - 2*L**(-p)*Q1**2/Th.diff(a)**2)
Bp = atzero(sp.diff(L**(-p/2)*q, a))/Th.diff(a)
chk("B'(theta_j) = L^(-p/2) q'/Theta'", Bp - L**(-p/2)*Q1/Th.diff(a))
# Step 6: rho = |S|^p A(arg S) and xi = |S|^(p/2) B(arg S) at X = P(a, s)
s = sp.symbols('s', real=True); Lp = sp.symbols('Lp', positive=True); qa = sp.symbols('qa', real=True)
absS = sp.exp(l*s)*Lp
chk('rho formula', absS**p*Lp**(-p)*qa**2 - sp.exp(s)*qa**2)
chk('xi formula', absS**(p/2)*Lp**(-p/2)*qa - sp.exp(s/2)*qa)
# chart (u, v) = (xi, y): xi(chi(u,v), v) = u with xi = x + c20 x^2 + c11 x y + c02 y^2 (xi_y(0) = 0); chi_v(0,0) = 0
x, y, u, v = sp.symbols('x y u v'); c20, c11, c02 = sp.symbols('c20 c11 c02')
xi = x + c20*x**2 + c11*x*y + c02*y**2
k1, k2 = sp.symbols('k1 k2')                # chi = u + k1 v + ... ; first order
lin = sp.expand(xi.subs({x: u + k1*v, y: v})); k1v = sp.solve(sp.Poly(lin, u, v).coeff_monomial(v), k1)[0]
chk('chi_v(0,0) = 0', k1v)
# g(u, v) = V_2(chi(u,v), v) with V_2 = b0 y + d20 x^2 + d11 x y + d02 y^2 (DV(0) = diag(1/2, b0)): Dg(0,0) = (0, b0)
d20, d11, d02 = sp.symbols('d20 d11 d02')
g = (b0*y + d20*x**2 + d11*x*y + d02*y**2).subs({x: u, y: v})   # chi = u + O(2) at first order
chk('g_u(0,0) = 0', sp.diff(g, u).subs({u: 0, v: 0}))
chk('g_v(0,0) = b', sp.diff(g, v).subs({u: 0, v: 0}) - b0)
# Step 7: axis reduction of V.grad rho = rho at order x^2
h, hp, bb, bp = sp.symbols('h hp bb bp'); k4 = sp.symbols('k4')
rho = x**2*h/2; rho_y = x**2*hp/2; V1 = x*(2*l - bp); V2 = bb
eq = sp.expand(V1*sp.diff(rho, x) + V2*rho_y - rho)
chk('b h\' = (1 - 4l + 2b\') h', sp.solve(eq.coeff(x, 2), hp)[0] - (1 - 4*l + 2*bp)*h/bb)
# log-derivative of h |y|^(2-p) on a tail, with b = l y + w
w, wp = sp.symbols('w wp'); yy = sp.symbols('yy', positive=True)
bv = l*yy + w; bpv = l + wp
dlog = (1 - 4*l + 2*bpv)/bv + (2 - p)/yy
chk('dlog(h y^(2-p)) = (2 y w\' - (p-2) w)/(y(ly+w))', dlog - (2*yy*wp - (p - 2)*w)/(yy*(l*yy + w)))
# (b h)' = (1 - l + 3 w') h
chk("(bh)' = (1-l+3w')h", (bpv*h + bv*((1 - 4*l + 2*bpv)*h/bv)) - (1 - l + 3*wp)*h)
# integrated identity: 0 = (1-l) int h + 3 int h w'
Ih = sp.symbols('Ih', positive=True)
chk('int h w\' = (l-1)/3 int h', sp.solve(sp.Eq(0, (1 - l)*Ih + 3*sp.Symbol('Ihw')), sp.Symbol('Ihw'))[0] - (l - 1)/3*Ih)
# exponents: b h = O(|y|^(p-1)), h w' = O(|y|^(2p-3)), 2p-3 < -1 iff p < 1
chk('exponent of h w\'', (p - 2) + (p - 1) - (2*p - 3))
# |y| < r/2 => |x| > (sqrt 3/2) r
r = sp.symbols('r', positive=True)
chk('x^2 > 3 r^2/4 at |y| = r/2', (r**2 - (r/2)**2) - sp.Rational(3, 4)*r**2)
print('ALL OK', ok)
