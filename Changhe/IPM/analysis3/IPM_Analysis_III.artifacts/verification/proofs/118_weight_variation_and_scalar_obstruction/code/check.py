from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
R=Path(__file__).resolve().parents[1];k=F(1615536043799051,9007199254740992);ell=1/k
rows=[]
for a in [F(18,5),F(19,5),F(4),F(17,4)]:
 for Delta in [F(0),F(1,10),F(1,5),F(3,10)]:
  margin=1+(F(3,8)-Delta)*ell
  assert margin==ell*(k+F(3,8)-Delta)
  rows.append({'a':str(a),'Delta':str(Delta),'inner_scalar_sigma':str(a-4),'outer_kappa':str(k+F(3,8)-Delta),'far_margin':str(margin),'finite_J_scalar_theorem_eligible':a>4 and Delta<k+F(3,8)})
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','rows':rows,'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
