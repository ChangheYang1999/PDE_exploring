from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json
import sympy as S
from flint import arb, ctx
ctx.prec=384
root=Path(__file__).resolve().parents[1]
s=Q(31,10)
corners=[]
for A,mu,g in product([Q(10),Q(51,5)],[Q(99,100),Q(101,100)],[Q(29),Q(30)]):
 b=1+(A+mu)/2
 corners.append(dict(A=str(A),mu=str(mu),g=str(g),slow=str(b-s*mu),fast=str(b+g-s*A),threshold_slow=str(b/mu),threshold_fast=str((b+g)/A)))
assert min(Q(c['slow']) for c in corners)==Q(1687,500)
assert min(Q(c['fast']) for c in corners)==Q(159,40)
assert min(Q(c['threshold_slow']) for c in corners)==Q(1301,202)
assert min(Q(c['threshold_fast']) for c in corners)==Q(2373,680)
x,y,A,mu,ss=S.symbols('x y A mu ss',positive=True)
w=(1+x*x+y*y)**(ss/2)
assert S.simplify((A*x*S.diff(w,x)+mu*y*S.diff(w,y))/w-ss*(A*x*x+mu*y*y)/(1+x*x+y*y))==0
trace=1/(8*arb.pi()*(arb(31)/10-1)*(arb(31)/10-2)).sqrt()
inv=arb(500)/1687
out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'corners':corners,'inverse_bound':inv.str(85),'jet_bound':(trace*inv).str(85),'max_uniform_s':(arb(2373)/680).str(85),'algebra':'PASS','scope':'rational parameter box only; no candidate source association'}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
