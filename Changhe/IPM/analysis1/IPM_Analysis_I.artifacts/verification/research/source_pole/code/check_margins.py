"""Exact endpoint arithmetic for the uniform coupled-source theorem."""
import json,hashlib,itertools
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
base=Path(__file__).resolve().parents[1];s=Q(31,10);rows=[]
for A,mu,g in itertools.product([Q(10),Q(51,5)],[Q(99,100),Q(101,100)],[Q(29),Q(30)]):
 b=1+(A+mu)/2;slow=b-s*mu;fast=b+g-s*A
 assert slow>=Q(1687,500) and fast>=Q(159,40)
 rows.append({'A':str(A),'mu':str(mu),'g':str(g),'slow_margin':str(slow),'fast_margin':str(fast)})
assert min(Q(v['slow_margin']) for v in rows)==Q(1687,500)
assert min(Q(v['fast_margin']) for v in rows)==Q(159,40)>Q(1687,500)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((base/'PROOF.md').read_bytes()).hexdigest(),'corners':rows,'delta_exact':'1687/500','inverse_upper_exact':'500/1687','scope':'Finite exact rational inequalities. The continuum claim uses affine dependence as proved in PROOF.md.'}
(base/'evidence/margins.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
