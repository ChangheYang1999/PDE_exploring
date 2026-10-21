"""Independent exact integrand and exponent checks; no sampled profile claim."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
R=Path(__file__).resolve().parents[1]
A,g,q,b,r,t=s.symbols('A g q b r t',positive=True)
z=s.symbols('z',positive=True);checks=[]
def ck(name,value):
 v=s.simplify(value);assert v==0,(name,v);checks.append({'name':name,'residual':str(v)})
ck('q divergence exponent',(q-1-(2*A-3)).subs(q,2*(A-1)))
ck('curl scalar multiplier',(1+z)*(1+z)**(-b-1)-(1+z)**(-b))
ck('first component high radial power',(A-3-q*(b+1)+A+1+g).subs(b,g/q).subs(q,2*(A-1)))
ck('second component high radial power',(q-2-q*(b+1)+2+g).subs(b,g/q))
ck('first component Fourier branch power',A+1-2-A-2+A-(A-3))
ck('second component Fourier branch power',(2*A-2-A-2+A-(q-2)).subs(q,2*(A-1)))
ck('first anchored zero-endpoint phase exponent',A-3+A-(2*A-3))
ck('second anchored zero-endpoint cosine exponent',A-3+2-(A-1))
ck('constant zero derivative',s.diff(s.Symbol('C'),r))
params=[s.Rational(101,100),s.Rational(6,5),s.Rational(4,3),s.Rational(3,2),s.Rational(7,4),s.Integer(2),s.Integer(3),s.Rational(203,20)]
criteria=[]
for a in params:
 qq=2*(a-1);bad=[];k=0
 while a-2+k*qq<=0:bad.append(k);k+=1
 assert a-2+k*qq>0
 assert 2*a-3>-1 and a-1>-1 and qq-1>-1
 criteria.append({'A':str(a),'q':str(qq),'required_vanishing_moment_indices':bad,'first_integrable_index':k,'first_integrable_radial_power':str(a-3+k*qq)})
proof=R/'PROOF.md';out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','exact_identities':checks,'moment_criterion_examples':criteria,'scope':'Exact arithmetic examples and symbolic identities supplement the analytic proof. They are not its proof for every parameter.','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [proof,Path(__file__)]}}
(R/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'identities and',len(criteria),'parameter examples')
