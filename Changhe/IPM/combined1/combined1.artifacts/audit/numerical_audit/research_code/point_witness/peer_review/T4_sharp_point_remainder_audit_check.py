from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
from flint import arb,ctx
start=time.monotonic();ctx.prec=512
root=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=root/'source/fields.json';q=root/'source/N4_sharp_box.json'
fields=json.loads(p.read_text())['rows'];target=json.loads(q.read_text())['point_rows']
s=arb(1)/8192;r=arb(43)/50000
C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt()
rows=[]
for w in fields:
 f=w['fields'];upper=r*(C1*arb(f['velocity_norm'])+C0*(1+arb(f['gradient_norm'])))+C0*C1*r*r
 gap=abs(arb(f['residual']))-upper;t=next(x for x in target if x['candidate']==w['candidate'])
 assert upper.overlaps(arb(t['upper'])) and gap.overlaps(arb(t['gap']))
 assert bool(gap>0)==t['strict_exclusion']
 rows.append({'candidate':w['candidate'],'upper':upper.str(75),'gap':gap.str(75),'excluded':bool(gap>0),'both_intervals_overlap':True})
record={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':digest(root/'PROOF.md'),'code_sha256':digest(Path(__file__)),'fields_sha256':digest(p),'N4_sha256':digest(q),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(root/'verification/results.json').write_text(json.dumps(record,indent=2)+'\n')
for x in rows:print(x)
