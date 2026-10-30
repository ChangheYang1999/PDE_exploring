from pathlib import Path
from fractions import Fraction as Q
from math import factorial
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
ctx.prec=1024
p=Path(__file__).resolve().parents[1];start=time.monotonic();rows=[]
for n in range(1,64):
 h=Q(factorial(n-1),2**(n+3));w=Q(factorial(n+1),2**(n+3));ratio=n*n*h/w
 assert ratio==Q(n,n+1)
 rows.append({'n':n,'ratio':str(ratio)})
gaussian=[]
for xx in [1,10,100]:
 x=arb(xx);v=arb.pi().sqrt()*x*(x*x).exp()*x.erfc()
 assert v>0 and v<1 and 1-v<1/(2*x*x)
 gaussian.append({'x':xx,'squared_ratio':str(v)})
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
r={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':sha(p/'PROOF.md'),'code_sha256':sha(Path(__file__)),'gaussian_radial_examples':rows,'logarithmic_gaussian':gaussian,'elapsed_seconds':time.monotonic()-start,'verdict':'exact ratio checks pass; origin-domain extension requires the stated cancellation convention'}
(p/'verification/result.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:v for k,v in r.items() if k!='gaussian_radial_examples'},indent=2))
