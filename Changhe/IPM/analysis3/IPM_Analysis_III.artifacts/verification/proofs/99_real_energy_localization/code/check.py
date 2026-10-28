from sympy import Matrix,eye,Rational as R,diag
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
C=Matrix([[1,2,-1],[3,-2,4],[5,1,2]])
xs=[diag(R(3,5),R(5,13),0),diag(R(4,5),R(12,13),1)]
assert sum((x*x for x in xs),Matrix.zeros(3))==eye(3)
comm=lambda A,B:A*B-B*A
lhs=C-sum((x*C*x for x in xs),Matrix.zeros(3))
rhs=sum((comm(x,comm(x,C)) for x in xs),Matrix.zeros(3))/2
assert lhs==rhs
for i in range(3):
 for j in range(3):assert 1-sum(x[i,i]*x[j,j] for x in xs)==sum((x[i,i]-x[j,j])**2 for x in xs)/2
p=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'exact rational matrices','checks':['paired localization double commutator','square-partition kernel factor'],'proof_sha256':hashlib.sha256((p/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(p/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n');print(o['date'],o['status'])
