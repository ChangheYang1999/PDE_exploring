"""New symbolic reconstruction of R12's third/fifth axis equations.
No code from a teammate or previous verifier is used.
"""
import json
from pathlib import Path
import sympy as s
import mpmath as mp
A,u,L=s.symbols('A u L',positive=True)
S=6*A*(4*A-3)/(8*A-1)
dx=lambda f:s.diff(f,u)/L
w=-A*L*u*(1-u*u)/(1+u*u)
g=L*L*u*u/(1+u*u)
h=A+1-dx(w)
a2=(dx(g)-dx(dx(w)))/2
G3=10*A*u*u/((8*A-1)*(1+u*u)**3)
F3=-a2*dx(g)+dx(a2)*g/3
T3=s.factor(w*dx(G3)+(3*h-1)*G3-F3)
T3zero=s.factor(T3.subs(L,s.sqrt(S)))
assert T3zero==0
b3=-dx(a2)/3
a4=(dx(b3)+dx(G3))/4
b5=-dx(a4)/5
F5=s.factor(-a2*dx(G3)-3*b3*G3-a4*dx(g)-b5*g)
F5=s.factor(F5.subs(L,s.sqrt(S)))
poly=s.Poly(s.cancel(F5*(1+u*u)**6/u**2),u)
assert all(m[0]%2==0 for m in poly.monoms())
q=4/A
aa=-4-2/A
# Each u^(2j) moment contributes beta(aa+j,q)/2.
# Reduction uses the beta recurrence, derived from integration by parts.
ratio=0
for (power,),coef in poly.terms():
 j=power//2
 ratio+=coef*s.rf(aa,j)/s.rf(aa+q,j)
ratio=s.factor(ratio/(2*A))
P=1248*A**4-548*A**3+297*A*A-178*A+84
claimed=P/(15*A*(2*A-1)*(3*A-2)*(4*A-3)*(8*A-1))
assert s.factor(ratio-claimed)==0
# A=2 is evaluated as the Laurent polynomial integral, not by a parameter limit.
p2=s.expand(poly.as_expr().subs(A,2)*u**(-11)*(1-u*u))
fp2=0
residue=0
for term in s.Add.make_args(p2):
 coeff,exp=term.as_coeff_exponent(u)
 if exp==-1:residue+=coeff
 else:fp2+=coeff/(exp+1)
Bres=s.factor(fp2/(2*2**12))
assert residue==0 and Bres==s.Rational(11,1474560)
# The limiting beta ratio can be evaluated without gamma at its poles:
# a=-5+(A-2)/2+O((A-2)^2), a+q=-3-(A-2)/2+O((A-2)^2).
betalimit=-s.Rational(1,20)
Blimit=s.factor(claimed.subs(A,2)*betalimit/2**12)
assert Blimit == -s.Rational(11,1474560)
assert Blimit-Bres == -s.Rational(11,737280)
mp.mp.dps=55
rows=[]
for val in ['1.05','1.25','1.5','1.8','1.95','2.001','2.5','3','3.5','3.9']:
 av=mp.mpf(val); sv=6*av*(4*av-3)/(8*av-1); lv=mp.sqrt(sv)
 pv=1248*av**4-548*av**3+297*av**2-178*av+84
 bv=pv*mp.beta(-4-2/av,4/av)/(15*av*(2*av-1)*(3*av-2)*(4*av-3)*(8*av-1)*lv**(10+4/av))
 rows.append({'A':val,'B5':mp.nstr(bv,42),'natural':mp.nstr(bv*lv**(6+4/av),42)})
result={'T3_on_S':str(T3zero),'F5':str(F5),'reduced_Beta_coefficient':str(ratio),
 'P_shift':str(s.Poly(s.expand(P.subs(A,1+u)),u).as_expr()),
 'resonant_log_coefficient':str(residue),'resonant_B5':str(Bres),
 'curve_limit_B5':str(Blimit),'jump':str(Blimit-Bres),'rows':rows}
print(json.dumps(result,indent=2))
Path('verifier/fifth-order/verification/axis.json').write_text(json.dumps(result,indent=2)+'\n')
