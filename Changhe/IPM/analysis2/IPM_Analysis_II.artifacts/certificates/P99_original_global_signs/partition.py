"""Exact completeness audit of the new far Taylor-box table, not a field audit."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from hashlib import sha256
import json,math,time
from flint import arb,ctx
here=Path(__file__).parent;root=here.parents[2];num=root.parent/'s1-num/research';ctx.prec=256;start=time.monotonic()
source=num/'data/certM_131_far.jsonl';rows=[json.loads(x) for x in source.read_text().splitlines() if x.strip()];origin=[r for r in rows if 'origin_box_h' in r];cells=[r for r in rows if 'origin_box_h' not in r]
nr=math.ceil(math.log(1000000/10000)/math.log(1.02));assert nr==233;rr=[10000*1.02**i for i in range(nr+1)];tt=[k*math.pi/2/80 for k in range(81)];seen=set()
for row in cells:
 key=row['i'],row['k'];assert key not in seen;seen.add(key);i,k=key;assert 0<=i<nr and 0<=k<80;assert row['depth']==0 and row['status']=='ok' and not row.get('split');assert all(math.isfinite(x) for x in row.values() if isinstance(x,float));assert (row['r_lo'],row['r_hi'],row['t_lo'],row['t_hi'])==(rr[i],rr[i+1],tt[k],tt[k+1])
assert seen=={(i,k) for i in range(nr) for k in range(80)}
assert F(rr[0])==10000 and F(rr[-1])>1000000
old=json.loads((root/'research/93_polar_covering_audit/verification/partition.json').read_text());assert old['all_pass'] and F(old['radial_outer_exact'])>F(rr[0])
def A(v):
 q=F(v);return arb(q.numerator)/q.denominator
angles=[]
for k,t in enumerate(tt):
 for name in ['sin','cos']:
  v=getattr(A(t),name)();lo=F(float(v.lower()))*(1-F(1,2**40)) if float(v.lower())>0 else F(0);hi=F(float(v.upper()))*(1+F(1,2**40));assert A(lo)<=v and A(hi)>=v;angles.append([k,name])
assert A(tt[-1])<arb.pi()/2 and A(F(float(A(tt[-1]).sin().upper()))*(1+F(1,2**40)))>1
stored={}
for suffix in ['summary','B2','Mk']:
 p=num/f'data/certM_131_far_{suffix}.json';stored[suffix]=json.loads(p.read_text())
record={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'cell_count':len(cells),'extra_origin_records':len(origin),'radial_intervals':nr,'angles':80,'angle_checks':len(angles),'first_radius_exact':str(F(rr[0])),'last_radius_exact':str(F(rr[-1])),'cover_overlap_exact':str(F(old['radial_outer_exact'])-F(rr[0])),'table_sha256':sha256(source.read_bytes()).hexdigest(),'stored_outputs':stored,'seconds':time.monotonic()-start,'scope':'Exact table completeness, finite endpoints, overlap and enclosing angle-box geometry. Does not independently certify each Cartesian field enclosure.'}
(here/'partition.json').write_text(json.dumps(record,indent=2)+'\n');print(record['utc'],len(cells),'cells and',len(angles),'angle checks PASS',record['seconds'],flush=True)
