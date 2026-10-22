"""Freeze the complete two-engine density Hessian bound and declared dependencies."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/n8_density_hessian';E=D/'evidence';R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());d=json.loads((E/'density_inputs.json').read_text())
assert c['status']=='PASS_INDEPENDENT_DENSITY_HESSIAN_BOUND' and a['status']=='PASS_DENSITY_OUTPUT_ALGEBRA_GEOMETRY_AUDIT'
assert F(c['bound_exact'])==F(a['bound_exact'])==F(5059,10000)
assert a['counts']=={'exact_differential_coefficient_identities':233856,'interval_square_checks':10,'complete_radial_cells':13}
for doc in [c,a,d]:
 for p,h in doc['files'].items():assert sha(B/p)==h,p
for kind in ['arb','iv']:assert F(c[kind+'_squared_upper_exact'])<F(5059,10000)**2
assert F(a['source_coefficient_uncertainty_upper_exact'])<F(1,10**50)
reviews={};files={}
for tag in ['n8_density_proof','n8_density_closure','n8_density_provenance']:
 m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),tag
 if tag=='n8_density_provenance':assert 'ACCEPT_DENSITY_HESSIAN_BOUND_ARCHIVE_DEPENDENCY' in ans[:200] and 'No concrete unresolved calculation gap remains' in ans
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_DENSITY_HESSIAN_BOUND_WITH_ARCHIVE_DEPENDENCY','bound_exact':'5059/10000','disc_radius_exact':'99/2000','counts':c['counts'],'fresh_audit_counts':a['counts'],'reviews':reviews,'dependencies':['Audited canonical modal_v2 density coefficient archive and exact partition','Normalization and stated source-center bracket'],'scope':'Complete own Hessian enclosure on full covering rectangle. No geometric exclusion filter or producer derivative claim is used. Shared canonical archive is explicit.','open':['Velocity Hessian bound','Full local source inverse hypotheses','Global inverse, rank-one denominator, nonlinear closure and decisive endpoints'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
