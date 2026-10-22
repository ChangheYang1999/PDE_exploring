"""Freeze only the scoped qualitative theorem after actual whole-bundle review.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_repair';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
assert not (E/'verdict.json').exists();a=load(E/'audit.json');o=load(E/'inputs.json');pf=load(E/'proof_first.json')
assert a['status']=='PASS_EXACT_OUTPUT_REPLAY_EXPONENTS_RESONANCES_AND_BETA_MOMENTS'
assert o['status']=='PASS_TWO_EXACT_INPUT_EXPONENT_AND_ANGULAR_IDENTITY_AUDITS'
assert a['counts']=={'original_Aout_entries':2600,'original_knots_entries':1573,'strict_public_endpoints':10,'distinct_pairs_per_input_method':55,'independent_nonresonance_checks':4437,'surviving_product_rows':100,'exact_beta_moments':2,'exact_transition_coefficients':17,'complete_input_replays':2}
assert pf['sha256']==sha(D/'PROOF.md') and datetime.fromisoformat(pf['utc'])<datetime.fromisoformat(o['utc'])
assert load(D/'source/plan.json')['new_finite_norm_constants_evaluated'] is False
files={}
for data in (a,o):
 for f,h in data['files'].items():assert sha(B/f)==h,f;files[f]=h
assert sha(Path(a['source_archive']['path']))==a['source_archive']['sha256']
publication=(D/'PUBLICATION.md').read_text()
for key,(lo,hi) in o['strict_public_exponent_intervals'].items():
 for method in o['outputs'].values():assert F(lo)<F(method['exact'][key])<F(hi)
 assert f'| {key} | {lo} | {hi} |' in publication
reviews={}
for kind in ('proof','closure'):
 tag='hminus1_tail_repair_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5'
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 for text in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'):assert text in req
 assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
 if kind=='closure':
  need=[D/n for n in ('PROOF.md','ADDENDUM.md','PUBLICATION.md','CLOSURE_NOTES.md','evidence/proof_first.json','evidence/inputs.json','evidence/audit.json')]+list((D/'code').glob('*.py'))+list((D/'source').glob('*.json'))
  assert all(str(p.relative_to(B)) in m['files'] for p in need)
  verdicts=re.findall(r'^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?Verdict:[ \t]*(ACCEPT|REJECT)(?:\*\*)?[ \t]*$',ans,re.MULTILINE)
  assert verdicts==['ACCEPT']
 for f in m['files']:files[f]=sha(B/f)
 for suffix in ('_metadata.json','_response.md','_response.json','_request.txt'):
  p=R/(tag+suffix);files[str(p.relative_to(B))]=sha(p)
 reviews[kind]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_REVIEW'
assert adj['response_sha256']==sha(R/'hminus1_tail_repair_closure_response.json')
assert datetime.fromisoformat(adj['utc'])>=datetime.fromisoformat(reviews['closure']['end_utc'])
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_NORMALIZED_TAIL_REPAIR_WITH_HMINUS1_RESIDUAL','scope':'PROOF plus mandatory ADDENDUM. Explicit finite angular cutoff counterterms and exact compact strain compensation preserve the kinematic P2 conditions and c_l=1/k; the residual satisfies ||epsilonT||dotH^-1<=||r epsilonT||2<infinity. Weighted factor distance tends to zero. Unevaluated C2,Cd and residual size; unchanged leading modal tail; no stationarity, inverse, nonlinear closure or decisive endpoint.','strict_public_exponent_intervals':o['strict_public_exponent_intervals'],'counts':a['counts'],'reviews':reviews,'refuted':['Necessity of cancelling the actual a2,d rows without proving their coefficients nonzero','Every ordered pair involving d has the same exponent 2k-3','C7 correction automatically upgrades an old C6 join'],'open':['Numerical C2,Cd and full residual norm ceiling','Smallness and source control as T varies','Growing scaling-source codomain','X3 leading-tail inclusion','Full inverse, nonlinear closure and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
