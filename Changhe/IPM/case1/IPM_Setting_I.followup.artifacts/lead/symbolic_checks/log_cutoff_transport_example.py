# Lead check of the referee's example (M): logarithmic cutoff F = r^(1-q) v^5 c(log v/log r)/(q-1), s = -r, A q = 4.
import sympy as sp
r, v, A = sp.symbols('r v A', positive=True)
s = sp.Symbol('s', negative=True)
c = sp.Function('c')
q = 4/A
rr = -s
ell = sp.log(rr)
t = sp.log(v)/ell
F = rr**(1-q)*v**5*c(t)/(q-1)
Fv, Fs = sp.diff(F, v), sp.diff(F, s)
Fvv, Fsv, Fss = sp.diff(F, v, 2), sp.diff(F, s, v), sp.diff(F, s, 2)
J = 1 + Fsv
a = (A*(s + Fv) - v*Fvv)/J
T = sp.Symbol('T')
cp = sp.diff(c(T), T).subs(T, t); cpp = sp.diff(c(T), T, 2).subs(T, t)
M = rr**(1-q)*v**4/((q-1)*J)*(5*(A*t-1)*cp/ell + ((A*t-1)*cpp + A*cp)/ell**2)
d = sp.simplify((a - A*s - M).doit())
print('a - As - (M):', d)
# numeric spot check with a concrete c
cc = lambda T: sp.tanh(T-4)
sub = {A: sp.Rational(3, 2), s: -sp.Rational(1, 7), v: sp.Rational(1, 3000)}
expr = (a - A*s - M).subs(c, sp.Lambda(T, sp.tanh(T-4))).doit()
print('numeric:', sp.N(expr.subs(sub), 20), ' scale of a-As:', sp.N((a - A*s).subs(c, sp.Lambda(T, sp.tanh(T-4))).doit().subs(sub), 10))
