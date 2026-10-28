from flint import arb,ctx
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
ctx.threads=1
assert 2*(16*F(19,25)*F(23,29)-8*F(19,25)+1)==F(6618,725)
res=[]
for bits in (256,384):
 ctx.prec=bits
 def beta(a,b):return a.gamma()*b.gamma()/(a+b).gamma()
 a=arb(3)/2;b=arb(19)/4
 I=arb(6618)/725*beta(a,b)
 I2=2*(16*beta(a,b+2)-8*beta(a,b+1)+beta(a,b))
 assert I.overlaps(I2)
 C=(arb(58)/99*I/arb.pi()**2).sqrt()
 assert C<arb(20757)/100000
 res.append({'bits':bits,'ball':C.str(80),'safe_upper_exact':'20757/100000'})
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','results':res,'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n');print(o['date'],o['status'])
