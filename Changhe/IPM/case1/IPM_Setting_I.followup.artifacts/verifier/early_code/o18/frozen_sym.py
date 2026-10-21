# (o18)(b): physical-space check of the fred31 frozen solutions (own route, no Fourier transform).
# Frozen model: E[v] + g U_2[v] = 0, E = A s d_s + y d_y - 1, -Laplace U_2[v] = d_s^2 v.
# For v homogeneous of degree d and odd in y, put U := -E[v]/g.  Then -Laplace U = d_s^2 v  <=>  Laplace E[v] = g v_ss.
# Since d_y E[v] = (A s d_s + y d_y) v_y, it suffices that Laplace((A s d_s + y d_y) phi) = g phi_ss for phi = v_y
# (the remaining function of s alone vanishes because both sides are odd in y).
import sympy as sp
s, y, t = sp.symbols('s y t', real=True)
A = sp.symbols('A', positive=True)
R2 = s**2 + y**2
lap = lambda f: sp.diff(f, s, 2) + sp.diff(f, y, 2)
for name, phi, g in [('V_A', R2**((A - 1)/2), A**2 - 1), ('Q_A', s*R2**((2*A - 3)/2), (A - 1)*(2*A + 1))]:
    lhs = lap(A*s*sp.diff(phi, s) + y*sp.diff(phi, y)) - g*sp.diff(phi, s, 2)
    print(name, ': Laplace((A s d_s + y d_y) phi) - g phi_ss =', sp.simplify(lhs))
    # control: wrong g
    lhs2 = lap(A*s*sp.diff(phi, s) + y*sp.diff(phi, y)) - (g + 1)*sp.diff(phi, s, 2)
    print('   control with g + 1:', sp.simplify(lhs2) == 0)
# Euler: E[v] = (d - 1 + (A - 1) s d_s) v for v homogeneous of degree d (V_A: d = A; Q_A: d = 2A - 1)
# axis jets (16): expand v_y in y at s = -r < 0 and integrate
r = sp.symbols('r', positive=True)
for name, phi in [('V_A', R2**((A - 1)/2)), ('Q_A', s*R2**((2*A - 3)/2))]:
    ser = sp.series(phi.subs(s, -r), y, 0, 6).removeO()
    v = sp.integrate(ser, (y, 0, y))
    G3 = sp.simplify(sp.expand(v).coeff(y, 3)); G5 = sp.simplify(sp.expand(v).coeff(y, 5))
    print(name, ': G_3(-r) =', sp.factor(G3), '  G_5(-r) =', sp.factor(G5))
    for Av in [sp.Rational(7, 4), 2, sp.Rational(5, 2)]:
        print('    A = %s: Z_3 = %s, Z_5 = %s' % (Av, sp.simplify((r**(2/A)*G3).subs(A, Av)),
                                              sp.simplify((r**(4/A)*G5).subs(A, Av))))
# Q_2 closed form (14) and the cone value (17)
Q2 = s/2*(y*sp.sqrt(R2) + s**2*sp.asinh(y/(-s)))      # on s < 0, |s| = -s
sneg = sp.symbols('sn', negative=True)
print('Q_2: d_y (14) - s sqrt(s^2+y^2) =', sp.simplify((sp.diff(Q2, y) - s*sp.sqrt(R2)).subs(s, sneg)))
k = sp.symbols('kappa', positive=True)
print('d_y^4 Q_2(-r, kappa r) =', sp.simplify(sp.diff(s*sp.sqrt(R2), y, 3).subs({s: -r, y: k*r})))
# homogeneity degree vs h/A, h = 1 + g*
for name, d, g in [('V_A', A, A**2 - 1), ('Q_A', 2*A - 1, (A - 1)*(2*A + 1))]:
    print(name, ': (1 + g)/A - d =', sp.simplify((1 + g)/A - d))
