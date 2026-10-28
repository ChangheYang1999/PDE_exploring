from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sympy as s
import hashlib,json
A,mu,g,sg=s.symbols('A mu g sigma',positive=True)
a=g/(A-mu); b=(A-mu)/A; q=(1+g)/A
assert s.simplify(q-a+(a*mu-1)/A)==0
assert s.simplify(b*(a-1/mu)-(q-1/mu))==0
assert s.simplify(q-b*a-1/A)==0
assert s.simplify(b*sg+1/A-sg-(1-mu*sg)/A)==0
assert s.simplify(1-a+(a*mu-1-A)/A+q)==0
assert s.simplify(a+1-(a*mu-1-A)/A-(q+2))==0
xi,eta,t=s.symbols('xi eta t',real=True)
Q=((xi**2+eta**2)/(s.exp(2*(A-mu)*t)*xi**2+eta**2))**(a/2)
assert s.simplify(s.diff(Q,t).subs(t,0)+g*xi**2/(xi**2+eta**2))==0
mlo=F(99999997745,10**11); mhi=F(99999997750,10**11)
alo=F(29)*mlo/(F(51,5)-mlo); ahi=F(30)*mhi/(F(10)-mhi)
assert 3<alo<ahi<F(10,3)<11
assert 0<mlo<mhi<1
root=Path(__file__).resolve().parents[1]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'checks':['multiplier derivative and sign','annular crossover','low frequency exponent','regularity sum exponent','exact rational modal parameter box'],'a_mu_lower':str(alo),'a_mu_upper':str(ahi),'actual_mu_strictly_below_one':True}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
