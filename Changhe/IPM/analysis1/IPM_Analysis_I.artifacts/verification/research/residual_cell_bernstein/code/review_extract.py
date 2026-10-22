"""Compact exact-ceiling extract of completed three-cell arithmetic and guards."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
a=json.loads((D/'evidence/output_audit.json').read_text());g=json.loads((D/'evidence/guard_audit.json').read_text());assert a['status']=='PASS_COMPLETE_THREE_CELL_BERNSTEIN_RANGE_AUDIT' and g['status']=='PASS_EXPLICIT_INPUT_PINS_DIMENSIONS_CHRONOLOGY_AND_ORDER_BINDING';pins=dict(g['files'])
for n,h in pins.items():assert sha(B/n)==h
for p in [D/'evidence/guard_audit.json',D/'REVIEW_RESOLUTIONS.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
records=[]
for r in a['records']:
 x={k:r[k] for k in ['cell','left_exact','right_exact','h_exact']};x['bounds']={k:{n:v[n] for n in ['bernstein_strict_ceiling_exact','old_strict_ceiling_exact','chosen_strict_ceiling_exact','choice','saved_cap_exact','saved_comparison','display_only']} for k,v in r['bounds'].items()};records.append(x)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SCOPED_COMPLETED_BERNSTEIN_REVIEW_EXTRACT','counts':a['counts'],'comparison_counts':a['comparison_counts'],'records':records,'selected_cell_majorant_maxima':{k:{q:v[q] for q in ['cell','strict_ceiling_exact','display_only']} for k,v in a['selected_cell_majorant_maxima'].items()},'guard_counts':{k:g[k] for k in ['inherited_paths_explicitly_checked','coefficient_row_dimensions_checked','cell_derivative_bindings','chunk_chronology_and_primary_pins_checked','source_saved_row_ids_inherited']},'files':dict(sorted(pins.items())),'scope':a['scope']+' Text reviewer sees this exact-ceiling extract, not unbundled coefficient data. Local checks reread the completed data.'}
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'comparison_counts':out['comparison_counts']}))
