"""Full Arb512 Laurent convolutions and collected quotient inverse.
No JS/TS, servers/listeners/tunnels, RLScience, or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,arb_poly,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_quantitative';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def a(q):q=F(q);return arb(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=ep(x.lower()),ep(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(35)}
def cv(x,y):
 lo=min(x);hi=max(x);ll=min(y);hh=max(y);p=arb_poly([x.get(i,arb(0)) for i in range(lo,hi+1)])*arb_poly([y.get(i,arb(0)) for i in range(ll,hh+1)])
 return {i+lo+ll:p[i] for i in range(hi+hh-lo-ll+1)}
def product(aa,bb,A,C):
 vr={};wt={};s={};dc={}
 for n in range(1,len(A)+1):
  prev=A[n-1];nxt=A[n] if n<len(A) else arb(0);den=4*n*n-(aa+1)**2;assert den>0
  fn=(a(aa+1-2*n)*prev+a(aa+1+2*n)*nxt)/2;v=-2*n*fn/a(den);w=a(aa+1)*fn/a(den)
  vr[2*n]=vr[-2*n]=v/2;wt[2*n]=w;wt[-2*n]=-w
 for j,x in enumerate(C):
  f=2*j+1;s[f]=x;s[-f]=-x;dc[f]=dc[-f]=f*x/2
 p,q=cv(vr,s),cv(wt,dc)
 return {i:a(bb)*p.get(i,arb(0))+q.get(i,arb(0)) for i in set(p)|set(q)}
def run():
 st=time.monotonic();ctx.prec=512;ctx.threads=1
 inp=B/'data_exact/modal_v2.json';assert sha(inp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';data=json.loads(inp.read_text());ar=data['arrays'];hx=lambda x:F(float.fromhex(x));k=hx(data['scalars_hex']['k']);L=hx(data['scalars_hex']['L']);t=hx(ar['knots']['hex'][-1]);beta=2*k-1;a2=3*k-2;ad=k-2;assert 0<k<F(1,4)
 cols=[];sines=[]
 for col in (0,1,2,6):
  c=[hx(ar['Aout']['hex'][10*m+col]) for m in range(260)];cols.append(c);d=[F(0)]*261
  for m,x in enumerate(c):
   for f in (1+2*m,1-2*m,3+2*m,3-2*m):d[(abs(f)-1)//2]+=F(1 if f>0 else -1,8)*x
  sines.append(d)
 np=B/'research/modal_repair/evidence/scalar_result.json';z=arb(json.loads(np.read_text())['A00_correction']['ball'])
 lp=B/'research/outer_leading_cancellation/evidence/leading_result.json';lead=json.loads(lp.read_text());eps=[a(r['value']['lower_exact']).union(a(r['value']['upper_exact'])) for r in lead['residual_coefficients']];assert len(eps)==522
 d0=[a((3-k)*t).exp()*(a(x)+(z/4 if j<2 else 0)) for j,x in enumerate(sines[0])]
 A1=[a((3-beta)*t).exp()*a(sines[1][j] if j<261 else 0)+a(k/(1-k))*a(-beta*t).exp()*eps[j] for j in range(522)]
 p=product(k,beta,d0,A1);q=product(beta,k,A1,d0);h2=[]
 for j in range(783):
  freq=2*j+1;v=a(k/(2*(1-k)))*(p.get(freq,arb(0))+q.get(freq,arb(0)))-a((3-a2)*t).exp()*a(sines[2][j] if j<261 else 0);h2.append(v)
  assert (p.get(freq,arb(0))+p.get(-freq,arb(0))).contains(0) and (q.get(freq,arb(0))+q.get(-freq,arb(0))).contains(0)
 def c(i):return (-1 if i%2 else 1)*(i//2+1)
 quotient=[4*sum((c(j-1)*h2[j] for j in range(1,783)),arb(0))]+[8*sum((c(j-m-1)*h2[j] for j in range(m+1,783)),arb(0)) for m in range(1,782)]
 assert (h2[0]-(2*quotient[0]-quotient[2])/8).contains(0)
 nd=a((5-k)*t).exp()*sum((a(abs(x)) for x in cols[3]),arb(0));idd=-a((5-k)*t).exp()*a(sines[3][1]);n2=sum((abs(x) for x in quotient),arb(0));i2=h2[1]
 omega=(3-k)/2;jb=F(1,145860);bmax=F(1,2**16);sc=a((k-3)*F(1))*a(L).log()
 def cost(N,I,aa):return sc.exp()*(a(2)**a(omega)*N+a(4*bmax/((1-aa)*jb))*a(5)**a(omega)*abs(I))
 Sj=[F(4,3),F(44,9),F(416,27),F(1312,27)];ns=[a('38.37961982'),n2,nd];exps=[beta,a2,ad];ks=[[2*N*a(max(F(1,2),2/(3-aa)))*a(S) for S in Sj] for N,aa in zip(ns,exps)]
 vals={'N2':n2,'Nd':nd,'I2':i2,'Id':idd,'C2':cost(n2,i2,a2),'Cd':cost(nd,idd,ad),'H20':h2[0]}
 for T in (3000,10000,100000):
  for j in range(4):vals[f'local_T{T}_j{j}']=a(9**(3-j))*sum((K[j]*a((aa-3)*F(1)).__mul__(a(T).log()).exp() for K,aa in zip(ks,exps)),arb(0))
 for T in (10000,1000000,100000000):vals[f'factor_T{T}']=a('.334616')*a(T)**a(k-1)+vals['C2']*a(T)**a(2*k-2)+vals['Cd']/a(T*T)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'Arb512 full Laurent polynomial products and exact collected inverse quotient','files':{str(p.relative_to(B)):sha(p) for p in (inp,np,lp,D/'PROOF.md',Path(__file__))},'exact':{'k':str(k),'L':str(L),'tplus':str(t),'exponents':list(map(str,exps)),'Sj':list(map(str,Sj))},'values':{n:box(x) for n,x in vals.items()},'H2_sines':[box(x) for x in h2],'H2_quotient':[box(x) for x in quotient],'counts':{'sines':783,'quotient_coefficients':782,'antisymmetry_diagnostics':1566,'full_Laurent_convolutions':4,'collected_integer_terms':sum(range(1,783))+782},'seconds':time.monotonic()-st}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({n:x['display'] for n,x in out['values'].items()}));print(out['seconds'])
if __name__=='__main__':run()
