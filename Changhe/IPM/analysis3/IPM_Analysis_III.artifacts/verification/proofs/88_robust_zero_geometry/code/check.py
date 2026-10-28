from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
pm=F(4841405518533377,562949953421312);pp=F(4841405518533711,562949953421312)
qm=F(4559930541822721,562949953421312);qp=F(5122880495244367,562949953421312)
eps=F(1,100000);m=F(1801,10000)
assert pm-qm==F(1,2) and qp-pp==F(1,2)
assert qp*qp+F(1,4)<100
assert 10*eps<m/2
assert F(3,12500)-eps==F(23,100000)
assert m-eps==F(18009,100000)
assert 10*eps/m==F(1,1801)
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','epsilon':str(eps),'complement_rate':'23/100000','source_monotonicity':'18009/100000','source_displacement':'1/1801','proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2))
