"""verifier: lead notes S-18 (a), own sympy derivation. Profile system W.grad(rho) = rho, W = c_l X + U, U = (-psi_y, psi_x),
-Laplace psi = d_x rho; rho = g y + G3 y^3, psi = y p1 + y^3 p3 + y^5 p5 (odd in y). Checks: p3 = -(g' - w'')/6 with
w = c_l x - p1; W_1 = w + a2 y^2 + O(y^4), a2 = (g' - w'')/2; W_2 = h y + b3 y^3, b3 = -a2'/3; the y^1 and y^3 equations;
F3 = (g^4/3) Q', Q = a2/g^3 = (1/2) d_y^2 W_1/(d_y rho)^3 at y = 0; H3 = A^b g^(3+b) (-w)^(-b) solves w H' + (3h - 1) H = 0;
-F3/(w H3) = Q' m^(b-1)/(3 A^b), m = -w/g (w < 0)."""
import sympy as sp
x, y, cl = sp.symbols('x y c_l', positive=True)
g, G3, p1, p3, p5 = [sp.Function(n)(x) for n in ('g', 'G3', 'p1', 'p3', 'p5')]
rho = g * y + G3 * y**3
psi = y * p1 + y**3 * p3 + y**5 * p5
eq = sp.expand(-(sp.diff(psi, x, 2) + sp.diff(psi, y, 2)) - sp.diff(rho, x))
p3sol = sp.solve(eq.coeff(y, 1), p3)[0]
w = cl * x - p1
print('p3 + (g\' - w\'\')/6 =', sp.simplify(p3sol + (sp.diff(g, x) - sp.diff(w, x, 2)) / 6))
W1 = cl * x - sp.diff(psi, y)
W2 = cl * y + sp.diff(psi, x)
a2 = sp.expand(W1).coeff(y, 2).subs(p3, p3sol)
print('a2 - (g\' - w\'\')/2 =', sp.simplify(a2 - (sp.diff(g, x) - sp.diff(w, x, 2)) / 2))
b3 = sp.expand(W2).coeff(y, 3).subs(p3, p3sol)
print('b3 + a2\'/3 =', sp.simplify(b3 + sp.diff(a2, x) / 3), '; div W - 2 c_l =', sp.simplify(sp.diff(W1, x) + sp.diff(W2, y) - 2 * cl))
h = sp.expand(W2).coeff(y, 1)
T = sp.expand(W1 * sp.diff(rho, x) + W2 * sp.diff(rho, y) - rho)
A = 2 * cl - 1
e1 = T.coeff(y, 1)
print('y^1: (w g\' - (w\' - A) g) - eq =', sp.simplify(e1 - (w * sp.diff(g, x) - (sp.diff(w, x) - A) * g)), '; h - (A + 1 - w\') =', sp.simplify(h - (A + 1 - sp.diff(w, x))))
e3 = sp.expand(T.coeff(y, 3).subs(p3, p3sol))
Q = a2 / g**3
F3 = g**4 * sp.diff(Q, x) / 3
print('y^3: eq - [w G3\' + (3h - 1) G3 - F3] =', sp.simplify(e3 - (w * sp.diff(G3, x) + (3 * h - 1) * G3 - F3)))
print('Q - (1/2) d_y^2 W_1/(d_y rho)^3 at y = 0:', sp.simplify(Q - (sp.diff(W1, y, 2) / 2 / sp.diff(rho, y)**3).subs(y, 0).subs(p3, p3sol)))
b = 2 / A
H3 = A**b * g**(3 + b) * (-w)**(-b)
lawg = {sp.diff(g, x): (sp.diff(w, x) - A) * g / w}
print('w H3\' + (3h - 1) H3 with the axis law, / H3:', sp.simplify(((w * sp.diff(H3, x) + (3 * h - 1) * H3) / H3).subs(lawg)))
m = -w / g
print('-F3/(w H3) - Q\' m^(b-1)/(3 A^b):', sp.simplify(sp.powsimp(sp.powdenest(-F3 / (w * H3) - sp.diff(Q, x) * m**(b - 1) / (3 * A**b), force=True), force=True)))
# the last two residuals are 0 only after combining powers with -w > 0, g > 0 (sympy does not); numeric substitution:
H3res = sp.simplify(((w * sp.diff(H3, x) + (3 * h - 1) * H3) / H3).subs(lawg))
F3res = -F3 / (w * H3) - sp.diff(Q, x) * m**(b - 1) / (3 * A**b)
for cv, xv in [(5.5753626, 0.7), (3.2, 2.1)]:
    sub = {p1: cl * x + x * (1 + x**2 / 7) / (1 + x**2 / 11), g: x**2 * (1 + x**2 / 5) / (1 + x**2 / 13)}
    r1 = H3res.subs(sub).doit().subs({cl: cv, x: xv}).evalf(30)
    r2 = F3res.subs(sub).doit().subs({cl: cv, x: xv}).evalf(30)
    print('numeric (c_l, x) = (%g, %g): H3 equation residual %s, -F3/(w H3) - Q\' m^(b-1)/(3A^b) = %s (Q\' m^(b-1)/(3A^b) = %s)' % (
        cv, xv, sp.N(r1, 3), sp.N(r2, 3), sp.N((sp.diff(Q, x) * m**(b - 1) / (3 * A**b)).subs(sub).doit().subs({cl: cv, x: xv}), 6)))
