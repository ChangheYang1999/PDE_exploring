"""Freeze scoped forcing-norm theorem only after current whole-bundle review.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import sys,json,hashlib,re
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_forcing_norms';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def main():
 assert not (E/'verdict.json').exists();audit=load(E/'audit.json');pf=load(E/'proof_first.json');assert pf['sha256']==sha(D/'PROOF.md')
 assert audit['status']=='PASS_TWO_METHOD_CONSTANTS_EXACT_KERNEL_REPLAY_AND_DEPENDENCIES'
 assert audit['counts']=={'distinct_dependency_pins':179,'exact_exponent_relations':7,'exact_simpson_kernel_identities':5,'simpson_enclosure_directions':4,'strict_public_enclosures':10,'nonzero_lower_constants':4,'overlap_diagnostics_only':6,'complete_engine_replays':2}
 files={}
 for p,h in audit['files'].items():assert sha(B/p)==h,p;files[p]=h
 assert sha(Path(audit['source_archive']['path']))==audit['source_archive']['sha256']
 text=(D/'PUBLICATION.md').read_text()
 for key,(lo,hi) in audit['public_strict_enclosures'].items():
  assert f'| {key} | {lo} | {hi} |' in text
  for engine in ('arb','iv'):
   rec=load(E/(engine+'.json'))['values'][key];assert Q(lo)<Q(rec['lower_exact'])<=Q(rec['upper_exact'])<Q(hi)
 reviews={}
 for kind in ('proof_followup','closure'):
  tag='tail_forcing_norms_'+kind;m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();ans=(R/(tag+'_response.md')).read_text()
  assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
  assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
  assert ans=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
  assert req.endswith('\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']))
  for s in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'):assert s in req
  if kind=='closure':
   need=[D/n for n in ('PROOF.md','ADDENDUM.md','PUBLICATION.md','CLOSURE_NOTES.md','evidence/proof_first.json','evidence/arb.json','evidence/iv.json','evidence/audit.json')]+list((D/'code').glob('*.py'))
   assert all(str(p.relative_to(B)) in m['files'] for p in need)
   assert re.findall(r'^[ \t]*(?:#{1,6}[ \t]*)?(?:\*\*)?Verdict:[ \t]*(ACCEPT|REJECT)(?:\*\*)?[ \t]*$',ans,re.MULTILINE)==['ACCEPT']
  for f in m['files']:files[f]=sha(B/f)
  for suffix in ('_metadata.json','_response.md','_response.json','_request.txt'):
   p=R/(tag+suffix);files[str(p.relative_to(B))]=sha(p)
  reviews[kind]={k:m[k] for k in ('start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256')}
 adj=load(E/'review_adjudication.json');assert adj['status']=='ACCEPT_AFTER_INDEPENDENT_REVIEW' and adj['response_sha256']==sha(R/'tail_forcing_norms_closure_response.json')
 assert datetime.fromisoformat(adj['utc'])>=datetime.fromisoformat(reviews['closure']['end_utc'])
 abort=load(R/'tail_forcing_norms_proof_metadata.json');assert abort['stop_reason']=='max_tokens'
 for suffix in ('_metadata.json','_response.md','_response.json','_request.txt'):
  p=R/('tail_forcing_norms_proof'+suffix);files[str(p.relative_to(B))]=sha(p)
 for p in D.rglob('*'):
  if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_NEGATIVE_NORM_OBSTRUCTION_ASYMPTOTIC_REPAIR_NORM_GROWTH_AND_WEIGHTED_THRESHOLDS','scope':'PROOF plus mandatory ADDENDUM. Exact modal residual outside L2,H^-1,dotH^-1; both repairs have positive T^(2k) lower growth in L2,H^-1, and topic106 has positive T^(2k+1) lower growth in dotH^-1. Sharp weighted distance thresholds. No finite T threshold, norm upper bound, global inverse or decisive endpoint.','public_strict_enclosures':audit['public_strict_enclosures'],'counts':audit['counts'],'reviews':reviews,'refuted':['Treating max_tokens without a final answer as model acceptance','Inferring a small forcing norm from weighted factor convergence','Using a T exponent as a proof of canonical spatial growth'],'open':['Finite T threshold and upper forcing bounds','Single-tail dotH^-1 membership and necessity of higher counterterms in this theorem','Full inverse, nonlinear closure and every decisive endpoint'],'files':dict(sorted(files.items()))}
 (E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
if __name__=='__main__':main()
