"""Exact Cartesian polynomial audit of dynamic-rescaling identities."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
start=time.monotonic();checks={}
def clean(p):return {k:v for k,v in p.items() if v}
def add(*ps):
 out={}
 for p in ps:
  for k,v in p.items():out[k]=out.get(k,F())+v
 return clean(out)
def scale(p,a):return clean({k:a*v for k,v in p.items()})
def der(p,axis):
 out={}
 for k,v in p.items():
  if k[axis]:
   j=list(k);j[axis]-=1;out[tuple(j)]=v*k[axis]
 return clean(out)
def mul(p,q):
 out={}
 for (i,j),v in p.items():
  for (k,l),w in q.items():out[(i+k,j+l)]=out.get((i+k,j+l),F())+v*w
 return clean(out)
def check(name,condition):
 assert condition,name
 checks[name]=checks.get(name,0)+1
for it in range(1,101):
 a=F(it%7+1,it%5+1);b=F((-1)**it*(it+1),it%9+2);e=F((-1)**(it//2)*(it+3),it%11+3);c=F(1-it,it+7);d=F(it+3,17);f=-b/3-d
 cw=F(it+2,it+5);cx=F(it+3,it+7)
 rho={(0,1):a,(2,1):b,(0,3):e,(4,1):F(it,7),(2,3):F(-it,13),(0,5):F(1,19)}
 psi={(1,1):c,(3,1):d,(1,3):f,(5,1):F(it,3),(3,3):F(-it,5),(1,5):F(it,11)}
 ux=scale(der(psi,1),-1);uy=der(psi,0)
 rhs=add(scale(rho,cw),scale(mul(add({(1,0):cx},ux),der(rho,0)),-1),scale(mul(add({(0,1):cx},uy),der(rho,1)),-1))
 check('origin_slope',rhs.get((0,1),F())==(cw-cx-c)*a)
 check('x2y_coefficient',rhs.get((2,1),F())==(cw-3*cx+c)*b-3*a*d)
 check('y3_coefficient',rhs.get((0,3),F())==(cw-3*cx-3*c)*e-a*f)
 poisson=add(scale(der(der(psi,0),0),-1),scale(der(der(psi,1),1),-1),scale(der(rho,0),-1))
 check('quartic_Poisson',poisson.get((1,1),F())==0)
 cw=-f/(2*e);cx=cw-c
 check('fixed_slope_gauge',cw-cx-c==0)
 check('fixed_y3_gauge',(cw-3*cx-3*c)*e-f==0)
 # Symbolic logarithm in the moving-map chain rule is a free indeterminate.
 s=F(it,it+101);kappa=F(it+102,it+1);kp=F(it-11,17);Lrate=F(it-3,13);logfactor=F(it+13,11)
 dlogds=F(1,2)/s+kappa/(1-s)
 sp=(kp*logfactor-Lrate)*2*s*(1-s)/(1-s+2*kappa*s)
 check('moving_map_chain_rule',Lrate-kp*logfactor+dlogds*sp==0)
 xi=2*s-1
 check('fixed_map_radial_speed',2/dlogds==(1-xi*xi)/(kappa+F(1,2)+(kappa-F(1,2))*xi))
 for m,n in [(0,1),(2,1),(0,3),(4,1),(2,3),(0,5)]:
  cw=F(it+1,it+5);ell=F(it+3,it+2);cx=ell*cw;c=cw-cx
  rate=cw-(cx-c)*m-(cx+c)*n
  check('monomial_rate_identity',rate/cw==1-n-(2*ell-1)*m)
  check('higher_transport_jet_rate',rate==0 if (m,n)==(0,1) else rate<0)
proof=Path('research/dynamic_rescaling_audit/PROOF.md')
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS',passed=sum(checks.values()),counts=checks,elapsed_seconds=time.monotonic()-start,proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact polynomial and rational identities only. Infinite physical-time criteria are proved in PROOF.md. No simulated solution, time-integrator stability or profile existence is established.')
(proof.parent/'verification/EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
