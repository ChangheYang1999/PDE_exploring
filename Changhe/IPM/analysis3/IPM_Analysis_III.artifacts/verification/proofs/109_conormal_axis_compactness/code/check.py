from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[1]
y=s.symbols('y',positive=True);T=s.Function('T')(y)
q=T/y;target=[s.diff(T,y)-T/y,y*s.diff(T,y,2)-s.diff(T,y)+T/y,y*y*s.diff(T,y,3)+s.diff(T,y)-T/y]
for v in target:
 q=s.simplify(y*s.diff(q,y));assert s.simplify(q-v)==0
a=F(17,4);eta=F(5,4);k=F(1615536043799051,9007199254740992)
assert a>4 and eta<2 and 2*a-9> -1 and eta-9< -1
assert a-2==F(9,4) and 4-F(1,2)==F(7,2)
assert 2*(k-F(35,8))+F(27,4)==2*k-2<0
# Homogeneous kernel Euler identity and the strain kernel's degree.
x,z=s.symbols('x z',real=True)
K=(x*x-z*z)/(2*s.pi*(x*x+z*z)**2)
C=z*(3*x*x-z*z)/(s.pi*(x*x+z*z)**3)
assert s.simplify(x*s.diff(K,x)+z*s.diff(K,z)+2*K)==0
assert s.simplify(x*s.diff(C,x)+z*s.diff(C,z)+3*C)==0
# Odd-part derivative is the strain kernel.
Ko=(K.subs(z,y-z)-K.subs(z,y+z))/2
assert s.simplify(s.diff(Ko,y).subs(y,0)-C)==0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','identities':['three logarithmic trace derivatives','kernel Euler identity','strain Euler identity','odd-kernel strain coefficient','endpoint integrability powers'],'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
