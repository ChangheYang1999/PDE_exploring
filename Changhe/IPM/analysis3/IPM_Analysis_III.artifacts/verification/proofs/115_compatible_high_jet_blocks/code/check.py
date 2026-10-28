from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s,json,hashlib
R=Path(__file__).resolve().parents[1]
t,th=s.symbols('t th',real=True);P,Q,S,B=s.symbols('P Q S B')
# r^(-2) psi; d_t includes the r^2 prefactor and the exact moment equations.
f=((P-Q)*s.sin(2*th)-S*s.sin(4*th))/8
Ur=-s.diff(f,th)
Ut=2*f+s.diff(f,P)*(-B)+s.diff(f,Q)*(B-4*Q)+s.diff(f,S)*(B-6*S)
assert s.simplify(Ur-(-(P-Q)*s.cos(2*th)/4+S*s.cos(4*th)/2))==0
assert s.simplify(Ut-((P+Q-B)*s.sin(2*th)/4+(4*S-B)*s.sin(4*th)/8))==0
# Verify the Green equation, independently of the polar differentiation.
Bp=s.symbols('Bp')
def Dt(expr):
    return s.diff(expr,P)*(-B)+s.diff(expr,Q)*(B-4*Q)+s.diff(expr,S)*(B-6*S)+s.diff(expr,B)*Bp
f2=(P-Q)/8; f4=-S/8
assert s.expand(-(Dt(Dt(f2))+4*Dt(f2))-((Bp-2*B)/4+B))==0
assert s.expand(-(Dt(Dt(f4))+4*Dt(f4)-12*f4)-(Bp-2*B)/8)==0
assert s.expand(-F(2,3)*2+F(4,3))==0
k=F(1615536043799051,9007199254740992);delta=F(9,5);gamma=-F(1,2)
rates=[delta+6,gamma+3,delta+8,gamma+5,delta+2,1-gamma]
assert all(x>0 for x in rates)
assert 2-delta>0 and k-gamma-F(11,8)<0 and 2*k-1-gamma<0
out={'date':datetime.now(timezone.utc).isoformat(),'status':'PASS','moment_rates':[str(x) for x in rates],'inner_axis_decay':str(2-delta),'outer_axis_decay':str(k-gamma-F(11,8)),'zeta_outer_decay':str(2*k-1-gamma),'proof_sha256':hashlib.sha256((R/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
