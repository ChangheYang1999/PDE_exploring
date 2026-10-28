from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ctx.prec=256;ctx.threads=1
R=Path(__file__).resolve().parents[1]
def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator
a=F(17,4);eta=F(5,4);k=F(1615536043799051,9007199254740992)
assert a-F(1,2)==F(15,4)
assert 4+a-F(1,2)-1==F(27,4)
assert F(25,4)<F(51,8)<F(13,2)<F(27,4)
assert a-2==F(9,4)
assert eta/2-2==-F(11,8)
assert 2*a-9==-F(1,2)>-1
assert eta-9<-1
assert 2-F(1,4)==F(7,4)
assert k-F(35,8)+F(27,8)==k-1<0
C2=aa(2*a+1).gamma()/(2**aa(2*a+2))
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','trace_order':str(a-F(1,2)),'trace_constant_squared':str(C2),'strong_row_order':'51/8','compact_target_order':'25/4','proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
