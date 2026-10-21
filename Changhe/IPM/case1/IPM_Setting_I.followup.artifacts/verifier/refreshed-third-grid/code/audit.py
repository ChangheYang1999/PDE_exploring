"""Independent physical audit of a frozen radial-domain trial; own lane imports only."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
from math import ceil,isqrt,sqrt
import sys,json,time,gc
import numpy as np
import torch
from scipy.optimize import brentq
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
from gpu import GPUField
from split_kernel import SplitKernel
source=Path(sys.argv[1]);tag=source.stem;outpath=ROOT/'verification'/(tag+'_physical.json')
d=NodalDensity(source);assert d.L>=1 and d.L==int(d.L) and 0<d.k<.2
H=isqrt(2*d.N*(2*d.M-1));H+=H*H<2*d.N*(2*d.M-1)
B0=ceil(float(np.max(abs(d.b))));C=int(d.L)**3*H*B0
out={'start':datetime.now(timezone.utc).isoformat(),'source_md5':d.md5,'source':str(source),'N':d.N,'M':d.M,'L':d.L,'cl':d.cl,'beta':d.beta,'first_row_unit':bool(np.all(d.b[0]==1.)),'node_range':[float(np.min(d.b)),float(np.max(d.b))],'exact_tail_C':C,'exact_strain_tail_bound':str(F(5*C,2*10**24)),'passes':[]}
def save():
 tmp=outpath.with_suffix('.temporary');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(outpath)
def log(*args):print(datetime.now(timezone.utc).isoformat(),*args,flush=True)
def tail(point):
 n=ceil(sqrt(sum(float(t)**2 for t in point)))
 while sum(F(t)**2 for t in point)>n*n:n+=1
 return F(5*C*n,2*10**24)/(1-F(n,10**30)**2)**2
save();torch.set_num_threads(1)
for nang,order,panel in [(2048,24,.1),(4096,28,.08)]:
 log('BUILD',tag,nang);begin=time.monotonic();ker=SplitKernel(GPUField(d),nang,order,panel,rmax=1e30)
 row={'nang':nang,'order':order,'panel':panel,'rmax':'1e30','transport':[]};out['passes'].append(row);save();cache={}
 def velocity(point):
  key=tuple(map(float,point))
  if key not in cache:cache[key]=ker.velocity(key)
  return cache[key]
 def w(x):return d.cl*x+velocity((x,0.))[0]
 bracket=[8.,9.];ends=list(map(w,bracket))
 if ends[0]*ends[1]>=0:
  scan=[(x,w(x)) for x in [1.,2.,4.,6.,8.,10.,12.,16.,24.]];row['axis_scan']=scan
  intervals=[(p[0],q[0]) for p,q in zip(scan[:-1],scan[1:]) if p[1]*q[1]<0]
  if not intervals:raise RuntimeError('No nonzero canonical axis root found in the stated scan')
  bracket=intervals[0]
 root=brentq(w,*bracket,xtol=3e-10);row['root']={'xstar':root,'bracket':bracket,'w':w(root),'origin_U':velocity((0.,0.)).tolist(),'g':float(gradient_fd(d,root,0.,relative_step=1/32000)[1])};save();log('ROOT',tag,nang,row['root'])
 points=[[5.403023058681398,8.414709848078965],[.20794827803092428,9.99783764189357],[8.6,.1],[8.6,1.],[1000*np.cos(.3),1000*np.sin(.3)],[10000*np.cos(.3),10000*np.sin(.3)],[root,.1],[root,1.]]
 for pt in points:
  u=velocity(pt);rho=float(d(*pt));gs=[gradient_fd(d,*pt,relative_step=h) for h in [1/8000,1/16000,1/32000]];g=gs[-1];W=d.cl*np.array(pt)+u;R=float(W@g-rho);Nf=float(abs(rho)+sum(abs(W*g)));Nv=float(abs(rho)+abs(np.array(pt)@g)+abs(u@g))
  row['transport'].append({'point':list(map(float,pt)),'U':u.tolist(),'rho':rho,'gradient':g.tolist(),'gradient_steps':[1/8000,1/16000,1/32000],'gradient_signed_changes':[(gg-g).tolist() for gg in gs[:-1]],'R':R,'N_report_f':Nf,'N_report_v':Nv,'absR_report_f':abs(R)/Nf,'absR_report_v':abs(R)/Nv,'gradient_R_changes_fixed_Nf':[float(W@(gg-g)/Nf) for gg in gs[:-1]],'exact_U_tail_bound':str(tail(pt))});save();log('TRANSPORT',tag,nang,len(row['transport']),abs(R)/Nf)
 def derivative(point,h):
  ans=np.zeros((2,2));pt=np.array(point)
  for ax in [0,1]:
   for j,weight in enumerate([4/5,-1/5,4/105,-1/280],1):
    step=np.zeros(2);step[ax]=j*h;ans[:,ax]+=weight*(velocity(pt+step)-velocity(pt-step))/h
  return ans
 if nang==4096:
  row['source_jacobian']=[]
  for h in [.005,.0025]:
   du=derivative((root,0.),h);row['source_jacobian'].append({'h':h,'DU':du.tolist(),'wprime':float(d.cl+du[0,0]),'hP':float(d.cl+du[1,1]),'divU':float(np.trace(du))});save();log('JET',tag,h,row['source_jacobian'][-1])
  row['elliptic']=[]
  for pt in [[root,.1],[root,1.]]:
   g=gradient_fd(d,*pt,relative_step=1/32000);checks=[]
   for h in [.005,.0025]:
    du=derivative(pt,h);E=float(-du[1,0]+du[0,1]-g[0]);den=float(abs(du[1,0])+abs(du[0,1])+abs(g[0]));checks.append({'h':h,'DU':du.tolist(),'E':E,'denominator':den,'E_normalized':abs(E)/den,'E_over_rho_x':abs(E/g[0]),'divU':float(np.trace(du))})
   row['elliptic'].append({'point':pt,'rho_x':float(g[0]),'checks':checks});save();log('ELLIPTIC',tag,pt,checks)
  p=(1.,.5);u=velocity(p);row['parity']={'point':p,'U':u.tolist(),'U_minus_x_defect':(velocity((-1.,.5))-[-u[0],u[1]]).tolist(),'U_minus_y_defect':(velocity((1.,-.5))-[u[0],-u[1]]).tolist(),'rho_x_even':float(d(-1.,.5)-d(1.,.5)),'rho_y_odd':float(d(1.,-.5)+d(1.,.5))};save()
 row['seconds']=time.monotonic()-begin;row['date_end']=datetime.now(timezone.utc).isoformat();save();log('PASS_COMPLETE',tag,nang,row['seconds']);del ker;cache.clear();gc.collect();torch.cuda.empty_cache()
out['complete']=True;out['end']=datetime.now(timezone.utc).isoformat();save();log('COMPLETE',tag)
