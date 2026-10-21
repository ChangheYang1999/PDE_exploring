# Recheck of the Z' formula in fred27 (3.15) with m as a positive symbol (w = -g m), sympy could not combine the powers.
import sympy as sp
x, A = sp.symbols('x A', positive=True)
g = sp.Function('g', positive=True)(x); mf = sp.Function('m', positive=True)(x); a2 = sp.Function('a2')(x)
w = -g*mf
beta = 2/A
Q = a2/g**3; H = A**beta*g**3*mf**(-beta)
F3 = -a2*sp.diff(g, x) + g*sp.diff(a2, x)/3
e = F3/(w*H) + A**(-beta)/3*mf**(beta - 1)*sp.diff(Q, x)
print("Z' formula", sp.simplify(sp.powsimp(sp.expand(e), force=True)) == 0)
# numeric spot check with concrete functions
xs = sp.Rational(7, 10)
sub = {g: 1 + x**2, mf: 2 + sp.sin(x), a2: sp.cos(3*x)}
print('numeric', sp.N((e.subs(sub).doit()).subs({x: xs, A: sp.Rational(101, 10)}), 30))
