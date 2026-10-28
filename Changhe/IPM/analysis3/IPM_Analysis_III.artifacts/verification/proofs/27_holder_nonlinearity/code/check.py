from pathlib import Path
from datetime import datetime,timezone
import sympy as s
from flint import arb,ctx
import json,hashlib
ctx.prec=160
x,y,n,w1,w2=s.symbols('x y n w1 w2',real=True)
P=w2*x*x/2-w1*x*y
U=s.Matrix([-s.diff(P,x,y),s.diff(P,x,2)])
h=-s.diff(P,x,2)-s.diff(P,y,2)
assert U==s.Matrix([w1,w2])
assert h==-w2
assert s.diff(h,x)==s.diff(h,y)==0
S=2*s.cos(n*x)*s.sin(n*y)
Uwave=s.Matrix([(s.sin(n*(x+y))+s.sin(n*(x-y)))/2,(-s.sin(n*(x+y))+s.sin(n*(x-y)))/2])
assert s.trigsimp(Uwave.dot(s.Matrix([s.diff(S,x),s.diff(S,y)]))+n*s.sin(2*n*y))==0
assert s.sin(2*n*y).subs(y,0)==0
z=s.symbols('z');Psi=z*z
assert s.diff(Psi,z).subs(z,0)==0
assert s.diff(Psi,z).subs(z,1)==2
v=(arb.pi()/arb(2).sqrt()).sin()
assert arb('0.79')<v<arb('0.796')
root=Path(__file__).resolve().parents[1]
o={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':['compact Hessian velocity prescription','constant local density','exact crossing-wave interaction','axis parity','strip profile derivatives','strict sine lower bound'],'sin_pi_over_sqrt2':str(v),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(o,indent=2)+'\n')
print(json.dumps(o,indent=2))
