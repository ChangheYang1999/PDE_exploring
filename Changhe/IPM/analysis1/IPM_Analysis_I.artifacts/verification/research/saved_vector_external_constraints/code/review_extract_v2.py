"""Join actual arithmetic and complete source convention/metadata audits."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/saved_vector_external_constraints'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
e=json.loads((D/'evidence/review_extract.json').read_text());a=json.loads((D/'evidence/convention_audit.json').read_text());pins={}
assert e['status']=='PASS_COMPLETE_SAVED_VECTOR_CONSTRAINT_REVIEW_EXTRACT'
assert a['status']=='PASS_COMPLETE_CONVENTION_TYPES_MANUAL_METADATA_AND_INCIDENCE_AUDIT'
for obj in [e,a]:
 for n,h in obj['files'].items():assert sha(B/n)==h and (n not in pins or pins[n]==h);pins[n]=h
expected={'guarded_piece_scalars':555920,'manual_metadata_scalars':18,'manual_column_labels':7210,'manual_column_modes':7210,'endpoint_contributions':1286,'exact_trace_rechecks':28840,'source_float_trace_comparisons':28840,'symbolic_identities':16}
assert a['counts']==expected and a['scalar_types']=={'builtins.float':152844,'numpy.float64':403076}
assert F(a['max_source_float_trace_error_exact'])<F('4.1e-14')
assert [r['M'] for r in a['families']]==[16,24] and [r['endpoint_contributions'] for r in a['families']]==[515,771]
assert sum(a['incidence_breakdown'].values())==1286
for pp in [D/'evidence/review_extract.json',D/'evidence/convention_audit.json',D/'REVIEW_GAPS_RESOLVED.md',Path(__file__)]:pins[str(pp.relative_to(B))]=sha(pp)
out=dict(e);out.update(utc=datetime.now(timezone.utc).isoformat(),status='PASS_COMPLETE_SAVED_VECTOR_CONSTRAINT_REVIEW_EXTRACT_V2',original_extract_utc=e['utc'],convention_audit={k:v for k,v in a.items() if k!='files'},files=dict(sorted(pins.items())))
with (D/'evidence/review_extract_v2.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'supplemental_counts':expected}))
