from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sympy as sy
from flint import arb,ctx
ctx.prec=256
TOP=Path(__file__).resolve().parents[1]
A,D,a,b=sy.symbols('A D a b',real=True)
kappa=(A+3)/2+a*A-b*(2*A+1)
assert sy.expand(kappa.subs({a:sy.Rational(7,2),b:sy.Rational(6,5)})-(8*A/sy.Integer(5)+sy.Rational(3,10)))==0
assert sy.expand((A*(1-2*a)-(2*A+1)*(1-2*b))/2-1+kappa)==0
sig=sy.symbols('sigma',positive=True)
assert sy.simplify(1/(2*sig)-2/(2*sig+2)+1/(2*sig+4)-1/(sig*(sig+1)*(sig+2)))==0
k=arb(1615536043799051)/2**53;Av=2/k-1;kap=8*Av/5+arb(3)/10
assert kap>arb('16.5')
def beta(x,y):return x.gamma()*y.gamma()/(x+y).gamma()
aa=arb(7)/2;bb=arb(6)/5;ss=aa+bb-4
Cang2=2*beta((9-2*aa)/2,(3-2*bb)/2);assert Cang2.contains(arb(20)/3)
Cr2=2*(9*beta(aa+arb(1)/2,bb+arb(3)/2)-24*beta(aa+arb(1)/2,bb+arb(5)/2)+16*beta(aa+arb(1)/2,bb+arb(7)/2))/(arb.pi()**2*(2*aa+2*bb-4))
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','kappa':kap.str(65),'kappa_inverse':(1/kap).str(65),'sigma':str(F(7,10)),'Cang_squared':'20/3','strain_jet_derivative_constant':(1/(8*(ss*(ss+1)*(ss+2)).sqrt())).str(65),'strain_remainder_constant':Cr2.sqrt().str(65),'proof_sha256':hashlib.sha256((TOP/'PROOF.md').read_bytes()).hexdigest(),'lead_snapshot_sha256':hashlib.sha256((TOP/'evidence/lead_snapshot.md').read_bytes()).hexdigest()}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
