"""Independent physical-space diagnostics, with a checkpoint after each point.
Uses only this lane's density reconstruction, kernel, and Cartesian differences.
"""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from gpu import GPUField,Kernel,load_source
from density import gradient_fd

p=argparse.ArgumentParser();p.add_argument('density');p.add_argument('output')
p.add_argument('--nang',type=int,default=2048);p.add_argument('--order',type=int,default=20)
p.add_argument('--panel',type=float,default=.19);p.add_argument('--rmax',type=float,default=1e14)
p.add_argument('--mode',choices=['transport','elliptic','axis'],default='transport')
p.add_argument('--points-file');p.add_argument('--kernel',choices=['centered','split'],default='centered')
p.add_argument('--offset',type=float,default=.37)
p.add_argument('--difference-steps',help='Comma-separated Cartesian steps, overriding the default elliptic sweep')
p.add_argument('--difference-orders',default='4,8')
p.add_argument('--density-step',type=float,default=.0005)
a=p.parse_args()
source=load_source(a.density);field=GPUField(source)
if a.kernel=='split':
 from split_kernel import SplitKernel
 ker=SplitKernel(field,a.nang,a.order,a.panel,rmax=a.rmax,offset=a.offset)
else:ker=Kernel(field,a.nang,a.order,a.panel,rmax=a.rmax,offset=a.offset)
out={'configuration':vars(a),'source_md5':source.md5,'cl':source.cl,'L':source.L,'rows':[]}
cache={}
def velocity(point):
 key=tuple(float(x) for x in point)
 if key not in cache:cache[key]=ker.velocity(key)
 return cache[key]
def save(row):
 out['rows'].append(row);Path(a.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(row),flush=True)
def fd_u(point,h,order=4):
 weights=[2/3,-1/12] if order==4 else [4/5,-1/5,4/105,-1/280]
 mat=np.zeros((2,2));pt=np.array(point)
 for axis in [0,1]:
  for j,w in enumerate(weights,1):
   step=np.zeros(2);step[axis]=j*h
   mat[:,axis]+=w*(velocity(pt+step)-velocity(pt-step))/h
 return mat

if a.mode=='transport':
 if a.kernel=='split':raise ValueError('Use split_kernel.py for partitioned transport and its distinct panel records')
 if a.points_file:points=json.loads(Path(a.points_file).read_text())
 else:
  points=[[float(r*np.cos(t)),float(r*np.sin(t))] for r in [.05,.15,.5,1.5,5,10,30,100,1000,10000] for t in [.001,.03,.15,.5,1.,1.4,1.55]]
  points += [[x,y] for x in [8.5,8.57,8.6,8.63,8.7] for y in [.0001,.01,.1,1.]]
 for i,point in enumerate(points):
  start=time.monotonic();u,pp=ker.velocity(point,True);rv=float(source(*point))
  grads=[gradient_fd(source,*point,relative_step=h) for h in [.002,.001,.0005]]
  g=grads[-1];W=source.cl*np.array(point)+u;R=float(W@g-rv)
  nf=abs(rv)+abs(np.array(point)@g)+abs(u@g);nv=abs(rv)+np.sum(np.abs(W*g))
  tails=[]
  for rad in [100.,1e3,1e4,1e6,1e8,1e10,1e12]:
   if rad>=a.rmax:continue
   j=int(np.searchsorted(pp[:,0],np.log(rad)));missing=pp[j:,2:].sum(0)
   tails.append({'actual_cutoff':float(np.exp(pp[j,0])),'velocity_added_to_cutoff':missing.tolist(),
                  'transport_change':float(missing@g)})
  save({'point':point,'U':u.tolist(),'rho':rv,'R':R,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv,
    'gradients':np.array(grads).tolist(),'R_gradient_step_spread':float(np.ptp([W@gx-rv for gx in grads])),
    'a_value':rv/(point[0]**2*point[1]),'cutoff_comparison':tails,'seconds':time.monotonic()-start})
  np.savez_compressed(Path(a.output).with_suffix('.pieces'+str(i)+'.npz'),panels=pp)
elif a.mode=='elliptic':
 points=json.loads(Path(a.points_file).read_text()) if a.points_file else [[1.,.5],[8.6,.1],[8.6,1.],[1.,100.]]
 for point in points:
  start=time.monotonic();g=gradient_fd(source,*point,relative_step=a.density_step);checks=[]
  sweep=[(4,.04),(4,.02),(4,.01),(8,.01)]
  if a.difference_steps:
   sweep=[(order,h) for h in map(float,a.difference_steps.split(',')) for order in map(int,a.difference_orders.split(','))]
   assert all(order in [4,8] for order,h in sweep)
  for order,h in sweep:
   du=fd_u(point,h,order);E=-du[1,0]+du[0,1]-g[0]
   en=abs(g[0])+abs(du[1,0])+abs(du[0,1]);dn=abs(du[0,0])+abs(du[1,1])
   checks.append({'difference_order':order,'h':h,'DU':du.tolist(),'E':float(E),'E_normalized':float(abs(E)/en) if en else None,
    'E_over_rho_x':float(abs(E/g[0])) if g[0] else None,
    'divU':float(np.trace(du)),'divU_normalized':float(abs(np.trace(du))/dn) if dn else None})
  save({'point':point,'rho_x':float(g[0]),'checks':checks,'seconds':time.monotonic()-start})
else:
 start=time.monotonic();root=brentq(lambda x:source.cl*x+velocity((x,0))[0],8.,9.,xtol=2e-10)
 data={'xstar':root,'w_at_root':float(source.cl*root+velocity((root,0))[0]),'g_at_root':float(gradient_fd(source,root,0,relative_step=.0005)[1]),'origin_velocity':velocity((0.,0.)).tolist(),'checks':[]}
 for h in [.04,.02,.01,.005]:
  du=fd_u((root,0),h,4);data['checks'].append({'h':h,'wprime':float(source.cl+du[0,0]),'hP':float(source.cl+du[1,1]),'divU':float(np.trace(du))})
 point=(1.,.5);u=velocity(point)
 data['parity']={'point':point,'U':u.tolist(),'minus_x_defect':(velocity((-1.,.5))-np.array([-u[0],u[1]])).tolist(),
   'minus_y_defect':(velocity((1.,-.5))-np.array([u[0],-u[1]])).tolist()}
 data['seconds']=time.monotonic()-start;save(data)
