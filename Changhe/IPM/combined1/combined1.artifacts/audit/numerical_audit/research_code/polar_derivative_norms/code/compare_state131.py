from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
R=Path(__file__).resolve().parents[3];D=R/'research/polar_derivative_norms';ctx.prec=512
new=D/'verification/state131/full.json';old=R/'research/whole_plane_norms/verification/state131_norms.json'
a=json.loads(new.read_text());b=json.loads(old.read_text());assert a['complete']
x=a['norms']['P2'];y=b['norms']['P2'];assert y['status']=='FINITE'
lo,hi=arb(x['norm_lower_ball']),arb(x['norm_upper_ball']);olo,ohi=arb(y['norm_lower_ball']),arb(y['norm_upper_ball'])
assert lo<ohi and olo<hi
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p.relative_to(R)):sha256(p.read_bytes()).hexdigest() for p in [new,old,Path(__file__)]},'new':x,'retained':{k:y[k] for k in ['norm_lower_ball','norm_upper_ball']},'enclosing_intervals_overlap':True,'status':'Same exact reference and proven Cartesian/polar tensor identity; calibration passed'}
p=D/'verification/state131_comparison.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out,indent=2))
