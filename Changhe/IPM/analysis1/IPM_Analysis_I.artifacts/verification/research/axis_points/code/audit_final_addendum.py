"""Final exact input-count, singular-point and immutable-audit checks."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
from mpmath import iv
iv.dps=80
B=Path(__file__).resolve().parents[3];E=B/'research/axis_points/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def q(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
raw=json.loads((B/'data_exact/x3.json').read_text());assert raw['integers']['angular']==200
k,L=[q(F.from_float(float.fromhex(raw['scalars_hex'][v]))) for v in ('k','L')]
hs={'rule_cover_audit.json':'b0268e3093bd7ed2af59e67a1614cf226919aef83d1de843a79cef24706b53ee','final_iv_audit.json':'8c5feb388782f05b9659f19adab30f3738edf5f1862f8d322f7197f9b56f9ce8','library_provenance_audit.json':'4d4a3c7826ffe4cd16ab896c06c1e2e32a301d96b95b837df0908fccc57b3e6f'}
for name,h in hs.items():assert sha(E/name)==h
rows=[]
for tag in ('axis7','axis10'):
 p=E/(tag+'_partition.json');part=json.loads(p.read_text());x=q(part['settings']['x']);lo,hi=map(F,part['removed_q_strip']);qs=1-(1+(x/L)**2)**((k-1)/2)
 assert q(lo).b<qs.a and qs.b<q(hi).a
 rows.append({'tag':tag,'partition_sha256':sha(p),'q_star':str(qs),'removed_q_strip':list(map(str,(lo,hi))),'q_star_strictly_inside_strip':True})
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'x3_angular_max':200,'pinned_prior_audits':hs,'singular_point_checks':rows,'scope':'Lightweight addendum. Does not repeat either full real quadrature or the complex remainder computation.'}
(E/'final_addendum.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
