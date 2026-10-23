# Lead check of the moment (A3) of A.3.76(b) and of the exterior forms of the smoothed chart.
import sympy as sp
p,s,a,t=sp.symbols('p s a t',positive=True)
# F_* from (A2) with the jump p-1 of W_*' at 1: F = -s^p ( (p-1) + int_1^s t^{-p-1} p(p-1) t^{p-2} dt ) for s > 1
Fst=sp.simplify(-s**p*((p-1)+sp.integrate(t**(-p-1)*p*(p-1)*t**(p-2),(t,1,s))))
Ks=(1-p)*(p+2)/2; bs=-p*(1-p)/2
print('F_* check', sp.simplify(Fst-(Ks*s**p+bs*s**(p-2))))
W=s**p; T=p*sp.diff(W,s)*Fst-(p+1)*W*sp.diff(Fst,s); d=2*p-1
print('T_* check', sp.simplify(sp.expand(T-(-p*Ks*s**d+(p+2)*bs*s**(d-2)))))
# check (A2) on the exterior: W'' = pF - sF'
print('A2 check', sp.simplify(sp.diff(W,s,2)-(p*Fst-s*sp.diff(Fst,s))))
# finite parts on (1,inf): FP int_1^inf s^{d+1} = -1/(d+2), FP int_1^inf s^{d-1} = -1/d (0<d<1)
M=-(p+1)*(1-p)+(-p*Ks)*(-1/(d+2))+((p+2)*bs)*(-1/d)
print('A3 check', sp.simplify(M-(1-p)**2*(2*p**2+2*p+1)/(4*p**2-1)))
# jump term: int s*(-(p+1)) W(1) * (1-p) delta_1 = -(p+1)(1-p); the F_* jump at 1 is F_*(1+) - 0
print('jump', sp.simplify(Fst.subs(s,1)-(1-p)))
# smoothed exterior: F_e(s) = int exp((p-2)a) F_*(s e^{-a}) eta_e da -> K_* s^p int e^{-2a} eta_e + b_* s^{p-2} int eta_e
print('Fe exterior', sp.simplify(sp.expand(sp.exp((p-2)*a)*(Ks*(s*sp.exp(-a))**p+bs*(s*sp.exp(-a))**(p-2)) - (Ks*s**p*sp.exp(-2*a)+bs*s**(p-2)))))
# W_e exterior: int exp(pa) (s e^{-a})^p eta_e = s^p
print('We exterior', sp.simplify(sp.exp(p*a)*(s*sp.exp(-a))**p - s**p))
for pv in (sp.Rational(3,5),sp.Rational(3,4),sp.Rational(9,10)): print('M_* at p =',pv,float(M.subs(p,pv)))
