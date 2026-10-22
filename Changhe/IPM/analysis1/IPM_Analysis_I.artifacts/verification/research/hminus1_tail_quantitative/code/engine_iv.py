"""iv180 normalized Green rows, exact integer midpoint/radius convolutions.
No JS/TS, servers/listeners/tunnels, RLScience, or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from mpmath import iv
from flint import fmpz_poly,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_quantitative';E=D/'evidence';S=2**512
COUNTS={'integer_convolutions':0,'quantized_inputs':0,'integer_output_boxes':0}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def ep(t):sg,m,e,bc=t;assert bc>=0;return F(-int(m) if sg else int(m))*F(2)**int(e)
def box(x):
 lo,hi=map(ep,x._mpi_);assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':str(x)}
def bound(lo,hi):assert lo<=hi;return iv.mpf([a(lo).a,a(hi).b])
def cv(x,y):
 def pack(d):
  lo,hi=min(d),max(d);m=[];r=[]
  for i in range(lo,hi+1):
   l,h=[q*S for q in map(ep,d.get(i,iv.mpf(0))._mpi_)];ll=l.numerator//l.denominator;hh=-((-h.numerator)//h.denominator);assert F(ll)<=l<=h<=F(hh)
   m.append(ll+hh);r.append(hh-ll);COUNTS['quantized_inputs']+=1
  return lo,hi,m,r
 lo,hi,m,r=pack(x);ll,hh,n,s=pack(y)
 mm=fmpz_poly(m)*fmpz_poly(n);rr=fmpz_poly(list(map(abs,m)))*fmpz_poly(s)+fmpz_poly(r)*fmpz_poly(list(map(abs,n)))+fmpz_poly(r)*fmpz_poly(s)
 out={}
 for j in range(hi+hh-lo-ll+1):
  mi,ri=int(mm[j]),int(rr[j]);assert ri>=0;out[j+lo+ll]=bound(F(mi-ri,4*S*S),F(mi+ri,4*S*S));COUNTS['integer_output_boxes']+=1
 COUNTS['integer_convolutions']+=1
 return out
def product(aa,bb,A,C):
 vr={};wt={};s={};dc={}
 for n in range(1,len(A)+1):
  prev=A[n-1];nxt=A[n] if n<len(A) else iv.mpf(0);assert 2*n-aa-1>0 and 2*n+aa+1>0
  fn=(a(aa+1-2*n)*prev+a(aa+1+2*n)*nxt)/2;plus=fn/a(2*n-aa-1);minus=fn/a(2*n+aa+1);v=-(plus+minus)/2;w=(plus-minus)/2
  vr[2*n]=vr[-2*n]=v/2;wt[2*n]=w;wt[-2*n]=-w
 for j,x in enumerate(C):f=2*j+1;s[f]=x;s[-f]=-x;dc[f]=dc[-f]=f*x/2
 p,q=cv(vr,s),cv(wt,dc)
 return {i:a(bb)*p.get(i,iv.mpf(0))+q.get(i,iv.mpf(0)) for i in set(p)|set(q)}
def smul(x,y):
 d={}
 for i,q in x.items():
  for j,r in y.items():d[i+j]=d.get(i+j,F(0))+q*r
 return {i:q for i,q in d.items() if q}
def run():
 st=time.monotonic();iv.dps=180;ctx.threads=1
 archive=B.parent/'ipmA-num/data/trial_v2_h0.008.npz';assert sha(archive)=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
 with np.load(archive,allow_pickle=False) as z:k=F(float(z['k']));L=F(float(z['L']));t=F(float(z['knots'][-1]));ar=z['Aout'].copy()
 assert ar.shape==(260,10) and 0<k<F(1,4);beta=2*k-1;a2=3*k-2;ad=k-2
 base=smul(smul({1:F(1,2),-1:F(1,2)},{1:F(1,2),-1:F(1,2)}),{1:F(1),-1:F(-1)})
 cols=[];sines=[]
 for col in (0,1,2,6):
  cosine={};c=[F(float(x)) for x in ar[:,col]];cols.append(c)
  for m,x in enumerate(c):
   for freq in (2*m,-2*m):cosine[freq]=cosine.get(freq,F(0))+x/2
  sn=smul(base,cosine);sines.append([sn.get(2*j+1,F(0)) for j in range(261)])
 normpath=B/'research/modal_repair/evidence/independent_gauss_iv.json';nr=json.loads(normpath.read_text())['values']['A00_correction'];z=bound(F(nr['lower_exact_dyadic']),F(nr['upper_exact_dyadic']))
 lp=B/'research/outer_leading_cancellation/evidence/leading_iv_audit.json';lead=json.loads(lp.read_text());assert lead['status']=='PASS';eps=[bound(F(r['value']['lower_exact']),F(r['value']['upper_exact'])) for r in lead['residual_coefficients']];assert len(eps)==522
 radius=iv.exp(a(t));d0=[a(x)+a(base.get(2*j+1,0))*z for j,x in enumerate(sines[0])]
 A1=[a(sines[1][j] if j<261 else 0)+(a(k)/a(1-k))*eps[j]/radius**3 for j in range(522)]
 p=product(k,beta,d0,A1);q=product(beta,k,A1,d0);h2=[]
 for j in range(783):
  f=2*j+1;v=radius**a(3-a2)*((a(k)/a(2-2*k))*radius**2*(p.get(f,iv.mpf(0))+q.get(f,iv.mpf(0)))-a(sines[2][j] if j<261 else 0));h2.append(v)
  for row in (p,q):lo,hi=map(ep,(row.get(f,iv.mpf(0))+row.get(-f,iv.mpf(0)))._mpi_);assert lo<=0<=hi
 M=781;poly=[iv.mpf(0)]*(2*M+4)
 for j,x in enumerate(h2):poly[M+2+j]+=x;poly[M+1-j]-=x
 remainders=[]
 for root in (-1,-1,1):
  out=[iv.mpf(0)]*(len(poly)-1);out[-1]=poly[-1]
  for j in range(len(out)-2,-1,-1):out[j]=poly[j+1]+root*out[j+1]
  rem=poly[0]+root*out[0];lo,hi=map(ep,rem._mpi_);assert lo<=0<=hi;remainders.append(box(rem));poly=out
 poly=[4*x for x in poly];assert len(poly)==1563
 quotient=[poly[M]]+[2*poly[M+j] for j in range(1,M+1)]
 for j in range(1,M+1):lo,hi=map(ep,(poly[M-j]-poly[M+j])._mpi_);assert lo<=0<=hi
 n2=sum((abs(x) for x in quotient),iv.mpf(0));i2=(2*quotient[0]+quotient[1]-quotient[2]-quotient[3])/8
 nd=radius**a(5-k)*a(sum(map(abs,cols[3]),F(0)));idd=-(radius**a(5-k))*a((2*cols[3][0]+cols[3][1]-cols[3][2]-cols[3][3])/8)
 omega=(3-k)/2;jb=F(1,145860)
 def cost(N,I,aa):return (N*a(2)**a(omega)+abs(I)*a(4)*a(F(1,4)**8)/a((1-aa)*jb)*a(5)**a(omega))/a(L)**a(3-k)
 Sj=[F(4,3),F(44,9),F(416,27),F(1312,27)];exps=[beta,a2,ad];ns=[a('38.37961982'),n2,nd];K=[[a(2*max(F(1,2),2/(3-aa))*s)*N for s in Sj] for aa,N in zip(exps,ns)]
 vals={'N2':n2,'Nd':nd,'I2':i2,'Id':idd,'C2':cost(n2,i2,a2),'Cd':cost(nd,idd,ad),'H20':h2[0]}
 for T in (3000,10000,100000):
  for j in range(4):vals[f'local_T{T}_j{j}']=sum((a(9**(3-j))*ks[j]*(a(T)**a(aa))/a(T**3) for ks,aa in zip(K,exps)),iv.mpf(0))
 for T in (10000,1000000,100000000):vals[f'factor_T{T}']=a('.334616')*a(T)**a(k-1)+vals['C2']*a(T)**a(2*k-2)+vals['Cd']/a(T*T)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'iv180 original NPZ Laurent rows and normalized Green factors, exact512-bit outward integer convolutions and three quotient divisions','files':{str(p.relative_to(B)):sha(p) for p in (normpath,lp,D/'PROOF.md',Path(__file__))},'source_archive':{'path':str(archive),'sha256':sha(archive)},'exact':{'k':str(k),'L':str(L),'tplus':str(t),'exponents':list(map(str,exps)),'Sj':list(map(str,Sj))},'values':{n:box(x) for n,x in vals.items()},'H2_sines':[box(x) for x in h2],'H2_quotient':[box(x) for x in quotient],'remainders':remainders,'counts':dict(COUNTS,sines=783,quotient_coefficients=782,antisymmetry_diagnostics=1566,symmetry_diagnostics=781,synthetic_divisions=3),'seconds':time.monotonic()-st}
 (E/'iv.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:x['display'] for n,x in out['values'].items()}));print(out['seconds'])
if __name__=='__main__':run()
