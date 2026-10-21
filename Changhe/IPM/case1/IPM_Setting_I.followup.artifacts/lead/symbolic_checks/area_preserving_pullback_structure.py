# Lead check of the referee's counterexample structure for a generic generating function F(s,v).
import sympy as sp
s, v, A = sp.symbols('s v A')
F = sp.Function('F')(s, v)
Fs, Fv = sp.diff(F, s), sp.diff(F, v)
J = 1 + sp.diff(F, s, v)
vs = -sp.diff(F, s, 2)/J; vy = 1/J          # from y = v + F_s(s,v)
def Ds(e): return sp.diff(e, s) + vs*sp.diff(e, v)   # d/ds at fixed y
def Dy(e): return vy*sp.diff(e, v)                   # d/dy at fixed s
u = s + Fv
a = (A*(s + Fv) - v*sp.diff(F, v, 2))/J
b = J*v + sp.diff(F, s, 2)*a
print('jacobian', sp.simplify(Ds(u)*Dy(v) - Dy(u)*Ds(v) - 1))
print('W.grad u - A u', sp.simplify(a*Ds(u) + b*Dy(u) - A*u))
print('W.grad v - v', sp.simplify(a*Ds(v) + b*Dy(v) - v))
print('div W - (A+1)', sp.simplify(Ds(a) + Dy(b) - (A + 1)))
