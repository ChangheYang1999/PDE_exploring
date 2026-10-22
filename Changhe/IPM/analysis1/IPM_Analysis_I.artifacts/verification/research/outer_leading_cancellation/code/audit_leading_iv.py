"""Independent direct Poisson/trigonometric leading-cancellation audit with iv."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from mpmath import iv
B=Path(__file__).resolve().parents[3];E=B/'research/outer_leading_cancellation/evidence';iv.dps=160
ZERO=(F(0),F(0))
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def rf(x):
 sign,m,e,bc=x;assert bc>=0
 return (-1 if sign else 1)*F(int(m))*F(2)**int(e)
def ends(x):
 assert not iv.isnan(x) and not iv.isinf(x)
 a,b=map(rf,x._mpi_);assert a<=b;return a,b
def interval(a,b):assert a<=b;return iv.mpf([iq(a).a,iq(b).b])
def out(x):a,b=ends(x);return {'lower_exact':str(a),'upper_exact':str(b),'display':str(x)}
def enclosed(old,x,tag):
 a,b=ends(x);lo,hi=F(old['lower_exact']),F(old['upper_exact']);assert lo<=hi
 if not lo<=a<=b<=hi:raise AssertionError((tag,'primary does not enclose independent interval',str(a-lo),str(hi-b)))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,q):return a[0]*q,a[1]*q
def run():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 rp=E/'leading_result.json';res=json.loads(rp.read_bytes());assert res['status']=='COMPUTED_REQUIRES_INDEPENDENT_AUDIT'
 assert sha(B/'research/outer_leading_cancellation/code/combine_leading.py')==res['source_sha256'] and sha(B/'research/outer_leading_cancellation/PROOF.md')==res['proof_sha256']
 vp=B/'research/outer_majorant/evidence/verdict.json';assert sha(vp)==res['outer_verdict_sha256']=='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac'
 v=json.loads(vp.read_bytes());assert v['status']=='CONFIRMED';op=B/'research/outer_majorant/evidence/outer_result.json';assert sha(op)==res['outer_result_sha256']==v['files'][str(op.relative_to(B))];old=json.loads(op.read_bytes())
 inp=B/'data_exact/modal_v2.json';assert sha(inp)==old['dependency_pins']['input']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 data=json.loads(inp.read_bytes());ar=data['arrays'];hx=lambda s:F.from_float(float.fromhex(s));k=hx(data['scalars_hex']['k']);L=hx(data['scalars_hex']['L']);tb=hx(ar['knots']['hex'][-1]);bo=hx(data['scalars_hex']['bo']);assert 0<k<F(1,2) and bo>120
 assert res['scalars_exact']=={'k':str(k),'L':str(L),'tb':str(tb)}
 zp=B/'research/modal_repair/evidence/independent_gauss_iv.json';assert sha(zp)==old['dependency_pins']['normalization'];zz=json.loads(zp.read_bytes())['values']['A00_correction'];zlo,zhi=[F(zz[key]) for key in ['lower_exact_dyadic','upper_exact_dyadic']];assert [str(zlo),str(zhi)]==res['normalization_interval_exact'];z=interval(zlo,zhi)
 def ev(pair):return iq(pair[0])+iq(pair[1])*z
 d=[ZERO]*262;d1=[ZERO]*262;assert ar['Aout']['shape']==[260,10]
 for m in range(260):
  a0=(hx(ar['Aout']['hex'][m*10]),F(1) if m==0 else F(0));a1=(hx(ar['Aout']['hex'][m*10+1]),F(0))
  for freq in [1+2*m,1-2*m,3+2*m,3-2*m]:
   q=(abs(freq)-1)//2;w=F(1 if freq>0 else -1,8);d[q]=add(d[q],mul(a0,w));d1[q]=add(d1[q],mul(a1,w))
 assert d[-1]==d1[-1]==ZERO
 cp=B/'research/outer_majorant/evidence/exact_outer_coefficients.json';assert sha(cp)==res['exact_coefficients_sha256']==old['coefficient_sha256'];co=json.loads(cp.read_bytes());exactchecks=0
 assert len(co['rows'])==262
 for j in range(262):
  assert len(co['rows'][j]['basis'][0])==len(co['rows'][j]['basis'][1])==1
  assert tuple(map(F,co['rows'][j]['basis'][0][0]))==d[j] and tuple(map(F,co['rows'][j]['basis'][1][0]))==d1[j];exactchecks+=4
 pairs=[(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(0,1),(1,1),(2,1),(0,2)];assert data['outer_jl']==[list(x) for x in pairs]
 beta=[k-j*(1-k)-2*l for j,l in pairs]+[3-bo];gs=2*k-1;assert str(gs)==res['gamma_star_exact']
 assert [i for i,b in enumerate(beta) if b==gs]==[1] and [(i,j) for i,b in enumerate(beta) for j,c in enumerate(beta) if b+c-1==gs]==[(0,0)]
 assert all(-2*n-2+b<gs for n in range(1,262) for b in beta)
 ds=[ev(x) for x in d[:261]];rad=[iq(k)*x for x in ds];ang=[(2*j+1)*x for j,x in enumerate(ds)]
 vel=[];checks=0;a=k+1
 for n in range(1,262):
  m=2*n;fn=mul(add(mul(d[n-1],a-m),mul(d[n],a+m)),F(1,2));den=F(m*m)-a*a;assert den>0
  vn=ev(mul(fn,-m/den));wn=ev(mul(fn,a/den));oldv=res['leading_velocity'][n-1];assert oldv['n']==n
  enclosed(oldv['v'],vn,('v',n));enclosed(oldv['w'],wn,('w',n));checks+=2;vel.append((vn,wn))
 product=[iv.mpf(0) for _ in range(522)];pairs_done=0
 def accumulate(freq,value):
  assert freq and abs(freq)<=1043 and abs(freq)%2==1
  q=(abs(freq)-1)//2;product[q]+=value if freq>0 else -value
 for n,(vn,wn) in enumerate(vel,1):
  m=2*n
  for j in range(261):
   nu=2*j+1;radial=vn*rad[j]/2;angular=wn*ang[j]/2
   accumulate(nu+m,radial);accumulate(nu-m,radial);accumulate(m+nu,angular);accumulate(m-nu,angular);pairs_done+=1
  if n%65==0:print(json.dumps({'utc':utc(),'stage':'direct_trigonometric_products','velocity_modes':n,'pairs':pairs_done,'seconds':time.monotonic()-start}),flush=True)
 ep3=iv.exp(iq(3*tb));ep5=iv.exp(iq(5*tb));eps=[]
 assert len(res['residual_coefficients'])==522
 for q in range(522):
  linear=iq(gs/k-1)*ev(d1[q]) if q<261 else iv.mpf(0);value=ep3*linear+ep5*product[q]
  row=res['residual_coefficients'][q];assert row['q']==q;enclosed(row['value'],value,('epsilon',q));checks+=1;eps.append(value)
 newc=sum((abs(x) for x in eps),iv.mpf(0));enclosed(res['new_C_star'],newc,'C_star');checks+=1
 assert ends(newc)[1]<F(res['old_C_star_upper_exact'])
 C=[];replaced=0
 for row in old['majorant']:
  g=F(row['gamma_exact']);cs=[iq(F(x['upper_exact'])) for x in row['coefficients']]
  if g==gs:assert len(cs)==1;cs=[newc];replaced+=1
  C.append((g,cs))
 assert replaced==1 and len(C)==1864 and sum(len(p) for g,p in C)==3508 and pairs_done==261*261
 def maximum(rate,l,T):
  assert rate>0 and T>=0
  x=max(T,F(l)/rate);return iq(x**l)*iv.exp(iq(-rate*x))
 u=iv.exp(iq(tb))/iq(L);cases=[];assert [F(c['T_exact']) for c in res['cases']]==list(map(F,[0,1,5,9,10,17]))
 for oldcase in res['cases']:
  T=F(oldcase['T_exact']);vals={'absolute_W':sum((cc*maximum(-g,l,T) for g,p in C for l,cc in enumerate(p)),iv.mpf(0))}
  for delta in [F(0),F(1,2),F(1,2)-k]:
   K=iv.exp(iq(delta-k)*iv.log(u)+iq((3-k)/2)*iv.log(1+iv.exp(iq(-2*T))/(u*u))+iq(delta)*iv.log(1+iv.exp(iq(-T))/u))
   vals['weighted_delta_'+str(delta)]=K*sum((cc*maximum(k-delta-g,l,T) for g,p in C for l,cc in enumerate(p)),iv.mpf(0))
  assert set(vals)==set(oldcase['values'])
  for key,value in vals.items():enclosed(oldcase['values'][key],value,('bound',str(T),key));checks+=1
  cases.append({'T_exact':str(T),'values':{key:out(x) for key,x in vals.items()}})
 assert all(k-g>0 for g,p in C)
 K0=iv.exp(-iq(k)*iv.log(u)+iq((3-k)/2)*iv.log(1+u**(-2)))
 l2=iv.sqrt(iv.pi)*iq(L)*K0*sum((cc*iv.sqrt(iq(F(math.factorial(2*l))/(2*(k-g))**(2*l+1))) for g,p in C for l,cc in enumerate(p)),iv.mpf(0));enclosed(res['exterior_L2_majorant'],l2,'L2');checks+=1
 result={'utc':utc(),'status':'PASS','source_sha256':sha(__file__),'primary_source_sha256':res['source_sha256'],'primary_result_sha256':sha(rp),'proof_sha256':res['proof_sha256'],'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'iv_dps':iv.dps,'exact_projection_scalar_checks':exactchecks,'direct_trigonometric_pairs':pairs_done,'enclosure_checks':checks,'new_C_star':out(newc),'residual_coefficients':[{'q':q,'value':out(x)} for q,x in enumerate(eps)],'cases':cases,'exterior_L2_majorant':out(l2),'seconds':time.monotonic()-start,'method':'Independent exact raw cosine-to-sine affine projection, direct radial Poisson solution and elementary product-to-sum identities for all pairs; mpmath.iv scalar maxima.','scope':'New leading coefficient independently reconstructed; nonleading coefficient upper endpoints are shared audited dependencies.'}
 dest=E/'leading_iv_audit.json';dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','status':'PASS','checks':checks,'seconds':result['seconds']}),flush=True)
if __name__=='__main__':run()
