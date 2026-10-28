from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
k=F(1615536043799051,9007199254740992);D=4/k-1;c=D/4
lo=F('5.325362610420');hi=F('5.325362610421')
# Report outward endpoints without assuming a recalled decimal.
scale=10**12;floor=c.numerator*scale//c.denominator
lo=F(floor,scale);hi=F(floor+1,scale);assert lo<c<hi
# Finite triangular algebra with a nontrivial lower block, exact rational arithmetic.
A=F(3,7);S=F(5,11);X=F(-2,13)
for beta,u in [(F(2,3),F(-7,5)),(F(0),F(11))]:
 y1=A*beta;y2=X*beta+S*u
 assert y1/A==beta and (y2-X*y1/A)/S==u
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','k_exact':str(k),'critical_lambda_exact':str(c),'critical_lambda_enclosure':[str(lo),str(hi)],'critical_lambda_decimal':float(c),'proof_sha256':hashlib.sha256((ROOT/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(ROOT/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
