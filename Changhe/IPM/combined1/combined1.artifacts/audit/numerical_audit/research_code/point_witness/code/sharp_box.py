"""Apply the necessary point inequality and confirmed norm components to T2-R2."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'research/point_witness/verification/cartesian_witnesses.json';data=json.loads(p.read_text())
s=arb(1)/8192;r=arb(43)/50000;eta=arb(5289)/50000000
C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt();rows=[]
for row in data['rows']:
 f=row['fields'];upper=r*(C1*arb(f['velocity_norm'])+C0*(1+arb(f['gradient_norm'])))+C0*C1*r*r
 gap=abs(arb(f['residual']))-upper
 rows.append({'candidate':row['candidate'],'point':row['point'],'upper':upper.str(65),'gap':gap.str(65),
              'strict_exclusion':bool(gap>0),'test_inconclusive':not bool(gap>0)})
parts={};inputs={}
for label in ('G0','G1','P2'):
 q=ROOT/f'research/whole_plane_norms/verification/d2_{label}_ball_2048.json';v=json.loads(q.read_text())
 parts[label]=arb(v['norm_lower_ball']);inputs[label]=sha256(q.read_bytes()).hexdigest()
partial=(parts['P2']**2+16384*parts['G1']**2+262144*parts['G0']**2).sqrt()
lower=(1-34*s)*partial
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'framework':'FW-T-TB-sharp-v1','s':'1/8192','r':'43/50000','eta':'5289/50000000',
     'field_source_sha256':sha256(p.read_bytes()).hexdigest(),'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
     'point_rows':rows,'component_sha256':inputs,'partial_E2_lower':partial.str(70),'d2_Ns_lower':lower.str(70),'d2_threshold_ratio_lower':(lower/eta).str(70),
     'scope':'A failed point exclusion is inconclusive, not a feasibility result. The d2 norm bound omits its nonnegative H contribution.'}
q=ROOT/'research/point_witness/verification/T2_R2_sharp_box.json';q.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
