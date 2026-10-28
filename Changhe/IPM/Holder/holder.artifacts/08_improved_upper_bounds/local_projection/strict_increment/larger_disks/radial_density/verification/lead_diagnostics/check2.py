import sympy as sp
v, al = sp.symbols('v alpha')
A = ((1-v)**al + (1+v)**al)/2
d = sp.diff(A, v, 4) + al*(1-al)*(2-al)*(3-al)*((1-v)**(al-4)+(1+v)**(al-4))/2
for a in [sp.Rational(1,10), sp.Rational(1,2), sp.Rational(9,10)]:
    for vv in [sp.Rational(1,7), sp.Rational(2,3)]:
        print(a, vv, sp.N(d.subs({al:a, v:vv}), 30))
print(sp.simplify(sp.expand(sp.powsimp(d, force=True))))
