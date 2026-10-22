from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/graph_center_norm'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(q,s):
 if not q:raise ValueError(s)
a,b=F(4,3),F(-1,3)
check(a+b==1,'central coefficient');check(a+4*b==0,'strain cancellation')
# A second construction solves the two exact constraints by elimination.
second=F(-1,4-1);first=1-second;check((a,b)==(first,second),'independent 2x2 elimination')
primary=json.loads((D/'evidence/compute.json').read_text());ind=json.loads((D/'evidence/independent.json').read_text());check(F(primary['strain_exact'])==F(ind['strain_exact'])==F(1,56),'both exact unit strains')
files={str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'ADDENDUM.md',D/'FIXED_STRAIN.md',D/'evidence/compute.json',D/'evidence/independent.json',Path(__file__)]}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_TWO_SCALE_CENTER_AND_STRAIN_CONSTRAINTS','coefficients':['4/3','-1/3'],'scale_factors':[1,2],'center_exact':'1/1','strain_exact':'0/1','files':files,'scope':'Finite identities only. Graph convergence and domain restrictions proved in FIXED_STRAIN.md. No actual kernel or inverse certificate.'};p=D/'evidence/fixed_strain.json';check(not p.exists(),'immutable');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status']}))
