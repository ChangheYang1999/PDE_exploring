from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3];ctx.prec=192
V=Path(__file__).resolve().parent
m=json.loads((ROOT/'verifier/center-moment/verification/certificates.json').read_text());h=json.loads((V/'hessian_bounds.json').read_text());assert m['complete'] and h['complete']
assert len(m['rows'])==len(h['states'])==5 and len(h['points'])==150
assert len(set(map(tuple,h['points'])))==150
assert hashlib.sha256(json.dumps(h['points']).encode()).hexdigest()==h['points_sha256']
for obj in [m,h]:
 for dep in obj['dependencies']:assert hashlib.sha256((ROOT/dep['file']).read_bytes()).hexdigest()==dep['sha256']
rows=[]
for a,s in zip(m['rows'],h['states']):
 assert a['source']==s['source'];src=ROOT/'verifier'/s['source'];raw=src.read_bytes();assert hashlib.md5(raw).hexdigest()==a['source_md5']==s['md5'];assert hashlib.sha256(raw).hexdigest()==a['source_sha256']==s['source_sha256']
 mj=ROOT/'verifier/center-moment'/a['exact_json'];hj=Path(s['exact_json']);assert mj.read_bytes()==hj.read_bytes();assert hashlib.sha256(mj.read_bytes()).hexdigest()==a['json_sha256']==s['exact_json_sha256']
 c64=arb(a['c64']);c96=arb(a['c96']);defect=arb(a['self_consistency_ball']);assert (c64-c96).contains(0);assert not defect.contains(0) and not a['self_consistency_contains_zero']
 assert len(s['rows'])==len(h['points']);maximum=F(0)
 for pt,r in zip(h['points'],s['rows']):
  assert r['point']==pt and min(pt)>1e-7 and F(r['epsilon_exact'])==F(1,10**7)
  H=[[arb(x) for x in rr] for rr in r['Hessian_balls']];assert (H[0][1]-H[1][0]).contains(0)
  # Stored strings may be wider than their original balls, so the true
  # integer bound need not be re-derived by ceil on strings. Their sum of
  # absolute upper bounds must instead stay below the recorded integer.
  assert sum(x.abs_upper() for rr in H for x in rr)<=r['Hessian_operator_bound_integer']
  exact=F(r['Hessian_operator_bound_integer'],4*10**14);assert exact==F(r['local_hole_U_bound_exact']);assert float(exact)==r['local_hole_U_bound_float'];maximum=max(maximum,exact)
 rows.append({'source':s['source'],'source_md5':s['md5'],'center_strain':a['c96'],'identity':a['self_consistency_ball'],'points_checked':len(s['rows']),'maximum_local_hole_exact':str(maximum),'maximum_local_hole_float':float(maximum)})
out={'date':datetime.now(timezone.utc).isoformat(),'checks':'all source bytes, JSON equality and pins, dependencies, 750 point coverage and Hessian-bound/rational-hole relations, five center-ball flags','verdict':'CONFIRMED_OUTPUT_ASSEMBLY','rows':rows,'scope':'This output audit checks provenance and exact assembly, not a second enclosure computation of all Hessians.'}
(V/'certificate_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
