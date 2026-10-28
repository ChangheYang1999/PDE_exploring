from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S

def sine_coeff(m):
    out={}
    for n in (1+2*m,1-2*m,3+2*m,3-2*m):
        if n:out[abs(n)]=out.get(abs(n),Q(0))+Q(1 if n>0 else -1,8)
    return {n:v for n,v in out.items() if v}
D=[sine_coeff(m) for m in range(8)]
A0=[[sum((dm.get(n,0)*dj.get(n,0) for n in set(dm)|set(dj)),Q(0)) for dj in D] for dm in D]
A1=[[sum((n*n*dm.get(n,0)*dj.get(n,0) for n in set(dm)|set(dj)),Q(0)) for dj in D] for dm in D]
assert A0[0][0]==Q(1,8)
assert A1[0][0]==Q(5,8)
assert all(max(dm)<=2*m+3 for m,dm in enumerate(D))
assert S.Matrix([[S.Rational(x.numerator,x.denominator) for x in row] for row in A0]).det()>0
s,e,d,c=S.symbols('s e d c',positive=True)
# Block solution: coefficient maps are S^-1 and -S^-1 B D^-1, etc.
assert S.simplify((d+d*c*s*e)-d*(1+c*s*e))==0
root=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'sine_coefficients':[{str(k):str(v) for k,v in dm.items()} for dm in D],'A0_over_pi':[[str(x) for x in row] for row in A0],'A1_over_pi':[[str(x) for x in row] for row in A1],'checks':'PASS','scope':'exact identities only; no finite-section singular value certified'}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(out['checks'])
