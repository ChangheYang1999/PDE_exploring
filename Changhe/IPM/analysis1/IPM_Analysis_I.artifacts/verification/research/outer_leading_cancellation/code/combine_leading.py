"""Exact leading-exponent identification and Arb Laurent angular convolution."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,math,time,resource
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint,mpmath
from flint import arb,arb_poly,ctx
B=Path(__file__).resolve().parents[3];E=B/'research/outer_leading_cancellation/evidence'
OV='7857fb1b2347ec5ec1e1206db7272c5144d903b0209f23e2a5d46cad9664d1ac'
def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def out(x):
 assert x.is_finite()
 return {'lower_exact':str(dy(x.lower())),'upper_exact':str(dy(x.upper())),'display':x.str(28)}
def run():
 start=time.monotonic();resource.setrlimit(resource.RLIMIT_AS,(15*1024**3,15*1024**3));ctx.prec=384
 assert flint.__version__=='0.9.0' and mpmath.__version__=='1.3.0'
 vp=B/'research/outer_majorant/evidence/verdict.json';assert sha(vp)==OV;v=json.loads(vp.read_bytes());assert v['status']=='CONFIRMED'
 rp=B/'research/outer_majorant/evidence/outer_result.json';cp=B/'research/outer_majorant/evidence/exact_outer_coefficients.json'
 for p in [rp,cp]:assert sha(p)==v['files'][str(p.relative_to(B))]
 old=json.loads(rp.read_bytes());data=json.loads(cp.read_bytes());assert sha(cp)==old['coefficient_sha256']
 k=F(old['scalars_exact']['k']);L=F(old['scalars_exact']['L']);tb=F(old['tb_exact']);beta=[F(x) for x in data['beta_exact']]
 assert k==F(1615536043799051,9007199254740992) and 0<k<F(1,2) and beta[0]==k and beta[1]==2*k-1 and len(beta)==11
 gs=2*k-1
 assert [i for i,b in enumerate(beta) if b==gs]==[1]
 assert [(i,j) for i,x in enumerate(beta) for j,y in enumerate(beta) if x+y-1==gs]==[(0,0)]
 assert all(-2*n-2+b<gs for n in range(1,262) for b in beta)
 assert all(b<gs for b in beta[2:])
 zlo,zhi=map(F,data['correction_parameter_exact_interval']);assert zlo<=zhi
 z=aa(zlo).union(aa(zhi))
 def ev(pair):a,b=map(F,pair);return aa(a)+aa(b)*z
 assert len(data['rows'])==262 and len(old['green'])==261
 d=[];d1=[]
 for j,row in enumerate(data['rows']):
  assert row['j']==j and len(row['basis'])==11
  assert len(row['basis'][0])==len(row['basis'][1])==1
  d.append(ev(row['basis'][0][0]));d1.append(ev(row['basis'][1][0]))
 assert len(d)==262 and d[-1].is_zero() and d1[-1].is_zero()
 V=[arb(0)]*523;S=[arb(0)]*523;D=[arb(0)]*522;Q=[arb(0)]*522
 qrecords=[]
 for n,row in enumerate(old['green'],1):
  assert row['n']==n and len(row['plus_exact'][0])==len(row['minus_exact'][0])==1
  qp=ev(row['plus_exact'][0][0]);qm=ev(row['minus_exact'][0][0]);vn=-(qp+qm)/2;wn=(qm-qp)/2
  V[261+n]=vn/2;V[261-n]=vn/2;S[261+n]=wn;S[261-n]=-wn
  qrecords.append({'n':n,'v':out(vn),'w':out(wn)})
 for j in range(261):
  nu=2*j+1;D[261+j]=aa(k)*d[j];D[260-j]=-aa(k)*d[j];Q[261+j]=nu*d[j]/2;Q[260-j]=nu*d[j]/2
 conv=arb_poly(V)*arb_poly(D)+arb_poly(S)*arb_poly(Q)
 assert conv.degree()<=1043
 ep3=aa(3*tb).exp();ep5=aa(5*tb).exp();epsilon=[];parity=0
 for q in range(522):
  assert (conv[522+q]+conv[521-q]).contains(0);parity+=1
  linear=aa(gs/k-1)*d1[q] if q<261 else arb(0)
  epsilon.append(ep3*linear+ep5*conv[522+q])
 newc=sum((abs(x) for x in epsilon),arb(0));C=[];replacements=0
 for row in old['majorant']:
  g=F(row['gamma_exact']);cs=[aa(F(x['upper_exact'])) for x in row['coefficients']]
  if g==gs:
   assert len(cs)==1;oldc=cs[0];cs=[newc];replacements+=1
  C.append((g,cs))
 assert dy(newc.upper())<dy(oldc.upper())
 assert replacements==1 and len(C)==1864 and sum(len(p) for g,p in C)==3508
 print(json.dumps({'utc':utc(),'stage':'combined','C_star':newc.str(20),'old_C_star':oldc.str(20),'seconds':time.monotonic()-start}),flush=True)
 def maximum(rate,l,T):
  assert rate>0 and T>=0
  x=max(T,F(l)/rate);return aa(x**l)*aa(-rate*x).exp()
 u=aa(tb).exp()/aa(L);cases=[]
 for T in map(F,[0,1,5,9,10,17]):
  vals={'absolute_W':sum((cc*maximum(-g,l,T) for g,p in C for l,cc in enumerate(p)),arb(0))}
  for delta in [F(0),F(1,2),F(1,2)-k]:
   K=u**aa(delta-k)*(1+u**(-2)*aa(-2*T).exp())**aa((3-k)/2)*(1+u**(-1)*aa(-T).exp())**aa(delta)
   vals['weighted_delta_'+str(delta)]=K*sum((cc*maximum(k-delta-g,l,T) for g,p in C for l,cc in enumerate(p)),arb(0))
  cases.append({'T_exact':str(T),'values':{key:out(x) for key,x in vals.items()}})
  print(json.dumps({'utc':utc(),'T_exact':str(T),'values':{key:x.str(15) for key,x in vals.items()}}),flush=True)
 assert all(k-g>0 for g,p in C)
 K0=u**aa(-k)*(1+u**(-2))**aa((3-k)/2)
 l2=arb.pi().sqrt()*aa(L)*K0*sum((cc*(aa(math.factorial(2*l))/aa(2*(k-g))**(2*l+1)).sqrt() for g,p in C for l,cc in enumerate(p)),arb(0))
 result={'utc':utc(),'status':'COMPUTED_REQUIRES_INDEPENDENT_AUDIT','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/outer_leading_cancellation/PROOF.md'),'outer_verdict_sha256':OV,'outer_result_sha256':sha(rp),'exact_coefficients_sha256':sha(cp),'precision_bits':ctx.prec,'versions':{'python-flint':flint.__version__,'mpmath':mpmath.__version__},'scalars_exact':{'k':str(k),'L':str(L),'tb':str(tb)},'gamma_star_exact':str(gs),'normalization_interval_exact':[str(zlo),str(zhi)],'leading_velocity':qrecords,'residual_coefficients':[{'q':q,'value':out(x)} for q,x in enumerate(epsilon)],'old_C_star_upper_exact':str(dy(oldc.upper())),'new_C_star':out(newc),'cases':cases,'exterior_L2_majorant':out(l2),'checks':{'leading_linear_sources':1,'leading_particular_sources':1,'transient_inequalities':261*11,'parity_zero_containments':parity,'positive_angular_coefficients':522,'majorant_exponents':1864,'majorant_monomials':3508},'seconds':time.monotonic()-start,'method':'Arb384 Laurent polynomial convolution, exact exponent isolation, replacing entire gamma-star row; scalar maxima on complete half-lines.','scope':'Retains only the leading exterior cancellation; audited nonleading upper endpoints are shared dependencies.'}
 dest=E/'leading_result.json';dest.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':utc(),'stage':'done','sha256':sha(dest),'seconds':result['seconds']}),flush=True)
if __name__=='__main__':run()
