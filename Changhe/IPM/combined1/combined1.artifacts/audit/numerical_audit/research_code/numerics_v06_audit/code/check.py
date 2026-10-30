from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,time,sys
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'research/numerics_v06_audit'
H=lambda p:sha256(Path(p).read_bytes()).hexdigest()
def binomial(x,n):
 v=Q(1)
 for k in range(n):v*=Q(x-k,k+1)
 return v
def run():
 start=time.monotonic()
 src=ROOT/'research/candidate_audits/data/C1-N1-007-d2w-j7-e2bal/canonical.json'
 assert H(src)=='153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316'
 state=json.loads(src.read_text());c=Q(state['cl']);gamma=1/c;delta=1-gamma;p=(3+gamma)/2
 assert 1<c<2
 rows=[]
 for q in range(7):
  d=2*p-2*q
  density=Q(0)
  for (j,m,k),coef in zip(state['order'],state['coefficients'],strict=True):
   if j or m>1:continue
   A=Q(coef)*binomial(p-k,q);n=2*m
   for freq,val in [(n+1,-A*(d*d-n*n)*(d-2-n)/2),(n-1,A*(d*d-n*n)*(d-2+n)/2)]:
    if abs(freq)==1:density+=val*(1 if freq>0 else -1)
  residual=-2*c*q*density
  rows.append({'q':q,'density_exponent':str(gamma-2*q),'rho_sine1_exact':str(density),
               'linear_residual_sine1_exact':str(residual),'residual_nonzero':bool(residual),
               'residual_float_diagnostic':float(residual)})
 assert rows[4]['residual_nonzero'] and Q(rows[4]['density_exponent']) < -7
 assert all(((ell-1)*delta/2).denominator!=1 for ell in range(2,17))
 rankpath=ROOT/'research/quotient_coordinates/verification/007_legendre/result.json'
 rank=json.loads(rankpath.read_text())
 assert rank['reduced_dimension']==1922 and rank['zero_potential_dimension']==1060
 assert rank['all_kernel_relations_exact'] and rank['all_potential_coefficients_preserved']
 out={'utc':datetime.now(timezone.utc).isoformat(),'candidate':'C1-N1-007-d2w-j7-e2bal',
      'canonical_sha256':H(src),'publication_sha256':H(BASE/'source/numerics_v06.md'),
      'code_sha256':H(__file__),'proof_sha256':H(BASE/'PROOF.md'),
      'rank_evidence_sha256':H(rankpath),'rows':rows,'no_other_branch_resonance':True,
      'damped_physical_steps':['1/2','2/3'],'coefficient_tangent':2556,'physical_tangent':1496,'exact_kernel':1060,
      'elapsed_seconds':time.monotonic()-start}
 with (BASE/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print(json.dumps({k:out[k] for k in ['utc','canonical_sha256','elapsed_seconds']},indent=2))
 print('q4',rows[4]['density_exponent'],rows[4]['residual_float_diagnostic'],'nonzero exact',rows[4]['residual_nonzero'])
if __name__=='__main__':run()
