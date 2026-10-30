"""Finite checks for the smooth normalized universal velocity sequence."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time
import sympy as s
from flint import arb,ctx,fmpq
B=Path(__file__).resolve().parents[1]
start=time.monotonic();ctx.prec=768
sha=lambda p:sha256(p.read_bytes()).hexdigest()
manifest=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==manifest['proof_sha256']
for name,h in manifest['source_sha256'].items():assert sha(B/'source'/name)==h
assert sha(B/'data/parameters.json')==manifest['parameters_sha256']
p=json.loads((B/'data/parameters.json').read_text())
def ar(q):
 v=fmpq(str(q));return arb(v.p)/arb(v.q)
checks=[]
def exact(label,x):
 assert s.simplify(x)==0,(label,x);checks.append(label)
a,R,r=s.symbols('a R r',positive=True);q=s.symbols('q',real=True)
t=s.symbols('theta',real=True)
f=r*(R*R+r*r)**(-(a+1)/2)/a
exact('radial gradient',s.diff(f,r)-(R*R-a*r*r)*(R*R+r*r)**(-(a+3)/2)/a)
exact('angular gradient',f/r-(R*R+r*r)**(-(a+1)/2)/a)
exact('Cauchy gap',(1+R**-2)*(R*R+r*r)-(1+r)**2-(r/R-R)**2)
exact('gradient upper signed positive',a*(R*R+r*r)-(R*R-a*r*r)-((a-1)*R*R+2*a*r*r))
exact('gradient upper signed negative',a*(R*R+r*r)+(R*R-a*r*r)-(a+1)*R*R)
exact('contact angular orthogonality',s.integrate(s.sin(3*t)*s.sin(t),(t,0,2*s.pi)))
exact('normalization',-R**(-a-1)/(4*a)+R**(-a-1)/(4*a))
exact('scale identity',R**(-a)*(r/R)*(1+(r/R)**2)**(-(a+1)/2)/a-f)
# These beta recurrences evaluate the two exact radial integrals.
beta2=lambda z:1/(z*(z+1))
exact('first moment beta coefficient',s.pi/(2*a)*beta2((a-3)/2)-2*s.pi/(a*(a-1)*(a-3)))
exact('L2 squared beta coefficient',s.pi/(2*a*a)*beta2(a-1)-s.pi/(2*a**3*(a-1)))
exact('homogeneous Green inverse',((q+2)**2-1)/(a*(q+1)*(q+3))-1/a)
# At theta=pi/4 the two vector components have equal magnitude.
exact('homogeneous remainder square',2*((q+1)/(2*s.sqrt(2)*a*(q+3)))**2-(q+1)**2/(4*a*a*(q+3)**2))
exact('universal constant',((q+1)**2/(4*a*a*(q+3)**2)).subs(q,-a)-(a-1)**2/(4*a*a*(a-3)**2))
c=fmpq(p['c']);av=fmpq(4)-1/c
A=ar(av);E=(A-1)/(2*A*(A-3));K=5*arb(2)**(A+1)
assert E>ar('7930365/10000000') and E<ar('7930366/10000000')
rows=[]
for st in p['radii']:
 rv=ar(st);C=(1+rv**-2)**((A+1)/2);bound=C+rv**(-A-1)*K/A
 # ||b||2 <= sqrt(pi)/2 since |b|<=|y| on the unit disk.
 fn=(arb.pi()/(2*A**3*(A-1))).sqrt()*rv**(1-A)
 kn=fn+rv**(-A-1)*arb.pi().sqrt()/(2*A)
 rows.append({'R':st,'H_upper':bound.str(90),'L2_upper':kn.str(90),'necessary_E':(E/bound).str(90)})
assert arb(rows[-1]['necessary_E'])>ar('785064/1000000')
assert arb(rows[-1]['L2_upper'])<ar(p['fixed_sharpw_L2'])
checks.extend(['universal interval','normalized test exceeds critical E','test L2 below fixed sharpw radius'])
out={'completed_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'proof_sha256':manifest['proof_sha256'],'manifest_sha256':sha(B/'data/manifest.json'),'checker_sha256':sha(Path(__file__)),'source_sha256':manifest['source_sha256'],'symbolic_and_interval_checks':checks,'check_count':len(checks),'a':str(av),'E_lower':E.str(110),'sequence':rows,'status':'PASS finite identities; normalized-domain theorem OPEN independent review','foreign_code_executed':False}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
