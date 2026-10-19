"""V32: principal (third-order) part of the linearisation of the referee result 9 label equation, own derivation (sympy).
E(X) = {Nx, x} + {Ny, y} + 2u y_v, {f, g} = f_u g_v - f_v g_u, N = al u d_u + be v d_v, X = (x, y)(u, v).
Variation dX = DX J grad h, J grad h = (h_v, -h_u). Claim (referee result 9): the third-order part of dE equals that of
-Delta_g N h, Delta_g = d_i(g^{ij} d_j), g_ij = X_i.X_j, when det DX = 1; symbol -(g^{ij} z_i z_j)(al u z_u + be v z_v)
up to a nonzero constant factor. Also: lower-order check of the full claimed operator L h = -Delta_g (N - 2l) h - D_x(2u h_v)
on the exact example X = (u, v + k u^2), k = 1/(be - 1) (rho = x^2, V = (al x, be y - x^2))."""
import sympy as sp
u, v, al, be, eps = sp.symbols('u v alpha beta epsilon', real=True)
x = sp.Function('x')(u, v); y = sp.Function('y')(u, v); h = sp.Function('h')(u, v)
N = lambda f: al*u*sp.diff(f, u) + be*v*sp.diff(f, v)
PB = lambda f, g: sp.diff(f, u)*sp.diff(g, v) - sp.diff(f, v)*sp.diff(g, u)
E = lambda X, Y: PB(N(X), X) + PB(N(Y), Y) + 2*u*sp.diff(Y, v)
dx = sp.diff(x, u)*sp.diff(h, v) - sp.diff(x, v)*sp.diff(h, u)
dy = sp.diff(y, u)*sp.diff(h, v) - sp.diff(y, v)*sp.diff(h, u)
dE = sp.expand(sp.diff(E(x + eps*dx, y + eps*dy), eps).subs(eps, 0))
# metric and inverse metric (adjugate / det g; det g = (det DX)^2)
xu, xv, yu, yv = [sp.diff(f, w) for f in (x, y) for w in (u, v)][0], sp.diff(x, v), sp.diff(y, u), sp.diff(y, v)
g11 = xu**2 + yu**2; g12 = xu*xv + yu*yv; g22 = xv**2 + yv**2
dg = g11*g22 - g12**2
Nh = N(h)
claim3 = -(g22*sp.diff(Nh, u, u) - 2*g12*sp.diff(Nh, u, v) + g11*sp.diff(Nh, v, v))/dg
third = [sp.Derivative(h, u, 3), sp.Derivative(h, u, 2, v), sp.Derivative(h, u, v, 2), sp.Derivative(h, v, 3)]
J = xu*yv - xv*yu
ok = True
for d in third:
    a = sp.expand(dE).coeff(d)
    b = sp.expand(claim3).coeff(d)
    # impose det DX = 1 by y_v = (1 + x_v y_u)/x_u in both, compare
    sub = {sp.Derivative(y, v): (1 + xv*yu)/xu}
    r = sp.simplify(a.subs(sub) - b.subs(sub))
    print('third-order coeff', d, ': dE - claim =', r, flush=True)
    ok = ok and r == 0
print('principal part matches -Delta_g N h at det DX = 1:', ok)
# exact example, full operator
l = sp.symbols('l', positive=True)
k = 1/(be - 1)
Xe, Ye = u, v + k*u**2
sub_ex = {al: sp.Rational(1, 2), be: 2*l - sp.Rational(1, 2)}
print('example solves E = 0:', sp.simplify(E(Xe, Ye).subs(sub_ex)))
dxe = sp.diff(Xe, u)*sp.diff(h, v) - sp.diff(Xe, v)*sp.diff(h, u)
dye = sp.diff(Ye, u)*sp.diff(h, v) - sp.diff(Ye, v)*sp.diff(h, u)
dEe = sp.diff(E(Xe + eps*dxe, Ye + eps*dye), eps).subs(eps, 0)
G = sp.Matrix([[sp.diff(Xe, u)**2 + sp.diff(Ye, u)**2, sp.diff(Xe, u)*sp.diff(Xe, v) + sp.diff(Ye, u)*sp.diff(Ye, v)],
               [0, sp.diff(Xe, v)**2 + sp.diff(Ye, v)**2]]); G[1, 0] = G[0, 1]
Gi = sp.simplify(G.inv())
w = (N(h) - 2*l*h)
lapg = sp.diff(Gi[0, 0]*sp.diff(w, u) + Gi[0, 1]*sp.diff(w, v), u) + sp.diff(Gi[1, 0]*sp.diff(w, u) + Gi[1, 1]*sp.diff(w, v), v)
yv_e, yu_e = sp.diff(Ye, v), sp.diff(Ye, u)
Dx = lambda f: yv_e*sp.diff(f, u) - yu_e*sp.diff(f, v)
Lh = -lapg - Dx(2*u*sp.diff(h, v))
for sgn in (1, -1):
    print('example: dE - (%d) L h =' % sgn, sp.simplify(sp.expand((dEe - sgn*Lh).subs(sub_ex))), flush=True)
