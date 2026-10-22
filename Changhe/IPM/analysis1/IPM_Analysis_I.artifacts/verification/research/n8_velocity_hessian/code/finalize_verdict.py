"""Freeze the complete independent velocity Hessian certificate and review chain."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_velocity_hessian';E=D/'evidence';R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
c=json.loads((E/'full_checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());d=json.loads((E/'moment_inputs.json').read_text())
assert c['status']=='PASS_FULL_INDEPENDENT_VELOCITY_HESSIAN_BOUND' and a['status']=='PASS_FULL_VELOCITY_COVERAGE_OUTPUT_AND_EXACT_ALGEBRA_AUDIT'
assert c['counts']==a['counts'] and c['counts']['angular_radial_boxes']==8320 and c['counts']['cells']==13
assert F(c['bound_exact'])==F(a['bound_exact'])==F(743,2500)
for doc in [c,a,d]:
 for p,h in doc['files'].items():assert sha(B/p)==h,p
for kind in ['arb','iv']:assert F(c[kind+'_squared_upper_exact'])<F(743,2500)**2
reviews={};files={}
for tag in ['n8_velocity_proof','n8_velocity_implementation','n8_velocity_closure']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),tag
 if tag=='n8_velocity_closure':assert 'ACCEPT_FULL_VELOCITY_HESSIAN_WITH_ARCHIVE_DEPENDENCY' in ans[:200] and 'no concrete unresolved gap' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_VELOCITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY','bound_exact':'743/2500','disc_radius_exact':'99/2000','counts':c['counts'],'fresh_audit_counts':a['audit_counts'],'reviews':reviews,'dependencies':['Audited canonical modal_v2 complete density coefficient archive and I(a), J(b) anchors','Normalization and exact source-center bracket','Topic84 exact density partition and coverage data'],'scope':'Complete own velocity Hessian enclosure on full covering rectangle. No producer N8 derivative claim or geometric filter is used. Both methods retain every source-ball error and proved remainder.','open':['Producer N8 tighter bounds','Full local source inverse hypotheses','Global inverse, rank-one denominator, nonlinear closure and decisive endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
