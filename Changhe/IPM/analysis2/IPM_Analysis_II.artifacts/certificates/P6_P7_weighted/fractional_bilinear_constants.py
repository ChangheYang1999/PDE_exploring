from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json
from flint import arb,ctx
ctx.prec=512
th=arb(1)/62
K=(th*(1-th)).exp()*arb(3)**(th/2)*(arb(9)/5-th)**th
D=K/(arb.pi().sqrt()*th**((2-th)/4))
C=Q(13,2)*(2**26+5)
assert D<5 and C<2**29
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'theta':'1/62','K_arb':K.str(70),'D_arb':D.str(70),'D_upper':5,'bilinear_exact_upper':str(C),'bilinear_rounded_upper':2**29,'status':'PENDING_PROOF_AUDIT'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
