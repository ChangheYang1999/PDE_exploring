"""Exact Cartesian Poisson checks for distance-norm counterexamples."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import json,time,sys
sys.dont_write_bytecode=True
from laurent_log_audit import L,Poly,Q,parse
root=Path('research/86_distance_weight_obstruction');start=time.monotonic();rows=[]
def inv(poly,s,sgn=1):
 out=Poly([]);der=poly
 for h in range(len(poly)):
  out+=der*Q((-sgn)**h)/s**(h+1);der=der.derivative()
 return out
for family in ['constant','top']:
 for r in range(3,43):
  n=3*r+(2 if family=='constant' else 1);k=r-1;m=2*r-(0 if family=='constant' else 2);P=Q(2)-Q(2*n,3);t=Poly([0]*k+[1]);s=P+m
  b=-inv(t,s)/2;other=inv(t,m-2-P,-1)/2
  F=parse(P-1,{m-1:t.coeffs()});G=parse(P,{m:b.coeffs(),m-2:other.coeffs()})
  assert (G.X().X().scale(-1)+G.Y().Y()-F.X()).zero()
  assert k==(n-1)//3-1
  if family=='constant':
   dF=abs(Q(m-1)-abs(P));ratio=abs(b[0])/(Q(factorial(k))/(1+dF)**k);expected=Q(3,4)*2**k
  else:
   dF=abs(Q(m-1)-abs(P));dG=abs(Q(m)-abs(P));ratio=abs(b[k])*((1+dF)/(1+dG))**k;expected=Q(3,4)*Q(8,5)**k
  assert ratio==expected
  rows.append(dict(family=family,n=n,r=r,k=k,output_mode=m,density_mode=m-1,poisson_identity=True,ratio_identity=True,ratio=str(ratio)))
res=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,checks=2*len(rows),cases=rows,source_sha256={})
for name in ['distance_weight_counterexample.py','laurent_log_audit.py']:
 raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw);res['source_sha256'][name]=sha256(raw).hexdigest()
(root/'verification/checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='cases'}))
