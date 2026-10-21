"""verifier: (n5), the normalized hierarchy of FINAL_REPORT 6.4 (line 1839), sympy.
 y^3 equation w G3' + (3h - 1) G3 = (g^4/3) Q', h = A + 1 - w', axis law w g' = (w' - A) g, z = G3/g^3.
 Claims: (i) the equation is g^3 (w z' + 2 z - (g/3) Q') = 0; (ii) with m = -w/g, dm/dx = -A/g it reads
 A m z_m + 2 z = -(A/3) Q_m; (iii) z_P = -(1/3) sum_j j q_j m^(j-1)/(j-1+beta) solves it with P; (iv) Z = z - z_P gives
 (m^beta Z)_m = -(1/3) m^(beta-1) R_m."""
import sympy as sp
x, A, mm = sp.symbols('x A m', positive=True)
q1, q3, q5, Qs = sp.symbols('q1 q3 q5 Qs')
w, g, z, Q = [sp.Function(n)(x) for n in ('w', 'g', 'z', 'Q')]
gp = (sp.diff(w, x) - A) * g / w
G3 = g**3 * z
h = A + 1 - sp.diff(w, x)
lhs = w * sp.diff(G3, x) + (3 * h - 1) * G3 - g**4 / 3 * sp.diff(Q, x)
res1 = sp.simplify(sp.expand(lhs.subs(sp.Derivative(g, x), gp)) - g**3 * (w * sp.diff(z, x) + 2 * z - g / 3 * sp.diff(Q, x)))
print('(i)  lhs - g^3 (w z\' + 2 z - (g/3) Q\') =', res1)
# (ii) chain rule: d/dx = -(A/g) d/dm, w = -m g
zf, Qf = sp.Function('zm'), sp.Function('Qm')
gg = sp.Symbol('g', positive=True)
e2 = (-mm * gg) * (-(A / gg)) * sp.diff(zf(mm), mm) + 2 * zf(mm) - gg / 3 * (-(A / gg)) * sp.diff(Qf(mm), mm)
print('(ii) w z\' + 2 z - (g/3) Q\' - (A m z_m + 2 z + (A/3) Q_m) =', sp.simplify(e2 - (A * mm * sp.diff(zf(mm), mm) + 2 * zf(mm) + A / 3 * sp.diff(Qf(mm), mm))))
be = 2 / A
P = q5 * mm**5 + q3 * mm**3 + q1 * mm
zP = -sp.Rational(1, 3) * sum(j * q * mm**(j - 1) / (j - 1 + be) for j, q in ((1, q1), (3, q3), (5, q5)))
print('(iii) A m zP_m + 2 zP + (A/3) P_m =', sp.simplify(A * mm * sp.diff(zP, mm) + 2 * zP + A / 3 * sp.diff(P, mm)))
Z, R = sp.Function('Z')(mm), sp.Function('R')(mm)
# z = Z + zP, Q = R + P + Qs satisfy (ii) iff ...
e4 = A * mm * sp.diff(Z + zP, mm) + 2 * (Z + zP) + A / 3 * sp.diff(R + P + Qs, mm)
print('(iv) (A/m^(beta-1)) [(m^beta Z)_m + (1/3) m^(beta-1) R_m] - e(ii) =',
      sp.simplify(sp.expand(A / mm**(be - 1) * (sp.diff(mm**be * Z, mm) + mm**(be - 1) * sp.diff(R, mm) / 3)) - e4))
