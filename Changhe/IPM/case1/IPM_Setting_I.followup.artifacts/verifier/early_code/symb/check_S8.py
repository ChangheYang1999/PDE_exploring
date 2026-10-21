"""verifier: own symbolic checks of lead notes S-8 (a) source-motion identity, (c) model problems, (d) frozen modes at P."""
import sympy as sp

# ---------- (a) source-motion identity from T_1 = w g' + (h - 1) g on the axis (Taylor polynomials at P, z = x - x*)
z, eps, A = sp.symbols('z epsilon A')
w2, w3, g0, g1, g2, cl = sp.symbols('w2 w3 g0 g1 g2 c_l')
dw0, dw1, dw2, dg0, dg1, dcl = sp.symbols('dw0 dw1 dw2 dg0 dg1 dcl')
wb = A * z + w2 * z ** 2 + w3 * z ** 3                 # w(P) = 0, w'(P) = A = 2 c_l - 1
gb = g0 + g1 * z + g2 * z ** 2
hb = lambda W, c: 2 * c - sp.diff(W, z)
T1 = lambda W, G, c: sp.expand(W * sp.diff(G, z) + (hb(W, c) - 1) * G)
Tb = T1(wb, gb, (A + 1) / 2)
print('(a) background T_1 coefficients z^0, z^1:', [sp.simplify(Tb.coeff(z, j)) for j in range(2)])
dW = dw0 + dw1 * z + dw2 * z ** 2
dG = dg0 + dg1 * z
lin = sp.expand(sp.diff(T1(wb + eps * dW, gb + eps * dG, (A + 1) / 2 + eps * dcl), eps).subs(eps, 0))
print('(a) linearized T_1 at P (z^0):', sp.simplify(lin.coeff(z, 0)))
dh0 = 2 * dcl - dw1                                     # dh(P) = 2 dc_l - dw'(P)
h1 = sp.diff(hb(wb, (A + 1) / 2), z).subs(z, 0)         # h'(P) = -2 w2
g1sol = sp.solve(Tb.coeff(z, 1), g1)[0]                  # A g'(P) + g(P) h'(P) = 0
dclsol = sp.solve(lin.coeff(z, 0).subs(g1, g1sol), dcl)[0]
p = -dw0 / A
print('(a) dh(P) + p h\'(P) on {T_1 = 0, dT_1(P) = 0}:', sp.simplify((dh0 + p * h1).subs(dcl, dclsol)))
print('(a) w_new(x* + p) = A p + dw(P) at first order:', sp.simplify(A * p + dw0))
# dC: C eta_y(P) = g(P); normalization at the moved source: dC = dg(P) + p g'(P)
print('(a) g_new(x* + p) - g(P) at first order:', sp.expand(sp.series((gb + eps * dG).subs(z, eps * p / eps * 0 + p * eps), eps, 0, 2).removeO().coeff(eps)))

# ---------- (c+) model kernel of A xi d_xi + y d_y - nu
xi, y, nu, Am = sp.symbols('xi y nu A', positive=True)
F = sp.Function('F')
v = y ** nu * F(xi / y ** Am)
res = sp.simplify(Am * xi * sp.diff(v, xi) + y * sp.diff(v, y) - nu * v)
print('(c+) residual on y > 0:', res)
gstar, Ax3 = sp.Float('29.74948'), sp.Float('10.150725')
print('(c+) X3: nu - 3A =', (1 + gstar) - 3 * Ax3, ' (1 + g*)/A =', (1 + gstar) / Ax3)

# ---------- (c-) torus model: multiplier of d_t + (1 - d_s^2)^(-1) on e^{i(k t + n s)}
k, n = sp.symbols('k n', real=True)
mult = sp.I * k + 1 / (1 + n ** 2)
print('(c-) |multiplier|^2 =', sp.simplify(sp.expand(mult * sp.conjugate(mult))), '(>= 1/(1+n^2)^2 > 0)')

# ---------- (d) frozen model at P: (A xi d_xi + y d_y - 1) v + g u_2 = 0, div u = 0, curl u = d_xi u_2 - d_y u_1 = -v_xi
C, r, gg = sp.symbols('C r g')
def frozen(v, u1, u2):
    tr = sp.simplify((Am * xi * sp.diff(v, xi) + y * sp.diff(v, y) - v + gg * u2))
    dv = sp.simplify(sp.diff(u1, xi) + sp.diff(u2, y))
    cu = sp.simplify(sp.diff(u2, xi) - sp.diff(u1, y) + sp.diff(v, xi))
    return tr, dv, cu
r1 = gg / Am
v1 = C * xi ** r1 * y
print('(d) j=1:', frozen(v1, C * xi ** (r1 + 1) / (r1 + 1), -C * xi ** r1 * y))
r3 = (gg - 2) / Am
v3 = C * xi ** r3 * y ** 3 - 3 * gg * C / ((Am - 1) * (r3 + 1) * (r3 + 2)) * xi ** (r3 + 2) * y
dw3 = -3 * Am * C / ((Am - 1) * (r3 + 1) * (r3 + 3)) * xi ** (r3 + 3)
da2 = 3 * C / (r3 + 1) * xi ** (r3 + 1)
u1 = dw3 + da2 * y ** 2
# u_2 from div u = 0 (odd in y, vanishing on the axis)
u2 = -sp.integrate(sp.diff(u1, xi), (y, 0, y))
print('(d) j=3 with companion (u_2 from div):', [sp.simplify(e) for e in frozen(v3, u1, u2)])
# companion needed: v = C xi^r y^3 alone, general u_1 = a(xi) + b(xi) y^2, u_2 from div
a_, b_ = sp.Function('a')(xi), sp.Function('b')(xi)
u1g = a_ + b_ * y ** 2
u2g = -sp.integrate(sp.diff(u1g, xi), (y, 0, y))
tr, dv, cu = frozen(C * xi ** r3 * y ** 3, u1g, u2g)
trp = sp.Poly(sp.expand(tr), y)
cup = sp.Poly(sp.expand(cu), y)
print('(d) j=3 alone: transport coefficients in y:', [sp.simplify(c) for c in trp.all_coeffs()])
print('(d) j=3 alone: curl coefficients in y     :', [sp.simplify(c) for c in cup.all_coeffs()])
# orbit ratio companion / main along xi = s y^A
s = sp.symbols('s', positive=True)
print('(d) companion/main on xi = s y^A:', sp.simplify((xi ** (r3 + 2) * y / (xi ** r3 * y ** 3)).subs(xi, s * y ** Am)))
print('(d) gap of mu_j + j between j and j + 2:', sp.simplify(((1 + gg + (Am - 1) * 5) - (1 + gg + (Am - 1) * 3)) / Am),
      '=', (2 * (Ax3 - 1) / Ax3))
