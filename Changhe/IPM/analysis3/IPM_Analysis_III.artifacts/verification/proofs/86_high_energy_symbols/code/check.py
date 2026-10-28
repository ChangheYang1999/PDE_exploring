from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json
ell=F(9007199254740992,1615536043799051);A=2*ell-1;D=4*ell-1;S=A+D
v={'ell':ell,'A':A,'D':D,'Sigma':S,'sx':F(3,2)+F(9,5)*A/S,'sy_threshold':F(1,2)+F(9,5)*D/S,'mx':S*(F(3,2)-F(41,20))+F(9,5)*A,'my':S*(F(25,4)-F(1,2))-F(9,5)*D,'m_infinity':1+ell/2}
assert S==3*A+1
assert v['mx']>F(9726,10000) and v['my']>F(1425,10) and v['m_infinity']>F(37876,10000)
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','values':{k:{'exact':str(x),'diagnostic':float(x)} for k,x in v.items()},'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2))
