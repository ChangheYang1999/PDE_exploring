from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
import json
from flint import arb,ctx
ctx.prec=384
A=lambda q:arb(Q(q).numerator)/Q(q).denominator
d=Q(4,9);sigma=Q(11,5);M=A(d/2)*A((2-d)/d)**A(1-d/2)
C=4*A(sigma)*M/A(3-sigma-d)
assert C<15
err=(23+16*190+A(sigma)*(9*23+2*23+56/arb(2).sqrt()))/(arb(2)**32)**A(d)
assert A(Q(2,5))-err>A(Q(1,5))
assert arb(100)**A(Q(2,45))<A(Q(5,4))
record={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONDITIONAL_ARITHMETIC_ONLY','decay_exponent':str(d),'commutator_factor':C.str(60),'candidate_radius':'2^32','candidate_margin':(A(Q(2,5))-err).str(60),'required_tuple':[190,23,23,56],'open':'Exterior sector powers and general low-energy formula must be checked before certification.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
