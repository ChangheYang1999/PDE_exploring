"""Exact rational images of sparse modal maps versus the frozen binary64 code."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,time,hashlib,argparse,math,random
from fractions import Fraction as F
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_certificate/evidence';sys.path.insert(0,str(E/'source'))
from cert_resid import Certifier
from midrad import MR
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rweights(j,M):
 if j<0 or j>M:return {}
 terms={0:2,2:-1} if j==0 else ({0:2,1:1,2:-1,3:-1} if j==1 else {j-1:1,j:1,j+1:-1,j+2:-1})
 return {m:F(w,8) for m,w in terms.items() if 0<=m<M}
def weights(kind,q,j,M,deg,alpha):
 z={}
 def add(qq,jj,f):
  if qq>deg:return
  for m,v in rweights(jj,M).items():z[(qq,m)]=z.get((qq,m),F())+f*v
 if kind=='R':add(q,j,F(1))
 elif kind=='dR':add(q,j,alpha+3);add(q+1,j,F(q+1))
 else:
  n=j+1;add(q,n-1,(alpha+4-2*n)/2);add(q,n,(alpha+4+2*n)/2);add(q+1,n-1,F(q+1,2));add(q+1,n,F(q+1,2))
 return {k:v for k,v in z.items() if v}
def image(w,mid,rad):
 m=sum((v*mid[k] for k,v in w.items()),F());r=sum((abs(v)*rad[k] for k,v in w.items()),F());return m-r,m+r

def audit_case(Tm,Tr,alpha,cache=None):
 deg,M=Tm.shape[0]-1,Tm.shape[1];C=Certifier.__new__(Certifier);C.M=M;C.Nf=M+1
 ft,rt=C.f_terms_from_a([(alpha,MR(Tm,Tr))]);outputs={'R':rt[0][1],'dR':rt[0][2],'F':MR(ft[0][1].m.T,ft[0][1].r.T)}
 mid={k:F(float(Tm[k])) for k in np.ndindex(Tm.shape)};rad={k:F(float(Tr[k])) for k in mid};am,ar=F(float(alpha.m)),F(float(alpha.r));ae=sorted(set([am-ar,am+ar]));count=0;min_ratio=math.inf
 for kind,out in outputs.items():
  assert np.isfinite(out.m).all() and np.isfinite(out.r).all()
  for q,j in np.ndindex(out.m.shape):
   hull=[]
   for a in ae:
    key=(kind,q,j,M,deg,a)
    if cache is not None:
     if key not in cache:cache[key]=weights(kind,q,j,M,deg,a)
     w=cache[key]
    else:w=weights(kind,q,j,M,deg,a)
    hull.append(image(w,mid,rad))
   l=min(v[0] for v in hull);u=max(v[1] for v in hull);m=F(float(out.m[q,j]));r=F(float(out.r[q,j]));assert m-r<=l<=u<=m+r,(kind,q,j,str(l),str(u),str(m),str(r))
   needed=max(abs(l-m),abs(u-m));ratio=float(r/needed) if needed else math.inf;min_ratio=min(min_ratio,ratio);count+=1
 return count,min_ratio

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--first',type=int,default=0);ap.add_argument('--count',type=int,default=100);ap.add_argument('--stress',type=int,default=0);ap.add_argument('--tag',default='modal_benchmark');args=ap.parse_args();start=time.monotonic();count=0;cases=0;min_ratio=math.inf;cache={};pins={str(p.relative_to(B)):sha(p) for p in [Path(__file__),E/'source/cert_resid.py',E/'source/midrad.py']}
 if args.stress:
  rng=random.Random(20261020)
  fixtures=[np.array([1.,.75*(1+2**-52),2.,0.,0.,0.]),np.array([1.,2**-53+2**-105,1+2**-52,-2**-53,0.,0.]),np.array([3*2.**-1072]*6)]
  for i in range(args.stress):
   if i<len(fixtures):tm=np.tile(fixtures[i],(8,1));tr=np.zeros_like(tm)
   else:
    base=rng.choice([-1074,-1022,-500,-53,0,50,500]);tm=np.array([[math.ldexp(rng.choice([-1.,1.])*rng.uniform(.5,1),base) for j in range(6)] for q in range(8)]);tr=np.abs(tm)*rng.choice([0.,2**-53,1e-8,1.])
   alpha=MR(rng.choice([-3.,0.,1.,47.]),rng.choice([0.,2**-48]));n,rat=audit_case(tm,tr,alpha,cache);count+=n;cases+=1;min_ratio=min(min_ratio,rat)
 else:
  data=B.parent/'ipmA-num/data/cert_green.npz';pins[str(data)]=sha(data);z=np.load(data);tm=z['T_mid'];tr=z['T_rad'];assert tm.shape==tr.shape and tm.shape[0]==7809;stop=min(7809,args.first+args.count)
  for i in range(args.first,stop):
   n,rat=audit_case(tm[i],tr[i],MR.exact(0.),cache);count+=n;cases+=1;min_ratio=min(min_ratio,rat)
   if cases%25==0:
    pr={'utc':datetime.now(timezone.utc).isoformat(),'first':args.first,'last':i,'cases':cases,'checks':count,'seconds':time.monotonic()-start};(E/f'{args.tag}_progress.json').write_text(json.dumps(pr)+'\n');print(json.dumps(pr),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINITE_INPUT_BOXES','cases':cases,'checks':count,'first':args.first,'count_requested':args.count,'stress':args.stress,'min_radius_to_required_ratio_display':min_ratio,'method':'Exact Fraction sparse affine image, including dependencies; alpha interval checked at both endpoints; frozen source outputs compared as exact dyadics.','seconds':time.monotonic()-start,'files':pins,'scope':'Specified finite input boxes only; not a universal arithmetic proof.'};(E/f'{args.tag}.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
if __name__=='__main__':main()
