"""Freeze topic102 after both engines, independent output and actual-model review.
No JavaScript/TypeScript, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from functools import lru_cache
import hashlib,json,sys,re
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/sobolev_source_box';E=D/'evidence';R=B/'notes/reviews'
@lru_cache(None)
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def load(p):return json.loads(p.read_text())
assert not (E/'verdict.json').exists()
c=load(E/'checks.json');a=load(E/'output_audit.json');p=load(D/'source/parameters.json')
assert c['status']=='PASS_TWO_INDEPENDENT_SOURCE_BOX_ENCLOSURES'
assert a['status']=='PASS_EXACT_OUTPUT_AND_SYMBOLIC_AUDIT' and a['checks_sha256']==sha(E/'checks.json') and a['source_sha256']==sha(D/'code/audit_output.py')
assert c['counts']['exact_simple_interior_knots']==a['counts']['independent_exact_simple_knots']==1557
assert c['counts']['closed_ball_neighbourhood_checks']==a['counts']['independent_neighbourhood_checks']==4
assert c['counts']['direct_imported_numeric_links']==5
for eng in ('arb384','rational_machin_isqrt'):
 assert c['counts'][eng+'_positive_enclosures']==30 and c['counts'][eng+'_strict_upper']==20 and c['counts'][eng+'_strict_lower']==4
 for name,target in p['upper_claims'].items():assert Q(c['engines'][eng][name]['upper_exact'])<Q(target)
 for name,target in p['lower_claims'].items():assert Q(c['engines'][eng][name]['lower_exact'])>Q(target)
assert a['counts']['exact_endpoint_pairs']==60 and a['counts']['strict_ceiling_audit']==40 and a['counts']['strict_floor_audit']==8
assert a['counts']['fourier_constant_exact_square_audit']==8 and a['counts']['fresh_symbolic_identities']==11
assert c['counts']['exact_angular_recurrence_checks']==28 and c['counts']['exact_radial_identity_checks']==9
files={};seen=set();comparisons=0
for f,h in c['files'].items():assert sha(B/f)==h,f;files[f]=h
assert a['counts']['current_input_pins']==len(c['files'])
def dep(f,h):
 global comparisons
 assert sha(B/f)==h,f;comparisons+=1
 if f in seen:return
 seen.add(f)
 if f.endswith('/evidence/verdict.json'):
  v=load(B/f);assert v['status'].startswith('CONFIRMED')
  for name,digest in v['files'].items():dep(name,digest)
for f,h in p['dependencies'].items():dep(f,h)
assert comparisons==c['counts']['dependency_hash_comparisons']
proof_auth=load(E/'proof_review_audit.json')
for item in proof_auth['files']:assert sha(B/item['reviewed_snapshot'])==item['sha256']
for f,h in proof_auth['review_files'].items():assert sha(B/f)==h
reviews={}
for kind in ('proof','closure'):
 tag='sobolev_source_box_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'))
 req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'):assert phrase in req
 assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
 if kind=='closure':
  for f in ['ADDENDUM.md','PUBLICATION.md','CLOSURE_NOTES.md','code/finalize_verdict.py','code/engine_arb.py','code/engine_rational.py','code/check_constants.py','code/audit_output.py','evidence/checks.json','evidence/output_audit.json']:
   assert 'research/sobolev_source_box/'+f in m['files'],f
  verdict_tokens=re.findall(r'^\s*(?:#{1,6}\s*)?(?:\*\*)?Verdict:\s*(ACCEPT|REJECT)(?:\*\*)?\s*$',ans,flags=re.MULTILINE)
  assert verdict_tokens==['ACCEPT'], 'Require one explicit acceptance verdict; manual full-response review remains mandatory.'
 for f in m['files']:files[f]=sha(B/f)
 for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):
  f=R/(tag+suffix);files[str(f.relative_to(B))]=sha(f)
 reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
for f in D.rglob('*'):
 if f.is_file() and f.name!='verdict.json':files[str(f.relative_to(B))]=sha(f)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_SOBOLEV_SOURCE_BOX_K1_AND_NARROW_TRIAL_NONSTATIONARITY','counts':c['counts'],'output_audit_counts':a['counts'],'closure_recursive_dependency_hash_comparisons':comparisons,'exact_parameters':p['inputs'],'strict_upper_claims':p['upper_claims'],'strict_lower_claims':p['lower_claims'],'scope':'PROOF with mandatory ADDENDUM, CLOSURE_NOTES and PUBLICATION. At s=153/50, H<=7/50 yields source geometry and uniform local K1<0.32123200. H<=3.2318e-7 excludes stationarity near the moving source for the exact modal trial only. No X3 exclusion.','refuted':['Strict delta_h<0.0165 for every correction','Containment or noncontainment of a numerical uncertainty ball inferred from unlike norm magnitudes'],'open':['Uniform K2,K3,K4,R and moving norms','Physical global inverse and canonical matching','Weighted-space control and certified high-norm residual','Nonlinear closing inequality and every decisive endpoint'],'reviews':reviews,'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'manifest_pins':len(files),'sha256':sha(E/'verdict.json'),'dependency_hash_comparisons':comparisons},indent=2))
