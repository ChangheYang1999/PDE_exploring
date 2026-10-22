"""Freeze only the selected-expression, contemporary finite inequality result."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 return h.hexdigest()
a=read(D/'evidence/source_binding.json');assert a['status']=='PASS_SELECTED_FROZEN_EXPRESSION_REPLAY' and a['original_audit_pins']==165 and a['epsSup_entries']==33995 and a['r2_entries']==195
pins=dict(a['pins']);assert len(pins)==168
for p,h in pins.items():assert sha(B/p)==h,p
reviews={}
for tag in ['forcing_angular_reduction_closure','forcing_angular_reduction_followup']:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 txt='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert txt==(R/(tag+'_response.md')).read_text() and 'ACCEPT' in txt[:200]
 for suff in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suff);pins[str(p.relative_to(B))]=sha(p)
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','end_utc']}
for p in [D/'evidence/source_binding.json',D/'FINAL_ADJUDICATION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_REGENERATED_ANGULAR_REDUCTIONS_ONLY','mode_sups':33995,'coefficient_entries':441935,'angular_factors':2615,'radial_powers':351,'r2_reductions':195,'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'PROOF plus mandatory ADDENDUM and FINAL_ADJUDICATION. Contemporary selected expressions and finite arithmetic only. Physical radial models, historical arrays and full forcing OPEN. No endpoint.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
