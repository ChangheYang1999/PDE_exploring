from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
p=Path(__file__).resolve().parents[1]; start=time.monotonic()
c=Q(4076476460239181,2**51);g=1/c;delta=1-g
q=4*g-5;q2=1-9*delta
assert -3<q<-1 and q2<-3 and -2<q+1<0
rows=[]
for a in [Q(-2),Q(-19,10),q+1]:
 k=q+1-a; assert k>=0
 rows.append({'a':str(a),'kappa':str(k),'cost_power':str(k/(-q-1))})
f=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
r={'utc':datetime.now(timezone.utc).isoformat(),'q':str(q),'q2':str(q2),'eta':str(q-q2),'rows':rows,'proof_sha256':f(p/'PROOF.md'),'code_sha256':f(Path(__file__)),'elapsed_seconds':time.monotonic()-start,'verdict':'exact campaign exponents confirmed; analytic proof supplies the inequality'}
(p/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
