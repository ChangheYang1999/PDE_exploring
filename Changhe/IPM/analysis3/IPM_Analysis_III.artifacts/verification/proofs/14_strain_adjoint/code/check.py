from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
import sympy as S
from flint import arb,ctx
root=Path(__file__).resolve().parents[1];lane=root.parents[1]
A=S.symbols('A',positive=True);D=2*A+1;C=3*A+1;p=(4*A+2)/C;q=(5*A+1)/C
assert S.simplify(p+q-3)==0
th=S.symbols('theta',positive=True);ss=S.sin(th);cc=S.cos(th)
b=-A*cc**2+D*ss**2;v=C*ss*cc
assert S.trigsimp(3*b-(D-A+1)-C*(-p*cc**2+q*ss**2))==0
F0=cc**2*ss
assert S.trigsimp(v*S.diff(F0,th)+(3*b-1)*F0)==0
assert S.trigsimp(S.diff(v,th)-(D-A-2*b))==0
assert S.integrate(S.expand_trig(F0*S.sin(3*th)),(th,0,2*S.pi))==S.pi/4
ctx.prec=384;ctx.threads=1
k=F(1615536043799051,2**53);aa=2/k-1;ca=3*aa+1;pp=(4*aa+2)/ca;qq=(5*aa+1)/ca
def ball(x):return arb(x.numerator)/x.denominator
def beta(a,b):return a.gamma()*b.gamma()/(a+b).gamma()
pa,qa=ball(pp),ball(qq)
I=(2-pa)/2*beta((pa+1)/2,qa/2)
KA=beta(pa/2,qa/2)*beta(1-pa/2,pa/2)/(2*arb.pi()*ball(ca))
assert I>0 and KA>0
out={'date':datetime.now(timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((root/'PROOF.md').read_bytes()).hexdigest(),'A_exact':str(aa),'p_exact':str(pp),'q_exact':str(qq),'compatibility_integral':I.str(60),'K_A':KA.str(60),'K_A_upper':KA.upper().str(70),'symbolic_checks':'PASS','scope':'frozen normalized origin transport, zero outer flux, bounded factor forcing only'}
(root/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
