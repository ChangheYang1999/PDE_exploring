# lead check (2026-10-21T18:00Z) of the new d78 A.3.80 identities: (A8) <=> phi(u_*) = 0, the formula for v_1 and T,
# 13/z - 1/(z - 1) = -2n/z at d = 13. The d = 13 quadratic and discriminant: research/p_ext/e3_m13_check.py.
import sympy as sp
z,A0=sp.symbols('z A0')
vs=sp.symbols('w1:5'); As=sp.symbols('a1:5')
ust=1/z-1
phi=A0/ust+sum(a/(ust-(1/v-1)) for a,v in zip(As,vs))
dd=A0+sum(As)
A8=A0/(z-1)+sum(a/(z-v) for a,v in zip(As,vs))-dd/z
print('phi(u_*)/A8 =',sp.factor(sp.simplify(phi/A8)))
P,A1,b,v1,d,n=sp.symbols('P A1 b v1 d n')
zz=2*P/(2*P-1)
sol=sp.solve(sp.Eq(A0/(zz-1)+(A1-b)/(zz-v1),d/zz),v1)[0]
T=2*P*A0-d
print('v1 formula, T:',sp.simplify(sol-zz*(1+(A1-b)/T)), sp.expand(T.subs(P,(d+2*n)/2)-((A0-1)*d+2*A0*n)))
zn=(13+2*n)/(12+2*n)
print('d = 13:',sp.simplify(13/zn-1/(zn-1)+2*n/zn), sp.simplify(zn/(zn-1)-(13+2*n)))
