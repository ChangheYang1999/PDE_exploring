"""Exact rational exhaustive monotonicity audit, independent of tail numeric values."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/tail_audit/evidence'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def hx(s):return F.from_float(float.fromhex(s))
def run():
 start=time.monotonic();inp=BASE/'data_exact/modal_v2.json';assert sha(inp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(inp.read_bytes());sc={s:hx(v) for s,v in raw['scalars_hex'].items()};k,bi,bo=[sc[s] for s in ('k','bi','bo')]
 assert 0<k<F(1,2) and bi>50 and bo>120
 inner=[(F(0),0)]+[(F(2*j),0) for j in range(1,8)]+[(bi,6)]
 outer=[(k-3-j*(1-k)-2*l,0) for j,l in raw['outer_jl']]+[(-bo,6)]
 assert raw['outer_jl']==[[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[0,1],[1,1],[2,1],[0,2]]
 streams=[];near=[];min_nonzero_mu=None
 for n in range(1,262):
  m=F(2*n);streams.append(('upper_transient',n,m,0))
  for alpha,degree in inner:
   # The exact cubic is x^2 y, whose x derivative is r^2 sin2theta.
   if alpha==0 and n!=1:continue
   lam=m+4+alpha;mu=4-m+alpha;assert lam>0
   streams.append(('A_particular',n,4+alpha,degree))
   if mu:
    streams.append(('B_nonzero_particular',n,4+alpha,degree))
    min_nonzero_mu=abs(mu) if min_nonzero_mu is None else min(min_nonzero_mu,abs(mu))
   # These are exactly the near-zero possibilities throughout T in [2,3].
   if abs(mu)*3<F(1,2):
    near.append({'n':n,'alpha_exact':str(alpha),'mu_exact':str(mu),'original_degree':degree})
    streams.append(('B_near_primitive',n,m,degree+1))
    if mu:streams.append(('B_near_exp_remainder',n,m-abs(mu),degree+2))
   else:assert abs(mu)*2>=F(1,2)
 assert [r['n'] for r in near]==[3,4,5,6,7,8,9,27]
 T=F(2);inner_count=0;inner_min=None;inner_witness=None
 def check_inner(label,gamma,degree):
  nonlocal inner_count,inner_min,inner_witness
  margin=gamma-5-F(degree)/T;assert margin>=0,(label,str(gamma),degree,str(margin))
  inner_count+=1
  if inner_min is None or margin<inner_min:inner_min=margin;inner_witness={'term':label,'gamma_exact':str(gamma),'degree':degree,'margin_exact':str(margin)}
 for alpha,degree in inner:
  if alpha:check_inner('linear:'+str(alpha),3+alpha,degree)
 for label,n,exponent,degree in streams:
  for alpha,rd in inner:
   if label=='upper_transient' and n==1 and alpha==0:continue
   check_inner(label+':n='+str(n)+':density_alpha='+str(alpha),exponent+1+alpha,degree+rd)
 outer_results=[];denoms=[];upper_rates=[]
 for n in range(1,262):
  for alpha,degree in outer:
   lam=2*n+4+alpha;mu=4-2*n+alpha;assert lam!=0 and mu<0
   denoms.append((abs(lam),n,alpha));upper_rates.append(mu)
 for delta in (F(1,2),F(1,2)-k):
  T=F(9);coded=[F(-100)]+[3+alpha+delta-k for alpha,deg in outer[1:-1]]+[3-bo+6/T+delta-k,k-1+delta,5-bo+6/T+delta]
  worst=max(coded);assert worst==k-1+delta<0
  count=0;largest=None;witness=None
  def check_outer(label,gamma,degree):
   nonlocal count,largest,witness
   rate=gamma+F(degree)/T+delta-k;assert rate<=worst<0,(label,str(rate),str(worst))
   count+=1
   if largest is None or rate>largest:largest=rate;witness={'term':label,'gamma_exact':str(gamma),'degree':degree,'rate_exact':str(rate)}
  for alpha,degree in outer[1:]:check_outer('linear:'+str(alpha),3+alpha,degree)
  for alpha,degree in outer:
   for ar,rd in outer:check_outer('particular:'+str(alpha)+':density:'+str(ar),5+alpha+ar,degree+rd)
  for n in range(1,262):
   for alpha,degree in outer:check_outer('A_transient:n='+str(n)+':density:'+str(alpha),1-2*n+alpha,degree)
  domination=bo+k-6/T;assert domination>0
  outer_results.append({'delta_exact':str(delta),'T_lower_exact':str(T),'terms_checked':count,'coded_max_rate_exact':str(worst),'true_max_rate_exact':str(largest),'max_witness':witness,'coarse_line_excess_over_degree12_exact':str(domination)})
 minimum=min(denoms)
 result={'utc':utc(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':sha(BASE/'research/tail_audit/PROOF.md'),'input_sha256':sha(inp),'k_exact':str(k),'bi_exact':str(bi),'bo_exact':str(bo),'inner':{'T_lower_exact':'2','stream_monomials_checked':len(streams),'residual_monomials_checked':inner_count,'min_r5_log_derivative_exact':str(inner_min),'min_witness':inner_witness,'near_zero_cases':near,'minimum_nonzero_upper_mu_exact':str(min_nonzero_mu),'cubic_transient_product_removed_by_exact_identity':True},'outer':outer_results,'outer_denominators':{'number':len(denoms),'minimum_absolute_lower_rate_exact':str(minimum[0]),'witness_n':minimum[1],'witness_alpha_exact':str(minimum[2]),'largest_upper_rate_exact':str(max(upper_rates))},'seconds':time.monotonic()-start,'scope':'Only exact exponent coverage and monotonicity for these parameters. No acceptance of tail coefficient imports, boundary moments, numerical tail bounds, derivative norms, or a global endpoint.'}
 path=E/'exponent_audit.json';path.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':run()
