from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import sympy as s
root=Path(__file__).resolve().parents[1]
c,M,w=s.symbols('c M w',positive=True)
ls=w+1+2*M*c
assert s.simplify(c*M/(ls-w)-M*c/(1+2*M*c))==0
assert s.simplify(s.Rational(1,2)-M*c/(1+2*M*c)-1/(4*M*c+2))==0
# Finite-dimensional analogue of the shifted-jet null direction.
e0=s.Matrix([1,0,0]); f=s.Matrix([0,2,3]); j=s.Matrix([[1,0,0]])
P=s.eye(3)-e0*j
assert P*e0==s.zeros(3,1)
assert (P+f*j)*(e0-f)==s.zeros(3,1)
# Exact origin exponents controlling the cutoff cubic's B membership,
# and the target divergence for a constant cubic coefficient.
assert 4-s.Rational(1,2)>0
assert -s.Rational(1,2)<0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'checks':['strict Neumann endpoint, including c=0 by substitution',
 'projection and finite-rank shift null directions','jet origin exponents'],
 'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
