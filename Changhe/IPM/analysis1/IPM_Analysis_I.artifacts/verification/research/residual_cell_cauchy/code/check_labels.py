from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
a=json.loads((D/'evidence/output_audit.json').read_text());assert a['status']=='PASS_COMPLETE_THREE_CELL_CAUCHY_OUTPUT_AUDIT'
pins=dict(a['files']);name='research/derivative_scalar_aggregation/sources/runs__cert_deriv_middle.json';assert name in pins and sha(B/name)==pins[name]
rows=json.loads((B/name).read_text())['rows'];assert isinstance(rows,list) and len(rows)==7809
for i,row in enumerate(rows):assert row['ci']==i
counts={};checks=0
for rec in a['records']:
 cell=rec['cell'];assert rows[cell]['ci']==cell
 for key,obj in rec['bounds'].items():
  if key in rows[cell]:
   cap=F.from_float(rows[cell][key]);assert str(cap)==obj['saved_cap_exact'];label='INDEPENDENT_BOUND_BELOW_SAVED_CAP' if F(obj['total_upper_exact'])<=cap else 'INDEPENDENT_UPPER_TOO_LARGE_TO_VALIDATE_SAVED_CAP'
  else:label='NO_SAVED_FIELD'
  assert label==obj['saved_comparison'];counts[label]=counts.get(label,0)+1;checks+=1
assert counts==a['comparison_counts'] and checks==63
for p in [D/'evidence/output_audit.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
for n,h in pins.items():assert sha(B/n)==h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXPLICIT_SAVED_ROW_BINDING_AND_ALL_LABELS','source_rows_checked':7809,'selected_comparisons_checked':checks,'comparison_counts':counts,'files':dict(sorted(pins.items())),'scope':'Supplementary explicit binding guard. Does not change any cell bound; all 63 independent upper bounds exceed the saved caps, so none validates those tighter caps.'}
with (D/'evidence/label_audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({k:out[k] for k in ['utc','status','source_rows_checked','selected_comparisons_checked','comparison_counts']}))
