"""Independent real-coordinate diagnostics for all pair classes and interval bounds."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import numpy as np,json,hashlib
from flint import arb,ctx
from certify_full_range_profile import bound
ctx.prec=192;ROOT=Path(__file__).resolve().parents[1]
def main():
 rng=np.random.default_rng(609306);rows=[]
 for aa in ['3/4','9/10']:
  alpha=float(F(aa));row={'alpha':aa,'classes':{}}
  for mode in ['same','opposite']:
   excess=-1e20;count=0
   for _ in range(6000):
    den=2**int(rng.integers(4,18));box=[]
    for j in range(3):
     x,y=sorted(map(int,rng.integers(0,den if j==0 else den//2+1,2)))
     if j==0:x=max(1,x);y=max(x,y)
     box.extend([F(x,den),F(y,den)])
    ub=float(bound(tuple(box),arb(aa),mode).upper());v=rng.random((24,3))
    for j in range(3):v[:,j]=float(box[2*j])+v[:,j]*float(box[2*j+1]-box[2*j])
    u=v[:,0];a=v[:,1]*np.pi;b=v[:,2]*np.pi
    sa=np.maximum(0,np.sin(2*a))**alpha;sb=np.maximum(0,np.sin(2*b))**alpha
    dy=np.sin(a)+(1 if mode=='opposite' else -1)*u*np.sin(b)
    D=np.hypot(np.cos(a)-u*np.cos(b),dy)
    num=1-u**alpha+(sa+u**alpha*sb if mode=='opposite' else abs(sa-u**alpha*sb))
    use=D>1e-12;vs=num[use]/(2*D[use]**alpha)
    if len(vs):
     ex=float(vs.max()-ub);excess=max(excess,ex);count+=len(vs);assert ex<1e-10,(aa,mode,box,ex)
   row['classes'][mode]={'point_checks':count,'largest_excess':excess}
  p=rng.normal(size=(300000,2));q=rng.normal(size=(300000,2))*np.exp(rng.uniform(-12,12,(300000,1)))
  def g(v):
   r=np.hypot(v[:,0],v[:,1]);return .5*(r**alpha+np.sign(v[:,0]*v[:,1])*(2*abs(v[:,0]*v[:,1])/r)**alpha)
  ratios=abs(g(p)-g(q))/np.linalg.norm(p-q,axis=1)**alpha
  row['arbitrary_pair_checks']=len(p);row['largest_arbitrary_ratio']=float(ratios.max());rows.append(row)
 out={'time_utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'status':'Independent numerical diagnostics passed; rigor comes from exhaustive interval coverings.','source_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'code/certify_full_range_profile.py']}}
 target=ROOT/'07_diagonal_identity_term/full_range_profile/verification/independent_diagnostics.json';target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
