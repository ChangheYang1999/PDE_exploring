from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
p=Path(__file__).resolve().parents[1]
k=F(1615536043799051,9007199254740992)
s_hi=F('37.63077494715567')
upper=3/k-12+s_hi*(F(4,3)-1/(1-k))
assert 0<k<F(1,4)
assert 0<upper<F('9.06')
obj={'date':datetime.now(timezone.utc).isoformat(),'verdict':'PASS','k':str(k),'S_upper':str(s_hi),'universal_N4_upper':str(upper),'decimal_for_orientation':float(upper),'reported_bound':'9.06','method':'exact rational arithmetic; S interval inherited from independent original-data certificate V034','proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps(obj,indent=2))
