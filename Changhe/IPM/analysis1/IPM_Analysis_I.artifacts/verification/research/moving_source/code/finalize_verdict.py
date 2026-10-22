"""Freeze the independently checked moving-source result."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/moving_source';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());pf=json.loads((E/'proof_first.json').read_text())
assert c['status']=='PASS_MOVING_SOURCE_CONSTANTS_WITH_ONE_CORRECTION' and a['status']=='PASS_FRESH_MOVING_SOURCE_AUDIT' and a['checks']==45
assert sha(D/'PROOF.md')==pf['proof_sha256'] and sha(E/'source/lead_lemma.md')==pf['lead_lemma_sha256']
for v in [c,a]:
 for rel,h in v['files'].items():assert sha(B/rel)==h,rel
reviews={};files={}
for kind in ['proof','closure']:
 tag='moving_source_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(z['text'] for z in raw['content'] if z['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if kind=='closure':assert 'ACCEPT (scoped conditional theorem)' in ans and 'cutoff scale: retracted' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for ext in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+ext);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
for p in c['files']:files[p]=sha(B/p)
v={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_MOVING_SOURCE_THEOREM_WITH_SCALAR_CORRECTION','counts':c['counts']|{'fresh_audit_checks':a['checks']},'motion_m_lower':c['m_public_lower'],'motion_inverse_ceiling':'0.09866','moving_velocity_obstruction_epsilon':c['epsilon'],'corrected_mu_margin':c['corrected_mu_margin'],'refuted_lead_mu_margin':c['refuted_lead_mu_margin'],'local_rows':c['local_rows'],'reviews':reviews,'scope':'Mandatory PROOF, ADDENDUM and PUBLICATION. Conditional source motion and source data, moving-source narrow exclusion, Sobolev/tail estimates and local forcing coefficient for transported family. Imported exact canonical trial data, no new full summation.','open':['Actual X3 perturbation norms','Moved cutoff norm comparisons and K2 K3 K4','Auxiliary inverse norm and physical rank-one denominator','Outer matching, full inverse and nonlinear contraction','Every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(v,indent=2)+'\n');print(json.dumps({'utc':v['utc'],'status':v['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
