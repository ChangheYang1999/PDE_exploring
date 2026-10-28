from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from functools import lru_cache
from math import comb
import json,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
root=Path(__file__).resolve().parents[3];here=Path(__file__).parent

def clean(d):return {k:v for k,v in d.items() if v}
def add(d,kind,n,k,v):
 if n<0:
  n=-n
  if kind=='s':v=-v
 if kind=='s' and not n:return
 key=kind,n,k;d[key]=d.get(key,Q(0))+v

def deriv(D,p,d,axis):
 out={}
 for (kind,n,k),v in D.items():
  z=2*k-d;u=p-k
  if axis=='x':
   add(out,kind,n+1,k,v*(z-n)/2);add(out,kind,n-1,k,v*(z+n)/2)
   add(out,kind,n+1,k+1,v*u);add(out,kind,n-1,k+1,v*u)
  elif kind=='c':
   add(out,'s',n+1,k,v*(z-n)/2);add(out,'s',n-1,k,-v*(z+n)/2)
   add(out,'s',n+1,k+1,v*u);add(out,'s',n-1,k+1,-v*u)
  else:
   add(out,'c',n-1,k,v*(z+n)/2);add(out,'c',n+1,k,-v*(z-n)/2)
   add(out,'c',n-1,k+1,v*u);add(out,'c',n+1,k+1,-v*u)
 return clean(out)

@lru_cache(None)
def cheb(n,kind):
 if n==0:return (1,)
 if n==1:return (0,1 if kind=='T' else 2)
 x,y=cheb(n-1,kind),cheb(n-2,kind);out=[0]*(n+1)
 for k,v in enumerate(x):out[k+1]+=2*v
 for k,v in enumerate(y):out[k]-=v
 return tuple(out)

def recover(name):
 src=root.parent/f's1-num/research/data/{name}.json';raw=src.read_bytes();s=json.loads(raw);c=Q(s['cl']);a={}
 for g in s['generators']:
  j,m,v,sp=g['j'],g['m'],Q(g['coef']),g['spec']
  if sp[0]=='mono':terms={m+sp[1]:v}
  else:
   assert sp[0]=='leg';w,n=sp[1:];terms={m+w+h:v*(-1)**(n-h)*comb(n,h)*comb(n+h,h) for h in range(n+1)}
  for k,vv in terms.items():a[j,m,k]=a.get((j,m,k),Q(0))+vv
 a=clean(a);oldpath=root/f'research/19_nb_candidates/verification/{name}.audit.json';old=json.loads(oldpath.read_text())
 assert sha256(raw).hexdigest()==old['source_sha256']
 assert sorted(a)==list(map(tuple,old['canonical_order'])) and [a[k] for k in sorted(a)]==list(map(Q,old['canonical_coefficients']))
 # Fraction-style strings are used by the previous canonical hash, with integer denominators omitted.
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(a.items()))+'\n';digest=sha256(serial.encode()).hexdigest()
 assert digest==old['canonical_sha256']
 return c,a,src,sha256(raw).hexdigest(),digest

def main(name):
 start=time.monotonic();c,a,src,sha,digest=recover(name);delta=1-1/c;polys={};fourier={};degrees={}
 for j in range(6):
  p=(3+1/c-j*delta)/2;base={('c',2*m,k):v for (jj,m,k),v in a.items() if jj==j}
  for label,axes in [('chi22','xxyy'),('chi04','yyyy'),('chi31','xxxy'),('chi13','xyyy'),('e','xy')]:
   D=base
   for d,ax in enumerate(axes):D=deriv(D,p,d,ax)
   if label=='e':D={('c',n,k):-n*v for (kind,n,k),v in D.items() if n};assert all(kind=='s' for kind,n,k in deriv(deriv(base,p,0,'x'),p,1,'y'))
   P={};F={}
   for (kind,n,k),v in D.items():
    assert n%2==0 and k>=2,(j,label,kind,n,k)
    assert kind==('s' if label in ['chi31','chi13'] else 'c')
    F[k-2,n//2]=F.get((k-2,n//2),Q(0))+v
    C=cheb(n//2-1,'U') if kind=='s' else cheb(n//2,'T')
    for l,cc in enumerate(C):P[k-2,l]=P.get((k-2,l),Q(0))+v*cc
   P=clean(P);F=clean(F);polys[f'{label}_{j}']=[[i,k,str(v)] for (i,k),v in sorted(P.items())];fourier[f'{label}_{j}']=[[i,k,str(v)] for (i,k),v in sorted(F.items())]
   degrees[f'{label}_{j}']=[max((i for i,k in P),default=0),max((k for i,k in P),default=0)]
  print(name,'branch',j,'seconds',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'name':name,'cl':str(c),'delta':str(delta),'source':str(src),'source_sha256':sha,'canonical_sha256':digest,'polynomials':polys,'fourier_polynomials':fourier,'degrees':degrees,'proof_sha256':sha256((here.parent/'PROOF.md').read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 (here/f'{name}.polynomials.json').write_text(json.dumps(out,indent=2)+'\n');print(name,'BUILT',out['seconds'],flush=True)
if __name__=='__main__':
 for name in sys.argv[1:] or ['nb_d2_exact']:main(name)
