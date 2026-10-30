"""Locate the last four-branch radial degree excluded by this L2 bound."""
from floor import distance,BASE,ROOT,ar
from flint import fmpq,arb,ctx
from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,time
ctx.prec=512;start=time.monotonic();source=ROOT/'research/sector_audit/verification/stationary_principal.json'
d=json.loads(source.read_text());delta=1-1/fmpq(d['cl']);E=(arb.pi()*ar(sum((fmpq(v)**2 for v in d['branches'][3]['forcing_sin'].values()),fmpq(0)))).sqrt()
eta=ar(fmpq(1,163840));s=fmpq(1,131072)
def ratio(K):return (1-ar(34*s))*512*E*distance(4,K,delta)[0]/arb(2).sqrt()/eta
low,high=10000,100000;assert ratio(low)>1 and ratio(high)<1
steps=[]
while high-low>1:
 mid=(low+high)//2;r=ratio(mid);steps.append({'K':mid,'ratio':r.str(45)})
 if r>1:low=mid
 elif r<1:high=mid
 else:raise ArithmeticError('inconclusive interval')
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'last_excluded_degree':low,'first_inconclusive_degree':high,
     'last_ratio':ratio(low).str(65),'next_ratio':ratio(high).str(65),'steps':steps,
     'source_sha256':sha256(source.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'elapsed_seconds':time.monotonic()-start,'scope':'Assumes the stated finite-family theorem and T4-019 norm comparison; no claim above the boundary.'}
(BASE/'verification/boundary.json').write_text(json.dumps(out,indent=2)+'\n')
print(low,out['last_ratio'],high,out['next_ratio'],flush=True)
