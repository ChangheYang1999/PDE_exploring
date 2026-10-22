"""Freeze the fully instantiated local source result and exact review provenance."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_instance';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks_v2.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_FRESH_SOURCE_AND_LOCAL_INSTANCE'
assert a['status']=='PASS_SOURCE_INSTANCE_OUTPUT_AND_LINKAGE_AUDIT'
for obj in [c,a]:
 for f,h in obj['files'].items():assert sha(B/f)==h,f
assert json.loads((E/'proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md')
reviews={};files={}
for tag in ['source_instance_proof','source_instance_followup','source_instance_closure','source_instance_publication']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='source_instance_closure':assert 'ACCEPT_ACTUAL_LOCAL_SOURCE_INSTANCE' in ans[:200]
 if tag=='source_instance_publication':assert 'accept' in ans.lower() and '0.9999999776' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ACTUAL_LOCAL_SOURCE_INSTANCE','counts':c['counts'],'output_audit_counts':a['counts'],'source_bracket':['4841405518533377/562949953421312','4841405518533711/562949953421312'],'common_mu_outward':['0.9999999774','0.9999999776'],'coefficient_E_strict_upper':'22953051/100000000','coefficient_K1_strict_upper':'0.3181','reviews':reviews,'scope':'Actual exact canonical normalized modal_v2 source and all hypotheses of topic77 local estimate, topic78 auxiliary maximal-domain inverse, and topic88 local radial source cutoff sign. PROOF, ADDENDUM, CLOSURE_NOTES, PUBLICATION jointly specify the result. Shared audited canonical archive remains a dependency.','open':['Numerical lower-order R and inverse norm','Canonical rank-one strain denominator','Outer matching and global normalized IPM inverse','Residual in target norm and nonlinear closure','Every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
