"""Authenticate two reviews and freeze only the conditional replacement theorem."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
a=read(D/'evidence/audit.json');assert a['status']=='PASS_CONDITIONAL_HESSIAN_REPLACEMENT_REQUIRES_REVIEW'
assert a['prior_pins']==139 and a['rows_each_engine']==43949 and a['finite_endpoint_tests']==22 and a['exact_polynomial_coefficients']==9
pins=dict(a['pins']);assert len(pins)==148
for f,h in pins.items():assert sha(B/f)==h,f
reviews={}
for tag in ['forcing_hessian_replacement_closure','forcing_hessian_replacement_followup']:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 txt='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert txt==(R/(tag+'_response.md')).read_text()
 assert '# FINAL ANSWER: ACCEPT' in txt
 for suf in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suf);pins[str(p.relative_to(B))]=sha(p)
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','end_utc']}
for p in [D/'evidence/audit.json',D/'ADDENDUM.md',D/'FINAL_ADJUDICATION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_HESSIAN_REPLACEMENT_ONLY','strict_conditional_ceilings':{k:v['strict_conditional_ceilings'] for k,v in a['results'].items()},'M':'9363/1000000','rows_each_arithmetic_engine':43949,'prior_pins':139,'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'PROOF plus mandatory ADDENDUM, NUMERICAL_RESULT and FINAL_ADJUDICATION. Physical G and global second partials OPEN. No actual forcing norm, original FL1/FL2, or endpoint accepted.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
