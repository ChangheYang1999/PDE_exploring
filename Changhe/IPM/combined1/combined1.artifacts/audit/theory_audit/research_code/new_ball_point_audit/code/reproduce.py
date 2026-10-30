from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
import hashlib,json
from flint import arb,ctx
ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def A(x):
 x=Q(x);return arb(x.numerator)/x.denominator
p=ROOT/'source/N4_cartesian_witnesses.json'
fields=json.loads(p.read_text())['rows']
q=ROOT/'source/N4_new_ball_gaps.json'
target=json.loads(q.read_text())['rows']
boxes=[('FW-T-TB-rebal-v1',A(Q(1,65536)),A(Q(3,32768))),
       ('T4-graded-rational-box-1',A(Q(1,50000)),(A(Q(1,5000))**2+2*A(Q(1,3000000))**2+A(Q(1,50000000))**2).sqrt())]
rows=[]
for name,s,r in boxes:
 C0=1/(2*(arb.pi()*(1+s)).sqrt())
 C1=1/(8*arb.pi()*s*(1+s)).sqrt()
 for w in fields:
  F=abs(arb(w['fields']['residual']))
  V=arb(w['fields']['velocity_norm']);D=arb(w['fields']['gradient_norm'])
  a=C1*V+C0*(1+D);b=C0*C1
  bound=a*r+b*r*r;gap=F-bound;radius=2*F/(a+(a*a+4*b*F).sqrt())
  t=next(x for x in target if x['candidate']==w['candidate'] and x['framework']==name)
  assert gap>0
  assert bound.overlaps(arb(t['necessary_upper']))
  assert gap.overlaps(arb(t['gap']))
  assert radius.overlaps(arb(t['necessary_radius_lower']))
  rows.append({'candidate':w['candidate'],'framework':name,'point':w['point'],
    'H2s_radius_upper':r.str(70),'necessary_upper':bound.str(70),'gap':gap.str(70),
    'necessary_radius_lower':radius.str(70),'positive_gap':True,'all_N4_intervals_overlap':True})
record={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
 'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'target_sha256':hashlib.sha256(q.read_bytes()).hexdigest(),
 'rows':rows,'scope':'Independent scalar reproduction from the already independently confirmed Cartesian field intervals. This does not recompute those fields.'}
(ROOT/'verification/reproduction.json').write_text(json.dumps(record,indent=2)+'\n')
for row in rows:print(row['candidate'],row['framework'],row['gap'])
