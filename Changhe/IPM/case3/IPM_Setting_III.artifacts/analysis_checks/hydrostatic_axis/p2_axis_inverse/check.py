# lead hand-check of the elementary axis inverse at P = 2 (verifier item of 15:10Z): dV/dy = k(w), V(0) = 0
import sympy as sp
t,C=sp.symbols('t C',positive=True)
d=7; k=sp.symbols('k1:%d'%(d+1))
w=1-t**2; y=C*t/(1-t**2)**2
P=-3*k[1]*t+sum(k[j-1]*sum((-1)**m*sp.binomial(j-3,m)*(t**(2*m+1)/(2*m+1)+3*t**(2*m+3)/(2*m+3)) for m in range(j-2)) for j in range(3,d+1))
V=C*(2*k[0]*t/(1-t**2)+(4*k[1]-k[0])*sp.atanh(t)+P)
kw=sum(k[j-1]*w**j for j in range(1,d+1))
print('dV/dt - k(w) dy/dt =',sp.simplify(sp.diff(V,t)-kw*sp.diff(y,t)))
print('V(0) =',V.subs(t,0))
print('dy/dt =',sp.factor(sp.diff(y,t)))
