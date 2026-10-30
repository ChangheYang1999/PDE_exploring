"""Bind and accept the analytic Opus reference-compatibility review."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
from hashlib import sha256
import json, time
R=Path(__file__).resolve().parents[3];B=R/'research/reference_difference_opus_acceptance';P=R.parent/'c1-t1';sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def main():
 start=time.monotonic();target=B/'verification/result.json';assert not target.exists();prep=json.loads((B/'verification/PREPARE.json').read_text());bindings={}
 refs=[('nonlinear_closure/REVIEWS_v39.md','b99568b859e635ab9e6f66c11bc37cc309c1a0f6aa0d38b6a15e75d58dcc0db0'),('artifacts/checks/check_N4refdiff.py','d790aa42bae7e94394717ea56473410a9f42e5c6c6faf3c5e8e5205d03b1bd09'),('artifacts/checks/check_N4refdiff.out','1de3740f40bb6c7fa2bb9bde2a3566d344196c1f8177fb1638ff89f34b117008')]
 for rel,h in refs:
  p=P/rel;assert sha(p)==h;q=B/'source'/p.name
  if q.exists():assert sha(q)==h
  else:
   with q.open('xb') as f:f.write(p.read_bytes())
  bindings[str(q.relative_to(R))]=h
 own=[Path(__file__),B/'PROOF.md',B/'verification/PREPARE.json',R/'research/reference_difference/PROOF.md',R/'research/reference_difference/PROOF_POSTPROCESS.md',R/'research/reference_difference/verification/fixtures.json']
 fixture=json.loads(own[-1].read_text())
 for rel,h in fixture['inputs'].items():p=R/rel;assert sha(p)==h;own.append(p)
 c=Q(4076476460239181,2251799813685248);d=1-1/c;checks={
 'proof_binding':sha(B/'PROOF.md')==prep['proof_sha256'] and sha(R/'research/reference_difference/PROOF.md')==prep['original_proof_sha256'],
 'exact_delta':d==Q(1824676646553933,4076476460239181) and Q(2,5)<d<Q(1,2),
 'universal_tail_maximum':4-5*d>2-d and 1-5*d<-1 and -1-d<-1,
 'retained_density_sectors_nonintegrable':all(1-ell*d>-1 for ell in range(1,5)),
 'differentiated_square_integrable':2*(1-5*d)+1<-1,
 'calibrated_fixture_graph':fixture['check_count']==10 and all(fixture['checks'].values()),
 }
 recursion=0
 for b in [d-1,3*d-2,5*d-3,Q(2)]:
  for a in [99,624,2499,9999]:
   for k in range(2,10):
    assert b>-1 and a>0
    lhs=[b+1,(b+1)*a-(k-1)*a];rhs=[b-k+2+k-1,(b-k+2)*a];assert lhs==rhs;recursion+=1
 checks['recursion_all_linear_coefficients']=recursion==128
 output=(B/'source/check_N4refdiff.out').read_text();exact=[s for s in output.splitlines() if s.startswith('PASS A')];floatrows=[s for s in output.splitlines() if s.startswith('PASS B')]
 checks['review_record_labels']=len(exact)==8 and len(floatrows)==3 and '11 checks, ALL PASS' in output
 review=(B/'source/REVIEWS_v39.md').read_text();checks['review_preserves_scope']=all(s in review for s in ['CONFIRMED as stated','The review does not','A parent distance bound transfers','only if it was proved in C','A failure of (P) proves nothing','Part B is FLOAT'])
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 out={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'exact_recursion_cases':recursion,'independent_review_exact_checks':8,'peer_FLOAT_diagnostics_not_proof':3,'frozen_peer_sources':bindings,'own_inputs':{str(p.relative_to(R)):sha(p) for p in own},'peer_model_configuration':'us.anthropic.claude-opus-5-5','actual_provider_identity_observed':False,'foreign_code_executed':False,'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED R1-041 analytic review of general(P), canonical velocity, compatible weak stationary equation and Euler integral; actual-pair numbers require separate acceptance'}
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(target),'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
