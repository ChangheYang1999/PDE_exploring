"""Freeze the restricted finite verdict with actual-model provenance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
a=read(D/'evidence/finite_audit.json');assert a['status']=='PASS_V21_FINITE_AUDIT_REVIEW_PENDING_PHYSICAL_OPEN';pins=dict(a['pins']);assert len(pins)==197
for f,h in pins.items():assert sha(B/f)==h,f
reviews={}
for tag,expected in [('forcing_composed_calculus','372abf769f01a447f463378dc23b6cb34a03fc5e47933b5436af311ce70ab890'),('forcing_composed_followup','3729dce5d40698b6d0418482dd8262d524577ba57d7c206c695db9194399fff9')]:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']==expected
 assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text()
 if tag.endswith('followup'):assert 'the restricted finite result is now acceptable' in text and 'No other gap was found' in text
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in [D/'evidence/finite_audit.json',D/'FINAL_ADJUDICATION.md',Path(__file__)]:pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_V21_FINITE_COMPONENTS_PHYSICAL_FORCING_OPEN','prior_finite_pins':197,'rows':43949,'geometry_each_engine':106496,'part_pairs':208,'conditional_strict_norm_ceilings':a['conditional_norm_ceilings'],'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'PROOF plus ADDENDUM plus FINAL_ADJUDICATION; physical models, individual series operands, historical execution and every PDE endpoint remain OPEN.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
