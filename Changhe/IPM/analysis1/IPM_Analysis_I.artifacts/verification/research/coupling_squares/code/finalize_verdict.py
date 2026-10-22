"""Freeze conditional coupling theorem and exact whole-review provenance."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/coupling_squares';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_EXACT_COUPLING_IDENTITIES_AND_SOURCE_BOX'
assert c['counts']=={'noncommuting_matrix_identities':4,'exact_frequency_inequalities':3528,'source_box_corners':8,'quadratic_cases':164}
assert c['directional_gap_exact']=='449/1000' and c['source_margin_exact']=='1687/500'
for f,h in c['files'].items():assert sha(B/f)==h,f
assert json.loads((E/'proof_first.json').read_text())['sha256']==sha(D/'PROOF.md')
reviews={};files={}
for tag in ['coupling_squares_proof','coupling_squares_closure']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='coupling_squares_closure':assert 'ACCEPT_CONDITIONAL_COUPLING_SQUARES' in ans[:200] and 'No mathematical gap remains' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_COUPLING_SQUARES','counts':c['counts'],'directional_gap_exact':c['directional_gap_exact'],'reviews':reviews,'scope':'PROOF and ADDENDUM jointly; publication supersedes pending status. Universal conditional analytic proof plus exact finite regressions, no actual coefficient constants.','open':['Actual global Wiener norms and positive coefficient extension','Weighted fractional errors, axis jets and asymptotic block','Global inverse and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
