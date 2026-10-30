from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json,hashlib
ctx.prec=512;root=Path(__file__).resolve().parents[1]
p=root.parent/'residual_witness/source/N4_cartesian_witnesses.json'
if not p.exists():p=root.parent/'new_ball_point_audit/source/N4_cartesian_witnesses.json'
q=root/'source/N4_point_gaps.json'
fields=json.loads(p.read_text())['rows'];targets=json.loads(q.read_text())['rows']
def A(x):
    x=Q(x);return arb(x.numerator)/x.denominator
s=A(Q(1,131072));r=A(Q(1,16384));C0=1/(2*(arb.pi()*(1+s)).sqrt());C1=1/(8*arb.pi()*s*(1+s)).sqrt()
rows=[]
for w in fields:
    f=w['fields'];bound=(C1*arb(f['velocity_norm'])+C0*(1+arb(f['gradient_norm'])))*r+C0*C1*r*r
    gap=abs(arb(f['residual']))-bound
    target=next(t for t in targets if t['candidate']==w['candidate'])
    checks={}
    for key,val in [('gap',gap),('necessary_upper',bound)]:
        t=target[key];lo,hi=A(t['lower']),A(t['upper'])
        checks[key]=not(val<lo or val>hi)
    assert gap>0 and all(checks.values())
    rows.append({'candidate':w['candidate'],'point':w['point'],'gap':gap.str(70),'necessary_upper':bound.str(70),'N4_interval_overlap':checks})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'s':'1/131072','radius':'1/16384','rows':rows,
'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_sha256':hashlib.sha256(q.read_bytes()).hexdigest()}
(root/'verification/point_reproduction.json').write_text(json.dumps(out,indent=2)+'\n')
for row in rows:print(row['candidate'],row['gap'])
