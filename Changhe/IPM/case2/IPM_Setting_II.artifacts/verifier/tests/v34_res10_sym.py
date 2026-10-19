"""V34: referee result 10 (22:39Z) identities, own sympy derivations (no referee result 10 code)."""
import sympy as sp
s, y, r, th, p, t = sp.symbols('s y r theta p t', real=True)
out = []
def chk(name, e):
    v = sp.simplify(sp.Matrix(e)) if isinstance(e, list) else sp.simplify(e)
    v = (v == sp.zeros(*v.shape)) if isinstance(v, sp.MatrixBase) else v
    out.append((name, v)); print(name, ':', v, flush=True)
X = sp.Function('X')(s, y); v = sp.Function('v')(s, y); F = sp.Function('F')(s); h = sp.Function('h')(s)
# 2. graph reduction: Y = v (X_y, 1); d_x = X_s^-1 d_s, d_y^phys = d_y - (X_y/X_s) d_s
dx = lambda g: sp.diff(g, s)/sp.diff(X, s)
dyp = lambda g: sp.diff(g, y) - sp.diff(X, y)/sp.diff(X, s)*sp.diff(g, s)
Y1, Y2 = v*sp.diff(X, y), v
div = dx(Y1) + dyp(Y2)
chk('2 div Y - (1/X_s) d_y(X_s v)', div - sp.diff(sp.diff(X, s)*v, y)/sp.diff(X, s))
curl = dx(Y2) - dyp(Y1)
vy = (2*sp.diff(X, s) - sp.diff(X, s, y)*v)/sp.diff(X, s)      # from div Y = 2
lhs = (1 + sp.diff(X, y)**2)*sp.diff(v, s) + (2*sp.diff(X, y)*sp.diff(X, s, y) - sp.diff(X, s)*sp.diff(X, y, 2))*v - 2*sp.diff(X, s)*sp.diff(X, y)
chk('2 X_s (curl Y) - lhs (div Y = 2 used)', sp.expand(X.diff(s)*curl).subs(sp.Derivative(v, y), vy) - lhs)
chk('2 X_s * f_x = F\'', sp.diff(X, s)*dx(F) - sp.diff(F, s))
chk('2 Y.grad f = 0 (f = F(s))', Y1*dx(F) + Y2*dyp(F))
# arc traces: X(s, h(s)) = s, v(s, h(s)) = 0, v_y = 2 there; curl eq at v = 0
Xs, Xy, hp, Fp = sp.symbols('X_s X_y hp Fp')
cl = {Xy: Fp/2 - hp, Xs: 1 + hp**2 - Fp*hp/2}
chk('2 arc traces satisfy X_s + X_y h\' = 1 and the curl eq at v = 0 (v_s = -2h\')',
    [sp.expand((Xs + Xy*hp - 1).subs(cl)), sp.expand(((1 + Xy**2)*(-2*hp) - 2*Xs*Xy + Fp).subs(cl))])
# 3. example trace F = s^2 - s^4 + s^6/3
Fe = s**2 - s**4 + s**6/3
chk('3 F(1) - 1/3, F\'(1), F\'\'(1)', [Fe.subs(s, 1) - sp.Rational(1, 3), sp.diff(Fe, s).subs(s, 1), sp.diff(Fe, s, 2).subs(s, 1)])
chk('3 F\' = 2 s (1 - s^2)^2', sp.factor(sp.diff(Fe, s)) - 2*s*(1 - s**2)**2)
# 4. exterior at fixed p: psi = r^{p+1} Phi, -Lap psi = d_x(r^p A); correction g = r^{2p-1} G solves Z.grad g - p g = -W.grad(r^p A)
A = sp.Function('A')(th); Phi = sp.Function('Phi')(th)
psi = r**(p + 1)*Phi
lap = sp.diff(psi, r, 2) + sp.diff(psi, r)/r + sp.diff(psi, th, 2)/r**2
dxA = sp.cos(th)*sp.diff(r**p*A, r) - sp.sin(th)/r*sp.diff(r**p*A, th)
chk('4 -Lap psi - d_x(r^p A) with Phi\'\' + (1+p)^2 Phi = sin A\' - p cos A',
    sp.expand((-lap - dxA)/r**(p - 1)).subs(sp.Derivative(Phi, (th, 2)), sp.sin(th)*A.diff(th) - p*sp.cos(th)*A - (1 + p)**2*Phi))
J = lambda a, b: (sp.diff(a, r)*sp.diff(b, th) - sp.diff(a, th)*sp.diff(b, r))/r      # W.grad b, W = (-psi_y, psi_x)
WgA = J(psi, r**p*A)
g = r**(2*p - 1)/(1 - p)*((1 + p)*Phi*A.diff(th) - p*Phi.diff(th)*A)
chk('4 Z.grad g - p g + W.grad(r^p A)', sp.simplify(r*sp.diff(g, r) - p*g + WgA))
# 4. moment law: Z.grad phi = -3 phi for phi = r^-3 sin 3th, div Z = 2  =>  int (Z.grad g - p g) phi = (1 - p) int g phi
phi = r**-3*sp.sin(3*th)
chk('4 Z.grad phi + 3 phi', r*sp.diff(phi, r) + 3*phi)
# 4. scaled trial g_a(Z) = a^2 f(Z/a): c scales by a, Q by a^2; Q - pi (1-p)(1-p/2) at c[f] = 1, Q[f] = pi
a = 1 - p/2
chk('4 pi a^2 - pi (1-p) a - pi p (1 - p/2)/2', sp.pi*a**2 - sp.pi*(1 - p)*a - sp.pi*p*(1 - p/2)/2)
# transport residual at Z = a xi, using (xi + W).grad f = 0: a^2 xi.grad f + a^3 W.grad f - p a^2 f
xg, f0 = sp.symbols('xig f')     # xig = xi.grad f
chk('4 residual - p a^2 (xig/2 - f)', a**2*xg + a**3*(-xg) - p*a**2*f0 - p*a**2*(xg/2 - f0))
# 4. area chart: det(z_s, z_t) = 1, f = F(s), B = p a z_s + (2 - p a') t z_t
aa = sp.Function('a')(s)
chk('4 div B (unit Jacobian) - 2', sp.diff(p*aa, s) + sp.diff((2 - p*aa.diff(s))*t, t) - 2)
tt = sp.Function('T')(s)
ch = tt.diff(s) - (2 - p*aa.diff(s))*tt/(p*aa)
Fs = sp.Function('F')(s)
cand = aa.subs(s, s)  # characteristic t(s) = C F^{2/p}/a with a = F/F'
tsol = Fs**(2/p)/(Fs/Fs.diff(s))
chk('4 characteristic t = C F^{2/p}/a', sp.simplify((tsol.diff(s) - (2 - p*sp.diff(Fs/Fs.diff(s), s))*tsol/(p*Fs/Fs.diff(s)))))
bad = [n for n, v in out if not (v == 0 or v is True or (isinstance(v, list) and all(sp.simplify(w) == 0 for w in v)))]
print('ALL', len(out), 'checks; nonzero:', bad)
