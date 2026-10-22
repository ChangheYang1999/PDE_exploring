"""Freeze topic103 only after exact audit and authenticated whole-bundle review.
No JavaScript/TypeScript, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys,re
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/far_profile_distance';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
assert not (E/'verdict.json').exists()
p=load(D/'source/parameters.json');c=load(E/'checks.json');a=load(E/'audit.json');pf=load(E/'proof_first.json')
assert pf['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(c['utc'])
assert c['status']=='PASS_TWO_INDEPENDENT_NONZERO_TAIL_WITNESSES' and a['status']=='PASS_INDEPENDENT_SOURCE_AND_OUTPUT_AUDIT'
assert a['counts']['x3_coefficients']==75382 and a['counts']['x3_names']==75381 and a['counts']['modal_outer_coefficients']==2600
assert a['counts']['exact_endpoint_checks']==28 and a['counts']['strict_public_bounds']==20
assert c['public_strict_enclosures']==p['public_strict_enclosures']==a['public_strict_enclosures']
for eng in ('arb512','iv180'):
 for key,(lo,hi) in p['public_strict_enclosures'].items():
  box=c['outputs'][eng]['values'][key];assert Q(lo)<Q(box['lower_exact'])<=Q(box['upper_exact'])<Q(hi)
files={}
for manifest in [p['files'],p['modal_dependency_pins'],c['files'],a['files']]:
 for f,h in manifest.items():assert sha(B/f)==h,f;files[f]=h
for s in p['source_archives'].values():assert sha(Path(s['path']))==s['sha256']
reviews={}
for kind in ('proof','closure'):
 tag='far_profile_distance_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'):assert phrase in req
 assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
 if kind=='closure':
  needed=['PROOF.md','ADDENDUM.md','PUBLICATION.md','CLOSURE_NOTES.md','source/parameters.json','source/original_gen_shape.py','source/evaluator_provenance.json','evidence/checks.json','evidence/audit.json']+[str(f.relative_to(D)) for f in (D/'code').glob('*.py')]
  assert all('research/far_profile_distance/'+f in m['files'] for f in needed)
  verdicts=re.findall(r'^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?Verdict:[ \t]*(ACCEPT|REJECT)(?:\*\*)?[ \t]*$',ans,re.MULTILINE)
  assert verdicts==['ACCEPT'],'Require a single explicit verdict and subsequent independent adjudication.'
 for f in m['files']:files[f]=sha(B/f)
 for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):
  f=R/(tag+suffix);files[str(f.relative_to(B))]=sha(f)
 reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_REVIEW' and adj['response_sha256']==sha(R/'far_profile_distance_closure_response.json')
assert datetime.fromisoformat(adj['utc'])>=datetime.fromisoformat(reviews['far_profile_distance_closure']['end_utc'])
for f in D.rglob('*'):
 if f.is_file() and f.name!='verdict.json':files[str(f.relative_to(B))]=sha(f)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_LEADING_TAIL_SEPARATION_AND_SHARP_WEIGHTED_L2_THRESHOLD','counts':a['counts'],'public_strict_enclosures':p['public_strict_enclosures'],'scope':'Exact X3 versus exact normalized modal trial: weighted L2 difference iff gamma>1+k; nonmembership in unweighted Hs for every s>=0. PROOF, ADDENDUM and PUBLICATION. No finite-radius error, PDE exclusion or decisive endpoint.','refuted':['A finite unweighted Hs ball about this modal trial can contain X3, for s>=0'],'open':['Quantitative finite-radius distance','Weighted Sobolev distance and admissible uncertainty neighborhood','Global inverse and nonlinear closing inequality','Every decisive endpoint'],'reviews':reviews,'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
