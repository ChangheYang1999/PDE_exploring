from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=LANE/'proofs/187_fractional_difference_constant/evidence/final_certificate.json'
x=json.loads(p.read_text());assert x['verdict']=='CONFIRMED'
q=LANE/'proofs/187_fractional_difference_constant/PROOF.md';assert sha(q)==x['hashes'][str(q.relative_to(LANE))]
k=F(1615536043799051,9007199254740992);lower=int(x['reported_lower_bound']);assert lower==38666592266
factor=F(50,453)-k/3;assert factor>0
bound=factor*lower;assert bound==F(3990663377048576117076359567,2040130631198834688) and bound>1956082280
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED','factor_exact':str(factor),'eta_lower':str(lower),'threshold_exact':str(bound),'reported_threshold':'1956082280','scope':'conditional necessary test; no actual norm upper bound or violating direction','hashes':{str(z.relative_to(LANE)):sha(z) for z in (ROOT/'PROOF.md',Path(__file__),p,q)}}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
