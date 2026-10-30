from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,time
from flint import arb,ctx
start=time.monotonic();ctx.prec=512
root=Path(__file__).resolve().parents[1]
def d(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert Q(1,2)-3*4708*Q(1,28248)==0
assert Q(1,2)-4708*Q(1,28248)==Q(1,3)
assert 168**2<28248
bound=Q(25,54684)
assert bound<Q(1,2000)
assert Q(29552675,10**8)>bound and Q(55006675,10**8)>bound
sharp=arb(50)/(651*arb(28248).sqrt())
a=arb(25)/(868*arb.pi().sqrt());b=arb(25)/(434*(9416*arb.pi()).sqrt())
p=root.parent/'sharp_point_remainder_audit/source/fields.json'
rows=[]
for row in json.loads(p.read_text())['rows']:
 f=row['fields'];upper=a*arb(f['velocity_norm'])+b*(1+arb(f['gradient_norm']))+a*b
 gap=abs(arb(f['residual']))-upper
 rows.append({'candidate':row['candidate'],'uniform_point_gap':gap.str(70),'excluded_by_point':bool(gap>0)})
record={'utc':datetime.now(timezone.utc).isoformat(),'proof_sha256':d(root/'PROOF.md'),'code_sha256':d(Path(__file__)),'T2_review_sha256':d(root/'source/T2_REVIEW.md'),'uniform_H2s_radius':sharp.str(70),'rational_upper':str(bound),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(root/'verification/results.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
