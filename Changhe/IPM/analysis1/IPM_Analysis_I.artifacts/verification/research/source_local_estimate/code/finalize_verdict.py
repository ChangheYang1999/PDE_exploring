"""Current whole-bundle closure of the conditional local source estimate."""
from pathlib import Path
import sys,json,hashlib
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_local_estimate';E=D/'evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());ad=json.loads((E/'addendum_checks.json').read_text())
assert c['status']=='PASS_LOCAL_ESTIMATE_CONSTANTS' and a['status']=='PASS_FRESH_LOCAL_CONSTANT_AUDIT' and ad['status']=='PASS_EXACT_ADDENDUM'
for d in [c,a,ad]:
 for p,h in d['files'].items():assert sha(B/p)==h,p
assert len(c['symbolic_identities'])==29 and len(c['scalar_enclosures'])==54 and len(c['cases'])==62
assert c['counts']=={'exact_box_inequalities':16,'arb512_exact_scalar_contains':15,'arb512_finite_pointwise_inequalities':186,'iv180_exact_scalar_contains':15,'iv180_finite_pointwise_inequalities':186}
assert a['counts']=={'current_producer_file_pins':7,'exact_affine_endpoint_bounds':16,'exact_box_records':8,'fresh_exact_constants':15,'fresh_full_ball_containment':240,'fresh_finite_pointwise_inequalities':186}
assert ad['circular_PV_local_strain_coefficient']=='1/4'
assert sha(D/'PROOF.md')==json.loads((E/'proof_first.json').read_text())['proof_sha256']
assert json.loads((E/'proof_first.json').read_text())['code_files']==[]
for name in ['primary_run.json','audit_run.json','addendum_run.json']:
 r=json.loads((E/name).read_text());assert r['returncode']==0 and r['resumed_worker']
files={};reviews={};root=B/'notes/reviews'
for tag in ['source_local_energy','source_local_kernels','source_local_localization','source_local_followup','source_local_closure']:
 m=json.loads((root/(tag+'_metadata.json')).read_text());req=(root/(tag+'_request.txt')).read_text();raw=json.loads((root/(tag+'_response.json')).read_text());ans=(root/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn' and len(ans)>200
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 assert ans=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 marker='\n\nFILE '+m['files'][0]+'\n';assert req.count(marker)==1
 assert req==req.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 if tag=='source_local_closure':assert ans.startswith('# FINAL ANSWER: ACCEPT_STATED_LOCAL_SCOPE')
 reviews[tag]={k:m[k] for k in ['start_utc','end_utc','actual_response_model','stop_reason','request_id','input_sha256']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:
  p=root/(tag+'_'+suf);files[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
for suf in ['metadata.json','request.txt','response.json','response.md']:
 p=root/('source_local_initial_'+suf)
 if p.exists():files[str(p.relative_to(B))]=sha(p)
files['PROMPT.md']=sha(B/'PROMPT.md');files['notes/reviews/focused_review.py']=sha(B/'notes/reviews/focused_review.py')
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_LOCAL_SOURCE_ESTIMATE','confirmed':['Inhomogeneous H^3.1 frozen box margin1687/500; fast box threshold2373/680.','Explicit first-order transport commutator and lower-order remainder for compact C4 coefficients; E<=C_V delta with C_V=41.7M_V+3M_rho for C_theta=2.','Local estimate26 with exact K1=1/(kappa-E) and fully defined K2,K3,K4, supported restriction infima, separated velocity/strain kernels and moment norm N.','Uniform-shape cutoff rates K2=O(delta^-3.2),K3=O(delta^-6.3),K4=O(delta^-5.1), provided E<=kappa/2.','Circular principal-value canonical raw strain has local term h_y(0)/4; for stipulated zero jets all earlier kernel bounds are unchanged.','Graph completion is precisely the forcing plus annular/local Sobolev and remote moment norms in ADDENDUM.','Conditional auxiliary semigroup comparison and rank-one algebra; no generation assertion in this topic.'],'arithmetic':{'primary_symbolic_identities':29,'primary_exact_box_inequalities':16,'primary_scalar_enclosures':54,'sample_pairs':62,'primary_Arb512_iv180_sample_inequalities':372,'fresh_Arb1536_full_ball_contains':240,'fresh_exact_constants':15,'fresh_exact_box_inequalities':16,'fresh_sample_inequalities':186,'addendum_symbolic_angular_integrals':4,'addendum_kernel_identities':1,'addendum_exact_moment_checks':3,'addendum_exact_scaling_checks':6},'review_resolutions':['Initial M_s-based scaling objection retracted after the actual B_s definition was supplied.','Our proposed raw-strain local coefficient1/2 was refuted; boundary calculation proves1/4.','Final closure accepts PROOF read with ADDENDUM; original bookkeeping wording is superseded without modifying the proof hash.','Initial whole-source review exhausted its budget without a final answer and is not acceptance.','Unsuccessful bibliographic lookup metadata was explicitly retracted and is unused.'],'reviews':reviews,'open':['Certified actual coefficient derivative bounds implying E<kappa','The auxiliary generator/domain construction, separately pursued after this topic','A certified high-Sobolev residual norm and usable numeric K2-K4','Outer estimates, centre/far-field spaces, global inverse and nonlinear closure','Every decisive IPM endpoint'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
