"""Evaluate audited pointwise necessity on two newly specified balls."""
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
BASE=Path(__file__).resolve().parents[1]
ctx.prec=512
source=BASE/'verification/cartesian_witnesses.json';old=json.loads(source.read_text())
balls=[('FW-T-TB-rebal-v1',arb(1)/65536,arb(3)/32768),
       ('T4-graded-rational-box-1',arb(1)/50000,((arb(1)/5000)**2+2*(arb(1)/3000000)**2+(arb(1)/50000000)**2).sqrt())]
rows=[]
for label,s,R in balls:
    C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt()
    for row in old['rows']:
        f={k:arb(v) for k,v in row['fields'].items()}
        A=C1*f['velocity_norm']+C0*(1+f['gradient_norm']);B=C0*C1
        upper=A*R+B*R*R;gap=abs(f['residual'])-upper
        root=2*abs(f['residual'])/(A+(A*A+4*B*abs(f['residual'])).sqrt())
        rows.append({'candidate':row['candidate'],'framework':label,'point':row['point'],
                     's':s.str(50),'H2s_radius_upper':R.str(50),'necessary_upper':upper.str(65),
                     'gap':gap.str(65),'positive_gap':bool(gap>0),'necessary_radius_lower':root.str(65)})
        print(label,row['candidate'],gap.str(20),bool(gap>0),flush=True)
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':ctx.prec,
        'status':'N4-ORIGIN; independent scalar reproduction requested','rows':rows}
(BASE/'verification/new_ball_gaps.json').write_text(json.dumps(result,indent=2)+'\n')
