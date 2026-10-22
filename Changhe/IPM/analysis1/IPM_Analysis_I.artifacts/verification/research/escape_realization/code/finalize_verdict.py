"""Finalize conditional V25 result with whole actual-model provenance."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/escape_realization';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_ESCAPE_REALIZATION_IDENTITIES_AND_BETA_BOUND' and a['status']=='PASS_FRESH_ESCAPE_SCALAR_AUDIT'
assert a['complete_primary_enclosures_containing_fresh_result']==2 and a['decimal_0078148_is_inward_upper']
for obj in [c,a]:
 for f,h in obj['files'].items():assert sha(B/f)==h,f
assert json.loads((E/'proof_first.json').read_text())['proof_sha256']==sha(D/'PROOF.md')
reviews={};files={}
for tag,stop in [('escape_realization_proof','max_tokens'),('escape_realization_complete2','end_turn'),('escape_realization_closure','end_turn')]:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']==stop
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='escape_realization_closure':assert 'ACCEPT_CONDITIONAL_ESCAPE_REALIZATION_CLOSED' in ans[:200] and 'retracted' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']};reviews[tag]['counts_as_complete_acceptance']=stop=='end_turn'
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
failed='escape_realization_complete';m=json.loads((R/(failed+'_metadata.json')).read_text());assert 'ValidationException' in m['availability_error'] and 'actual_response_model' not in m
for suffix in ['metadata.json','request.txt']:
 p=R/(failed+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_ESCAPE_REALIZATION','counts':c['counts'],'raw_strain_safe_upper':'78149/10000000','prompt_functional_safe_upper':'521/200000','fresh_scalar_precision_bits':1536,'reviews':reviews,'availability_attempt':{'tag':failed,'error':m['availability_error'],'counts_as_acceptance':False},'scope':'PROOF with ADDENDUM, CLARIFICATIONS, REVIEW_RESPONSE and PUBLICATION. In particular current SPEC3.22 raw-strain E2 coefficient agrees, while zero-derivative and outward-ceiling corrections remain for E5.','open':['Actual escape weight and weighted or conormal commutator norms','Equivalence of unspecified A_s to the exact models','Source basepoint hypotheses within this topic','E6 parametrix and assembled outer estimate','Global inverse and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
