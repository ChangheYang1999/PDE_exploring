"""Symbolic checks of lead proofs/structure_v1.md (Thm 5(c) ODE, Thm 7 homogeneous formulas and zero expansion,
Prop 6 divergence identity, Thm 3 Jacobian identity)."""
import sympy as sp
x, y, r, th, t, l, p, a, a3, b = sp.symbols('x y r theta t l p a a3 b', real=True)
# --- Prop 6: div(phi_* V) = -phi_* + W.grad phi_* when p l = 1, V = l X + W, div W = 0
Phi = sp.Function('Phi')
X, Y = sp.symbols('X Y', real=True)
R_ = sp.sqrt(X**2 + Y**2); TH = sp.atan2(Y, X)
phis = R_**(-2 - p)*Phi(TH)
W1, W2 = sp.Function('W1')(X, Y), sp.Function('W2')(X, Y)
divW = sp.diff(W1, X) + sp.diff(W2, Y)
expr = sp.diff(phis*(l*X + W1), X) + sp.diff(phis*(l*Y + W2), Y) - (-phis + W1*sp.diff(phis, X) + W2*sp.diff(phis, Y)) - phis*divW
print('Prop6 div identity residual (should be 0 at l = 1/p):', sp.simplify(expr.subs(l, 1/p)))
# --- Thm 5(c): differentiate V.grad rho = rho twice in x at x = 0 with V1 odd, V2 even, rho = rho_x = 0 on axis
c0, c1, c2, c3 = [sp.Function(f'v{i}')(y) for i in range(4)]
h, h3 = sp.Function('h')(y), sp.Function('h3')(y)
bb = sp.Function('b')(y)
# rho even in x with rho = h x^2/2 + h4 x^4/24 ..., V1 odd: V1 = (2l - b') x + e3 x^3, V2 even: V2 = b + f2 x^2
e3, f2, h4 = sp.Function('e3')(y), sp.Function('f2')(y), sp.Function('h4')(y)
rho = h*x**2/2 + h4*x**4/24
V1 = (2*l - sp.diff(bb, y))*x + e3*x**3
V2 = bb + f2*x**2
print('Thm5 div V - 2l (should be O(x^2)):', sp.expand(sp.diff(V1, x) + sp.diff(V2, y) - 2*l).subs(x, 0))
eq = V1*sp.diff(rho, x) + V2*sp.diff(rho, y) - rho
coef2 = sp.expand(eq).coeff(x, 2)
print('Thm5 x^2 coefficient:', sp.simplify(coef2 - (bb*sp.diff(h, y) - (1 - 4*l + 2*sp.diff(bb, y))*h)/2))
# --- Thm 7: Laplacian and d_x in polar coordinates, Jacobian H.grad F
Psi, A = sp.Function('Psi')(th), sp.Function('A')(th)
psiF = r**(p + 1)*Psi; F = r**p*A
lap = sp.diff(psiF, r, 2) + sp.diff(psiF, r)/r + sp.diff(psiF, th, 2)/r**2
print('Thm7 Laplacian:', sp.simplify(lap/r**(p - 1) - (sp.diff(Psi, th, 2) + (p + 1)**2*Psi)))
dxF = sp.cos(th)*sp.diff(F, r) - sp.sin(th)/r*sp.diff(F, th)
print('Thm7 d_x F:', sp.simplify(dxF/r**(p - 1) - (p*sp.cos(th)*A - sp.sin(th)*sp.diff(A, th))))
# H = (-psi_y, psi_x); H.grad F = psi_x F_y - psi_y F_x = (psi_r F_th - psi_th F_r)/r
jac = (sp.diff(psiF, r)*sp.diff(F, th) - sp.diff(psiF, th)*sp.diff(F, r))/r
print('Thm7 H.grad F:', sp.simplify(jac/r**(2*p - 1) - ((p + 1)*Psi*sp.diff(A, th) - p*sp.diff(Psi, th)*A)))
# check sign convention of the Jacobian in Cartesian form on an example
ex_psi = (X**2 + Y**2)**sp.Rational(3, 4)*X*Y; ex_F = (X**2 + Y**2)**sp.Rational(1, 4)*(X + 2*Y)/sp.sqrt(X**2 + Y**2)
cart = -sp.diff(ex_psi, Y)*sp.diff(ex_F, X) + sp.diff(ex_psi, X)*sp.diff(ex_F, Y)
rs, ts = sp.symbols('rs ts', positive=True)
pol_psi = ex_psi.subs({X: rs*sp.cos(ts), Y: rs*sp.sin(ts)}); pol_F = ex_F.subs({X: rs*sp.cos(ts), Y: rs*sp.sin(ts)})
polj = (sp.diff(pol_psi, rs)*sp.diff(pol_F, ts) - sp.diff(pol_psi, ts)*sp.diff(pol_F, rs))/rs
val = [(cart.subs({X: 1.3*sp.cos(0.7), Y: 1.3*sp.sin(0.7)})).evalf(), polj.subs({rs: 1.3, ts: 0.7}).evalf()]
print('Jacobian convention check (cartesian vs polar):', val)
# Psi = C A^{(p+1)/p} solves (p+1) Psi A' = p Psi' A
C = sp.symbols('C')
Ps = C*A**((p + 1)/p)
print('Thm7 arc solution:', sp.simplify((p + 1)*Ps*sp.diff(A, th) - p*sp.diff(Ps, th)*A))
# expansion of p cos(th) A - sin(th) A' at th = b + t, A = a t^2 + a3 t^3
At = a*t**2 + a3*t**3
e = p*sp.cos(b + t)*At - sp.sin(b + t)*sp.diff(At, t)
ser = sp.series(e, t, 0, 3).removeO()
print('Thm7 expansion t^1:', sp.simplify(ser.coeff(t, 1)), '| t^2:', sp.simplify(ser.coeff(t, 2) - (p*a*sp.cos(b) - 2*a*sp.cos(b) - 3*a3*sp.sin(b))))
# order of Psi'' + (p+1)^2 Psi for Psi = C (a t^2)^{(p+1)/p}: exponent of |t|
q = sp.symbols('q', positive=True)
print('Thm7 Psi exponent 2(p+1)/p - 2 =', sp.simplify(2*(p + 1)/p - 2), '(> 2 iff p < 1)')
# --- Thm 5(c) integration: 3 int b' h = (4l - 1) int h  <=>  int h w' = (l - 1)/3 int h with b' = l + w'
Ih, Ihw = sp.symbols('Ih Ihw')
print('Thm5 wall identity algebra:', sp.solve(sp.Eq(3*(l*Ih + Ihw), (4*l - 1)*Ih), Ihw))
# --- Thm 5(c) asymptotics: d/dy log(h/b^2) = (1-4l)/b ; with b = l y: h ~ y^{2 + (1-4l)/l} = y^{p-2}
print('Thm5 h exponent with b = l y:', sp.simplify(2 + (1 - 4*l)/l), ' = p - 2 with p = 1/l:', sp.simplify((2 + (1 - 4*l)/l).subs(l, 1/p) - (p - 2)))
