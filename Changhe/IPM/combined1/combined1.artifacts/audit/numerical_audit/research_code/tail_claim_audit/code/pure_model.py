"""Check pure-tail model arithmetic, explicitly not a full-residual bound."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json
from flint import arb, ctx, fmpq
ctx.prec=256
root=Path(__file__).resolve().parents[3]
source=root/'research/sector_audit/verification/stationary_principal.json'
doc=json.loads(source.read_text()); rows=[]
for branch in doc['branches']:
    if branch['index'] not in [4,5,6,7,8]: continue
    e=arb(fmpq(branch['residual_exponent']))
    A=arb(branch['forcing_full_circle_norm'])
    for R in [100,10000]:
        g0=A*arb(R)**(e+1)/(-2*e-2).sqrt()
        rf=A*arb(R)**(e+2)/(-2*e-4).sqrt() if e < -2 else None
        rows.append({'last_retained_branch':branch['index']-1,'missing_sector_h':branch['index'],
                     'radius':R,'exponent':branch['residual_exponent'],'angular_full_circle_norm':str(A),
                     'pure_model_G0':g0.str(30),'pure_model_rF':rf.str(30) if rf else 'INFINITE'})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
     'input_sha256':sha256(source.read_bytes()).hexdigest(),
     'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'scope':'Equalities for a pure exterior power only; not lower bounds for a complete IPM residual.',
     'rows':rows}
dest=Path(__file__).parent.parent/'verification/pure_model.json';dest.parent.mkdir(exist_ok=True)
dest.write_text(json.dumps(out,indent=2)+'\n')
for row in rows: print(row)
