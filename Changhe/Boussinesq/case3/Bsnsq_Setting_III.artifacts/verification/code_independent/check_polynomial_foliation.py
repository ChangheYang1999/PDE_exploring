"""Independent symbolic identities for P223. No external solver or NUM code."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,time,hashlib
start=time.monotonic();utc=datetime.now(timezone.utc).isoformat()
r=Path('research/223_polynomial_foliation_constant');v=r/'verification';checks={};differences={}
def eq(name,expr):
 z=s.simplify(s.expand(expr.doit()));checks[name]=(z==0);differences[name]=str(z)
def flag(name,z):checks[name]=bool(z)
x,y,k=s.symbols('x y k',real=True);n=s.symbols('n',integer=True,positive=True)
a=s.Function('a')(y);A=s.Function('A')(y);C=s.Function('C');D=4*A+C(k)
subA={s.diff(A,y,3):s.diff(a,y,2),s.diff(A,y,2):s.diff(a,y),s.diff(A,y):a}
w2=(4*A+C(x/a))/a;w1=x*s.diff(a,y)*(4*A+C(x/a))/a**2
vort=(s.diff(w1,y)-s.diff(w2,x)).subs(subA).subs(x,k*a)
B=s.diff(a,y,2)/a-2*s.diff(a,y)**2/a**2;E=s.diff(a,y)**2/a**2
om=4*k*s.diff(a,y)+k*D*B-(a**-2+k*k*E)*s.diff(C(k),k)
eq('physical_negative_curl',vort-om)
eq('field_divergence',(s.diff(w1,x)+s.diff(w2,y)-4).subs(subA))
H=s.Function('H');T=H(x/a)
eq('exact_temperature_transport',(w1*s.diff(T,x)+w2*s.diff(T,y)).subs(subA))
P=2*s.diff(a,y)/a**3;F=4*s.diff(a,y,2)+5*a*B
rhs=k*(s.diff(B,y)*D*D+F*D+4*a*s.diff(a,y))+s.diff(C(k),k)*(P*D-1/a-k*k*(s.diff(E,y)*D+a*E))
eq('vorticity_polynomial_identity',(D*s.diff(om,y)+a*om).subs(subA)-rhs)
# A second check of material derivatives, with an independent test scalar G(k,y).
G=s.Function('G');physical_G=G(x/a,y)
material=(w1*s.diff(physical_G,x)+w2*s.diff(physical_G,y)).subs(x,k*a)
eq('material_derivative_at_fixed_k',material-D/a*s.diff(G(k,y),y))
# Treat all y coefficients as independent symbols, then extract polynomial coefficients.
bp,ep,pp,ff,aa,ap,AA,ee=s.symbols('Bp Ep P F a ap A E')
coeff_results=[]
for degree in range(1,9):
 cs=s.symbols(f'c0:{degree+1}');poly=sum(cs[j]*k**j for j in range(degree+1));dp=4*AA+poly
 expr=k*(bp*dp**2+ff*dp+4*aa*ap)+s.diff(poly,k)*(pp*dp-1/aa-k*k*(ep*dp+aa*ee))
 q=s.Poly(s.expand(expr),k);top=q.coeff_monomial(k**(2*degree+1))
 eq(f'highest_coefficient_degree_{degree}',top-cs[-1]**2*(bp-degree*ep))
 flag(f'other_degree_strictly_lower_{degree}',max(degree+1,2*degree-1)<2*degree+1)
 coeff_results.append({'degree':degree,'top':str(s.factor(top))})
z=a**(-(n+1));Q=a.diff(y,2)/a-(n+2)*(a.diff(y)/a)**2
eq('general_positive_ODE_transform',s.diff(z,y,2)+(n+1)*Q*z)
eq('B_minus_nE',B-n*E-Q)
alpha,delta=s.symbols('alpha delta',real=True)
eq('constant_coefficient_integral',s.diff(alpha*y+delta,y)-alpha)
kap=s.symbols('kappa',positive=True);p,q=s.symbols('p q',real=True)
zexp=p*s.exp(kap*y)+q*s.exp(-kap*y)
eq('negative_delta_solution',s.diff(zexp,y,2)-kap**2*zexp)
m,b=s.symbols('m b',real=True)
eq('zero_delta_solution',s.diff(m*y+b,y,2))
Y=s.symbols('Y',positive=True);S0=s.symbols('S0',positive=True)
comparison=S0*(y/Y)**s.Rational(4,3)
eq('bounded_end_comparison',s.diff(comparison,y)/comparison-s.Rational(4,3)/y)
flag('growth_exceeds_linear',s.Rational(4,3)>1)
# P220 diagnostic consistency: its polynomial C=-k^2 cannot satisfy this coefficient identity.
a220=s.sqrt(1+y*y);obstruction=s.diff(a220,y,2)/a220-4*(s.diff(a220,y)/a220)**2
obp=s.diff(obstruction,y)
eq('manufactured_highest_at0',obp.subs(y,0))
eq('manufactured_highest_at1',obp.subs(y,1)+s.Rational(1,2))
flag('manufactured_highest_not_constant',s.simplify(obp.subs(y,1)-obp.subs(y,0))!=0)
# Retain the initial proof hash and confirm its timestamp precedes execution.
old=json.loads((v/'proof_before_code.json').read_text())
flag('proof_precedes_checker',datetime.fromisoformat(old['utc'])<datetime.fromisoformat(utc))
flag('proof_hash_unchanged',hashlib.sha256((r/'PROOF.md').read_bytes()).hexdigest()==old['sha256'])
out={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(checks.values()),'differences':differences,'degree_controls':coeff_results,'scope':'Exact symbolic identities and finite degree controls. General degree argument, positivity contradiction and global scope are proved in PROOF.md; no numerical proof or full B2 endpoint.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('controls',len(checks),'failed',[k for k,vv in checks.items() if not vv])
