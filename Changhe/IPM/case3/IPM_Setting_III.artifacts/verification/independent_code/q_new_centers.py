"""Independent center/jet audit of newly frozen Q coefficient files."""
from pathlib import Path
from datetime import datetime,timezone
import json
from q_checkpoint_reader import QCheckpoint
rows=[]
for manifest in [Path('evidence/q_snapshots_20261020T2016/manifest.json')]:
 for row in json.loads(manifest.read_text()):
    c=QCheckpoint(row['snapshot']);ct=c.center_and_tail()
    a=ct['a0'];b=ct['b'];e=ct['e'];H=ct['quadrature'][-1]['H']
    q1=(H-b/3)/2;q2=-(H+b/3)/2;A=2*c.cl-1
    rows.append(dict(utc=datetime.now(timezone.utc).isoformat(),metadata=c.meta,center=ct,
                     quartic_q1=q1,quartic_q2=q2,exact_profile_T1=2*A*b+3*a*q1,
                     exact_profile_T2=2*e+a*q2,poisson_quartic=q1+q2+b/3,
                     jet_elimination=6*e-(a-2*A)*b,a_b=a*b,a_e=a*e,
                     norm_reconstruction_error=c.node_reconstruction_error(),
                     scope='Frozen finite coefficients; own scalar reader, exact local coefficient formulas and adaptive canonical quadrature. Numerical values, no exact-profile or global-strain conclusion.'))
    out=Path('evidence/q_new_centers.json');out.write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps(rows[-1]),flush=True)
