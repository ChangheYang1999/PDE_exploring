"""Rigorous ball-polynomial Hessian integral with two independent radial bases.
Exact potential jets are converted once to Arb. All subsequent arithmetic is
outward rounded. Analytically zero origin/tail coefficients are removed only at
the locations specified in INTERVAL_HESSIAN_PROOF.md, after a zero containment test.
"""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from math import comb
import sys,json,time,hashlib
from flint import arb,arb_poly,ctx
HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'11_residual_norms/verification'))
import compact_norms as cn
import audit_norms as au
Z=arb_poly([0,1]); ONE=arb_poly([1]); OM=ONE-Z

def aq(q):return cn.aq(q)
def convert(p):return arb_poly([aq(c) for c in p.coeffs()])
def clean(D):return {k:p for k,p in D.items() if p}
def add(D,key,p):
 ell,kind,n=key
 if n<0:
  n=-n
  if kind=='s':p=-p
 if kind=='s' and n==0:return
 key=ell,kind,n
 D[key]=D.get(key,arb_poly([]))+p

def plus(*terms):
 out={}
 for scale,D in terms:
  for key,p in D.items():add(out,key,p*aq(scale))
 return clean(out)

def mul(D,E):
 out={}
 for (ell,k,n),p in D.items():
  for (ell2,l,m),q in E.items():
   v=p*q
   for kind,mode,factor in cn.trigprod(k,n,l,m):add(out,(ell+ell2,kind,mode),v*aq(factor))
 return clean(out)

def drop_t(p):
 assert p[0].contains(0),('origin nonzero',p[0])
 return arb_poly(p.coeffs()[1:])

def drop_om(p):
 # p=(1-t)q, so q_i=sum_{k<=i}p_k; p(1)=0 is analytical.
 assert p(arb(1)).contains(0),('tail nonzero',p(arb(1)))
 co=p.coeffs();out=[];acc=arb(0)
 for a in co[:-1]:
  acc+=a;out.append(acc)
 return arb_poly(out)

def diff(D,d,axis,delta):
 out={}
 for (ell,kind,n),p in D.items():
  if d%2==0:
   rad=(ONE-Z*aq(d+ell*delta))*p+2*Z*OM*p.derivative();ang=p
  else:
   rad=-aq(d-1+ell*delta)*p+2*OM*p.derivative();ang=drop_t(p) if n else arb_poly([])
  rk='c' if axis=='x' else 's'
  for kk,nn,fac in cn.trigprod(rk,1,kind,n):add(out,(ell,kk,nn),rad*aq(fac))
  if n:
   ak='s' if axis=='x' else 'c';dk='s' if kind=='c' else 'c'
   sign=(-1 if kind=='c' else 1)*(-1 if axis=='x' else 1)
   for kk,nn,fac in cn.trigprod(ak,1,dk,n):add(out,(ell,kk,nn),ang*aq(sign*n*fac))
 return clean(out)

def construct(name):
 c,A,sha,rawsha=cn.source(name);delta=1-1/c;j3={};j4={};start=time.monotonic()
 for d,nxs,save in [(3,range(3),j3),(4,range(4),j4)]:
  for nx in nxs:
   save[nx]={k:convert(p) for k,p in cn.chi_compact(A,c,d,nx).items()}
   print('chi',d,nx,'seconds',time.monotonic()-start,flush=True)
 rho=plus((-1,j3[0]),(-1,j3[2]));u1=plus((-1,j3[1]));u2=j3[2]
 rx=plus((-1,j4[1]),(-1,j4[3]));ry=plus((-1,j4[0]),(-1,j4[2]))
 F=plus((c,mul({(0,'c',1):ONE},rx)),(c,mul({(0,'s',1):ONE},ry)),(-1,rho),(1,mul(u1,rx)),(1,mul(u2,ry)))
 print('F assembled',len(F),'seconds',time.monotonic()-start,flush=True)
 D={(0,0):F}
 for d in range(2):
  for nx in range(d+2):D[d+1,nx]=diff(D[d,0],d,'y',delta) if nx==0 else diff(D[d,nx-1],d,'x',delta)
  print('D',d+1,'seconds',time.monotonic()-start,flush=True)
 return c,A,sha,rawsha,D

def compose(p,x):
 z=arb_poly([])
 for a in reversed(p.coeffs()):z=z*x+a
 return z

def group(D,delta,basis):
 groups={};facts=[]
 for nx in range(3):
  modes={}
  for (ell,kind,n),p in D[2,nx].items():
   # At ell=1, the leading linear residual c*gamma-1 vanishes identically.
   q=1 if ell==1 else 0
   pp=drop_om(p) if q else p
   if basis=='u':pp=compose(pp,OM)
   modes.setdefault((kind,n),[]).append((ell,q,pp))
   facts.append([nx,ell,kind,n,q])
  for (kind,n),rows in modes.items():
   for i,(ell,q,p) in enumerate(rows):
    others=rows if basis=='u' else rows[i:]
    for j,(ell2,q2,p2) in enumerate(others):
     if basis=='u':factor=comb(2,nx)*(2 if n==0 and kind=='c' else 1)
     else:factor=comb(2,nx)*(2 if n==0 and kind=='c' else 1)*(1 if j==0 else 2)
     b=-Q(9,5)+(ell+ell2)*delta/2+q+q2
     assert b>-1,(ell,ell2,q,q2,b)
     val=p*p2*factor
     groups[b]=groups.get(b,arb_poly([]))+val
  print('grouped',basis,nx,flush=True)
 return {b:p*(Z if basis=='t' else OM) for b,p in groups.items()},facts

def integrate_t(groups,N):
 w,e=cn.weight_poly(N);wp=convert(w);S=arb(0);T=arb(0)
 for idx,(b,p) in enumerate(sorted(groups.items())):
  pw=p*wp;bet=[1/aq(b+1)]
  for n in range(1,max(p.degree(),pw.degree())+1):bet.append(bet[-1]*n/aq(b+n+1))
  S+=sum((a*bet[n] for n,a in enumerate(p.coeffs())),arb(0))
  T+=sum((a*bet[n] for n,a in enumerate(pw.coeffs())),arb(0))
  if idx%10==0:print('integrated t',idx,len(groups),flush=True)
 return S,T,aq(e)

def integrate_u(groups,N):
 # Independent monomial antiderivatives and independently formed weight series.
 wp=arb_poly([]);z=arb_poly([aq(Q(3,5)),aq(-Q(6,5))]);p=ONE;coef=Q(1)
 for n in range(N+1):
  if n:coef*= (Q(4,5)-n+1)/n;p*=z
  wp+=p*aq(coef)
 nex=coef*(Q(4,5)-N)/(N+1);e=abs(nex)*Q(3,5)**(N+1)/Q(2,5)
 S=arb(0);T=arb(0)
 for idx,(b,p) in enumerate(sorted(groups.items())):
  S+=sum((a/aq(b+n+1) for n,a in enumerate(p.coeffs())),arb(0))
  T+=sum((a/aq(b+n+1) for n,a in enumerate((p*wp).coeffs())),arb(0))
  if idx%10==0:print('integrated u',idx,len(groups),flush=True)
 return S,T,aq(e)

def bound(S,T,eps):
 assert S>0
 lo=T-eps*S;hi=T+eps*S
 pref=arb.pi()/2*aq(Q(5,2))**aq(Q(4,5))
 assert lo>0
 return (pref*lo).sqrt(),(pref*hi).sqrt()

def evaluate(D,delta,xq,yq):
 r2=xq*xq+yq*yq;t=aq(r2/(1+r2));r=aq(r2).sqrt();z=(1-t)**(aq(delta)/2)
 maxn=max(n for fs in D.values() for ell,kind,n in fs)
 co=[arb(1),aq(xq)/r];si=[arb(0),aq(yq)/r]
 for n in range(2,maxn+1):co.append(2*co[1]*co[-1]-co[-2]);si.append(2*co[1]*si[-1]-si[-2])
 vals={}
 for (d,nx),fs in D.items():
  v=sum((z**ell*p(t)*(co[n] if kind=='c' else si[n]) for (ell,kind,n),p in fs.items()),arb(0))
  fac=(1-t)**aq(Q(d-1,2))
  if d%2==0:fac*=t.sqrt()
  vals[nx,d-nx]=v*fac
 return vals

def run(name,prec):
 ctx.prec=prec;start=time.monotonic();c,A,sha,rawsha,D=construct(name);delta=1-1/c
 gt,facts=group(D,delta,'t');s,t,e=integrate_t(gt,56);lo,hi=bound(s,t,e)
 print('T RESULT',lo.str(55),hi.str(55),'seconds',time.monotonic()-start,flush=True)
 gu,_=group(D,delta,'u');ss,tt,ee=integrate_u(gu,56);l2,h2=bound(ss,tt,ee)
 assert s.overlaps(ss) and t.overlaps(tt) and lo.overlaps(l2) and hi.overlaps(h2)
 checks=[]
 for xs,ys in [('0','1/10'),('1','0'),('1/2','1/2'),('1','2'),('3','1'),('60','80'),('0','1000')]:
  x,y=Q(xs),Q(ys);pv=evaluate(D,delta,x,y);cv=au.direct_F(A,c,aq(x),aq(y))
  ok={str(k):v.is_finite() and cv[k].is_finite() and v.overlaps(cv[k]) for k,v in pv.items()}
  assert all(ok.values()),(xs,ys,ok)
  checks.append({'point':[xs,ys],'components':ok});print('Cartesian',xs,ys,'PASS',flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':name,'precision_bits':prec,'canonical_sha256':sha,'source_record_sha256':rawsha,'method':'Arb polynomial integration; t-beta and independent ordered-pair u-monomial integration; 7 Cartesian checks','hessian_lower_ball':lo.str(80),'hessian_upper_ball':hi.str(80),'lower_endpoint':str(lo.lower()),'upper_endpoint':str(hi.upper()),'u_lower_ball':l2.str(80),'u_upper_ball':h2.str(80),'base_integral':s.str(80),'weighted_integral':t.str(80),'epsilon':e.str(80),'structural_endpoint_factors':facts,'cartesian_checks':checks,'seconds':time.monotonic()-start,'verdict':'PENDING_PROOF_AUDIT'}
 (HERE/(name+'_arb_hessian.json')).write_text(json.dumps(out,indent=2)+'\n')
 print('DONE',out['seconds'],lo.str(55),hi.str(55),flush=True)
if __name__=='__main__':run(sys.argv[1] if len(sys.argv)>1 else 'algebraic_n12_m10_k8',int(sys.argv[2]) if len(sys.argv)>2 else 1024)
