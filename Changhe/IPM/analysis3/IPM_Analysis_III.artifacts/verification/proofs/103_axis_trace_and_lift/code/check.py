from pathlib import Path
from datetime import datetime,timezone
import sympy as s
from flint import arb,ctx
import json,hashlib
root=Path(__file__).resolve().parents[1]
r=s.symbols('r',positive=True)
a=s.Rational(17,4);B=s.Rational(29,4);p=2*a+1
assert s.diff(1/(p+1)+(r**(p-B+1)-1)/(p-B+1),r)==r**(p-B)
for j in range(4):
 q=2*a-2*j-3
 assert s.simplify(s.diff(r**(q-B+1)/(B-q-1),r)+r**(q-B))==0
 assert q+1>0 and B-q-1>0 and 2*a-2*j-2>0
x=s.symbols('x',positive=True)
al=s.Function('al');T=s.Function('T')
# alpha is represented as alpha(log y).
v=al(s.log(x)); vp=s.diff(v,x)*x; vpp=s.diff(vp,x)*x
G=(v+vp)*T(x)/x-2*v*s.diff(T(x),x)
expect=(vpp-v)*T(x)/x+(v-vp)*s.diff(T(x),x)-2*v*x*s.diff(T(x),x,2)
assert s.simplify(x*s.diff(G,x)-expect)==0
results=[]
for prec in (256,384):
 ctx.prec=prec;ctx.threads=1
 aa=arb(17)/4;bb=arb(29)/4
 Ia=2*(aa+arb(1)/2).gamma()*(arb(1)/2).gamma()/(aa+1).gamma()
 vals=[]
 for j in range(4):
  pp=2*aa+1;qq=2*aa-2*j-3
  AA=1/(pp+1)+(arb(2)**(pp-bb+1)-1)/(pp-bb+1)
  BB=arb(2)**(qq-bb+1)/(bb-qq-1)
  near=arb('0.5')**(2*aa-2*j-2)/(2*aa-2*j-2)
  fact=1
  for m in range(1,j+2):fact*=m
  val=(arb(fact)/(2*arb.pi()))*(Ia*(near+arb(2)**(2*j+4)*(BB+AA))).sqrt()
  vals.append(str(val))
 results.append({'precision':prec,'N_j_at_1':vals})
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','values':results,
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
