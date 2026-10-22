"""Compact actual-output extract for saved-vector source-constraint review."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
a=json.loads((D/'evidence/output_audit.json').read_text());c=json.loads((D/'data_exact/constraints.json').read_text());m=json.loads((D/'data_exact/manifest.json').read_text());s=json.loads((D/'evidence/source_binding.json').read_text());pins=dict(a['files'])
assert a['status']=='PASS_EXACT_SAVED_VECTOR_EXTERNAL_CONSTRAINTS_INDEPENDENT_IEEE_MONOMIAL_AND_IV220'
for n,h in pins.items():assert sha(B/n)==h
for p in [D/'evidence/output_audit.json',D/'IMPLEMENTATION_REPAIR.md',D/'evidence/first_check_failure.json',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_COMPLETE_SAVED_VECTOR_CONSTRAINT_REVIEW_EXTRACT','producer_start':c['start_utc'],'producer_utc':c['utc'],'audit_start':a['start_utc'],'audit_utc':a['utc'],'source_binding_utc':s['utc'],'source_binding_status':s['status'],'capture_utc':m['utc'],'families':m['families'],'counts':a['counts'],'producer_counts':c['counts'],'summaries':a['summaries'],'files':dict(sorted(pins.items())),'scope':'Actual local exact full check, all5 vectors in both preselected files, all800 source functionals. Text reviewer sees complete scalar extract and code, not unbundled coefficient arrays. Same frozen column inputs, distinct vector importer and polynomial algorithms. Physical full-field traces, ideal SVD and PDE conclusions excluded.'}
with (D/'evidence/review_extract.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'counts':a['counts']}))
