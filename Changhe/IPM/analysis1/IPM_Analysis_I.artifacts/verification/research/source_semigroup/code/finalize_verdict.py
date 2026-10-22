"""Bind the auxiliary maximal-domain inverse theorem and all current dependencies."""
from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_semigroup';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());r=json.loads((E/'local_run.json').read_text());first=json.loads((E/'proof_first.json').read_text())
assert c['status']=='PASS_AUXILIARY_INVERSE_FORMULAS' and a['status']=='PASS_EXACT_INTEGER_ROOT_INVERSE_AUDIT'
assert c['counts']=={'symbolic_identities':10,'illustrative_rows':96,'exact_illustrative_inequalities':288,'primary_engine_scalar_enclosures':386}
assert a['counts']=={'exact_rational_row_checks':288,'exact_integer_root_enclosures':96,'full_enclosure_contains':193}
assert r['resumed_worker'] and len(r['commands'])==2 and all(v['returncode']==0 for v in r['commands'])
assert first['code_files']==[] and first['proof_sha256']==sha(D/'PROOF.md')
files={}
for obj in [c,a]:
 for p,h in obj['files'].items():assert sha(B/p)==h,p;files[p]=h
for p,h in first['dependencies'].items():assert sha(B/p)==h,p
p=B/'research/source_local_estimate/evidence/verdict.json';dep=json.loads(p.read_text());assert dep['status']=='CONFIRMED_CONDITIONAL_LOCAL_SOURCE_ESTIMATE';files[str(p.relative_to(B))]=sha(p)
for p,h in dep['files'].items():assert sha(B/p)==h,p;files[p]=h
reviews={};root=B/'notes/reviews'
for tag in ['source_semigroup_core','source_semigroup_decay','source_semigroup_closure']:
 m=json.loads((root/(tag+'_metadata.json')).read_text());req=(root/(tag+'_request.txt')).read_text();raw=json.loads((root/(tag+'_response.json')).read_text());ans=(root/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='source_semigroup_closure':assert ans.startswith('**ACCEPT_AUXILIARY_INVERSE_SCOPE**')
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:
  p=root/(tag+'_'+suf);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_AUXILIARY_MAXIMAL_DOMAIN_INVERSE','confirmed':['For global real C_c4 w,q, the cut-off source operator on H^3.1 with maximal distributional transport domain is a C0 semigroup generator.','L2 transport graph core proved by cutoffs and mollifiers; J^s conjugation is a bounded L2 perturbation, with explicit commutator constants.','J^-s C_cinfinity is a Schwartz graph core; energy estimates extend to the full generator domain.','Under the source box and E<1687/500, semigroup norm is <=(1+R/d)^3.1 exp(-(1687/500-E)t), with d>=3121/1000.','Its both-sided inverse is minus the forward semigroup integral, with norm at most(1+R/d)^3.1/(1687/500-E).','Raw strain is bounded by beta_s on Hs. Adding ell_delta*sigma is invertible iff1+sigma[Aop^-1 ell_delta] is nonzero, with explicit inverse/norm and a null vector when it vanishes.'],'arithmetic':c['counts']|{'fresh_integer_root_enclosures':96,'fresh_rational_checks':288,'fresh_full_enclosure_contains':193},'arithmetic_scope':'All96parameterrowsareabstractrationalillustrations, not actual coefficient data. Exact integer tenth-root method is independent of the primary Arb512/iv180 powers.','dependency_verdict_sha256':sha(B/'research/source_local_estimate/evidence/verdict.json'),'dependency_files_rechecked':len(dep['files']),'reviews':reviews,'review_resolution':'The core-only review called sections4-5 missing because it received only sections1-3. The whole-proof closure verifies both derivations are present and logically closes the union.','open':['Actual coefficient enclosures E<kappa and a useful numeric R/inverse bound','Nonzero rank-one denominator for the actual trial','Prescribed outer data and assembling the full IPM inverse','Centre/far-field realization, high-norm residual, nonlinear contraction and every decisive endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
