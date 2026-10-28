from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ctx.prec=256;ctx.threads=1
R=Path(__file__).resolve().parents[1]
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
def beta(a,b):return a.gamma()*b.gamma()/(a+b).gamma()
s=aa(F(1,4));half=aa(F(1,2))
c=((1-s)/2).gamma()/((2**s)*arb.pi().sqrt()*(s/2).gamma())
J=beta(half,s)+beta(half-s,s)+beta(half,half-s)
C2=aa(F(256,441))*(c*J)**2
assert F(16,49)*F(16,9)==F(256,441)
assert 4+F(9,4)==F(25,4)
assert 2*F(9,5)-F(1,2)>0
assert 2*(-F(1,2))+F(3,4)<0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','s':str(s),'c_s':str(c),'J_s':str(J),'Hardy_constant_squared':str(C2),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
