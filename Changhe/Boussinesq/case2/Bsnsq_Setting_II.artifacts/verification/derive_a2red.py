# Independent symbolic check of (P) -> (A2-red) and center relations.
import sympy as sp
x, y, b = sp.symbols('x y beta', real=True)
s, t = sp.symbols('s t', positive=True)
F = sp.Function('F'); G = sp.Function('G'); H = sp.Function('H')
Th = y*F(x**2, y**2); Om = x*y*G(x**2, y**2); Ps = x*y*H(x**2, y**2)
U1 = -sp.diff(Ps, y); U2 = sp.diff(Ps, x)
W1 = b*x + U1; W2 = b*y + U2
RO = W1*sp.diff(Om, x) + W2*sp.diff(Om, y) + Om - sp.diff(Th, x)
RT = W1*sp.diff(Th, x) + W2*sp.diff(Th, y) - (b-2)*Th
E = -(sp.diff(Ps, x, 2) + sp.diff(Ps, y, 2)) - Om
def to_st(expr):
    # replace derivatives of F(x^2,y^2) by s,t forms
    fs, ft = sp.symbols('fs ft')
    e = sp.expand(expr)
    rep = {}
    return e
# build reduced forms by hand and compare
Fs = sp.Function('F')
def red(fun):
    return fun
S, T = sp.symbols('S T', positive=True)
f = sp.Function('f')(S, T); g = sp.Function('g')(S, T); h = sp.Function('h')(S, T)
A = b - h - 2*T*sp.diff(h, T)
B = b + h + 2*S*sp.diff(h, S)
eqF = 2*S*A*sp.diff(f, S) + 2*T*B*sp.diff(f, T) + (B - b + 2)*f
eqG = 2*S*A*sp.diff(g, S) + 2*T*B*sp.diff(g, T) + (A + B + 1)*g - 2*sp.diff(f, S)
eqH = 4*S*sp.diff(h, S, 2) + 6*sp.diff(h, S) + 4*T*sp.diff(h, T, 2) + 6*sp.diff(h, T) + g
# substitute S=x^2,T=y^2 in the reduced equations and compare with Cartesian residuals
def sub(expr):
    return expr.subs({S: x**2, T: y**2})
# Cartesian residuals use F(x^2,y^2) with sympy Subs derivatives; replace F->f etc.
RT2 = RT.subs({F: sp.Lambda((S, T), f.func(S, T))})
# Simplest: test with concrete polynomial/test functions
import random
fx = S**2*T + 3*S*T**2 - 2*S + 0.5*T**3 + 7*S**3
gx = 1 + S - 4*T + S*T**2 - 3*S**2
hx = 2 - S*T + 5*T**2 + S**3 - 2*S*T
subsd = {f: fx, g: gx, h: hx}
def conc(eq):
    return sp.expand(eq.subs(subsd).doit())
eF = conc(eqF); eG = conc(eqG); eH = conc(eqH)
ThC = y*fx.subs({S: x**2, T: y**2}); OmC = x*y*gx.subs({S: x**2, T: y**2}); PsC = x*y*hx.subs({S: x**2, T: y**2})
U1c = -sp.diff(PsC, y); U2c = sp.diff(PsC, x)
W1c = b*x + U1c; W2c = b*y + U2c
ROc = sp.expand(W1c*sp.diff(OmC, x) + W2c*sp.diff(OmC, y) + OmC - sp.diff(ThC, x))
RTc = sp.expand(W1c*sp.diff(ThC, x) + W2c*sp.diff(ThC, y) - (b-2)*ThC)
Ec = sp.expand(-(sp.diff(PsC, x, 2) + sp.diff(PsC, y, 2)) - OmC)
print('RT == y*eqF :', sp.simplify(RTc - y*eF.subs({S: x**2, T: y**2})) == 0)
print('RO == x*y*eqG :', sp.simplify(ROc - x*y*eG.subs({S: x**2, T: y**2})) == 0)
print('E == -x*y*eqH... :', sp.simplify(Ec + x*y*eH.subs({S: x**2, T: y**2})) == 0, '(E = -xy*(Lap_red H + G))')
print('W1 == x*A :', sp.simplify(W1c - x*A.subs(subsd).doit().subs({S: x**2, T: y**2})) == 0)
print('W2 == y*B :', sp.simplify(W2c - y*B.subs(subsd).doit().subs({S: x**2, T: y**2})) == 0)
# center relations from the Taylor jets
a0, b0, c, a1, a2 = sp.symbols('a0 b0 c a1 a2')
# Theta = a0 x^2 y + ..., Psi = c x y + ..., Omega = b0 x y + ...
ThL = a0*x**2*y; PsL = c*x*y; OmL = b0*x*y
W1L = b*x - sp.diff(PsL, y); W2L = b*y + sp.diff(PsL, x)
rt = sp.expand(W1L*sp.diff(ThL, x) + W2L*sp.diff(ThL, y) - (b-2)*ThL)
print('x^2y coefficient of R_Theta:', sp.factor(rt.coeff(x, 2).coeff(y, 1)), '-> c =', sp.solve(rt.coeff(x, 2).coeff(y, 1), c))
ro = sp.expand(W1L*sp.diff(OmL, x) + W2L*sp.diff(OmL, y) + OmL - sp.diff(ThL, x))
cc = sp.solve(rt.coeff(x, 2).coeff(y, 1), c)[0]
print('xy coefficient of R_Omega:', sp.factor(ro.coeff(x, 1).coeff(y, 1).subs(c, cc)), '-> b0 =', sp.solve(ro.coeff(x, 1).coeff(y, 1).subs(c, cc), b0))
print('DW(0) =', sp.Matrix([[sp.diff(W1L, x), sp.diff(W1L, y)], [sp.diff(W2L, x), sp.diff(W2L, y)]]).subs(c, cc))
