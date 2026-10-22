from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
a=json.loads((D/'evidence/output_audit.json').read_text());labels=json.loads((D/'evidence/label_audit.json').read_text());assert a['status']=='PASS_COMPLETE_THREE_CELL_CAUCHY_OUTPUT_AUDIT' and labels['status']=='PASS_EXPLICIT_SAVED_ROW_BINDING_AND_ALL_LABELS';pins=dict(labels['files'])
for n,h in pins.items():assert sha(B/n)==h
for p in [D/'evidence/label_audit.json',D/'REVIEW_RESOLUTIONS.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
records=[{k:r[k] for k in ['cell','left_exact','right_exact','h_exact','producer_seconds','independent_seconds']} for r in a['records']]
maxima={k:{q:v[q] for q in ['cell','strict_ceiling_exact','display_only']} for k,v in a['selected_cell_maxima'].items()}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_SCOPED_OUTPUT_REVIEW_EXTRACT','counts':a['counts'],'comparison_counts':a['comparison_counts'],'source_row_identifiers_checked':labels['source_rows_checked'],'selected_cells':records,'selected_cell_majorant_maxima':maxima,'files':dict(sorted(pins.items())),'scope':a['scope']+' This extract reads local complete audited outputs; a text-only reviewer does not thereby inspect unbundled coefficient files.'}
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins)}))
