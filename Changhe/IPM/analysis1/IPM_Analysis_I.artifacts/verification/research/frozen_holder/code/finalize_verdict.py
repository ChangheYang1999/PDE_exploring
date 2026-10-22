"""Bind the frozen analytic result to its unchanged proof and evidence."""
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/frozen_holder/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
c=json.loads((E/'checks.json').read_text());a=json.loads((E/'output_audit.json').read_text());run=json.loads((E/'local_run.json').read_text());summary=json.loads((E/'closure_summary.json').read_text())
assert c['status']==a['status']=='PASS'
assert c['proof_sha256']==a['proof_sha256']==summary['proof_sha256']==sha(B/'research/frozen_holder/PROOF.md')
assert summary['addendum_sha256']==sha(B/'research/frozen_holder/ADDENDUM.md')
assert c['code_sha256']==sha(B/'research/frozen_holder/code/check_exponents.py') and a['code_sha256']==sha(B/'research/frozen_holder/code/audit_output.py')
assert c['inputs_sha256']==a['inputs_sha256']==sha(E/'inputs.json')
assert a['input_sha256']==summary['checks_file_sha256']==sha(E/'checks.json')
assert c['symbolic_identity_count']==len(c['symbolic_identities'])==20
assert len(c['parameter_sets'])==2 and sum(len(p['exact']) for p in c['parameter_sets'])==40
assert c['finite_integral_inequalities']==2240 and a['fresh_integral_inequalities']==1120 and a['scalar_exact_checks']==40 and a['containments']==172
assert a['selected_integral_examples']==c['selected_integral_examples']==46
assert run['resumed_worker'] and len(run['commands'])==2 and all(x['returncode']==0 for x in run['commands'])
proof=(B/'research/frozen_holder/PROOF.md').read_text();prefix=proof.split('## 2.')[0]
expected={'upper':proof.split('## 4.')[0],'packet':prefix+'\n## 4.'+proof.split('## 4.',1)[1].split('## 5.',1)[0],'logs':prefix+'\n## 5.'+proof.split('## 5.',1)[1].split('## 6.',1)[0],'ceiling':prefix+'\n## 6.'+proof.split('## 6.',1)[1].split('## 7.',1)[0]}
for name,text in expected.items():assert(E/f'review_{name}_excerpt.md').read_text()==text,name
reviews={};files={}
for tag in ['frozen_holder_upper','frozen_holder_packet','frozen_holder_logs','frozen_holder_ceiling','frozen_holder_closure']:
 meta=json.loads((B/f'notes/reviews/{tag}_metadata.json').read_text());request=(B/f'notes/reviews/{tag}_request.txt').read_text();answer=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert meta['actual_response_model']=='claude-opus-5-5' and meta['stop_reason']=='end_turn' and len(answer)>200
 assert hashlib.sha256(request.encode()).hexdigest()==meta['input_sha256']
 marker='\n\nFILE '+meta['files'][0]+'\n';assert request.count(marker)==1
 rebuilt=request.split(marker,1)[0]+'\n\n'+'\n\n'.join('FILE '+p+'\n'+(B/p).read_text() for p in meta['files']);assert request==rebuilt,tag
 if tag=='frozen_holder_closure':assert answer.startswith('# FINAL ANSWER: ACCEPT_STATED_FROZEN_SCOPE')
 reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'start_utc':meta['start_utc'],'end_utc':meta['end_utc']}
 for suffix in ['metadata.json','request.txt','response.json','response.md']:
  p=B/f'notes/reviews/{tag}_{suffix}';files[str(p.relative_to(B))]=sha(p)
for tag in ['frozen_holder_proof','frozen_holder_proof_retry','frozen_holder_mathreview']:
 for p in (B/'notes/reviews').glob(tag+'_*'):
  if p.is_file():files[str(p.relative_to(B))]=sha(p)
for p in [B/'research/frozen_holder/PROOF.md',B/'research/frozen_holder/ADDENDUM.md',*sorted((B/'research/frozen_holder/code').glob('*.py')),*sorted(E.iterdir()),*sorted((B/'research/frozen_holder/sources').iterdir())]:
 if p.is_file() and p.name!='verdict.json':files[str(p.relative_to(B))]=sha(p)
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_STATED_FROZEN_SCOPE','scope':'A>1,1<g/(A-1)<A+1; L=As partial_s+y partial_y-1-gM on D(T) in L2; selected inverse R=-integral_0^infinity S_t; fixed compact forcing support.','confirmed':['L2 inverse norm at most2/(A+3).','Sharp compact-input Cstar^sigma to Cstar^(sigma-(sigma-1)/A) bound for1<sigma<a, including the output endpoint.','For1<sigma<q, bounded input packets have same-order local norm growth comparable to N^((sigma-1)/(A-1)).','Same-order upper bound for0<sigma<1; necessary single logarithm at input1, with separate classical C1 and Cstar1 sequences.','For sigma>a the output lies in Cstar^q; one fixed smooth parity-compatible forcing is outside every local Cstar^beta with beta>q.','At sigma=a only the logarithmic q upper bound is proved.'],'arithmetic':{'symbolic_identities':20,'illustrative_exact_scalars':40,'primary_Arb512_iv180_integral_inequalities':2240,'fresh_Arb1536_integral_inequalities':1120,'fresh_containments':172},'illustrations':'Two explicit rational parameter sets, kept distinct; no inference of exact-profile derivatives. Saved constants are genuine enclosures of these illustrations, despite an imprecise contrary phrase in the final text review.','reviews':reviews,'failures_preserved':['Initial actual5.5 refusal returned no final text.','Disabled-thinking retry rejected as unsupported.','Medium-effort retry exhausted22000tokens with no final text.','Four focused actual5.5 reviews and a subsequent consistency closure supplied substantive end_turn answers.'],'resolved_review_points':['Explicit Fourier transport core density proof.','Section5 dependencies supplied across complete proof and local test bound.','Uniform positive packet contributions quantified.','Only the y derivative integral is needed; a reviewer fullC1 convergence overstatement is rejected.','Tests and negative-time majorants stated precisely.'],'open':['Sharpness of the sigma=a logarithm','Variable-coefficient Weyl sequence and graph-density transfer','Any full IPM inverse, source matching and global Banach realization','Quantitative forcing norms, nonlinear closing inequality and profile existence/exclusion'],'files':dict(sorted(files.items()))}
(E/'verdict.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({'utc':obj['utc'],'status':obj['status'],'pins':len(files),'sha256':sha(E/'verdict.json')}))
