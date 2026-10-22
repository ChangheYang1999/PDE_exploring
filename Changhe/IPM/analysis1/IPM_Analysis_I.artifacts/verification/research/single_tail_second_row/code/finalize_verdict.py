"""Authenticate completed independent audit and actual-model follow-up.
No JS/TS, no servers, no RLScience, no Lean/Lake. Lane-local writes only.
"""
import json,hashlib,sys,re
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_second_row';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
 assert not (E/'verdict.json').exists()
 a=load(E/'audit.json');assert a['status']=='PASS_INDEPENDENT_FINITE_AUDIT_REVIEW_STILL_OPEN'
 assert load(E/'proof_first.json')['proof_sha256']==sha(D/'PROOF.md')
 assert a['counts']=={'original_outer_coefficients':2600,'original_knots':1573,'third_projected_sines':786,'bilinear_basis_identities':2088,'support_pairs':272484,'ordered_exponent_pairs':121,'homogeneous_comparisons':5742,'strict_public_enclosures':4,'overlap_diagnostics':6,'complete_engine_reruns':2}
 files={}
 for f,h in a['files'].items():assert sha(B/f)==h,f;files[f]=h
 for eng in ('arb','iv'):
  x=load(E/(eng+'.json'))
  if 'source_archive' in x:
   r=x['source_archive'];assert sha(Path(r['path']))==r['sha256']
  for k,(lo,hi) in a['strict_public_bounds'].items():
   r=x['values'][k];assert Q(lo)<Q(r['lower_exact'])<=Q(r['upper_exact'])<Q(hi)
   assert f'| {k} | {lo} | {hi} |' in (D/'PUBLICATION.md').read_text()
 reviews={}
 for kind in ('followup2','adjudication'):
  tag='single_tail_second_row_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
  assert m['requested_model']=='us.anthropic.claude-opus-5-5'
  assert m['actual_response_model']==raw['model']=='claude-opus-5-5'
  assert m['stop_reason']==raw['stop_reason']=='end_turn'
  assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
  assert ans=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
  assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
  for s in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'):assert s in req
  assert re.search(r'Verdict:\s*(?:\*\*)?ACCEPT',ans),ans
  if kind=='followup2':
   need=['PROOF.md','ADDENDUM.md','PUBLICATION.md','source/public_bounds.json','evidence/arb.json','evidence/iv.json','evidence/audit.json','code/engine_arb.py','code/engine_iv.py','code/audit_outputs.py']
   assert len(m['files'])==10 and all(str((D/f).relative_to(B)) in m['files'] for f in need)
  for f in m['files']:files[f]=sha(B/f)
  reviews[kind]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
 assert load(R/'single_tail_second_row_closure_metadata.json')['stop_reason']=='max_tokens'
 fail=load(R/'single_tail_second_row_followup_metadata.json');assert 'ValidationException' in fail['availability_error'] and 'actual_response_model' not in fail
 adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_ADJUDICATION'
 assert adj['raw_final_response_sha256']==sha(R/'single_tail_second_row_adjudication_response.json')
 for p in R.glob('single_tail_second_row_*'):
  if p.is_file():files[str(p.relative_to(B))]=sha(p)
 for p in D.rglob('*'):
  if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_NONZERO_SECOND_EXTERIOR_ROW_AND_NECESSARY_FINITE_CLASS_COUNTERTERM','scope':'PROOF with mandatory ADDENDUM and CLOSURE_NOTES. For every fixed admissible T the topic105 residual has the nonzero physical first-sine coefficient C20 at r^(3k-2), so it fails dot H^-1 and r*epsilon fails L2. H2 is necessary in the stated finite exterior class. No arbitrary-tail exclusion, finite radius bound, inverse, existence or decisive endpoint.','strict_public_bounds':a['strict_public_bounds'],'counts':a['counts'],'reviews':reviews,'refuted':['Review introductory Delta inverse sign','Review bound |k+1|<1','Identifying formatted ball radii with native interval widths','Discarding exact normalization without a bound'],'open':['Full residual norm ceilings, inverse and nonlinear closure','Meaningful X3 uncertainty neighborhood or decisive endpoint'],'files':dict(sorted(files.items()))}
 (E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
if __name__=='__main__':main()
