import sys,json,time
from pathlib import Path
import numpy as np
import torch
from gpu import tensor,GPUField
from split_kernel import SplitKernel
class SlowField:
 def __init__(self,k):self.k=k;self.p=(1+k)/2
 def __call__(self,x,y):
  x,y=tensor(x),tensor(y);r2=x*x+y*y;p=self.p
  return -4*p*y*(1+r2)**(p-2)*(2+(p+1)*r2)
 def exact(self,pt):
  x,y=pt;r2=x*x+y*y;p=self.p
  return 2*p*(1+r2)**(p-2)*np.array([-x*(1+r2+2*(p-1)*y*y),y*(1+r2+2*(p-1)*x*x)])
pts=[[1,.5],[8.6,.1],[1,100],[1000,1],[1,10000]]
rows=[];path=Path(sys.argv[1]);now=time.monotonic()
for n,order,panel in [(512,16,.20),(1024,20,.16),(2048,24,.12)]:
 for kind in ['gaussian',.2,.9]:
  f=GPUField('manufactured') if kind=='gaussian' else SlowField(kind)
  ker=SplitKernel(f,n,order,panel,rmax=1e16,offset=.23)
  for pt in pts:
   u=ker.velocity(pt)
   if kind=='gaussian':
    x,y=pt;ex=np.array([2*x*(1-2*y*y),y*(4*x*x-2)])*np.exp(-x*x-y*y)
   else:ex=f.exact(pt)
   err=np.max(np.abs(u-ex));den=max(1.,np.max(np.abs(ex)))
   row={'kind':kind,'nang':n,'order':order,'panel':panel,'point':pt,'U':u.tolist(),'exact':ex.tolist(),'absolute_error':float(err),'error_over_max_1_U':float(err/den)}
   rows.append(row);path.write_text(json.dumps({'rows':rows,'seconds':time.monotonic()-now},indent=2)+'\n');print(json.dumps(row),flush=True)
  del ker
fin=[r for r in rows if r['nang']==2048]
assert max(r['error_over_max_1_U'] for r in fin)<1e-7, 'Manufactured split convergence unresolved, do not run candidate chain'
