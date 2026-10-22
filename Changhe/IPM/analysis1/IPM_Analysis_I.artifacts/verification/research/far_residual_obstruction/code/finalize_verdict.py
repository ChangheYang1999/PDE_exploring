"""Finalize the scoped L2 obstruction after current audits and actual whole-bundle Opus5.5.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,hashlib,sys,re
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/far_residual_obstruction';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
assert not (E/'verdict.json').exists()
a=load(E/'audit.json');p=load(E/'proof_first.json');A=load(E/'arb.json');I=load(E/'iv.json')
assert p['sha256']==sha(D/'PROOF.md')
assert a['status']=='PASS_INDEPENDENT_SOURCE_OUTPUT_AND_NONZERO_COEFFICIENT_AUDIT'
assert a['counts']=={'original_outer_coefficients':2600,'original_knots':1573,'exact_projection_entries':786,'primary_projection_witnesses':12,'exponent_comparisons':3001,'normalization_dependency_pins':14,'finite_ordered_endpoints':24,'strict_public_enclosures':6,'independent_intervals_contained':6,'prior_complete_convolution_coefficients':2,'angular_normalization_checks':3,'canonical_strain_sign_checks':3}
for out in (A,I):
 assert datetime.fromisoformat(p['utc'])<datetime.fromisoformat(out['utc'])
 for key,(lo,hi) in a['public_strict_enclosures'].items():
  b=out['values'][key];assert Q(lo)<Q(b['lower_exact'])<=Q(b['upper_exact'])<Q(hi)
files={}
for p,h in a['files'].items():assert sha(B/p)==h,p;files[p]=h
assert sha(Path(a['source_archive']['path']))==a['source_archive']['sha256']
reviews={}
# Keep and authenticate the superseded closure record; the current closure must
# cover the repaired files. Its former ACCEPT did not authorize finalization.
r1='far_residual_obstruction_closure_r1';m1=load(R/(r1+'_metadata.json'));raw1=load(R/(r1+'_response.json'));req1=(R/(r1+'_request.txt')).read_text()
assert m1['actual_response_model']==raw1['model']=='claude-opus-5-5' and m1['stop_reason']==raw1['stop_reason']=='end_turn'
assert hashlib.sha256(req1.encode()).hexdigest()==m1['input_sha256']
for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):
 f=R/(r1+suffix);files[str(f.relative_to(B))]=sha(f)
for kind in ('proof','closure'):
 tag='far_residual_obstruction_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'):assert phrase in req
 assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
 if kind=='closure':
  needed=['PROOF.md','ADDENDUM.md','PUBLICATION.md','CLOSURE_NOTES.md','evidence/arb.json','evidence/iv.json','evidence/audit.json','evidence/proof_first.json']+[str(f.relative_to(D)) for f in (D/'code').glob('*.py')]
  assert all('research/far_residual_obstruction/'+f in m['files'] for f in needed)
  verdicts=re.findall(r'^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?Verdict:[ \t]*(ACCEPT|REJECT)(?:\*\*)?[ \t]*$',ans,re.MULTILINE)
  assert verdicts==['ACCEPT'],'Require one explicit verdict plus independent adjudication.'
 for f in m['files']:files[f]=sha(B/f)
 for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):
  f=R/(tag+suffix);files[str(f.relative_to(B))]=sha(f)
 reviews[tag]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_REVIEW'
assert adj['response_sha256']==sha(R/'far_residual_obstruction_closure_response.json') and datetime.fromisoformat(adj['utc'])>=datetime.fromisoformat(reviews['far_residual_obstruction_closure']['end_utc'])
for f in D.rglob('*'):
 if f.is_file() and f.name!='verdict.json':files[str(f.relative_to(B))]=sha(f)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_NO_STATIONARY_CANONICAL_PROFILE_IN_MODAL_AFFINE_L2_CLASS','public_strict_enclosures':a['public_strict_enclosures'],'counts':a['counts'],'scope':'PROOF plus ADDENDUM: no actual locally regular canonical sublinear stationary rho0+h for h in L2 and any finite real c. Includes every unweighted Hs correction for s>=0. Residual weighted L2 iff gamma>2k. Does not exclude a weighted uncertainty neighborhood, and is not decisive NO.','refuted':['A stationary profile in the specified canonical class can differ from this exact normalized modal trial by an unweighted L2 function','The modal trial residual lies in unweighted L2'],'open':['Existence or exclusion in weighted neighborhoods allowing non-L2 tail corrections','Global inverse and nonlinear closing inequality','Every decisive endpoint'],'reviews':reviews,'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
