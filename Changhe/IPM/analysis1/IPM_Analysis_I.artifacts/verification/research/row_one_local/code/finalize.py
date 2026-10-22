"""Freeze the independently checked first-row corollary."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/row_one_local';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((D/'evidence/audit.json').read_text());assert a['status']=='PASS_FIRST_ROW_COROLLARY_REQUIRES_REVIEW' and a['prior_pins']==283 and a['strict_row_ceiling_checks']==8
assert F(a['exact_defect_lower_margin'])>F('6.7015e-7')
pins=dict(a['pins'])
for f,h in pins.items():assert sha(B/f)==h,f
tag='row_one_local_closure';m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text()
assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text() and '**ACCEPT.**' in text
for s in ('_request.txt','_metadata.json','_response.json','_response.md'):
 p=R/(tag+s);pins[str(p.relative_to(B))]=sha(p)
for p in [D/'evidence/audit.json',D/'FINAL_ADJUDICATION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ALL_ADMISSIBLE_SINGLE_TAIL_FIRST_ROW_LOCAL_BOUNDS','strict_component_C3_ceilings':a['strict_component_C3_ceilings'],'strict_source_derivative_lower':a['strict_source_derivative_lower'],'exact_defect_margin':a['exact_defect_lower_margin'],'prior_pins':a['prior_pins'],'reviews':{tag:{k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','end_utc']}},'scope':'PROOF with FINAL_ADJUDICATION. Reuses two independently audited114 row-majorants; no third convolution. Every admissible105 family cutoff, no surrounding exclusion or endpoint.','files':dict(sorted(pins.items()))}
p=D/'evidence/verdict.json';p.write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'pins':len(pins),'sha256':sha(p)}))
