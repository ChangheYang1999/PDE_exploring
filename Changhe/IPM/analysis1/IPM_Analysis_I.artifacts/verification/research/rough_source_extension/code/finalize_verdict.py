"""Freeze topic100 only after current dependency and whole review audits."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/rough_source_extension';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_EXACT_DIAGNOSTICS_AND_CURRENT_DEPENDENCIES'
assert c['counts']=={'exact_symbolic_identities':21,'affine_box_order_vertices':16,'dependency_current_hash_comparisons':416}
files={};pins=0
for f,h in c['files'].items():assert sha(B/f)==h,f;files[f]=h;pins+=1
for name,rec in c['dependencies'].items():
 p=B/'research'/name/'evidence/verdict.json';assert sha(p)==rec['verdict_sha256']
 v=json.loads(p.read_text());assert v['status']==rec['status'] and v['status'].startswith('CONFIRMED')
 assert len(v['files'])==rec['current_file_hash_comparisons']
 for f,h in v['files'].items():assert sha(B/f)==h,f;pins+=1
reviews={}
for kind in ('proof','closure'):
 tag='rough_source_extension_'+kind
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text())
 req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5'
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(z['text'] for z in raw['content'] if z['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert 'accept' in ans.lower()
 assert 'research/source_order_family/PROOF.md' in m['files']
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_ROUGH_SOURCE_EXTENSION','counts':c['counts'],'closure_current_hash_comparisons':pins,'scope':'V33(a-e), with the repairs and precise hypotheses in PROOF, ADDENDUM, CLOSURE_NOTES and PUBLICATION. Auxiliary rough maximal-domain inverse, local estimate with e_A replacement, global-Hs zero-jet graph completion, conditional K1 at3.06 and rough dilation. No new numerical enclosure.','refuted':['Lead r3 L5 omission of N2 from N','Lead r3 intermediate continuity claims for N of mollified h and N of its separate jet correction'],'open':['Weighted-space completion outside global Hs','Uniform K2,K3,K4,R over the perturbation family','Physical rank-one denominator and global inverse','Certified high-norm residual and nonlinear closure','Any decisive endpoint'],'reviews':reviews,'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'manifest_pins':len(files),'sha256':sha(E/'verdict.json'),'closure_current_hash_comparisons':pins},indent=2))
