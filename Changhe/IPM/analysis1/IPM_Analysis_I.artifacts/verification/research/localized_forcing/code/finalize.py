"""Freeze the finite result without accepting the physical forcing certificate."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
a=read(D/'evidence/followup_audit.json')
assert a['status']=='PASS_FINITE_FOLLOWUP_REQUIRES_REVIEW_PHYSICAL_FORCING_OPEN'
pins=dict(a['pins']);assert len(pins)==132
for f,h in pins.items():assert sha(B/f)==h,f
assert len(a['reviews'])==3 and len(a['historical_supplied_versions'])==1
assert a['new_counts']=={'source_assignments':17,'power_table_identity':598,'source_predecessor_pins':42,'r2_constant_checks':24576,'native_boundary_cases':7,'public_parsed_claims':36,'downward_displays':22}
tag='localized_forcing_linkage_followup'
m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']=='7fa9c8a2c67d424962b81b89223584b9bca0d152985cb446f885b2c561f5be88'
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
assert text==(R/(tag+'_response.md')).read_text() and 'ACCEPT for the restricted finite scope' in text
for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
 p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in [D/'evidence/followup_audit.json',D/'FINAL_ADJUDICATION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
reviews=dict(a['reviews']);reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','end_utc']}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN','prior_finite_pins':132,'checks':{'geometry_each_engine':106496,'retained':43949,'omitted_outside_support':62547,'cutoff_each_engine':219745,**a['new_counts']},'refuted':['Generic all-input r2 outward rule','Upward display of22of36 saved endpoints'],'conditional_strict_norm_ceilings':{'1':['2.84903','2696.18','5.65330'],'500':['4.43139','4583.92','8.87175']},'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'PROOF, component addenda and FINAL_ADJUDICATION. Actual physical forcing norm and all decisive endpoints OPEN.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
