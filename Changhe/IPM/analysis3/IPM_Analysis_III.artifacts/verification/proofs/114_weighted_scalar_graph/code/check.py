from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1]
k=F(1615536043799051,9007199254740992);delta=F(9,5);gamma=-F(1,2);lam=F(1,2);sigma=F(25,4)
assert F(1,4)<delta<2
assert gamma<-F(3,8) and gamma<k
assert 2*lam-F(1,2)>0 and lam-delta<0
assert 2-delta>0 and sigma-6<F(1,2)
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','origin_gap':str(2-delta),'outer_future_decay':str(k-gamma),'old_weight_counterexample':str(lam-delta),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
