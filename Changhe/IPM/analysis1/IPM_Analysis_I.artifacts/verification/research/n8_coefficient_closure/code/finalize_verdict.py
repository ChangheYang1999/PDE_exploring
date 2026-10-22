"""Freeze local coefficient closure after two complete actual-model reviews."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_coefficient_closure';E=D/'evidence';R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
c=json.loads((E/'checks.json').read_text());assert c['status']=='PASS_INDEPENDENT_SOURCE_COEFFICIENT_CLOSURE'
assert c['counts']=={'frozen_dependency_pins':82,'exact_scalar_identities':4,'engine_strict_inequalities':8}
for f,h in c['files'].items():assert sha(B/f)==h,f
assert F(c['exact']['K_1_upper'])==F(100000000,314446949)<F(3181,10000)
files={};dependencies={}
for name,h,status in [('n8_density_hessian','c590ba0d354b26595bd1131f68ca87bbc9875c9d248b4cf5fdf71344ef6e01ca','CONFIRMED_DENSITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY'),('n8_velocity_hessian','8a35f9cb43b241bd7a880b03aa8fcfdc01806a2517f50dbea99530e03a2455d5','CONFIRMED_VELOCITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY'),('source_local_estimate','81801cde767bf540ecc7dfc31ea89eeb1c641b0d0be1a93217468f7015be0cf7',None),('canonical_strain_sign','ca191db6d3e5902c5bed0e0fbb62e400d78740013762a7218d8c98636f180ae8',None)]:
 p=B/'research'/name/'evidence/verdict.json';assert sha(p)==h;v=json.loads(p.read_text())
 if status:assert v['status']==status
 dependencies[name]={'status':v['status'],'sha256':h};files[str(p.relative_to(B))]=h
reviews={}
for tag in ['n8_coefficient_closure','n8_coefficient_followup']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='n8_coefficient_followup':assert 'ACCEPT_SOURCE_COEFFICIENT_CLOSURE_WITH_EXPLICIT_DEPENDENCIES' in ans[:200] and 'I found no gap' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SOURCE_COEFFICIENT_SMALLNESS','exact':c['exact'],'counts':c['counts'],'dependencies':dependencies,'reviews':reviews,'scope':'Coefficient condition closed independently of tighter N8v2 producer outputs. Positive Frobenius tensor bounds match topic77 exactly. K1 is the resulting conditional local estimate coefficient.','remaining_local_hypotheses':['Exact equilibrium and derivative matrix at P','Source gradient bracket and constant divergence','Regularity, cutoff and function domain'],'open':['Tighter producer N8v2 derivative claims','Global inverse and rank-one denominator','Residual norm, nonlinear closure and endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
