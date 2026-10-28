from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,math
from flint import arb,ctx
ctx.prec=512;ctx.threads=1
TOP=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
B0=F(5,2)-F(3,200)-F(512,2197)-F(1,50)
exp5_lower=sum(F(5)**j/math.factorial(j) for j in range(8))
exp2half_lower=sum(F(5,2)**j/math.factorial(j) for j in range(5))
rational_gap=B0-F(1,16)-F(80,39)
assert exp5_lower>122 and exp2half_lower>10 and rational_gap>0
B=arb(B0.numerator)/B0.denominator-arb(5)/2*(1-arb(122)**(-arb(1)/200))
L=2*arb(10)**(arb(1)/100)
assert B>L and B>arb(217)/100 and L<arb(205)/100
out={'date':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED counterexample','p':1,'alpha':'1/100','R':1,
     'B0_exact':str(B0),'exp5_polynomial_lower':str(exp5_lower),'exp2half_polynomial_lower':str(exp2half_lower),'purely_rational_gap':str(rational_gap),'I_alpha_lower_ball':str(B),'Holder_seminorm_upper_ball':str(L),'strict_gap_ball':str(B-L),
     'reported_separated_bounds':'I_alpha>2.17; [h]_(y,1)<2.05','precision_bits':ctx.prec,'quadrature':'none; explicit analytic integral loss bounds',
     'proof_sha256':sha(TOP/'PROOF.md'),'code_sha256':sha(Path(__file__))}
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
