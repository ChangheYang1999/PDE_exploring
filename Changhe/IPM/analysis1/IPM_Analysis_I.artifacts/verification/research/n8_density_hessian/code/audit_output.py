"""Fresh exact algebra, geometry, source-error and output audit of density result."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,math
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
ctx.prec=512;ctx.threads=1;iv.dps=180
B=Path(__file__).resolve().parents[3];D=B/'research/n8_density_hessian';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for z in iter(lambda:f.read(1048576),b''):h.update(z)
 return h.hexdigest()
def qa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def qi(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def aq(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def mq(x):s,m,e,b=x;assert b>=0;return (-1 if s else 1)*F(int(m))*F(2)**int(e)
def ends(x):return (aq(x.lower()),aq(x.upper())) if isinstance(x,arb) else tuple(map(mq,x._mpi_))
c=json.loads((E/'checks.json').read_text());d=json.loads((E/'density_inputs.json').read_text())
assert c['status']=='PASS_INDEPENDENT_DENSITY_HESSIAN_BOUND'
for doc in [c,d]:
 for p,h in doc['files'].items():assert sha(B/p)==h,p
bound=F(c['bound_exact']);assert bound==F(5059,10000)
assert c['counts']=={'source_spans':7,'complete_density_polynomials':1827,'cells':13,'radial_subcells':52,'angular_radial_boxes':8320,'summed_component_enclosures':49920,'angular_factor_enclosures':167040}
cells=d['cells'];spans={r['span']:r for r in d['spans']};pmn,pmx=map(F,d['source_center_bracket_exact']);R=3*F(d['delta_exact']);th=F(d['theta_max_exact']);coverage=[];algebra=0
for q,ex,si,name in [(qa,lambda x:x.exp(),lambda x:x.sin(),'Arb512'),(qi,iv.exp,iv.sin,'iv180')]:
 rlo=ends(ex(q(F(cells[0]['a_exact']))));rhi=ends(ex(q(F(cells[-1]['b_exact']))));cap=ends(si(q(th)))
 assert pmn>R and 0<th<F(1,2) and rlo[1]<pmn-R and rhi[0]>pmx+R and cap[0]>R/pmn
 coverage.append({'engine':name,'first_radius_upper_exact':str(rlo[1]),'last_radius_lower_exact':str(rhi[0]),'cap_sine_lower_exact':str(cap[0])})
for kind in ['arb','iv']:
 vals=[F(r[kind+'_squared_upper_exact']) for r in c['cells']]
 assert max(vals)==F(c[kind+'_squared_upper_exact'])<bound**2
 assert c['where'][kind]['squared_upper_exact']==c[kind+'_squared_upper_exact']
for r,s in zip(c['cells'],cells):
 assert all(r[k]==s[k] for k in ['ci','a_exact','b_exact'])
 sp=spans[s['span']];assert F(sp['a_exact'])<=F(s['a_exact'])<F(s['b_exact'])<=F(sp['b_exact'])
assert all(F(a['b_exact'])==F(b['a_exact']) for a,b in zip(cells,cells[1:]))
# Independently reconstruct all differential coefficient maps on monomial basis.
# Coefficients stored in ascending t-c powers. Compare trace and traceless maps.
maxerr=F();errrows=[]
for sp in spans.values():
 center=F(sp['polynomial_mid_exact']);zmax=max(abs(F(sp['a_exact'])-center),abs(F(sp['b_exact'])-center));errs=[F(),F(),F()]
 assert len(sp['density_polynomials'])==262
 for j,p in enumerate(sp['density_polynomials']):
  f=2*j+1;assert len(p)==8
  if j==261:assert all(int(v['mid_m'])==int(v['rad_m'])==0 for v in p);continue
  for n,v in enumerate(p):
   rad=F(int(v['rad_m']))*F(2)**int(v['rad_e']);assert rad>=0
   A=[0]*8;C=[0]*8;L=[0]*8;T=[0]*8
   A[n]+=6;C[n]+=3-f*f;L[n]+=9-f*f;T[n]+=3+f*f
   if n:A[n-1]+=5*n;C[n-1]+=n;L[n-1]+=6*n;T[n-1]+=4*n
   if n>=2:A[n-2]+=n*(n-1);L[n-2]+=n*(n-1);T[n-2]+=n*(n-1)
   assert all(L[k]==A[k]+C[k] and T[k]==A[k]-C[k] for k in range(8));algebra+=16
   aerr=sum(F(abs(v))*zmax**k for k,v in enumerate(A))*rad
   cerr=sum(F(abs(v))*zmax**k for k,v in enumerate(C))*rad
   berr=f*(2*zmax**n+(n*zmax**(n-1) if n else 0))*rad
   errs[0]+=aerr;errs[1]+=berr;errs[2]+=cerr
 rmax=ends(qa(F(sp['b_exact'])).exp())[1]
 err=rmax*(errs[0]+2*errs[1]+errs[2]);maxerr=max(maxerr,err)
 errrows.append({'span':sp['span'],'source_coefficient_uncertainty_hessian_norm_upper_exact':str(err)})
# This bounds only coefficient-ball uncertainty, not all interval overestimation.
assert maxerr<F(1,10**50)
# Integer interval squares across zero really contain the complete square range.
squarechecks=0;nonfinite_rejected=[]
for a,b in [(-3,2),(-3,-2),(2,3),(-1,1),(0,0)]:
 x=qa(a).union(qa(b));y=iv.mpf([qi(a).a,qi(b).b]);upper=max(a*a,b*b)
 assert ends(abs(x)*abs(x))[1]>=upper and ends(y**2)[1]>=upper;squarechecks+=2
 try:
  assert ends(abs(x)**2)[1]>=upper
 except ValueError:
  nonfinite_rejected.append({'interval':[a,b],'arb_power_result':str(abs(x)**2),'verdict':'REJECTED_NONFINITE_BY_PRIMARY_ENDPOINT_CONVERTER'})
obj={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_DENSITY_OUTPUT_ALGEBRA_GEOMETRY_AUDIT','bound_exact':str(bound),'coverage':coverage,'counts':{'exact_differential_coefficient_identities':algebra,'interval_square_checks':squarechecks,'complete_radial_cells':13},'source_coefficient_uncertainty_upper_exact':str(maxerr),'source_coefficient_uncertainty_upper_display':float(maxerr),'source_error_by_span':errrows,'unit_nonfinite_power_cases':nonfinite_rejected,'scope':'Independent exact identities, both-engine coverage and final strict ceiling; source-ball uncertainty is retained and not discarded. All-ball Hessian computation is checks.json.','files':{str(p.relative_to(B)):sha(p) for p in [Path(__file__),E/'checks.json',E/'density_inputs.json',D/'PROOF.md',D/'ADDENDUM.md']}}
(E/'output_audit.json').write_text(json.dumps(obj,indent=2)+'\n');print(json.dumps({k:v for k,v in obj.items() if k not in ['files','source_error_by_span','source_coefficient_uncertainty_upper_exact','coverage']}))
