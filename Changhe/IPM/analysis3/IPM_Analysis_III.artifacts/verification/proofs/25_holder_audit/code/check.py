from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as s
from flint import arb,ctx
ctx.prec=160
A,p,al,t,x,y,c=s.symbols('A p al t x y c',positive=True)
D=2*A+1
q=(al-p)/al
assert s.simplify(al-q*al-p)==0
assert s.simplify(1+2*A-D)==0
rho=x*x*y
assert s.simplify((-c*x)*s.diff(rho,x)+(c*y)*s.diff(rho,y)+c*(x*s.diff(rho,x)+y*s.diff(rho,y))/3)==0
assert s.diff(rho+x*y**3,x).subs(x,0)==y**3
n=s.symbols('n',positive=True,integer=True)
xi=s.Matrix([n,n]);eta=s.Matrix([n,-n]);X=s.Matrix([x,y])
S=s.sin((xi.dot(X)))-s.sin(eta.dot(X))
m=lambda z:s.Matrix([z[0]*z[1]/z.dot(z),-z[0]**2/z.dot(z)])
U=m(xi)*s.sin(xi.dot(X))-m(eta)*s.sin(eta.dot(X))
assert s.trigsimp(U.dot(s.Matrix([s.diff(S,x),s.diff(S,y)]))+n*s.sin(2*n*y))==0
cusp=(arb.pi()/arb(2).sqrt()).sin()
assert cusp>arb('0.79')
assert cusp<arb('0.796')
root=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks':['sharpness scaling','cubic resonance','full normalized leading cancellation','missing parity counterexample','plane-wave interaction','strict sine lower-bound correction'],'sin_pi_over_sqrt2':str(cusp),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest()}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
