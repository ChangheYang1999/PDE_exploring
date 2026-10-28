from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import json
ctx.prec=384
theta=arb(1)/122;alpha=arb(1)/244
constant=arb(2)**(1-alpha)/(2*arb.pi()).sqrt()*(1/((arb(24000000)/21)*(2*alpha+4))+1/(2*(theta-alpha))).sqrt()
assert constant<9 and 40*constant<360
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'theta':'1/122','alpha':'1/244','precision_bits':384,'embedding_constant':constant.str(65),'inverse_to_holder_constant':(40*constant).str(65),'safe_embedding_bound':9,'safe_inverse_to_holder_bound':360,'forcing_norm':'E_theta in SOBOLEV_HOLDER_PROOF.md; not the ordinary Holder norm.'}
Path(__file__).with_name('holder_embedding_constant.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
