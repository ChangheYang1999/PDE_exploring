from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
from flint import arb,ctx
import json,time
B=Path(__file__).resolve().parents[1];ctx.prec=768
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(q.numerator)/q.denominator
start=time.monotonic();prep=json.loads((B/'verification/PREPARE.json').read_text());assert sha(B/'PROOF.md')==prep['proof_sha256']
c=Q(4076476460239181,2251799813685248);d=1-1/c;a=d+3;theta=d/(d+2);nu=2*(d+2)/(d+4);tau=d/(d+4)
assert Q(1,4)+1/(2*a-2)==(d+4)/(4*(d+2))
assert Q(1,4)+1/(a-3)==(d+4)/(4*d)
assert 2-4/(a+1)==nu and 1-4/(a+1)==tau
assert 2*tau/nu==theta and 4/(d+4)*(1-tau/nu)==1-theta
assert 1-theta/2==(d+4)/(2*(d+2))
J=2*arb.pi().sqrt()*ar((nu+1)/2).gamma()/ar((nu+2)/2).gamma()
C0=ar((d+4)/(4*(d+2)))*J;D0=ar((d+4)/(4*d))*J
C=ar((d+2)/d)*C0**ar(1-theta/2)
Cother=D0*C0**ar(-theta/2);assert C.overlaps(Cother)
S=ar((d+2)/(2*d))*arb.pi()**ar(theta/2)*arb(4)**ar(1-theta)
assert C>0 and C<S
# Constant/exponent calibration at d=2: nu=4/3 and beta=H=1.
rows=[]
for dv in [d,Q(2)]:
 av=dv+3;nv=2*(dv+2)/(dv+4);tv=dv/(dv+2)
 Jv=2*arb.pi().sqrt()*ar((nv+1)/2).gamma()/ar((nv+2)/2).gamma();C0v=ar((dv+4)/(4*(dv+2)))*Jv;D0v=ar((dv+4)/(4*dv))*Jv
 for beta,H in [(Q(1),Q(1)),(Q(3,7),Q(11,5))]:
  lam=(ar(beta*beta)/C0v/ar(H)**ar(4/(dv+4)))**ar(1/nv)
  norm2=C0v*ar(H)**ar(4/(dv+4))*lam**ar(nv)
  moment=D0v*ar(H)**ar(4/(dv+4))*lam**ar(dv/(dv+4))
  bound=ar((dv+2)/dv)*C0v**ar(1-tv/2)*ar(beta)**ar(tv)*ar(H)**ar(1-tv)
  assert norm2.contains(ar(beta*beta)) and moment.overlaps(bound)
  rows.append({'d':str(dv),'beta':str(beta),'H':str(H),'lambda':lam.str(100),'norm2':norm2.str(100),'moment':moment.str(100),'sharp_bound':bound.str(100),'norm_target_contained':True,'equality_overlap':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in [Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json']},'precision_bits':ctx.prec,'d_exact':str(d),'theta_exact':str(theta),'nu_exact':str(nu),'Jnu':J.str(100),'C0':C0.str(100),'Csharp':C.str(100),'Csplit':S.str(100),'Csharp_over_Csplit':(C/S).str(100),'checks':rows,'elapsed_seconds':time.monotonic()-start,'status':'OPEN independent Opus review; exact identities and Arb constant checks pass'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['Csharp'],out['Csharp_over_Csplit'],out['elapsed_seconds'])
