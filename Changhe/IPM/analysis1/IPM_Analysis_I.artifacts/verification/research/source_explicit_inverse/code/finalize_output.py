"""Final current-file and actual-model gates for the topic95 auxiliary bound."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from functools import lru_cache
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_explicit_inverse';E=D/'evidence';R=B/'notes/reviews'
@lru_cache(None)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
files={};checks=0
for name in ['checks.json','output_audit.json']:
 obj=json.loads((E/name).read_text())
 for p,h in obj['files'].items():assert sha(str(B/p))==h,p;checks+=1;files[p]=h
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text())
assert c['status']=='PASS_EXPLICIT_AUXILIARY_INVERSE_BOUND' and a['status']=='PASS_ARTIFACT_AND_FRESH_SCALAR_AUDIT'
assert a['counts']['manufactured_mixed_cartesian_identities']==1344 and a['counts']['fresh_scalar_containments']==16 and a['counts']['uniform_interval_ceiling_checks']==2
assert sha(str(D/'PROOF.md'))==json.loads((E/'proof_first.json').read_text())['proof_sha256']
for e in ('arb','iv'):
 assert F(a['scalar_results'][e]['uniform_inverse_upper_exact'])<F('1.2e35')
 for key,val in [('61/20','2.672e34'),('153/50','3.518e34'),('31/10','1.068e35')]:
  assert F(c['scalar_results'][e]['rows'][key]['inverse_upper'])<F(val)
for name in ['source_semigroup','source_order_family','n8_density_hessian','n8_velocity_hessian','n8_coefficient_closure','source_instance']:
 p=B/'research'/name/'evidence/verdict.json';v=json.loads(p.read_text());assert v['status'].startswith('CONFIRMED')
 files[str(p.relative_to(B))]=sha(str(p))
 for f,h in v['files'].items():assert sha(str(B/f))==h,f;checks+=1
reviews={}
for kind in ('proof','closure','final'):
 tag='explicit_source_inverse_'+kind;m=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5'
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(t['text'] for t in raw['content'] if t['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert any(word in ans.lower() for word in ('no fatal','accept','sound')),tag
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suffix in ['metadata.json','response.json','response.md','request.txt']:
  p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(str(p))
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(str(p))
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXPLICIT_AUXILIARY_INVERSE_BOUND','dependency_pin_comparisons':checks,'scope':'Exact normalized modal_v2, actual source P, chosen compact C4 cutoff at delta33/2000. Maximal distributional Hs auxiliary inverse on all3.05<=s<=3.1; uniform norm<1.2e35. Canonical moment archive imported, not a second whole-plane integration. Read PROOF,ADDENDUM,AUDIT_METHOD,CLOSURE_NOTES,PUBLICATION together.','named_order_ceilings':{'3.05':'2.672e34','3.06':'3.518e34','3.1':'1.068e35'},'uniform_ceiling':'1.2e35','producing_counts':c['counts'],'audit_counts':a['counts'],'reviews':reviews,'open':['Global normalized full-plane IPM inverse','Physical rank-one denominator','Outer matching, saddle and far-field realization','High-norm residual and nonlinear closing inequalities','Useful bound for the proposed closing estimate','Every decisive YES or NO endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'dependency_checks':checks,'sha256':sha(str(E/'verdict.json'))},indent=2))
