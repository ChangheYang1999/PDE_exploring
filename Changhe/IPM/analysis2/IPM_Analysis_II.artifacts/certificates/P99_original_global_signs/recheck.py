"""Direct power-polynomial restriction; independent of the adaptive evaluator."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import sys,json,time
from flint import arb,arb_mat,ctx
here=Path(__file__).parent;root=here.parents[2];ctx.prec=448

def A(v):
 q=F(v);return arb(q.numerator)/q.denominator

def polys(d,kind,target):
 p={(l,j):{(i,k):F(v) for i,k,v in d['polynomials'][f'{l}_{j}']} for l in ['chi22','chi04','chi31','chi13','e'] for j in range(4)}
 c=F(d['cl']);out={(l,j):{} for l in ['a','b','q'] for j in range(5)}
 def add(l,j,P,f,shift=0):
  for (i,k),v in P.items():out[l,j][i+shift,k]=out[l,j].get((i+shift,k),F(0))+f*v
 if kind=='M':const=2*c+1-target;linear=0
 elif kind=='B1':const=1-target;linear=0
 elif kind=='B2':const=1-c-target;linear=3+c/5-3*target
 elif kind=='B3':const=1-2*c-target;linear=3-F(14,5)*c-3*target
 elif kind in ['A','symDU']:const=target;linear=0
 else:const=-target;linear=0
 for l in ['a','b']:
  out[l,0][0,0]=const
  if linear:out[l,0][1,0]=linear
 for j in range(4):
  if kind=='M':terms=[('a','chi22',-2),('a','chi04',-1),('b','chi22',1),('q','chi31',1)]
  elif kind=='B1':terms=[('a','chi04',-1),('b','chi22',-1),('q','chi13',1)]
  elif kind in ['B2','B3']:
   k=2 if kind=='B2' else 3
   terms=[('a','chi22',k-1),('a','chi04',-1),('b','chi22',-k),('q','chi31',F(1-k,2)),('q','chi13',F(k+1,2))]
  elif kind=='symDU':terms=[('a','chi22',1),('b','chi22',-1),('q','chi13',F(1,2)),('q','chi31',-F(1,2))]
  elif kind=='A':terms=[('a','chi22',-1),('a','chi04',-1),('q','chi31',F(1,2)),('q','chi13',F(1,2))]
  else:terms=[('a','chi22',-1),('a','chi04',-1),('b','chi22',-1),('b','chi04',-1)]
  for l,label,f in terms:
   add(l,j if kind=='rho_scaled' else j+1,p[label,j],f)
   if kind in ['B2','B3']:add(l,j+1,p[label,j],3*f,1)
  if kind in ['B2','B3']:
   for l in ['a','b']:add(l,j+1,p['e',j],F(16,5),1)
 return {k:{q:v for q,v in P.items() if v} for k,P in out.items()}

@lru_cache(None)
def T(n,lo,hi):
 lo,hi=F(lo),F(hi)
 # Direct closed-form restriction of powers to the cell's Bernstein basis.
 return arb_mat([[A(sum((F(comb(k,l)*comb(i,l),comb(n,l))*lo**(k-l)*(hi-lo)**l for l in range(min(k,i)+1)),F(0))) for k in range(n+1)] for i in range(n+1)])

def endpoints(path,root_t):
 tl,th=map(F,root_t);zl,zh=F(-1),F(1)
 for letter in path:
  if letter=='t':th=(tl+th)/2
  elif letter=='T':tl=(tl+th)/2
  elif letter=='z':zh=(zl+zh)/2
  elif letter=='Z':zl=(zl+zh)/2
  else:raise ValueError(letter)
 return tl,th,zl,zh

def complete(paths,prefix=''):
 if prefix in paths:
  assert not any(p.startswith(prefix) and p!=prefix for p in paths);return
 nxt={p[len(prefix)] for p in paths if p.startswith(prefix)}
 assert nxt in [{'t','T'},{'z','Z'}],(prefix,nxt)
 for q in sorted(nxt):complete(paths,prefix+q)

def run(name):
 start=time.monotonic();src=here/name;d=json.loads(src.read_text());assert d['status']=='COMPLETE'
 ppath=root/'research/96_original_auxiliary_recomputation/verification/polynomials.json';data=json.loads(ppath.read_text());assert sha256(ppath.read_bytes()).hexdigest()==d['source_sha256'];S=polys(data,d['kind'],F(d['target']));nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p)
 P={}
 for key,poly in S.items():
  m=arb_mat(nt+1,nz+1)
  for (i,k),v in poly.items():m[i,k]=A(v)
  P[key]=m
 paths={v['path'] for v in d['accepted']};assert len(paths)==len(d['accepted']);complete(paths)
 delta=F(data['delta']);worst=arb(100);records=[]
 for cell in d['accepted']:
  tl,th,zl,zh=endpoints(cell['path'],d['root_t']);assert list(map(str,[tl,th]))==cell['t'] and list(map(str,[zl,zh]))==cell['z']
  left=T(nt,str(tl),str(th));right=T(nz,str(zl),str(zh)).transpose();wl=(1-A(th))**A(delta/2);wh=(1-A(tl))**A(delta/2)
  W=arb_mat([[sum((A(F(comb(n,k)*comb(i,k),comb(4,k)))*wl**(n-k)*(wh-wl)**k for k in range(min(n,i)+1)),arb(0)) for n in range(5)] for i in range(5)])
  ranges={}
  for label in ['a','b','q']:
   mat=arb_mat([(left*P[label,j]*right).entries() for j in range(5)]);vals=(W*mat).entries();low=vals[0];high=vals[0]
   for v in vals[1:]:low=low.min(v);high=high.max(v)
   ranges[label]=low.lower(),high.upper()
  x,y=ranges['a'][0],ranges['b'][0];qlo,qhi=ranges['q'];m=min(abs(zl),abs(zh)) if not zl<=0<=zh else F(0);off=abs(qlo).max(abs(qhi))*(1-A(m)**2).sqrt()
  lower=((x+y-((x-y)**2+4*off**2).sqrt())/2).max(x.min(y)-off);assert lower>=0,(name,cell['path'],lower)
  worst=worst.min(lower);records.append({'path':cell['path'],'lower':lower.str(75),'pass':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'kind':d['kind'],'target':d['target'],'root_t':d['root_t'],'precision_bits':ctx.prec,'leaves':len(records),'direct_restriction_rows':records,'worst':worst.str(80),'primary_sha256':sha256(src.read_bytes()).hexdigest(),'polynomials_sha256':sha256(ppath.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 dest=src.with_name(src.stem+'.recheck.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],name,len(records),'PASS',out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:]:run(name)
