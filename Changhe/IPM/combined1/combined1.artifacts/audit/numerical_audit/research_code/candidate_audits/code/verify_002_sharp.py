"""Reproduce T4-037's new sharp-box point gap from N4's prior Cartesian fields."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/candidate_audits'
a=BASE/'verification/C1-N1-002-7branch-frf_point.json'
b=BASE/'peer_review/T4_002_point.json'
data=json.loads(a.read_text());peer=json.loads(b.read_text())
assert data['canonical_sha256']==peer['canonical_sha256'] and data['point']==peer['point']
f=data['fields'];s=arb(1)/8192;r=arb(43)/50000
# Combine the directional-gradient and value terms only after enclosing each constant.
c0=1/(4*arb.pi()*(1+s)).sqrt();c1=1/(8*arb.pi()*s*(1+s)).sqrt()
upper=r*c1*arb(f['velocity_norm'])+r*c0*(1+arb(f['gradient_norm']))+r*r*c0*c1
gap=abs(arb(f['residual']))-upper
row=next(q for q in peer['ball_exclusions'] if q['framework']=='FW-T-TB-sharp-v1')
assert gap>0 and gap.overlaps(arb(row['gap'])) and upper.overlaps(arb(row['necessary_upper']))
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':data['candidate'],
 'framework':'FW-T-TB-sharp-v1','s_exact':'1/8192','radius_exact':'43/50000','point':data['point'],
 'necessary_upper':upper.str(80),'gap':gap.str(80),'independent_T4_overlap':True,'verdict':'CONFIRMED',
 'N4_fields_sha256':sha256(a.read_bytes()).hexdigest(),'T4_target_sha256':sha256(b.read_bytes()).hexdigest(),
 'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
(BASE/'verification/C1-N1-002_sharp_gap.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
