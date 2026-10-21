"""Independent exact identities, not imported from another lane's code."""
import sympy as S
import json
from pathlib import Path
s,y=S.symbols('s y')
a,b,f=(S.Function(n)(s,y) for n in ('a','b','f'))
D=lambda z:a*S.diff(z,s)+b*S.diff(z,y)
h=S.diff(f,y)/a
K=S.diff(f,y,4)-h*S.diff(a,y,3)
forcing=(S.diff(a,y)*S.diff(a,y,3)/a-S.diff(a,y,4))*(S.diff(f,s)+b*h)
forcing-=sum(S.binomial(4,k)*S.diff(a,y,k)*S.diff(f,s,y,4-k) for k in range(1,4))
forcing-=sum(S.binomial(4,k)*S.diff(b,y,k)*S.diff(f,y,5-k) for k in range(2,4))
forcing+=(S.diff(a,s)-3*S.diff(b,y))*h*S.diff(a,y,3)
E=D(f)-f; V=S.diff(a,s)+S.diff(b,y)
defect=S.expand(D(K)+(4*S.diff(b,y)-1)*K-forcing-S.diff(E,y,4)+S.diff(a,y,3)/a*S.diff(E,y)+S.diff(f,y)*S.diff(V,y,3))
assert defect==0
r,v,l,t,q=S.symbols('r v l t q',positive=True)
c=S.Function('c')(t); A=4/q
Dr=lambda z:S.diff(z,r)+S.diff(z,l)/r-t*S.diff(z,t)/(r*l)
Dv=lambda z:S.diff(z,v)+S.diff(z,t)/(v*l)
F=r**(1-q)*v**5*c/(q-1)
Fs=-Dr(F); Fv=Dv(F); Fsv=Dv(Fs); Fvv=Dv(Fv)
expected=r**(1-q)*v**4/(q-1)*(5*(A*t-1)*S.diff(c,t)/l+((A*t-1)*S.diff(c,t,2)+A*S.diff(c,t))/l**2)
log_defect=S.simplify((A*Fv-v*Fvv+A*r*Fsv-expected)/(r**(1-q)*v**4))
assert log_defect==0
core_n=S.simplify((A*Fv-v*Fvv+A*r*Fsv).subs({S.diff(c,t,2):0,S.diff(c,t):0,c:1}))
assert core_n==0
core_y=v+r**(-q)*v**5
# b-y when a=As and c=1, evaluated directly from the generating formulas.
core_b=S.simplify((-A*r)*(-Dr(Fs))+v*(1+Fsv)-core_y)
core_b=S.simplify(core_b.subs({S.diff(c,t,2):0,S.diff(c,t):0,c:1}))
assert core_b==0
leading=expected
for _ in range(4): leading=Dv(leading)
leading=S.simplify(S.limit(l*leading/r**(1-q),l,S.oo))
expected_leading=120*(A*t-1)*S.diff(c,t)/(q-1)
assert S.simplify(leading-expected_leading)==0
result={'unrestricted_K4_defect':str(defect),'log_cutoff_horizontal_defect':str(log_defect),'core_horizontal_correction':str(core_n),'core_vertical_correction':str(core_b),'log_cutoff_leading_fourth_derivative':str(leading),'status':'all exact symbolic assertions passed'}
p=Path(__file__).resolve().parents[1]/'verification'/'identities.json'
p.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
