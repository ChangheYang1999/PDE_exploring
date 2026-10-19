"""V27 (audit of referee result 8), symbolic parts (sympy; own derivations, no lead code).
Each check prints its name and a residual that must simplify to 0 (or True)."""
import sympy as sp

x, y, r, th, s, t, p, a, eps, L, u, v = sp.symbols('x y r theta s t p a epsilon L u v', real=True)
out = []
def chk(name, expr):
    val = sp.simplify(expr)
    out.append((name, val)); print(name, ':', val, flush=True)

# 1. Lyapunov identity (5): grad P = Y + f e2, L = P - y f  =>  Y.grad L = |Y|^2 - y Y.grad f  (= |Y|^2 when Y.grad f = 0)
f = sp.Function('f')(x, y); P = sp.Function('P')(x, y)
Y1 = sp.diff(P, x); Y2 = sp.diff(P, y) - f
Lf = P - y*f
chk('(5) Y.grad(P - y f) - |Y|^2 + y Y.grad f', Y1*sp.diff(Lf, x) + Y2*sp.diff(Lf, y) - (Y1**2 + Y2**2) + y*(Y1*sp.diff(f, x) + Y2*sp.diff(f, y)))
chk('(5) curl(grad P - f e2) + f_x', sp.diff(Y2, x) - sp.diff(Y1, y) + sp.diff(f, x))
chk('(14) div(grad P - f e2) - (Lap P - f_y)', sp.diff(Y1, x) + sp.diff(Y2, y) - (sp.diff(P, x, 2) + sp.diff(P, y, 2) - sp.diff(f, y)))

# 2. DY(0) from the quadratic jet: Y = A Z + o, f = x^2 + o; transport at order 2, div 2, curl -f_x(0) = 0
A11, A12, A21, A22 = sp.symbols('A11 A12 A21 A22')
tr2 = sp.Poly(sp.expand((A11*x + A12*y)*2*x), x, y).coeffs()
sol = sp.solve(tr2 + [A11 + A22 - 2, A21 - A12], [A11, A12, A21, A22], dict=True)
chk('DY(0) = diag(0, 2)', sol == [{A11: 0, A12: 0, A21: 0, A22: 2}])

# 3. (2)/(11): frame (t, n), DY = [[0, alpha], [0, 2]] (columns DY t = 0, DY n = alpha t + 2 n); curl = -alpha;
#    DY^T grad f = 0 with grad f = F' t + beta n gives beta = -alpha F'/2; (12) in fixed coordinates.
phi, Fp, al, be = sp.symbols('phi Fp alpha beta', real=True)
tv = sp.Matrix([sp.cos(phi), sp.sin(phi)]); nv = sp.Matrix([-sp.sin(phi), sp.cos(phi)])
Rm = sp.Matrix.hstack(tv, nv)
DY = Rm*sp.Matrix([[0, al], [0, 2]])*Rm.T
chk('(2) trace DY - 2', DY.trace() - 2)
chk('(2) curl DY + alpha', (DY[1, 0] - DY[0, 1]) + al)
g = Fp*tv + be*nv
bsol = sp.solve((DY.T*g)[0], be)[0]
chk('(2) beta + alpha F\'/2', bsol + al*Fp/2)
chk('(2) DY^T grad f = 0 (2nd comp.)', (DY.T*(Fp*tv + bsol*nv))[1])
fx = (Fp*tv + bsol*nv)[0]          # with alpha = f_x: f_x = F' cos phi + f_x F' sin phi/2
chk('(12) f_x(1 - F\' sin phi/2) - F\' cos phi at alpha = f_x', sp.solve(sp.Eq(al, fx.subs(al, al)), al)[0]*(1 - Fp*sp.sin(phi)/2) - Fp*sp.cos(phi))

# 4. endpoint flatness: leading transport 2 v d_v P_m = 0 forces P_m = a u^m (m = 2..5, generic homogeneous P_m)
for m in range(2, 6):
    cs = sp.symbols('k0:%d' % (m + 1))
    Pm = sum(cs[j]*u**(m - j)*v**j for j in range(m + 1))
    cond = sp.Poly(sp.expand(2*v*sp.diff(Pm, v)), u, v).coeffs()
    sl = sp.solve(cond, cs[1:], dict=True)
    chk('(3) m=%d: 2v dP/dv = 0 => only u^m survives' % m, all(sl[0][c] == 0 for c in cs[1:]))

# 5. exterior: Psi'' + Psi = sin th A' - 2Q solvable; psi_ext = r log r Q + r Psi solves -Lap psi = d_x A(th);
#    grad^perp psi_ext = C_A log r + B, C_A = (b2/2, -a2/2), B = -Psi' e_r + (Psi + Q) e_th.  A: trig polynomial, generic.
cA = sp.symbols('c0:6'); sA = sp.symbols('s1:6')
A = cA[0] + sum(cA[k]*sp.cos(k*th) + sA[k - 1]*sp.sin(k*th) for k in range(1, 6))
a2 = sp.integrate(A*sp.cos(2*th), (th, 0, 2*sp.pi))/sp.pi; b2 = sp.integrate(A*sp.sin(2*th), (th, 0, 2*sp.pi))/sp.pi
Qth = -(a2*sp.cos(th) + b2*sp.sin(th))/2
rhs = sp.expand(sp.sin(th)*sp.diff(A, th) - 2*Qth)
chk('(12) solvability cos', sp.integrate(rhs*sp.cos(th), (th, 0, 2*sp.pi)))
chk('(12) solvability sin', sp.integrate(rhs*sp.sin(th), (th, 0, 2*sp.pi)))
rhs_f = sp.fu(sp.expand(sp.expand_trig(rhs)))
# solve mode by mode: Psi = sum_k (alpha_k cos k th + beta_k sin k th)/(1 - k^2), k != 1
Psi = 0
for k in [0] + list(range(2, 8)):
    ck = sp.integrate(rhs*sp.cos(k*th), (th, 0, 2*sp.pi))/(sp.pi*(2 if k == 0 else 1))
    sk = sp.integrate(rhs*sp.sin(k*th), (th, 0, 2*sp.pi))/sp.pi
    Psi += (ck*sp.cos(k*th) + sk*sp.sin(k*th))/(1 - k**2)
chk('(12) Psi\'\' + Psi - rhs', sp.expand(sp.diff(Psi, th, 2) + Psi - rhs).rewrite(sp.exp).expand().simplify())
psi = r*sp.log(r)*Qth + r*Psi
lap = sp.diff(psi, r, 2) + sp.diff(psi, r)/r + sp.diff(psi, th, 2)/r**2
dxA = -sp.sin(th)*sp.diff(A, th)/r            # d_x of a degree-0 function A(th)
chk('(12) -Lap psi_ext - d_x A', sp.simplify(sp.expand(-lap - dxA).rewrite(sp.exp).expand()))
# velocity grad^perp psi = (-psi_y, psi_x): in polar, e_r comp. = -psi_th/r, e_th comp. = psi_r
Wr = -sp.diff(psi, th)/r; Wt = sp.diff(psi, r)
W1 = Wr*sp.cos(th) - Wt*sp.sin(th); W2 = Wr*sp.sin(th) + Wt*sp.cos(th)
Br = -sp.diff(Psi, th); Bt = Psi + Qth
B1 = Br*sp.cos(th) - Bt*sp.sin(th); B2 = Br*sp.sin(th) + Bt*sp.cos(th)
chk('(12) W1 - (b2/2) log r - B1', sp.simplify(sp.expand(W1 - b2/2*sp.log(r) - B1).rewrite(sp.exp).expand()))
chk('(12) W2 + (a2/2) log r - B2', sp.simplify(sp.expand(W2 + a2/2*sp.log(r) - B2).rewrite(sp.exp).expand()))

# 6. no exact degree-0 exterior: w_th = 0, w_r = C(th)/r => curl w = -C'(th)/r^2 (polar curl (1/r)(d_r(r w_th) - d_th w_r))
Cf = sp.Function('C')(th)
chk('(exact exterior) curl of (C/r) e_r + C\'/r^2', (sp.diff(r*0, r) - sp.diff(Cf/r, th))/r + sp.diff(Cf, th)/r**2)
chk('(exact exterior) d_x A(th) = -sin th A\'/r', sp.simplify(
    (sp.diff(sp.Function('A')(sp.atan2(y, x)), x)).subs({x: r*sp.cos(th), y: r*sp.sin(th)}) + sp.sin(th)*sp.Subs(sp.Derivative(sp.Function('A')(u), u), u, sp.atan2(r*sp.sin(th), r*sp.cos(th))).doit()/r))

# 7. foot coordinates (16): Z = z(s,t), det(z_s, z_t) = 1, Y = 2 t z_t, f = F(s); curl in curvilinear form
xs = sp.Function('X')(s, t); ys = sp.Function('Yc')(s, t); F = sp.Function('F')(s)
J = sp.diff(xs, s)*sp.diff(ys, t) - sp.diff(xs, t)*sp.diff(ys, s)
Ycov_s = 2*t*(sp.diff(xs, t)*sp.diff(xs, s) + sp.diff(ys, t)*sp.diff(ys, s))
Ycov_t = 2*t*(sp.diff(xs, t)**2 + sp.diff(ys, t)**2)
curlY = (sp.diff(Ycov_t, s) - sp.diff(Ycov_s, t))/J         # curl = (1/J)(d_s Y_t - d_t Y_s)
s_x = sp.diff(ys, t)/J                                        # inverse Jacobian
zt = sp.Matrix([sp.diff(xs, t), sp.diff(ys, t)]); zs = sp.Matrix([sp.diff(xs, s), sp.diff(ys, s)])
lhs16 = 2*t*(zt.dot(zt.diff(s)) - zs.dot(zt.diff(t))) - 2*zs.dot(zt) + sp.diff(F, s)*sp.diff(ys, t)
chk('(16) J*(curl Y + f_x) - lhs(16) at J = 1', sp.expand(J*(curlY + sp.diff(F, s)*s_x) - lhs16))
# check the curvilinear curl formula on a concrete map (polar-type, J != 1): Y = 2 t z_t pushed forward, Cartesian curl
X_, Y_ = sp.symbols('X_ Y_')
zmap = {xs: sp.exp(t)*sp.cos(s), ys: sp.exp(t)*sp.sin(s)}
Jc = sp.simplify(J.subs(zmap).doit())
Yvec = 2*t*sp.Matrix([sp.diff(sp.exp(t)*sp.cos(s), t), sp.diff(sp.exp(t)*sp.sin(s), t)])   # = 2 t (X, Y), t = log r
Yc = Yvec.subs({t: sp.log(sp.sqrt(X_**2 + Y_**2)), s: sp.atan2(Y_, X_)})
curl_cart = sp.simplify(sp.diff(Yc[1], X_) - sp.diff(Yc[0], Y_))
curl_curv = sp.simplify((curlY.subs(zmap).doit()).subs({t: sp.log(sp.sqrt(X_**2 + Y_**2)), s: sp.atan2(Y_, X_)}))
chk('(16) curvilinear curl formula vs Cartesian on test map', sp.simplify(curl_cart - curl_curv))
# inverse form: Y = 2 t grad^perp s (when det D(s,t) = 1), curl(2 t grad^perp s) = 2 div(t grad s)
S_ = sp.Function('S')(x, y); T_ = sp.Function('T')(x, y)
Yi = (-2*T_*sp.diff(S_, y), 2*T_*sp.diff(S_, x))
chk('(16) curl(2t grad^perp s) - 2 div(t grad s)', sp.diff(Yi[1], x) - sp.diff(Yi[0], y) - 2*(sp.diff(T_*sp.diff(S_, x), x) + sp.diff(T_*sp.diff(S_, y), y)))
chk('(16) Y.grad t - 2t det D(s,t)', Yi[0]*sp.diff(T_, x) + Yi[1]*sp.diff(T_, y) - 2*T_*(sp.diff(S_, x)*sp.diff(T_, y) - sp.diff(S_, y)*sp.diff(T_, x)))
chk('(16) div Y - 2 det D(s,t)', sp.diff(Yi[0], x) + sp.diff(Yi[1], y) - 2*(sp.diff(S_, x)*sp.diff(T_, y) - sp.diff(S_, y)*sp.diff(T_, x)))

# 8. (18): order-p transport Y.grad g + v.grad f = f at an arc point (Y = 0): v.grad f = F with grad f from (2) => a F' = F
vt, vn, fxs = sp.symbols('v_t v_n f_x')
gradf_dot_v = Fp*vt - fxs*Fp/2*vn
aco = vt - fxs*vn/2
chk('(18) v.grad f - a F\'', sp.expand(gradf_dot_v - aco*Fp))
# slow curve normal displacement: n.(DY eta n + v) = 2 eta + v_n = 0, tangential t.(DY eta n + v) = f_x eta + v_t
eta = sp.solve(2*sp.Symbol('eta') + vn, sp.Symbol('eta'))[0]
chk('(18) eta + v_n/2', eta + vn/2)
chk('(18) tangential coefficient - a', fxs*eta + vt - aco)

# 9. seed (25): mode-3 content and c = L a/(2(1-p)); with L = 4(1-p)(1-p/2), a = 1/2: c = 1 - p/2; cos 3th content 0
Sq = sp.sqrt(L**2 + r**2)
fseed = r**2*sp.cos(th)**2*(1 + r**2/L**2)**((p - 2)/2)*((1 + a*r*sp.sin(th)/Sq)**2 + eps*r**2*sp.cos(th)*sp.sin(th)/(L**2 + r**2))
ang = sp.expand(sp.expand_trig(fseed/((1 + r**2/L**2)**((p - 2)/2))))
im3 = sp.simplify(sp.integrate(ang*sp.sin(3*th), (th, 0, 2*sp.pi))/(2*sp.pi))   # = -Im rho_3/(...): rho_3 = mean(f e^{-3i th})
re3 = sp.simplify(sp.integrate(ang*sp.cos(3*th), (th, 0, 2*sp.pi))/(2*sp.pi))
chk('(25) cos 3th content', re3)
# Im rho_3 = -mean(f sin 3th); c = -2 int Im rho_3 r^-2 dr = 2 int mean(f sin3th) r^-2 dr
integrand = sp.simplify(2*im3*(1 + r**2/L**2)**((p - 2)/2)/r**2)
uu = sp.symbols('uu', positive=True)
cval = sp.integrate(sp.simplify((integrand.subs(r, L*sp.sqrt(uu))*L/(2*sp.sqrt(uu))).subs(L, sp.Symbol('Lp', positive=True))), (uu, 0, sp.oo),
                    conds='none')
cval = sp.simplify(cval.subs(sp.Symbol('Lp', positive=True), L))
chk('(25) c - L a/(2(1-p))', sp.simplify((cval - L*a/(2*(1 - p))).subs(sp.gamma(sp.Rational(3, 2) - p/2), (sp.Rational(1, 2) - p/2)*sp.gamma(sp.Rational(1, 2) - p/2))))
chk('(25) L a/(2(1-p)) - (1 - p/2) at L = 4(1-p)(1-p/2), a = 1/2', sp.simplify((L*a/(2*(1 - p))).subs({L: 4*(1 - p)*(1 - p/2), a: sp.Rational(1, 2)}) - (1 - p/2)))
# (27): r^-p f -> L^{2-p} cos^2 th [(1 + a sin th)^2 + eps cos th sin th]
A27 = L**(2 - p)*sp.cos(th)**2*((1 + a*sp.sin(th))**2 + eps*sp.cos(th)*sp.sin(th))
lim = sp.limit((fseed/r**p).subs({p: sp.Rational(1, 4), L: 3, a: sp.Rational(1, 2), eps: sp.Rational(1, 4), th: sp.Rational(7, 10)}), r, sp.oo)
chk('(27) |tail - A27| < 1e-25 at p=1/4, L=3, th=0.7', sp.Abs(sp.N(lim - A27.subs({p: sp.Rational(1, 4), L: 3, a: sp.Rational(1, 2), eps: sp.Rational(1, 4), th: sp.Rational(7, 10)}), 30)) < sp.Float('1e-25'))

# 10. (26) radial Green formulas: psi_n solves -(psi'' + psi'/r - n^2 psi/r^2) = g_n (test g = r^q e^{-r}... use g = r^k/(1+r^2)^m)
for n, gfun in [(1, r/(1 + r**2)**2), (2, r**2/(1 + r**2)**3), (3, r/(1 + r**2)**3)]:
    sv = sp.symbols('sv', positive=True); rp = sp.symbols('rp', positive=True)
    gs = gfun.subs(r, sv)
    if n == 1:
        psin = sp.Rational(1, 2)*(sp.integrate(sv**2*gs, (sv, 0, rp))/rp - rp*sp.integrate(gs, (sv, 0, rp)))
    else:
        psin = sp.Rational(1, 2*n)*(sp.integrate(sv**(n + 1)*gs, (sv, 0, rp))/rp**n + rp**n*sp.integrate(sv**(1 - n)*gs, (sv, rp, sp.oo)))
    res = sp.simplify(-(sp.diff(psin, rp, 2) + sp.diff(psin, rp)/rp - n**2*psin/rp**2) - gfun.subs(r, rp))
    chk('(26) n=%d radial Green residual' % n, res)
    if n == 1:
        chk('(26) n=1: psi_1/r -> 0 at r -> 0 (zero velocity at origin)', sp.limit(psin/rp, rp, 0))

bad = [n for n, v in out if not (v == 0 or v is True or v == sp.true)]
print('ALL', len(out), 'checks; nonzero:', bad)
