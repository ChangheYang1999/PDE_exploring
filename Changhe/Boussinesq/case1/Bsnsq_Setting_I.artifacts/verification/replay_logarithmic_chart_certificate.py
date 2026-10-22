"""Standalone rational replay. Imports no certificate generator or field evaluator.
Root identity: two integer power-basis expansions; subdivision: de Casteljau.
Interval implementation and exponential enclosure are separate from producer.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb,factorial,lcm
from functools import lru_cache
import argparse,datetime,hashlib,json,time
import numpy as np
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat()
def interval(a,b=None):return (Q(a),Q(a if b is None else b))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def sub(a,b):return add(a,neg(b))
def mul(a,b):
 p=[u*v for u in a for v in b];return min(p),max(p)
def div(a,b):
 assert not b[0]<=0<=b[1]
 return mul(a,(1/b[1],1/b[0]))
def power(a,n):
 assert n>=0
 if n==0:return interval(1)
 if n%2:return a[0]**n,a[1]**n
 return (0 if a[0]<=0<=a[1] else min(a[0]**n,a[1]**n),max(a[0]**n,a[1]**n))
def scale(a,s):return mul(a,interval(s))
def total(*a):
 s=interval(0)
 for b in a:s=add(s,b)
 return s
def round_out(a,bits=176):
 d=2**bits
 return Q((a[0]*d).__floor__(),d),Q((a[1]*d).__ceil__(),d)
@lru_cache(maxsize=16384)
def exponential(u):
 assert u>=0 and u<102
 # Independent direct powers and factorials, not the producer recurrence.
 s=sum((u**j/Q(factorial(j)) for j in range(101)),Q(0))
 r=u**101/Q(factorial(101))/(1-u/102)
 return round_out((s,s+r))
@lru_cache(maxsize=8192)
def compact_factors(alpha,tl,th):
 ea=exponential(alpha);den=sub(interval(1),div(interval(1),ea));assert den[0]>0
 eb=(exponential(alpha*tl)[0],exponential(alpha*th)[1])
 tval=div(sub(interval(1),div(interval(1),eb)),den)
 tval=round_out((max(Q(0),tval[0]),min(Q(1),tval[1])))
 ell=round_out(scale(sub(eb,interval(1)),-1/(6*alpha)))
 ell2=round_out(scale(mul(eb,sub(eb,interval(1))),1/(36*alpha)))
 return tval,ell,ell2

def shifted_cheb_power(n):
 if not n:return [1]
 out=[0]*(n+1)
 # Closed power formula T_n(z), expanded at z=2t-1.
 for k in range(n//2+1):
  j=n-2*k;v=Q(n*factorial(n-k-1)*(-1)**k*2**j,2*factorial(k)*factorial(j))
  for r in range(j+1):out[r]+=v*comb(j,r)*2**r*(-1)**(j-r)
 assert all(Q(a).denominator==1 for a in out)
 return list(map(int,out))
def compose_tensor(a,u,v):
 # columns of u and v are power coefficients of basis functions.
 n,m=len(a),len(a[0])
 tmp=[[sum(u[r][i]*a[i][j] for i in range(n)) for j in range(m)] for r in range(n)]
 return [[sum(tmp[r][j]*v[s][j] for j in range(m)) for s in range(m)] for r in range(n)]
def root_identity(c,b,d):
 n,m=len(c)-1,len(c[0])-1;dc=1
 for row in c:
  for a in row:dc=lcm(dc,a.denominator)
 cp=[[shifted_cheb_power(i) for i in range(n+1)],[shifted_cheb_power(j) for j in range(m+1)]]
 mats=[[[p[i][r] if r<len(p[i]) else 0 for i in range(len(p))] for r in range(len(p))] for p in cp]
 lhs=compose_tensor([[int(a*dc) for a in row] for row in c],*mats)
 bm=[]
 for degree in [n,m]:
  bm.append([[comb(degree,i)*comb(degree-i,r-i)*(-1)**(r-i) if r>=i else 0 for i in range(degree+1)] for r in range(degree+1)])
 rhs=compose_tensor(b,*bm)
 assert all(lhs[i][j]*d==rhs[i][j]*dc for i in range(n+1) for j in range(m+1)), 'Root polynomial identity failed'
 return (n+1)*(m+1)
def bisect_curve(a):
 n=len(a)-1;left=[];right=[];level=list(a)
 for k in range(n+1):
  left.append(level[0]*2**(n-k));right.append(level[-1]*2**(n-k))
  level=[level[i]+level[i+1] for i in range(len(level)-1)]
 return left,right[::-1]
def bisect(b,d,axis):
 if axis==0:
  cols=[bisect_curve(list(v)) for v in zip(*b)]
  return [list(v) for v in zip(*(c[0] for c in cols))],[list(v) for v in zip(*(c[1] for c in cols))],d*2**(len(b)-1)
 r=[bisect_curve(a) for a in b]
 return [a[0] for a in r],[a[1] for a in r],d*2**(len(b[0])-1)
def derivative_bound(b,d,i,j,ht,hw):
 a=b;factor=Q(1,d)
 for _ in range(i):
  n=len(a)-1
  if n==0:return interval(0)
  factor*=n/ht;a=[[a[k+1][l]-a[k][l] for l in range(len(a[0]))] for k in range(n)]
 for _ in range(j):
  m=len(a[0])-1
  if m==0:return interval(0)
  factor*=m/hw;a=[[r[l+1]-r[l] for l in range(m)] for r in a]
 return min(min(r) for r in a)*factor,max(max(r) for r in a)*factor

def lower(b,d,bounds,alpha):
 tl,th,wl,wh=bounds;T,ell,ell2=compact_factors(alpha,tl,th)
 if T[0]**6+wl**3>1:return 'outside',None
 v=power(interval(wl,wh),3);z=sub(sub(interval(1),power(T,6)),v)
 z=(max(Q(0),z[0]),min(Q(1),z[1]));assert z[0]<=z[1]
 w=interval(wl,wh);zv=mul(z,v)
 c0=total(interval(1),scale(add(scale(z,2),scale(v,6)),Q(1,3)),scale(zv,Q(-8,3)))
 cw=mul(w,total(interval(2),scale(z,Q(-2,3)),scale(v,-2),scale(zv,Q(8,3))))
 cww=scale(mul(mul(z,sub(interval(1),v)),power(w,2)),Q(-4,3))
 ct=add(mul(total(scale(z,2),scale(v,6),scale(zv,-4)),ell),scale(mul(zv,ell2),12))
 ctw=scale(mul(mul(mul(z,w),ell),sub(interval(1),scale(v,2))),4)
 ctt=scale(mul(zv,power(ell,2)),12)
 coeff=[c0,cw,cww,ct,ctw,ctt];orders=[(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)]
 r=total(*(mul(a,derivative_bound(b,d,i,j,th-tl,wh-wl)) for a,(i,j) in zip(coeff,orders)))
 return 'positive',r[0]

def coverage(leaves):
 trie={}
 for leaf in leaves:
  cur=trie
  for k,ch in enumerate(leaf['path']):
   assert ch in ('01' if k%2==0 else '23'),'Wrong split symbol'
   assert 'leaf' not in cur,'Nested leaf'
   cur=cur.setdefault(ch,{})
  assert not cur,'Duplicate leaf or leaf containing descendants'
  cur['leaf']=leaf
 def check(t,depth):
  if 'leaf' in t:assert len(t)==1;return 1
  a,b='01' if depth%2==0 else '23'
  assert set(t)=={a,b},'Incomplete coverage'
  return check(t[a],depth+1)+check(t[b],depth+1)
 return trie,check(trie,0)

def replay(folder,delta=Q(1,100000),manufacture=False,expected_source_sha=None):
 start=time.monotonic();folder=Path(folder);inp=json.loads((folder/'input.json').read_text());cert=json.loads((folder/'certificate.json').read_text())
 assert cert['input_sha256']==sha(folder/'input.json') and cert['remaining']==0
 c=[[Q(v) for v in row] for row in inp['coefficients']];b=[[int(v) for v in row] for row in inp['bernstein_numerators']];d=int(inp['denominator']);alpha=Q(inp['alpha'])
 assert alpha>0 and d>0 and delta>0
 assert len(b)==len(c) and all(len(v)==len(c[0]) for v in b)
 source=None
 if not manufacture:
  assert expected_source_sha is not None and len(expected_source_sha)==64, 'Require pinned source SHA for candidate replay'
  assert (folder/'source.json').is_file(), 'Candidate requires source metadata'
 if (folder/'source.json').exists():
  source=json.loads((folder/'source.json').read_text());p=Path(source['source']);assert sha(p)==source['source_sha256']
  if expected_source_sha is not None:assert source['source_sha256']==expected_source_sha
  with np.load(p,allow_pickle=False) as a:
   assert int(a['J'])==len(c)-1 and int(a['Kw'])==len(c[0])-1
   raw=np.asarray(a['c']);assert raw.dtype==np.dtype('float64') and raw.ndim==1 and raw.shape==(len(c)*len(c[0]),) and raw.flags.c_contiguous
   assert 'gam' not in a.files or float(a['gam'])==0, 'Angular remap not covered'
   cc=raw.reshape(len(c),len(c[0]),order='C');assert [[Q.from_float(float(v)) for v in row] for row in cc]==c
   assert alpha==Q.from_float(float(a['alpha'])) and int(a['m'])==3 and float(a['beta'])==3
   assert Q(source['se_exact_binary64'])==Q.from_float(float(a['se'])) if 'se' in a.files else Q(source['se_exact_binary64'])==1
 nidentity=root_identity(c,b,d);trie,nleaf=coverage(cert['leaves'])
 stack=[(trie,b,d,(Q(0),Q(1),Q(0),Q(1)),0)];done=0;outside=0;actual=None
 while stack:
  tree,b,d,bo,depth=stack.pop()
  if 'leaf' in tree:
   item=tree['leaf'];kind,low=lower(b,d,bo,alpha)
   if item['kind']=='outside':assert kind=='outside';outside+=1
   else:
    assert kind=='positive' and low>=delta,(item['path'],str(low),str(delta))
    assert Q(item['lower'])>=Q(cert['lower_bound'])>=delta
    actual=low if actual is None else min(actual,low)
   done+=1
   if done%128==0:print(json.dumps({'utc':now(),'replayed':done,'total':nleaf,'seconds':time.monotonic()-start}),flush=True)
   continue
  axis=depth%2;l,r,dd=bisect(b,d,axis);bounds=list(bo);a='01' if axis==0 else '23';mid=(bo[2*axis]+bo[2*axis+1])/2
  lo=bounds.copy();hi=bounds.copy();lo[2*axis+1]=mid;hi[2*axis]=mid
  stack.extend([(tree[a[1]],r,dd,tuple(hi),depth+1),(tree[a[0]],l,dd,tuple(lo),depth+1)])
 assert done==nleaf and actual>=delta
 result={'utc':now(),'seconds':time.monotonic()-start,'status':'CONFIRMED','claim':'Q>=delta over the entire compact physical domain; hence global smooth positive chart. No PDE/canonical-inverse claim.','delta':str(delta),'manufacture_mode':manufacture,'pinned_source_sha256':expected_source_sha,'source_path_base':str(Path.cwd()),'leaves':nleaf,'outside':outside,'positive':nleaf-outside,'coefficient_identities':nidentity,'source':source,'hashes':{str(p):sha(p) for p in [folder/'input.json',folder/'certificate.json',Path(__file__)]},'code_independence':'No producer imports. Closed Chebyshev expansion and Bernstein-to-power exact coefficient identity; dynamic de Casteljau; separate interval arithmetic and stronger exponential bounds.'}
 (folder/'replay.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));return result
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('folder');ap.add_argument('--delta',default='1/100000');ap.add_argument('--manufacture',action='store_true');ap.add_argument('--source-sha');a=ap.parse_args();replay(a.folder,Q(a.delta),a.manufacture,a.source_sha)
