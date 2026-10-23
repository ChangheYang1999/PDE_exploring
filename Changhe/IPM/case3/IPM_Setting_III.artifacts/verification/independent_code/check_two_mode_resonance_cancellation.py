#!/usr/bin/env python3
"""Own exact two-algebra full-polynomial cancellation test, with no external code imports."""
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time,resource
resource.setrlimit(resource.RLIMIT_AS,(512*1024**2,512*1024**2))
resource.setrlimit(resource.RLIMIT_CPU,(40,40))
start=time.monotonic();out=Path('research/two_mode_resonance_cancellation/verification');counts={}
assert(out/'PROOF_WRITTEN_BEFORE_CODE.txt').exists()
def ck(b,g):
 counts[g]=counts.get(g,0)+1
 if not b:raise AssertionError(g)
def clean(a):return{k:v for k,v in a.items() if v}
def accum(a,k,v):a[k]=a.get(k,F())+v
def add(a,b):
 r=dict(a)
 for k,v in b.items():accum(r,k,v)
 return clean(r)
def scl(a,c):return clean({k:v*c for k,v in a.items()})
def sineput(a,e,n,v):
 if n and e<=MAXE:accum(a,(e,abs(n)),v if n>0 else -v)
def rdx(a,s):
 r={}
 for (e,n),v in a.items():
  sineput(r,e,n+1,v*(s-n)/2);sineput(r,e,n-1,v*(s+n)/2)
 return clean(r)
def rB(h,a,si,sj):
 r={}
 for (e,m),v in h.items():
  for (f,n),w in a.items():
   if e+f>MAXE:continue
   sineput(r,e+f,n+m,v*w*((si+1)*n-m*sj)/2)
   sineput(r,e+f,n-m,-v*w*((si+1)*n+m*sj)/2)
 return clean(r)
def toC(a):
 r={}
 for (e,n),v in a.items():r[e,n]=-v/2;r[e,-n]=v/2
 return clean(r)
# Separately expressed Cartesian derivatives and epsilon-Laurent convolution.
def derivative(a,q,axis):
 r={}
 for (e,n),v in a.items():
  if axis==0:shifts=((1,q-n),(-1,q+n))
  else:shifts=((1,n-q),(-1,n+q))
  for dn,f in shifts:accum(r,(e,n+dn),v*f/2)
 return clean(r)
def conv(a,b):
 r={}
 for (e,n),v in a.items():
  for (f,m),w in b.items():
   if e+f<=MAXE:accum(r,(e+f,n+m),v*w)
 return clean(r)
def cB(h,a,si,sj):
 return add(conv(derivative(h,si+1,1),derivative(a,sj,0)),scl(conv(derivative(h,si+1,0),derivative(a,sj,1)),-1))
def inverse(g,s):
 r={}
 for (e,n),v in g.items():
  den=n*n-(s+1)**2
  ck(bool(den),'nonzero_inverse_denominator')
  r[e,n]=v/den
 return clean(r)
def ser(a):return{f'{e},{n}':str(v) for (e,n),v in sorted(a.items())}
from math import gcd,lcm

def trim(a):
 a=list(a)
 while a and not a[-1]:a.pop()
 return a

def divrem(a,b):
 a=trim(a);b=trim(b);assert b;q=[F()] * max(0,len(a)-len(b)+1)
 while len(a)>=len(b):
  k=len(a)-len(b);v=a[-1]/b[-1];q[k]+=v
  for j,w in enumerate(b):a[k+j]-=v*w
  a=trim(a)
 return trim(q),a

def pmul(a,b):
 r=[F()] * max(0,len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):r[i+j]+=v*w
 return trim(r)

def padd(a,b):return trim([(a[i] if i<len(a) else F())+(b[i] if i<len(b) else F()) for i in range(max(len(a),len(b)))])

def primitive(a):
 a=trim(a)
 if not a:return []
 d=lcm(*(v.denominator for v in a));ints=[int(v*d) for v in a];gc=0
 for v in ints:gc=gcd(gc,abs(v))
 return [F(v,gc) for v in ints]

def peval(a,x):
 v=F()
 for w in reversed(a):v=v*x+w
 return v

def sign(v):return (v>0)-(v<0)

def variation(ss):
 ss=[s for s in ss if s];return sum(a!=b for a,b in zip(ss,ss[1:]))

def sturm(a):
 a=primitive(a);seq=[a,primitive([i*v for i,v in enumerate(a)][1:])]
 while len(seq[-1])>1:
  q,r=divrem(seq[-2],seq[-1]);ck(padd(pmul(q,seq[-1]),r)==seq[-2],'polynomial_division_identity')
  if not r:break
  nxt=primitive([-v for v in r]);factor=nxt[-1]/(-r[-1]);ck(factor>0 and nxt==[-v*factor for v in r],'positive_sturm_normalization');seq.append(nxt)
 ck(len(seq[-1])==1 and bool(seq[-1][0]),'square_free_polynomial')
 return seq

pure=json.loads((out/'PURE150_EXACT.json').read_text());results=[]
for ell,K,M,brackets in ((F(3),5,2,[(F(28,100),F(29,100)),(F(64,100),F(65,100))]),(F(5,2),9,4,[(F(65,1000),F(67,1000)),(F(108,1000),F(110,1000)),(F(350,1000),F(352,1000)),(F(593,1000),F(595,1000))])):
 MAXE=K+1;N=3;p=1/ell;delta=1-p;s=[p-k*delta for k in range(K+1)]
 rp=[{(0,1):F(1),(1,N):F(1)}];cp=[{(0,1):F(-1,2),(0,-1):F(1,2),(1,N):F(-1,2),(1,-N):F(1,2)}];rh=[];ch=[];steps=[]
 for k in range(K+1):
  if k:
   r={};c={}
   for i in range(k):
    j=k-1-i;r=add(r,rB(rh[i],rp[j],s[i],s[j]));c=add(c,cB(ch[i],cp[j],s[i],s[j]))
   rp.append(scl(r,1/(ell*k*delta)));cp.append(scl(c,1/(ell*k*delta)))
  ck(toC(rp[k])==cp[k],'density_two_algebras')
  for (e,n) in rp[k]:ck(n>0 and n%2==1 and 0<=e<=k+1 and n<=4*k+3,'density_support')
  rg=rdx(rp[k],s[k]);cg=derivative(cp[k],s[k],0);ck(toC(rg)==cg,'source_two_algebras')
  if k<K:
   rh.append(inverse(rg,s[k]));ch.append(inverse(cg,s[k]));ck(toC(rh[k])==ch[k],'stream_two_algebras')
   q=s[k]+1;neg_lap=add(scl(derivative(derivative(ch[k],q,0),q-1,0),-1),derivative(derivative(ch[k],q,1),q-1,1));ck(neg_lap==cg,'Cartesian_Poisson')
  steps.append(dict(k=k,s=str(s[k]),density=ser(rp[k]),source=ser(rg),stream=ser(rh[k]) if k<K else None))
 g=trim([rg.get((e,M),F()) for e in range(MAXE+1)]);ck(len(g)==K+2,'full_polynomial_degree')
 ck(str(g[0])==next(row for row in pure['cases'] if F(row['ell'])==ell)['g_star_at_A1'],'pure_constant')
 seq=sturm(g);vsminus=variation([sign(a[-1])*(-1)**(len(a)-1) for a in seq]);vsplus=variation([sign(a[-1]) for a in seq]);vzero=variation([sign(a[0]) for a in seq]);vone=variation([sign(peval(a,F(1))) for a in seq]);intervals=[]
 for left,right in brackets:
  gl,gr=peval(g,left),peval(g,right);ck(gl*gr<0,'opposite_endpoint_signs')
  vl=variation([sign(peval(a,left)) for a in seq]);vr=variation([sign(peval(a,right)) for a in seq]);ck(vl-vr==1,'exactly_one_root_in_bracket')
  ol,orr=left,right
  for z in range(40):
   mid=(left+right)/2;gm=peval(g,mid)
   ck(bool(gm),'bisection_nonzero')
   if gm*gl>0:left=mid;gl=gm
   else:right=mid;gr=gm
  ck(gl*gr<0 and right-left==(orr-ol)/2**40,'refined_rational_bracket')
  intervals.append(dict(initial=[str(ol),str(orr)],refined=[str(left),str(right)],g_values=[str(gl),str(gr)],sturm_variations=[vl,vr],midpoint_float=float((left+right)/2)))
 ck(vsminus-vsplus==len(brackets),'all_real_roots_accounted')
 ck(vzero-vone==len(brackets),'all_roots_in_0_1')
 results.append(dict(ell=str(ell),K=K,M=M,N=N,g_coefficients=[str(v) for v in g],g_primitive_integer=[str(v) for v in primitive(g)],sturm_sequence=[[str(v) for v in a] for a in seq],sturm_variations=dict(minus_infinity=vsminus,zero=vzero,one=vone,plus_infinity=vsplus),root_brackets=intervals,steps=steps))
res=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='PASS',checks=sum(counts.values()),counts=counts,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,proof_sha256=hashlib.sha256((out.parent/'PROOF.md').read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),cases=results,scope='Exact trace coefficient polynomial and roots, no realized profile or all-order log cancellation')
(out/'EXACT_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='cases'},indent=2))
for row in results:print(json.dumps({k:v for k,v in row.items() if k in ('ell','g_coefficients','sturm_variations','root_brackets')},indent=2))
