from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sys,json,time
import numpy as np
import torch
import sympy as sp
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root.parent/'inverse/code'))
from gpu import tensor
from split_kernel import SplitKernel
from density import gradient_fd
torch.set_num_threads(1)
k=F(1,5);cl=5;t=F(37087,336)
assert 1/(2*(1-k)*(3-k)*(5-k))+1/(8*(1-k))+t/8==14
assert 2+2*t<224
th=sp.symbols('theta',real=True);ff=sp.cos(th)**2*sp.sin(th)*sp.cos(2*th)**2;gg=sp.cos(th)**2*sp.sin(th)
assert ff.subs(th,sp.pi/4)==0 and sp.diff(ff,th).subs(th,sp.pi/4)==0
assert sp.simplify((sp.diff(gg,th)+gg).subs(th,sp.pi/4))==0
class Field:
 def __init__(self,gpu=False):self.gpu=gpu
 def __call__(self,x,y):
  if self.gpu:x=tensor(x);y=tensor(y);exp=torch.exp
  else:x=np.asarray(x);y=np.asarray(y);exp=np.exp
  r2=x*x+y*y
  return x*x*y*((x*x-y*y)**2*(1+r2)**(-3.4)+(1+r2)**(-1.8)+float(t)*r2*exp(-r2))

def diagonal_grad(x):
 r2=2*x*x;base=(1+r2)**(-1.8);gau=float(t)*r2*np.exp(-r2);slope=-1.8*(1+r2)**(-2.8)+float(t)*(1-r2)*np.exp(-r2)
 rho=x**3*(base+gau)
 return rho,np.array([2*x*x*(base+gau)+2*x**4*slope,x*x*(base+gau)+2*x**4*slope])

out={'date_start':datetime.now(timezone.utc).isoformat(),'k':str(k),'cl':cl,'t':str(t),'central_strain_exact':'14','a_at_zero_exact':'1','limiting_R_over_Nf':'2/3','tail_envelope_C':224,'tail_observer_radius':'1e9','tail_outer_radius':'1e30','U_tail_bound':float(F(5,2)*224*10**9/F(10**24)/(1-F(1,10**21)**2)**2),'rows':[]}
p=root/'verification/degenerate.json';cpu=Field();gpu=Field(True)
for n,order,panel in [(1024,22,.14),(2048,26,.10)]:
 ker=SplitKernel(gpu,n,order,panel,rmax=1e30)
 for r in [1e2,1e4,1e6,1e8]:
  start=time.monotonic();x=r/np.sqrt(2);u=ker.velocity([x,x]);rho,g=diagonal_grad(x);W=cl*np.array([x,x])+u;R=W@g-rho;N=abs(rho)+np.sum(abs(W*g));gfd=gradient_fd(cpu,x,x,relative_step=.0005)
  row={'nang':n,'order':order,'panel':panel,'radius':float(np.sqrt(2)*x),'point':[x,x],'rho':rho,'U':u.tolist(),'R':float(R),'N_report_f':float(N),'R_over_N_report_f':float(abs(R)/N),'gradient_FD_relative_change':float(np.linalg.norm(g-gfd)/np.linalg.norm(g)),'seconds':time.monotonic()-start}
  out['rows'].append(row);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
 del ker;torch.cuda.empty_cache()
out['date_end']=datetime.now(timezone.utc).isoformat();p.write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['date_end'],flush=True)
