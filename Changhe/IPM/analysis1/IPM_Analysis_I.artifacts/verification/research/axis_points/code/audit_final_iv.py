"""Independent mpmath.iv endpoint parsing, constants, and downstream arithmetic."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/axis_points/evidence';iv.dps=80

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def exact(x):return F.from_float(float.fromhex(x))
def q(v):v=F(v);return iv.mpf(v.numerator)/v.denominator
def endpoints(s):
 v=s.strip('[]').split(' +/- ');m=F(v[0]);r=F(v[1]) if len(v)>1 else F(0);return m-r,m+r

def hull(d):return iv.mpf([q(endpoints(d['lower'])[0]).a,q(endpoints(d['upper'])[1]).b])
def interval(lo,hi):return iv.mpf([q(lo).a,q(hi).b])
def inside(v,lo,hi):return v.a>=q(lo).b and v.b<=q(hi).a
raw=json.loads((BASE/'data_exact/x3.json').read_text());assert sha(BASE/'data_exact/x3.json')=='1a8decfb0beb666a36bc14f08514d25b371b778872bdf13d5801c2a4c40b7946'
k,L=(q(exact(raw['scalars_hex'][v])) for v in ('k','L'));p=6+2*k/(2-k);P=4*L**2/(iv.pi*(1-k))
cpath=BASE/'research/canonical_inverse/evidence/strain_arb_20_32_result.json';assert sha(cpath)=='16135e23513f905fb835c57df9dbd424f5efe0b7d5fe76831bb18221520723db';strain=hull(json.loads(cpath.read_text())['strain'])
z=[exact(v) for v in raw['z_hex']];M=raw['integers']['angular']+1;nb=raw['integers']['degree'];modes=[[F(0)]+z[1+m*nb:1+(m+1)*nb] for m in range(M)];tail=z[1+M*nb:];assert len(tail)==6
Csum=sum((max(map(abs,row)) for row in modes),F(0));Ct=sum(map(abs,tail),F(0));Bp=((p-2)/p)**((p-2)/2)*2/p;globalM=iv.exp(q(Csum)+q(Ct)*Bp)
B=3*L**2/(4*(1-k));K=L**2/(1-k)*(q(F(1,36))+iv.sqrt(3)/(8*iv.pi));totalC=B+K
cover=json.loads((E/'rule_cover_audit.json').read_text());results=[]
public={7:{'velocity':('-54.520','-54.459'),'canonical_drift':('-15.492','-15.432')},10:{'velocity':('-41.680','-41.590'),'canonical_drift':('14.07','14.17')}}
for tag in ('axis7','axis10'):
 path=E/(tag+'_result.json');res=json.loads(path.read_text());partpath=E/(tag+'_partition.json');part=json.loads(partpath.read_text());assert sha(partpath)==res['partition_sha256'];assert any(v['tag']==tag and v['partition_sha256']==sha(partpath) for v in cover['partition_checks'])
 source=BASE/'research/axis_points/code'/('axis_arb_v2_archived.py' if tag=='axis7' else 'axis_arb.py');assert sha(source)==part['script_sha256'];assert res['input_sha256']==part['input_sha256']==sha(BASE/'data_exact/x3.json')
 entries=[]
 for line in (E/(tag+'_run.log')).read_text().splitlines():
  try:entries.append(json.loads(line))
  except json.JSONDecodeError:pass
 last=[v for v in entries if v.get('stage')=='quadrature'][-1];assert last['done']==last['total']==len(part['q'])
 x=int(part['settings']['x']);xx=q(x);ha,hb=map(F,part['removed_q_strip']);cap=F(part['cap_q']);tcap=F(part['cap_theta_normalized']);qstar=1-(1+(xx/L)**2)**((k-1)/2);assert qstar.a>q(ha).b and qstar.b<q(hb).a
 def beta(v):
  ss=1-(1-q(v))**(2/(1-k));return L**2*ss/(L**2*ss+xx**2*(1-ss))
 assert beta(ha).b<q(F(1,2)).a and beta(hb).a>q(F(1,2)).b
 errors={name:hull(v) for name,v in part['errors_before_prefactor'].items()};dd=q(tcap)*iv.pi/2
 check={'singular_strip':q(hb-ha)*3*iv.pi/16*globalM,'radial_caps':2*q(cap)*3*iv.pi/16*globalM,'angular_cap':dd**3/3*(1+4*dd**2)/(1-dd**2)**2*iv.exp(q(Csum)+q(Ct)*dd**(p-2))}
 # Independent bounds may be a few ulps wider than the stored intervals. Use their hull uniformly.
 for name,v in check.items():errors[name]=iv.mpf([min(errors[name].a,v.a),max(errors[name].b,v.b)])
 err=sum(errors.values(),q(0));summation=hull(last['sum']);velocity=xx*P*(summation+iv.mpf([-err.b,err.b]));drift=xx*(1+strain)/3+velocity;pert=q(F(1,100))*xx*totalC
 for name,v in [('velocity',velocity),('canonical_drift',drift)]:assert inside(v,*public[x][name]),(tag,name,str(v))
 margin=-drift.b-pert.b if x==7 else drift.a-pert.b;assert margin>0
 results.append({'tag':tag,'x_exact':x,'public_bounds':public[x],'iv_velocity':str(velocity),'iv_canonical_drift':str(drift),'iv_full_drift_perturbation_eps_0_01':str(pert),'strict_conditional_sign_margin_lower':str(margin),'independently_recomputed_strip_cap_bounds':{n:str(v) for n,v in check.items()},'source_sha256':sha(source),'partition_sha256':sha(partpath),'result_sha256':sha(path),'complete_log_sha256':sha(E/(tag+'_run.log')),'quadrature_nodes_evaluated':len(part['q'])*part['settings']['nq']*len(part['theta_over_pi_half'])*part['settings']['nt']})
out={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED independent downstream arithmetic and rational/root audit; analytic quadrature source has separate proof audit','method':'mpmath.iv80, exact decimal endpoint hulls, exact dyadic JSON coefficients, separately reconstructed global exponential and kernel bounds','source_sha256':sha(Path(__file__)),'strain_sha256':sha(cpath),'global_M':str(globalM),'axis_drift_factor_constant':str(totalC),'points':results,'conditional_result':'Any exact normalized canonical P2 profile within epsilon<=0.01 of X3 in the stated weighted factor norm has its unique positive-axis equilibrium in (7,10), provided the audited full quadratures are accepted. This asserts no profile existence.','limits':'One full rigorous quadrature per point. This script checks downstream arithmetic and removed strips/caps, not a second full quadrature or a separate evaluation of every complex remainder.'}
(E/'final_iv_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
