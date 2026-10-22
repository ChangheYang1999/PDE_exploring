"""Exact source polynomials and independent iv particular-solution propagation."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from datetime import datetime,timezone
import json,re,hashlib,bisect,gzip,time
from flint import fmpq,fmpq_mat
from mpmath import iv
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_archive_second';iv.dps=200
SOURCE=B/'data_exact/modal_v2.json';ARCHIVE=B/'research/middle_residual/evidence/original_knots.jsonl.gz';ZPATH=B/'research/modal_repair/evidence/independent_gauss_iv.json'
SOURCE_SHA='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';ARCHIVE_SHA='c762afdbea381b750f2c9e382ef2315b2652df9781ccf69511237d944e102648'
def need(x,s):
 if not x:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def q(s):return fmpq(str(s))
def hx(s):
 m=re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]*)p([+-]?[0-9]+)',s);need(m is not None,'exact hex');sg,a,b,e=m.groups();return fmpq((-1 if sg=='-' else 1)*int(a+b,16))*fmpq(2)**(int(e)-4*len(b))
def ii(x):
 x=q(x);return iv.mpf(int(x.numerator))/iv.mpf(int(x.denominator))
def iep(t):
 s,m,e,b=t;need(b>=0,'finite iv endpoint');return fmpq((-1)**s*int(m))*fmpq(2)**int(e)
def ends(x):return tuple(map(iep,x._mpi_))
def box(x):return list(map(str,ends(x)))
def decode(x):
 need(set(x)=={'schema','mid_m','mid_e','rad_m','rad_e'} and x['schema']=='arb-dyadic-mid-radius-v1','serialized ball schema');m=fmpq(int(x['mid_m']))*fmpq(2)**int(x['mid_e']);r=fmpq(int(x['rad_m']))*fmpq(2)**int(x['rad_e']);need(r>=0,'radius');return m-r,m+r

def weights():
 out=[]
 for j in range(262):
  if j==0:w={0:fmpq(1,4),2:fmpq(-1,8)}
  elif j==1:w={0:fmpq(1,4),1:fmpq(1,8),2:fmpq(-1,8),3:fmpq(-1,8)}
  else:w={m:fmpq(s,8) for m,s in [(j-1,1),(j,1),(j+1,-1),(j+2,-1)] if 0<=m<260}
  out.append(w)
 independent=[{} for _ in range(262)]
 for m in range(260):
  for v in [1+2*m,1-2*m,3+2*m,3-2*m]:
   j=(abs(v)-1)//2;independent[j][m]=independent[j].get(m,fmpq(0))+fmpq(1 if v>0 else -1,8)
 independent=[{m:x for m,x in w.items() if x} for w in independent];need(independent==out and out[-1]=={},'two exact angular constructions');return out

def mul_affine(p,a,b):
 out=[fmpq(0)]*(len(p)+1)
 for i,v in enumerate(p):out[i]+=a*v;out[i+1]+=b*v
 return out

def basis(t,left,right):
 ell=bisect.bisect_right(t,left)-1;need(t[ell]==left<right==t[ell+1],'original span');h=right-left;previous={ell:[fmpq(1)]}
 for degree in range(1,8):
  current={}
  for i in range(ell-degree,ell+1):
   val=[fmpq(0)]*(degree+1);a=t[i+degree]-t[i];b=t[i+degree+1]-t[i+1]
   if a and i in previous:
    add=mul_affine(previous[i],(left-t[i])/a,h/a);val=[x+y for x,y in zip(val,add,strict=True)]
   if b and i+1 in previous:
    add=mul_affine(previous[i+1],(t[i+degree+1]-left)/b,-h/b);val=[x+y for x,y in zip(val,add,strict=True)]
   current[i]=val
  previous=current
 need([sum(previous[i][j] for i in previous) for j in range(8)]==[1]+[0]*7,'exact partition of unity');return ell,fmpq_mat([[previous[i][j] for i in range(ell-7,ell+1)] for j in range(8)])

def polynomials(src,si):
 a,b=src['knots'][si:si+2];ell,mat=basis(src['t'],a,b);local=fmpq_mat(src['Hcontrol'][ell-7:ell+1]);out=mat*local;need(out.nrows()==8 and out.ncols()==262 and all(out[k,261]==0 for k in range(8)),'exact polynomial shape/lastzero');return [[out[k,j] for k in range(8)] for j in range(262)]

def endpoint_jets(P,h,right):
 return [[sum((row[k]*fmpq(factorial(k),factorial(k-v)) for k in range(v,8)),fmpq(0))/h**v if right else row[v]*factorial(v)/h**v for v in range(7)] for row in P]

def source():
 need(sha(SOURCE)==SOURCE_SHA,'fixed exact source');raw=json.loads(SOURCE.read_text());ar=raw['arrays'];need(raw['degree']==7 and ar['S']['shape']==[260,1565] and ar['D']['shape']==[260,7] and ar['Aout']['shape']==[260,10] and ar['knots']['shape']==[1573],'all original dimensions');t=list(map(hx,ar['knots']['hex']));knots=sorted(set(t));need(len(t)==1573 and len(knots)==1559 and t[:8]==[t[0]]*8 and t[-8:]==[t[-1]]*8 and all(t[i]<t[i+1] for i in range(7,1565)),'clamped simple-knot source');sc={k:hx(v) for k,v in raw['scalars_hex'].items()};k,bi,bo=sc['k'],sc['bi'],sc['bo'];need(0<k<fmpq(1,2) and bi>4 and bo>4-2*k,'trial exponent hypotheses');W=weights()
 def array(name,n):
  v=list(map(hx,ar[name]['hex']));need(len(v)==260*n,'complete exact array');return [v[m*n:(m+1)*n] for m in range(260)]
 def converted(name,n):
  a=array(name,n);return [[sum((v*a[m][i] for m,v in w.items()),fmpq(0)) for i in range(n)] for w in W]
 H=converted('S',1565);Hd=converted('D',7);Ha=converted('Aout',10);jl=raw['outer_jl'];need(len(jl)==10 and jl[0]==[0,0] and all(len(v)==2 and all(type(x) is int and x>=0 for x in v) for v in jl),'outer index layout');alpha=[k-3-j*(1-k)-2*l for j,l in jl];need(all(x<-2 for x in alpha) and alpha[0]+bo>0,'exterior convergence');src={'t':t,'knots':knots,'sc':sc,'weights':W,'Hcontrol':list(map(list,zip(*H,strict=True))),'alpha':alpha};p0=polynomials(src,0);p1=polynomials(src,1557);jin=endpoint_jets(p0,knots[1]-knots[0],False);jout=endpoint_jets(p1,knots[-1]-knots[-2],True);I=[];U=[];V=[];anchor_checks=0
 for n in range(1,262):
  m=2*n;C=W[n-1].get(0,fmpq(0));d=Hd[n-1];pin=[(C if v==0 else 0)+sum((d[l]*(2*l+2)**v for l in range(7)),fmpq(0)) for v in range(7)];ein=[sum(((-bi)**(l-v)*(jin[n-1][v]-pin[v])/factorial(v)/factorial(l-v) for v in range(l+1)),fmpq(0)) for l in range(7)];I.append(C/(m+4)+sum((d[l]/(m+6+2*l)+ein[l]*(-1)**l*factorial(l)/(m+4+bi)**(l+1) for l in range(7)),fmpq(0)))
  C=W[n].get(0,fmpq(0));a=Ha[n];pout=[sum((a[l]*alpha[l]**v for l in range(10)),fmpq(0)) for v in range(7)];eo=[sum((bo**(l-v)*(jout[n][v]-pout[v])/factorial(v)/factorial(l-v) for v in range(l+1)),fmpq(0)) for l in range(7)];need(all(m-4-x>0 for x in alpha) and m-4+bo>0,'every tail denominator');U.append(sum((a[l]/(m-4-alpha[l]) for l in range(10)),fmpq(0))+sum((eo[l]*factorial(l)/(m-4+bo)**(l+1) for l in range(7)),fmpq(0)));v=C*(1/(m-4-alpha[0])-sum(((alpha[0]+bo)**l/(m-4+bo)**(l+1) for l in range(7)),fmpq(0)));need(v==C*(alpha[0]+bo)**7/((m-4-alpha[0])*(m-4+bo)**7),'exact geometric correction');V.append(v);anchor_checks+=1
  for j in range(7):
   need(pin[j]+sum((fmpq(factorial(j),factorial(j-l))*ein[l]*bi**(j-l) for l in range(j+1)),fmpq(0))==jin[n-1][j],'all reconstructed inner jets');need(pout[j]+sum((fmpq(factorial(j),factorial(j-l))*eo[l]*(-bo)**(j-l) for l in range(j+1)),fmpq(0))==jout[n][j],'all reconstructed outer jets');anchor_checks+=2
 z=json.loads(ZPATH.read_text())['values']['A00_correction'];zl,zh=q(z['lower_exact_dyadic']),q(z['upper_exact_dyadic']);need(zl<=zh,'normalization interval');Z=iv.mpf([ii(zl).a,ii(zh).b]);src.update(I0=I,U0=U,V0=V,Z=Z,Z_exact=list(map(str,[zl,zh])),anchor_checks=anchor_checks);need(anchor_checks==3915,'complete anchor checks');return src

def reverse_poly(P):
 return [sum((P[k]*comb(k,j)*(-1)**j for k in range(j,len(P))),fmpq(0)) for j in range(len(P))]

def step(y,P,h,lam):
 h,lam=q(h),q(lam);z=lam*h
 if z==0:return y+ii(h*sum((v/fmpq(k+1) for k,v in enumerate(P)),fmpq(0)))
 # Particular polynomial calculated exactly, then evaluated in outward iv.
 parts=[fmpq(0)]*(len(P)+1)
 for k in reversed(range(len(P))):parts[k]=((k+1)*parts[k+1]-h*P[k])/z
 return ii(sum(parts,fmpq(0)))+iv.exp(ii(z))*(y-ii(parts[0]))

def contain(value,target):
 lo,hi=ends(value);a,b=decode(target);need(a<=lo<=hi<=b,'candidate not contained in fixed archive ball');return min(lo-a,b-hi),(lo,hi),(a,b)

def exact_H_check(P,h,targets):
 need(len(targets)==262 and all(len(p)==8 for p in targets),'all archived H shapes');count=0;worst=None
 for j in range(262):
  for power in range(8):
   exact=sum((P[j][k]*comb(k,power)/fmpq(2)**(k-power) for k in range(power,8)),fmpq(0))/h**power;lo,hi=decode(targets[j][power]);need(lo<=exact<=hi,'exact source H not in archive');margin=min(exact-lo,hi-exact);count+=1
   if worst is None or margin<worst['margin']:worst={'mode':j,'power':power,'margin':margin,'exact':str(exact),'target':list(map(str,[lo,hi]))}
 worst['margin']=str(worst['margin']);return count,worst
