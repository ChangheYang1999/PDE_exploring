from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
v=json.loads((B/'research/residual_point_jets/evidence/verdict.json').read_text());assert v['status']=='CONFIRMED_FINITE_POINT_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED';pins=dict(v['files'])
for n,h in pins.items():assert sha(B/n)==h
samples=json.loads((B/'research/residual_samples/evidence/sample_result.json').read_text())['samples'];prep=json.loads((B/'research/residual_point_jets/evidence/preparation.json').read_text());trial=json.loads((B/'data_exact/modal_v2.json').read_text());knots=[F.from_float(float.fromhex(q)) for q in trial['arrays']['knots']['hex']]
records=[]
for cell in [4102,4125,4211]:
 p=next(s for s in samples if s['cell']==cell);r=next(s for s in prep['points'] if s['cell']==cell);a,b=map(F,p['cell_endpoints_exact']);t=F(p['t_exact']);span=r['original_span'];assert knots[span]<=a<t<b<=knots[span+1] and t==(a+b)/2
 records.append({'cell':cell,'left_exact':str(a),'right_exact':str(b),'center_exact':str(t),'h_exact':str((b-a)/2),'original_span':span})
for i in range(6):assert F(66,4*(66-i))<1
# Signed angular frequency and two radial monomials; highest sums retain their slot.
checks=0
for f,g in [(522,521),(-522,-521),(2,1),(-2,1),(522,-521)]:
 for q,r in [(0,0),(64,64),(63,64),(1,0)]:
  idx=(522+f)*129+q+(521+g)*129+r;assert divmod(idx,129)==(1043+f+g,q+r);checks+=1
for p in [B/'research/residual_point_jets/evidence/verdict.json',B/'research/modal_repair/PROOF.md',D/'PROOF.md',D/'ADDENDUM.md',D/'evidence/proof_first.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_THREE_CELL_INPUT_BINDING','cells':records,'radial_degree':64,'disk_radius_exact':'4','radial_stride':129,'packing_checks':checks,'files':dict(sorted(pins.items())),'scope':'Point certificates inherited and whole cells exactly bound to their source spans. No cell derivative outputs yet.'}
with (D/'data_exact/manifest.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'status':out['status'],'cells':records,'pins':len(pins)}))
