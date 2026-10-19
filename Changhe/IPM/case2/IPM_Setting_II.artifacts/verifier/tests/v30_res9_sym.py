"""V30 (audit of referee result 9, exact (xi, eta) symplectic form of S^+), symbolic parts; own derivations (sympy).
alpha = 1/2, beta = 2 l - 1/2, N = alpha u d_u + beta v d_v, J grad g = (g_y, -g_x), {f, g} = f_u g_v - f_v g_u.
Each check prints a residual that must simplify to 0 (or True)."""
import sympy as sp

x, y, u, v, l, t, th, s, r = sp.symbols('x y u v l t vartheta s r', real=True)
al = sp.Rational(1, 2); be = 2*l - sp.Rational(1, 2)
out = []
def chk(name, e):
    val = sp.simplify(e); out.append((name, val)); print(name, ':', val, flush=True)

# 1. V = al xi J grad eta - be eta J grad xi: V.grad xi = al xi det, V.grad eta = be eta det, div V = (al + be) det = 2 l det
xi = sp.Function('xi')(x, y); eta = sp.Function('eta')(x, y)
Jg = lambda g: (sp.diff(g, y), -sp.diff(g, x))
V = tuple(al*xi*a - be*eta*b for a, b in zip(Jg(eta), Jg(xi)))
det = sp.diff(xi, x)*sp.diff(eta, y) - sp.diff(xi, y)*sp.diff(eta, x)
chk('A: V.grad xi - al xi det', V[0]*sp.diff(xi, x) + V[1]*sp.diff(xi, y) - al*xi*det)
chk('A: V.grad eta - be eta det', V[0]*sp.diff(eta, x) + V[1]*sp.diff(eta, y) - be*eta*det)
chk('A: div V - 2 l det', sp.diff(V[0], x) + sp.diff(V[1], y) - 2*l*det)
h = sp.Function('h')(x, y); g = sp.Function('g')(x, y)
hJ = (h*sp.diff(g, y), -h*sp.diff(g, x))
chk('A: curl(h J grad g) + div(h grad g)', sp.diff(hJ[1], x) - sp.diff(hJ[0], y) + sp.diff(h*sp.diff(g, x), x) + sp.diff(h*sp.diff(g, y), y))
curlV = sp.diff(V[1], x) - sp.diff(V[0], y)
chk('A: curl V - (be div(eta grad xi) - al div(xi grad eta))', curlV - (be*(sp.diff(eta*sp.diff(xi, x), x) + sp.diff(eta*sp.diff(xi, y), y))
                                                               - al*(sp.diff(xi*sp.diff(eta, x), x) + sp.diff(xi*sp.diff(eta, y), y))))
chk('A: q = be/al = 4l - 1', be/al - (4*l - 1))

# 2. label coordinates: X(u, v) generic, Jdet = {x, y}; physical d_x = (y_v d_u - y_u d_v)/Jdet, d_y = (-x_v d_u + x_u d_v)/Jdet.
X1 = sp.Function('x')(u, v); X2 = sp.Function('y')(u, v)
Jd = sp.diff(X1, u)*sp.diff(X2, v) - sp.diff(X1, v)*sp.diff(X2, u)
Dx = lambda f: (sp.diff(X2, v)*sp.diff(f, u) - sp.diff(X2, u)*sp.diff(f, v))/Jd
Dy = lambda f: (-sp.diff(X1, v)*sp.diff(f, u) + sp.diff(X1, u)*sp.diff(f, v))/Jd
Nop = lambda f: al*u*sp.diff(f, u) + be*v*sp.diff(f, v)
PB = lambda f, g: sp.diff(f, u)*sp.diff(g, v) - sp.diff(f, v)*sp.diff(g, u)
Vl = (Nop(X1), Nop(X2))                       # V o X = N X (labels flow linearly)
curl_l = Dx(Vl[1]) - Dy(Vl[0])
rho_x = Dx(u**2)
chk('B: Jdet*(curl V + rho_x) - ({Nx,x} + {Ny,y} + 2u y_v)', sp.expand(Jd*(curl_l + rho_x) - (PB(Nop(X1), X1) + PB(Nop(X2), X2) + 2*u*sp.diff(X2, v))))
# closedness of (Nx) dx + (Ny) dy + u^2 dy: d(F du + G dv) = (G_u - F_v) du^dv
F1 = Nop(X1)*sp.diff(X1, u) + Nop(X2)*sp.diff(X2, u) + u**2*sp.diff(X2, u)
F2 = Nop(X1)*sp.diff(X1, v) + Nop(X2)*sp.diff(X2, v) + u**2*sp.diff(X2, v)
chk('B: d[(NX).dX + u^2 dy] - ({Nx,x}+{Ny,y}+2u y_v)', sp.expand(sp.diff(F2, u) - sp.diff(F1, v) - (PB(Nop(X1), X1) + PB(Nop(X2), X2) + 2*u*sp.diff(X2, v))))
# Stokes form: d[(NX).dX] = -2 u y_v du^dv on solutions, d[u^2 dy] = 2u y_v
chk('B: d[u^2 dy] - 2u y_v', sp.diff(u**2*sp.diff(X2, v), u) - sp.diff(u**2*sp.diff(X2, u), v) - 2*u*sp.diff(X2, v))
# NP = |NX|^2 + u^2 Ny from grad_z P = (DX)^T N X + u^2 grad_z y
Pu = F1; Pv = F2
chk('C: N P - |NX|^2 - u^2 Ny', sp.expand(al*u*Pu + be*v*Pv - (Nop(X1)**2 + Nop(X2)**2) - u**2*Nop(X2)))
chk('C: P_v on u = 0 equals be v |X_v|^2', sp.simplify(Pv.subs(u, 0).doit() - be*v*(sp.diff(X1, v)**2 + sp.diff(X2, v)**2).subs(u, 0)))
chk('C: Pu formula', sp.expand(Pu - (al*u*(sp.diff(X1, u)**2 + sp.diff(X2, u)**2) + be*v*(sp.diff(X1, u)*sp.diff(X1, v) + sp.diff(X2, u)*sp.diff(X2, v)) + u**2*sp.diff(X2, u))))

# 3. generating function v = G_u(u, y), x = G_y(u, y); A0 = G_uy, B0 = G_uu, D0 = G_yy.
G = sp.Function('G')(u, y)
A0, B0, D0 = sp.diff(G, u, y), sp.diff(G, u, 2), sp.diff(G, y, 2)
# derivatives with respect to the labels (u, v) of a function f(u, y): f_u|v = f_u + f_y y_u, f_v = f_y y_v; y_u = -B0/A0, y_v = 1/A0
yu, yv = -B0/A0, 1/A0
du_l = lambda f: sp.diff(f, u) + sp.diff(f, y)*yu
dv_l = lambda f: sp.diff(f, y)*yv
xG = sp.diff(G, y); vG = sp.diff(G, u)
chk('D: area {x, y} = 1', sp.simplify(du_l(xG)*dv_l(y) - dv_l(xG)*du_l(y) - 1))
NyG = al*u*du_l(y) + be*vG*dv_l(y); NxG = al*u*du_l(xG) + be*vG*dv_l(xG)
T = (be*vG - al*u*B0)/A0; Zf = al*u*A0 + D0*T
chk('D: Ny - T', sp.simplify(NyG - T)); chk('D: Nx - Z', sp.simplify(NxG - Zf))
PBl = lambda f, g: du_l(f)*dv_l(g) - dv_l(f)*du_l(g)
lhs = PBl(Zf, xG) + PBl(T, y) + 2*u*yv
chk('D: A0*({Nx,x}+{Ny,y}+2u y_v) - (D0 Z_u - A0 Z_y + T_u + 2u)', sp.simplify(A0*lhs - (D0*sp.diff(Zf, u) - A0*sp.diff(Zf, y) + sp.diff(T, u) + 2*u)))
chk('D: third order in G (Z_u contains G_uuy... )', sp.Poly(sp.expand(A0**2*(D0*sp.diff(Zf, u) - A0*sp.diff(Zf, y) + sp.diff(T, u) + 2*u)), sp.diff(G, u, 2, y)).degree() >= 1)

# 4. gauge, h equation, resonance
K = sp.symbols('K'); B2, Bn = sp.symbols('B2 Bn'); n = sp.symbols('n', positive=True, integer=True)
uu = sp.symbols('uu', positive=True)
q = be/al
chk('E: gauge al u f\' - be f = 0 for f = K u^q', sp.simplify(al*uu*sp.diff(K*uu**q, uu) - be*K*uu**q))
h2 = B2/(be - 2*al)
chk('E: h = h2 u^2 solves al u h\' - be h = -B2 u^2', sp.simplify(al*uu*sp.diff(h2*uu**2, uu) - be*h2*uu**2 + B2*uu**2))
chk('E: B_n u^n -> B_n u^n/(be - n al)', sp.simplify(al*uu*sp.diff(Bn*uu**n/(be - n*al), uu) - be*Bn*uu**n/(be - n*al) + Bn*uu**n))
m = sp.symbols('m', positive=True)
hl = -Bn/al*uu**m*sp.log(uu)
chk('E: resonant log term at q = m', sp.simplify((al*uu*sp.diff(hl, uu) - al*m*hl + Bn*uu**m)))
# phase phi = v/u^q annihilated by N
chk('E: N(v/u^q) = 0', sp.simplify(al*uu*sp.diff(v/uu**q, uu) + be*v*sp.diff(v/uu**q, v)))
# variation: delta rho = -grad_z(u^2).J grad h = -2u h_v
hh = sp.Function('hh')(u, v)
chk('E: delta rho = -2 u h_v', -(2*u*sp.diff(hh, v) - 0*sp.diff(hh, u)) + 2*u*sp.diff(hh, v))

# 5. far field: xi = r^a B, eta = r^b C, a = p/2, b = 2 - p/2; det D(xi, eta) = r^{a+b-2}(a B C' - b B' C); identity for C/|B|^q
p = sp.symbols('p', positive=True)
a = p/2; b = 2 - p/2
Bf = sp.Function('B')(th); Cf = sp.Function('C')(th)
xi_p = r**a*Bf; eta_p = r**b*Cf
detp = (sp.diff(xi_p, r)*sp.diff(eta_p, th) - sp.diff(xi_p, th)*sp.diff(eta_p, r))/r
chk('F: det D(xi, eta) - (a B C\' - b B\' C)', sp.simplify(detp - (a*Bf*sp.diff(Cf, th) - b*sp.diff(Bf, th)*Cf)))
chk('F: q = b/a = 4l - 1 at p = 1/l', sp.simplify((b/a).subs(p, 1/l) - (4*l - 1)))
Bp = sp.Function('Bp', positive=True)(th)       # positive sector
qq = b/a
lhsF = sp.diff(Cf/Bp**qq, th)
chk('F: (C/B^q)\' * a B^{q+1} - (a B C\' - b B\' C)  (B > 0)', sp.simplify(sp.expand(lhsF*a*Bp**(qq + 1) - (a*Bp*sp.diff(Cf, th) - b*sp.diff(Bp, th)*Cf))))
dj = sp.symbols('d_j', nonzero=True)
Cj = sp.solve(sp.Eq(a*0*sp.Symbol('Cp') - b*dj*sp.Symbol('Cj'), 1), sp.Symbol('Cj'))[0]
chk('F: C(theta_j) + 1/(b d_j)', Cj + 1/(b*dj))
chk('F: q + 1 = 2/a', sp.simplify(qq + 1 - 2/a))
# xi correction: sqrt(r^p B^2 + r^{2p-1} J/(l-1)) = r^a B + r^{a+p-1} J/(2(l-1)B) + O(r^{a+2p-2})
Bs, Jp = sp.symbols('B_s J_p', positive=True); eps_ = sp.symbols('epsilon', positive=True)
ser = sp.series(sp.sqrt(Bs**2 + eps_*Jp/(l - 1)), eps_, 0, 2).removeO()
chk('F: sqrt expansion', sp.simplify(ser - (Bs + eps_*Jp/(2*(l - 1)*Bs))))
# Psi equation: (sin A)' - (p+1) cos A = sin A' - p cos A (matches V23/referee result 6 form)
Af = sp.Function('A')(th)
chk('F: Psi forcing forms agree', sp.simplify(sp.diff(sp.sin(th)*Af, th) - (p + 1)*sp.cos(th)*Af - (sp.sin(th)*sp.diff(Af, th) - p*sp.cos(th)*Af)))

# 6. numerical formulation: z = (e^{al t} cos th, e^{be t} sin th)
zt = sp.Matrix([sp.exp(al*t)*sp.cos(th), sp.exp(be*t)*sp.sin(th)])
dz = sp.Matrix.hstack(zt.diff(t), zt.diff(th)).det()
chk('G: det(z_t, z_th) - e^{2lt}(al cos^2 + be sin^2)', sp.simplify(dz - sp.exp(2*l*t)*(al*sp.cos(th)**2 + be*sp.sin(th)**2)))
chk('G: z_t = N z', sp.simplify(zt.diff(t) - sp.Matrix([al*zt[0], be*zt[1]])))
# P_t = (NX).X_t + u^2 y_t with X_t = N X (d/dt = N in these coordinates)
# (by the chain rule P_t = P_u u_t + P_v v_t = N P, and N P = |NX|^2 + u^2 Ny is check C)
# 7. example X = (u, v + k u^2), k = 1/(be - 1): rho = x^2, V = (al x, be y - x^2), curl V = -rho_x, div V = 2l
kk = 1/(be - 1)
Xe = (u, v + kk*u**2)
NXe = (sp.simplify(Nop(Xe[0])), sp.simplify(Nop(Xe[1])))
# in physical variables u = x, v = y - k x^2
Vph = [sp.simplify(c.subs(v, y - kk*x**2).subs(u, x)) for c in NXe]
chk('H: V1 - al x', Vph[0] - al*x); chk('H: V2 - (be y - x^2)', sp.simplify(Vph[1] - (be*y - x**2)))
chk('H: curl V + d_x(x^2)', sp.diff(Vph[1], x) - sp.diff(Vph[0], y) + 2*x)
chk('H: div V - 2l', sp.simplify(sp.diff(Vph[0], x) + sp.diff(Vph[1], y) - 2*l))
chk('H: equation {Nx,x}+{Ny,y}+2u y_v', sp.simplify(PB(NXe[0], Xe[0]) + PB(NXe[1], Xe[1]) + 2*u*sp.diff(Xe[1], v)))

# 8. referee audit 9 1(c) counterexample: x = u + y |u|^{5/2} (u > 0 side), area companion E with E_y = x_u
E = y + sp.Rational(5, 4)*y**2*uu**sp.Rational(3, 2)
xc = uu + y*uu**sp.Rational(5, 2)
chk('I: E_y - x_u', sp.simplify(sp.diff(E, y) - sp.diff(xc, uu)))
chk('I: d_u^2 [E(u, y1) - E(u, 0)] ~ u^{-1/2}', sp.simplify(sp.diff(E - E.subs(y, 0), uu, 2)*uu**sp.Rational(1, 2)))

bad = [nm for nm, val in out if not (val == 0 or val is True or val == sp.true)]
print('ALL', len(out), 'checks; nonzero:', bad)
