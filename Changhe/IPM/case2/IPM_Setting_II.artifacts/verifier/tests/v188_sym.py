# V188: independent symbolic checks of FR item 31 (4.17(f), 9.13 Step 11), candidate 7efa7fd9.
import sympy as sp
x, y, n, al, k = sp.symbols('x y n alpha kappa', real=True)
b = sp.Function('b')(x, y); Z = sp.Function('Z')(x, y)
phi = n**(-2-al)*b*sp.sin(n*Z)
D = lambda f, i, j: sp.diff(f, [x, y][i], [x, y][j])
gz = [sp.diff(Z, x), sp.diff(Z, y)]; gb = [sp.diff(b, x), sp.diff(b, y)]
ok = True
for i in range(2):
    for j in range(2):
        rhs = (n**(-2-al)*sp.sin(n*Z)*D(b, i, j) + n**(-1-al)*sp.cos(n*Z)*(b*D(Z, i, j) + gb[i]*gz[j] + gz[i]*gb[j])
               - n**(-al)*b*sp.sin(n*Z)*gz[i]*gz[j])
        ok &= sp.simplify(sp.expand(sp.powsimp(sp.expand(D(phi, i, j) - rhs), force=True))) == 0
print('D2 display (all four entries):', ok)
# forcing f = W[h].grad xi with W[h] = (-phi_xy, phi_xx); coefficient of n^-alpha sin(nZ)
xi = sp.Function('xi')(x, y)
f = -D(phi, 0, 1)*sp.diff(xi, x) + D(phi, 0, 0)*sp.diff(xi, y)
s = sp.Symbol('s'); c_ = sp.Symbol('c')
fe = sp.expand(f.subs({sp.sin(n*Z): s, sp.cos(n*Z): c_}))
# the sine part: keep the terms of order n^{-alpha}
sinpart = sp.expand(fe.coeff(s))
terms = sp.Add.make_args(sinpart)
leadsum = sum(t for t in terms if sp.simplify(t*n**al).has(n) is False)
g_claim = b*sp.diff(Z, x)*(sp.diff(Z, y)*sp.diff(xi, x) - sp.diff(Z, x)*sp.diff(xi, y))
print('leading coefficient equals g = b Th_x (Th_y xi_x - Th_x xi_y):', sp.simplify(leadsum*n**al - g_claim) == 0)
# with grad Th = kappa J V, J(v1,v2) = (-v2, v1), and V.grad xi = xi/2
V1, V2, xx, xy, X_i = sp.symbols('V1 V2 xi_x xi_y xival', real=True)
gsym = b*(-k*V2)*((k*V1)*xx - (-k*V2)*xy)
print('g = -(1/2) b kappa^2 V2 xi under V1 xi_x + V2 xi_y = xi/2:',
      sp.simplify(gsym.subs(xx, (X_i/2 - V2*xy)/V1) + sp.Rational(1, 2)*b*k**2*V2*X_i) == 0)
# Th_y xi_x - Th_x xi_y = kappa V.grad xi
print('Th_y xi_x - Th_x xi_y = kappa V.grad xi:', sp.simplify((k*V1)*xx - (-k*V2)*xy - k*(V1*xx + V2*xy)) == 0)
# cos 3th = x (4x^2 - 3r^2)/r^3
r = sp.sqrt(x**2 + y**2); th = sp.atan2(y, x)
print('cos 3th identity:', sp.simplify(sp.expand_trig(sp.cos(3*th)) - x*(4*x**2 - 3*r**2)/r**3) == 0)
# divergence and curl of v = (-phi_xy, phi_xx) for general phi; curl v = -d_x h with h = -Lap phi
p = sp.Function('p')(x, y)
v = (-sp.diff(p, x, y), sp.diff(p, x, 2)); h = -(sp.diff(p, x, 2) + sp.diff(p, y, 2))
print('div v = 0:', sp.simplify(sp.diff(v[0], x) + sp.diff(v[1], y)) == 0,
      ' curl v = -h_x:', sp.simplify(sp.diff(v[1], x) - sp.diff(v[0], y) + sp.diff(h, x)) == 0)
# psi = d_x p gives U = (-psi_y, psi_x) = v and -Lap psi = d_x h
psi = sp.diff(p, x)
print('U = grad-perp psi = v:', sp.simplify(-sp.diff(psi, y) - v[0]) == 0 and sp.simplify(sp.diff(psi, x) - v[1]) == 0,
      ' -Lap psi = h_x:', sp.simplify(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(h, x)) == 0)
# interpolation exponent: (n^-3)^(1-a) (n^-2)^a = n^(a-3)
print('interpolation exponent:', sp.simplify(sp.expand_power_exp(-3*(1 - al) - 2*al) - (al - 3)) == 0)
# reflection: for odd h, f = W[h].grad xi is even (W[h](RX) = -R W[h](X), grad xi(RX) = -R grad xi(X))
R = sp.Matrix([[-1, 0], [0, 1]]); w = sp.Matrix(sp.symbols('w1 w2')); gx = sp.Matrix(sp.symbols('g1 g2'))
print('f even:', sp.simplify(((-R*w).T*(-R*gx))[0] - (w.T*gx)[0]) == 0)
