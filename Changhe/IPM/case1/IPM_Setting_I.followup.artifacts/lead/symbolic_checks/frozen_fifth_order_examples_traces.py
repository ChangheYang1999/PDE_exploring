# Lead check of a referee answer, section 3: axis limits (16), the Q_2 closed form (14) and the cone blow-up (17).
# (It does not check the frozen equation itself or the full-neighbourhood regularity; a separate referee answer covers those.)
import sympy as sp
s, y, t, r, k = sp.symbols('s y t r kappa', real=True)
A = sp.symbols('A', positive=True)
def G(v, j):  # j-th axis coefficient at s = -r
    return sp.simplify((sp.diff(v, y, j).subs(y, 0)/sp.factorial(j)).subs(s, -r))
V = lambda A_: sp.Integral((s**2+t**2)**((A_-1)/2), (t, 0, y))
Q = lambda A_: s*sp.Integral((s**2+t**2)**((2*A_-3)/2), (t, 0, y))
rp = sp.symbols('rp', positive=True)
for name, v, A_ in [('Q7/4', Q(sp.Rational(7, 4)), sp.Rational(7, 4)), ('Q2', Q(2), 2), ('V5/2', V(sp.Rational(5, 2)), sp.Rational(5, 2))]:
    Z3 = sp.simplify((rp**(2/A_)*G(v, 3)).subs(r, rp)); Z5 = sp.simplify((rp**(4/A_)*G(v, 5)).subs(r, rp))
    print(name, ' Z3 =', Z3, '  Z5 =', Z5)
Q2 = sp.Rational(1, 2)*s*(y*sp.sqrt(s**2+y**2) + s**2*sp.asinh(y/sp.Abs(s)))
d = sp.simplify(sp.diff(Q2, y) - s*sp.sqrt(s**2+y**2))
print('Q2 closed form: d_y difference =', d, ', value at y=0:', Q2.subs(y, 0))
q4 = sp.simplify(sp.diff(s*sp.sqrt(s**2+y**2), y, 3).subs({s: -rp, y: k*rp}))
print('d_y^4 Q2(-r, kappa r) =', sp.simplify(q4))
