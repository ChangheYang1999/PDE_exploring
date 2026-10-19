"""V144: checks of a working draft (proposed FR 4.4 paragraph; referee result 29 routes, referee audit 27b 5.3).
sympy: the x^2 example (labels, transport, Darcy coupling, commuting fields, strain contractions, material loops),
the label identity X_v o Phi = R grad xi, the oscillatory integrand of d T (pointwise, general V, f, e), the
circulation coefficient identities (Q, Q', grad(r^(p+1) Q) = H + F e_2), the cos^2 / sin^2 angular examples,
the dilation and stationarity remarks.
"""
import sys
import sympy as sp
import mpmath as mp
ok = []
def rep(name, cond, extra=''):
    ok.append(bool(cond)); print(('OK   ' if cond else 'FAIL ') + name + (' ' + str(extra) if extra != '' else ''), flush=True)
x, y, u, v, l = sp.symbols('x y u v l', real=True)
a = sp.Rational(1, 2); b = 2*l - sp.Rational(1, 2); h = 1/(b - 1)
Rm = lambda w: sp.Matrix([-w[1], w[0]])          # R(s, t) = (-t, s)
grad = lambda g: sp.Matrix([sp.diff(g, x), sp.diff(g, y)])
div = lambda F: sp.diff(F[0], x) + sp.diff(F[1], y)
curl = lambda F: sp.diff(F[1], x) - sp.diff(F[0], y)
brk = lambda F, G: G.jacobian([x, y])*F - F.jacobian([x, y])*G   # [F, G] = (F.grad) G - (G.grad) F
Z0 = lambda M: sp.simplify(M) == sp.zeros(*M.shape)
# ---- x^2 example ----
Xm = sp.Matrix([u, v + h*u**2])
rep('E1 h = 1/(b - 1) = 1/(2l - 3/2); det DX = 1', sp.simplify(h - 1/(2*l - sp.Rational(3, 2))) == 0 and sp.simplify(Xm.jacobian([u, v]).det() - 1) == 0)
rho = x**2; V = sp.Matrix([x/2, b*y - x**2]); W = V - l*sp.Matrix([x, y])
NX = sp.Matrix([a*u*sp.diff(Xm[i], u) + b*v*sp.diff(Xm[i], v) for i in range(2)])
rep('E2 N X = V o X', Z0(NX - V.subs({x: Xm[0], y: Xm[1]}, simultaneous=True)))
rep('E3 rho o X = u^2, V.grad rho = rho, div W = 0, curl V = -rho_x, W(0) = 0',
    sp.simplify(rho.subs(x, Xm[0]) - u**2) == 0 and sp.simplify(V.dot(grad(rho)) - rho) == 0 and sp.simplify(div(W)) == 0
    and sp.simplify(curl(V) + sp.diff(rho, x)) == 0 and W.subs({x: 0, y: 0}) == sp.zeros(2, 1))
rep('E4 V + rho e_2 = grad(x^2/4 + (2l - 1/2) y^2/2) (differential Darcy coupling)', Z0(V + sp.Matrix([0, rho]) - grad(x**2/4 + b*y**2/2)))
rep('E5 W = ((1/2 - l) x, (l - 1/2) y - x^2): linear and quadratic terms (W = o(r) fails)', Z0(W - sp.Matrix([(a - l)*x, (l - a)*y - x**2])))
rep('E6 DV(0) = diag(1/2, 2l - 1/2); V = 0 only at 0 (x = 0 forces b y = 0)', Z0(V.jacobian([x, y]).subs({x: 0, y: 0}) - sp.diag(a, b)) and sp.solve(list(V), [x, y], dict=True) == [{x: 0, y: 0}])
# commuting fields as push-forwards of u d_u, v d_v
Phi = sp.Matrix([x, y - h*x**2])
DXm = Xm.jacobian([u, v])
sub = {u: Phi[0], v: Phi[1]}
Y1 = sp.simplify((DXm*sp.Matrix([u, 0])).subs(sub)); Y2 = sp.simplify((DXm*sp.Matrix([0, v])).subs(sub))
rep('E7 Y_1 = (x, 2h x^2), Y_2 = (0, y - h x^2)', Z0(Y1 - sp.Matrix([x, 2*h*x**2])) and Z0(Y2 - sp.Matrix([0, y - h*x**2])))
rep('E8 [V, Y_1] = [V, Y_2] = [Y_1, Y_2] = 0', Z0(brk(V, Y1)) and Z0(brk(V, Y2)) and Z0(brk(Y1, Y2)))
rep('E9 div Y_i = 1, Y_1 rho = 2 rho, Y_2 rho = 0, V = Y_1/2 + (2l - 1/2) Y_2',
    sp.simplify(div(Y1) - 1) == 0 and sp.simplify(div(Y2) - 1) == 0 and sp.simplify(Y1.dot(grad(rho)) - 2*rho) == 0
    and sp.simplify(Y2.dot(grad(rho))) == 0 and Z0(V - Y1/2 - b*Y2))
rep('E10 Y_2 = eta R grad xi with (xi, eta) = Phi', Z0(Y2 - Phi[1]*Rm(grad(Phi[0]))))
# general label identity X_v o Phi = R grad xi for det D Phi = 1
p11, p12, p21, p22 = sp.symbols('p11 p12 p21 p22')
DPhi = sp.Matrix([[p11, p12], [p21, p22]]); inv = DPhi.inv().subs(p11*p22 - p12*p21, 1)
inv1 = sp.simplify(DPhi.adjugate())   # inverse when det = 1
rep('E11 det D Phi = 1: D X = adj(D Phi), so X_u = (eta_y, -eta_x), X_v = (-xi_y, xi_x) = R grad xi',
    Z0(inv1[:, 1] - sp.Matrix([-p12, p11])) and Z0(inv1[:, 0] - sp.Matrix([p22, -p21])))
S1 = (Y1.jacobian([x, y]) + Y1.jacobian([x, y]).T)/2; S2 = (Y2.jacobian([x, y]) + Y2.jacobian([x, y]).T)/2
c1 = sp.factor(sp.expand((V.T*S1*V)[0])); c2 = sp.factor(sp.expand((V.T*S2*V)[0]))
rep('E12 V.S_1 V = x^2 (1/4 + 2hb y - 2h x^2), V.S_2 V = (by - x^2)(by - (1 + h) x^2)',
    sp.simplify(c1 - x**2*(sp.Rational(1, 4) + 2*h*b*y - 2*h*x**2)) == 0 and sp.simplify(c2 - (b*y - x**2)*(b*y - (1 + h)*x**2)) == 0)
sg = True
for lv in [sp.Rational(11, 10), 2, 5]:
    e1 = [c1.subs({l: lv, x: 1, y: yy}) for yy in (-10, 10)]
    bb = b.subs(l, lv); hh = h.subs(l, lv); ymid = (1 + (1 + hh))/(2*bb)
    e2 = [c2.subs({l: lv, x: 1, y: yy}) for yy in (ymid, 10)]
    sg &= (e1[0] < 0 < e1[1]) and (e2[0] < 0 < e2[1])
rep('E13 both contractions take both signs (l = 1.1, 2, 5; x = 1)', sg)
# material label loops: I(t) = oint_{phi_t C} V.dz with C = X(boundary of the unit label disk centred at (2, 1))
def I_direct(t, lv):
    bv = float(b.subs(l, lv)); hv = float(h.subs(l, lv))
    def integrand(s):
        u0, v0 = 2 + mp.cos(s), 1 + mp.sin(s); du, dv = -mp.sin(s), mp.cos(s)
        U, Vv = mp.e**(t/2)*u0, mp.e**(bv*t)*v0; dU, dV = mp.e**(t/2)*du, mp.e**(bv*t)*dv
        xx, yy = U, Vv + hv*U**2; dx, dy = dU, dV + 2*hv*U*dU
        return (xx/2)*dx + (bv*yy - xx**2)*dy
    return mp.quad(integrand, [0, mp.pi, 2*mp.pi])
okl = True
for lv in [sp.Rational(3, 2), 3]:
    bv = float(b.subs(l, lv))
    for t in [0.0, 0.4]:
        Id = I_direct(t, lv); Ipred = -2*mp.e**((1 + bv)*t)*2*mp.pi
        okl &= abs(Id - Ipred) < 1e-10*abs(Ipred)
rep('E14 label loops: I(t) = -2 e^{(1+b)t} int_D u (direct quadrature, two l, two t), hence I\' = (1 + b) I', okl)
# I' = I - oint rho dV^y for the example: direct quadrature of oint rho dV^y on the same loops, compared with -b I
def J_direct(t, lv):
    bv = float(b.subs(l, lv)); hv = float(h.subs(l, lv))
    def integrand(s):
        u0, v0 = 2 + mp.cos(s), 1 + mp.sin(s); du, dv = -mp.sin(s), mp.cos(s)
        U, Vv = mp.e**(t/2)*u0, mp.e**(bv*t)*v0; dU, dV = mp.e**(t/2)*du, mp.e**(bv*t)*dv
        xx, yy = U, Vv + hv*U**2; dx, dy = dU, dV + 2*hv*U*dU
        return xx**2*(bv*dy - 2*xx*dx)
    return mp.quad(integrand, [0, mp.pi, 2*mp.pi])
okj = True
for lv in [sp.Rational(3, 2), 3]:
    bv = float(b.subs(l, lv))
    for t in [0.0, 0.4]:
        Id = I_direct(t, lv); Jd = J_direct(t, lv)
        okj &= abs(Jd + bv*Id) < 1e-10*abs(Id)
rep('E15 oint rho dV^y = -b I on the same loops (quadrature), so I - oint rho dV^y = (1 + b) I = I\' (material-loop law)', okj)
# ---- oscillatory integrand (pointwise, general V, f, e) ----
k, al = sp.symbols('k alpha', positive=True)
f = sp.Function('f')(x, y); V1 = sp.Function('V1')(x, y); V2 = sp.Function('V2')(x, y)
Vg = sp.Matrix([V1, V2]); e = sp.Matrix([sp.cos(al), sp.sin(al)]); s_ = k*(e[0]*x + e[1]*y)
Zk = Rm(grad(f*sp.sin(s_)/k)); Hk = Rm(grad(f*sp.cos(s_)/k))
dd = lambda F: F.jacobian([x, y])*Vg        # (V.grad) F
integrand = (dd(Zk).T*Hk - dd(Hk).T*Zk)[0]
A0 = f*Rm(e); B0 = Rm(grad(f))
pred = k*f**2*Vg.dot(e) + ((dd(A0).T*B0)[0] - (dd(B0).T*A0)[0] + Vg.dot(e)*B0.dot(B0))/k
diffc = sp.simplify(sp.expand(sp.expand_trig(integrand - pred)))
diffc = sp.simplify(diffc.subs(sp.sin(s_)**2, 1 - sp.cos(s_)**2))
rep('E16 pointwise: (V.grad Z_k).H_k - (V.grad H_k).Z_k = k f^2 (V.e) + (1/k)[...] (no oscillating terms; referee audit 27b 1.2)', diffc == 0, '' if diffc == 0 else diffc)
Bpt = sp.expand((dd(A0).T*B0)[0] - (dd(B0).T*A0)[0] + Vg.dot(e)*B0.dot(B0))
Bau = sp.expand(Vg.dot(grad(f))*e.dot(grad(f)) - f*e.dot(sp.hessian(f, (x, y))*Vg) + Vg.dot(e)*grad(f).dot(grad(f)))
rep('E17 the 1/k coefficient equals referee audit 27b B integrand (V.grad f)(e.grad f) - f e.(D^2 f V) + (V.e)|grad f|^2', sp.simplify(Bpt - Bau) == 0)
rep('E18 Z_k, H_k divergence free', sp.simplify(div(Zk)) == 0 and sp.simplify(div(Hk)) == 0)
# ---- circulation coefficient identities ----
r, th, p = sp.symbols('r theta p', positive=True)
A = sp.Function('A')(th); Ps = sp.Function('Psi')(th)
ode_rhs = sp.sin(th)*sp.diff(A, th) - p*sp.cos(th)*A
Q = (A*sp.sin(th) - sp.diff(Ps, th))/(p + 1)
Qp = sp.diff(Q, th).subs(sp.diff(Ps, th, 2), ode_rhs - (p + 1)**2*Ps)
rep('E19 Psi\'\' + (p+1)^2 Psi = sin A\' - p cos A  =>  Q\' = (p + 1) Psi + A cos th', sp.simplify(Qp - ((p + 1)*Ps + A*sp.cos(th))) == 0)
# Cartesian check of -Lap(r^{p+1} Psi) = d_x(r^p A) <=> ODE, and grad(r^{p+1} Q) = H + F e_2 (polar components)
lap_pol = lambda g: sp.diff(g, r, 2) + sp.diff(g, r)/r + sp.diff(g, th, 2)/r**2
dx_pol = lambda g: sp.cos(th)*sp.diff(g, r) - sp.sin(th)*sp.diff(g, th)/r
psi = r**(p + 1)*Ps; F = r**p*A
eq = sp.simplify((-lap_pol(psi) - dx_pol(F))/r**(p - 1))
rep('E20 -Lap(r^{p+1} Psi) = d_x(r^p A)  <=>  Psi\'\' + (p+1)^2 Psi = sin A\' - p cos A', sp.simplify(eq + sp.diff(Ps, th, 2) + (p + 1)**2*Ps - ode_rhs) == 0)
# H = R grad psi in polar: (H_r, H_th) = (-(1/r) psi_th, psi_r); e_2 = sin e_r + cos e_th
Hr = -sp.diff(psi, th)/r; Hth = sp.diff(psi, r)
G = r**(p + 1)*Q
rep('E21 H = r^p(-Psi\' e_r + (p+1) Psi e_th) and grad(r^{p+1} Q) = H + F e_2',
    sp.simplify(Hr + r**p*sp.diff(Ps, th)) == 0 and sp.simplify(Hth - (p + 1)*r**p*Ps) == 0 and
    sp.simplify(sp.diff(G, r) - (Hr + F*sp.sin(th))) == 0 and sp.simplify((sp.diff(G, th)/r).subs(sp.diff(Ps, th, 2), ode_rhs - (p + 1)**2*Ps) - (Hth + F*sp.cos(th))) == 0)
# angular examples (referee audit 27b 3.2)
Ac = sp.cos(th)**2; Pc = -(2 + 3*p)/(4*p*(p + 2))*sp.cos(th) - sp.cos(3*th)/(4*(p + 4))
res_c = sp.simplify(sp.diff(Pc, th, 2) + (p + 1)**2*Pc - (sp.sin(th)*sp.diff(Ac, th) - p*sp.cos(th)*Ac))
Qc = (Ac*sp.sin(th) - sp.diff(Pc, th))/(p + 1)
rep('E22 A = cos^2: Psi solves the ODE; Q(pi/2) = -2/(p(p+2)(p+4)) = -Q(-pi/2)', res_c == 0 and sp.simplify(Qc.subs(th, sp.pi/2) + 2/(p*(p + 2)*(p + 4))) == 0 and sp.simplify(Qc.subs(th, -sp.pi/2) - 2/(p*(p + 2)*(p + 4))) == 0)
As = sp.sin(th)**2; Pss = (2 - p)/(4*p*(p + 2))*sp.cos(th) + sp.cos(3*th)/(4*(p + 4))
res_s = sp.simplify(sp.diff(Pss, th, 2) + (p + 1)**2*Pss - (sp.sin(th)*sp.diff(As, th) - p*sp.cos(th)*As))
Qs = (As*sp.sin(th) - sp.diff(Pss, th))/(p + 1)
rep('E23 A = sin^2: Psi solves the ODE and Q(0) = Q(pi) = 0 (the coefficient can vanish; "not shown to be nonzero")', res_s == 0 and sp.simplify(Qs.subs(th, 0)) == 0 and sp.simplify(Qs.subs(th, sp.pi)) == 0)
# dilation and stationarity remarks
ph = sp.Function('phi')(x, y)
rep('E24 z.R grad phi = div(phi (y, -x)) (so int l X.(Z o X) = 0 for compact Z = R grad phi)', sp.simplify(sp.Matrix([x, y]).dot(Rm(grad(ph))) - div(ph*sp.Matrix([y, -x]))) == 0)
rep('E25 rho Z^y with Z = R grad phi: rho phi_x = d_x(rho phi) - rho_x phi (stationarity forces rho_x = 0)', sp.simplify(x**2*Rm(grad(ph))[1] - (sp.diff(x**2*ph, x) - 2*x*ph)) == 0)
print('ALL OK' if all(ok) else 'SOME FAIL', sum(ok), 'of', len(ok))
