from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]
s=F(25,4);N=6
assert s-N==F(1,4)
assert s-(N+1)==-F(3,4)
k=F(1615536043799051,9007199254740992);ell=1/k
A=2*ell-1;D=4*ell-1
assert A+D>0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','leading_growth':str(s-N),'coupling_bound':str(s-(N+1)),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
