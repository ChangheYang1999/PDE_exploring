"""Exact power-integral lower bounds for T4's regularized weighted L2 norm."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import sys,json,time
from flint import fmpq,arb,arb_poly,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/whole_plane_norms/code'))
from radial import Radial,ar
from packed_residual import residual_sine
from norms import endpoint
BASE=ROOT/'research/weighted_forcing'

def run():
 ctx.prec=1024;start=time.monotonic();src=ROOT/'research/baseline/data/state131_independent.json'
 model=Radial(src);D=residual_sine(model);delta=model.delta
 a=fmpq(221,200);R=fmpq(2**29);modes={};groups={};t=arb_poly([1,-1])
 for (h,n),P in D.items():
  q,Q=endpoint(P)
  modes.setdefault(n,[]).append((h+1,q,arb_poly([ar(x) for x in Q])))
 for n,rows in modes.items():
  for i,(ell,q,P) in enumerate(rows):
   assert a-3+ell*delta+2*q>-1,(ell,n,q)
   for ell2,q2,Q in rows[i+1:]:assert ((ell-ell2)*delta/2).denominator!=1
   for j in range(i,len(rows)):
    ell2,q2,Q=rows[j];b=-3+(ell+ell2)*delta/2+q+q2
    groups[b]=groups.get(b,arb_poly([]))+P*Q*t*(1 if i==j else 2)
 print('assembled',len(D),'groups',len(groups),'seconds',time.monotonic()-start,flush=True)
 def primitive(b,P,U,shift=0):
  exp=b+shift+1
  assert all(exp+k for k in range(len(P)))
  poly=arb_poly([v/ar(exp+k) for k,v in enumerate(P)])
  u=ar(U);return poly(u)*u**ar(exp)
 def annulus(A,B):
  uA=1/(1+A*A);uB=1/(1+B*B)
  val=arb.pi()/2*sum((primitive(b,P,uA)-primitive(b,P,uB) for b,P in groups.items()),arb(0))
  assert val>0
  weight=(1+ar(B/R)**2)**ar(-a)
  return val,val*weight
 rows=[]
 for A in [fmpq(1),fmpq(10),fmpq(100),fmpq(1000),R,2*R,100*R]:
  B=2*A;norm2,weighted=annulus(A,B)
  rows.append({'inner_radius':str(A),'outer_radius':str(B),'unweighted_mass':norm2.str(75),'weighted_norm_lower':weighted.sqrt().str(75)})
  print('annulus',str(A),'weighted lower',weighted.sqrt().str(25),flush=True)
 U=1/(1+R*R)
 ext=arb.pi()/2*sum((primitive(b,P,U,a) for b,P in groups.items()),arb(0))
 assert ext>0
 lower=(ar(R*R/2)**ar(a)*ext).sqrt()
 q=2/model.c-1;assert a-1>q
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'state131','a':str(a),'R':str(R),
  'source_sha256':sha256(src.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
  'precision_bits':ctx.prec,'leading_residual_power':str(q),'membership_slack_a_minus_1_minus_q':str(a-1-q),
  'annuli':rows,'exterior_norm_lower':lower.str(90),'exterior_lower_squared':(lower*lower).str(90),
  'elapsed_seconds':time.monotonic()-start,'scope':'Lower bound for the prescribed weighted norm; no lower bound for an inverse correction and no nonexistence conclusion.'}
 (BASE/'verification/state131.json').write_text(json.dumps(out,indent=2)+'\n')
 print('full exterior weighted norm lower',lower.str(40),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':run()
