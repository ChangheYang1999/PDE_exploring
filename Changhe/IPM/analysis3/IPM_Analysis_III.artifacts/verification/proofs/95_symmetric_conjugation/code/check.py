from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
from sympy import symbols,expand,simplify
x,y,r=symbols('x y r', nonzero=True)
lhs=x*(r-1)+y*(1/r-1)
rhs=(x-y)*(r-1/r)/2+(x+y)*(r+1/r-2)/2
assert simplify(lhs-rhs)==0
path=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','arithmetic':'exact symbolic','checks':['paired kernel cancellation'],'proof_sha256':hashlib.sha256((path/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(path/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(o['date'],o['status'])
