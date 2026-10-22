"""Independent analytic-Jacobian least-squares search in packet42's basis.
One single-thread CPU process, bounded time, incremental reproducible records.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,os,time,json,hashlib
import numpy as np
from scipy.optimize import least_squares
from global_stream_basis import GlobalBasis,GlobalField,Resolution

parser=argparse.ArgumentParser();parser.add_argument('--out',required=True);parser.add_argument('--betas',default='2,2.25,2.5,2.9,3.5');parser.add_argument('--seeds',default='0,1,2');parser.add_argument('--angular',type=int,default=4);parser.add_argument('--tails',type=int,default=3);parser.add_argument('--radial',type=int,default=1);parser.add_argument('--radii',type=int,default=28);parser.add_argument('--angles',type=int,default=28);parser.add_argument('--rmin',type=float,default=1e-4);parser.add_argument('--rmax',type=float,default=1e3);parser.add_argument('--nfev',type=int,default=180);parser.add_argument('--regularization',type=float,default=1e-7);parser.add_argument('--free-beta',action='store_true');parser.add_argument('--init');args=parser.parse_args()
root=Path(args.out);root.mkdir(parents=True,exist_ok=True);start=time.monotonic();resolution=Resolution(args.angular,args.tails,args.radial)
r=np.geomspace(args.rmin,args.rmax,args.radii);phi=-np.pi/2+np.pi*(np.arange(args.angles)+.371)/args.angles
points=np.column_stack(((r[:,None]*np.cos(phi)).ravel(),(r[:,None]*np.sin(phi)).ravel()))
points=np.vstack((points,np.column_stack((np.zeros_like(r),r)),np.column_stack((np.zeros_like(r),-r)),np.column_stack((r,np.zeros_like(r))),[[0.,0.]]))
rval=np.linalg.norm(points,axis=1);logq=np.log1p(rval*rval)
# New nodes, angular and radial offsets, and an exterior radius beyond training.
er=np.geomspace(args.rmin*.71,args.rmax*2.7,args.radii+9);ep=-np.pi/2+np.pi*(np.arange(args.angles+11)+.613)/(args.angles+11)
evalpoints=np.column_stack(((er[:,None]*np.cos(ep)).ravel(),(er[:,None]*np.sin(ep)).ravel()))
evalpoints=np.vstack((evalpoints,np.column_stack((np.zeros_like(er),er)),np.column_stack((np.zeros_like(er),-er)),np.column_stack((er,np.zeros_like(er))),[[0.,0.]]))
manifest={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'arguments':vars(args),'resolution':resolution.__dict__,'training_points':len(points),'evaluation_points':len(evalpoints),'scope':'Exploratory finite-basis fit, no exact solution or endpoint asserted. Training weights are radial asymptotic balancing weights, not pointwise residual normalizations.','sources':{n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['global_stream_search.py','global_stream_basis.py']},'runs':[]}
def save():
 manifest['elapsed_seconds']=time.monotonic()-start;(root/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
save()
for beta0 in map(float,args.betas.split(',')):
 for seed in map(int,args.seeds.split(',')):
  runstart=time.monotonic();base=GlobalBasis(points,beta0,resolution);n=base.nvar
  if args.init:
   init=np.load(args.init,allow_pickle=False);z0=init['coefficients'].copy()
   if len(z0)!=n:raise ValueError('initial resolution mismatch')
  else:z0=np.zeros(n) if seed==0 else np.random.default_rng(seed).normal(size=n)*(.05 if seed==1 else .3)
  if args.free_beta:z0=np.r_[z0,beta0]
  tag=f"b{beta0:g}_s{seed}";record={'tag':tag,'initial_beta':beta0,'seed':seed,'started_utc':datetime.now(timezone.utc).isoformat(),'history':[]};manifest['runs'].append(record);save()
  cache={'beta':None,'basis':None};calls=0;best=np.inf
  def system(z,jac=False):
   beta=float(z[-1]) if args.free_beta else beta0;coeff=z[:-1] if args.free_beta else z
   if cache['beta']!=beta:cache.update(beta=beta,basis=GlobalBasis(points,beta,resolution))
   basis=cache['basis'];weights=np.r_[np.exp((1+2/beta)*logq/2),np.exp((1+1/beta)*logq/2)]/np.sqrt(len(points))
   if jac:
    raw,J=basis.residual(coeff,True);J=weights[:,None]*J
    if args.free_beta:
     h=2e-5
     # One-sided formula only at beta=2, the analytically excluded side is never sampled.
     lo=max(2.,beta-h);hi=beta+h
     def rb(b):
      bb=GlobalBasis(points,b,resolution);ww=np.r_[np.exp((1+2/b)*logq/2),np.exp((1+1/b)*logq/2)]/np.sqrt(len(points));return bb.residual(coeff)*ww
     col=(rb(hi)-rb(lo))/(hi-lo);J=np.column_stack((J,col))
    if args.regularization:
     reg=np.zeros((n,len(z)));reg[:,:n]=args.regularization*np.eye(n);J=np.vstack((J,reg))
    return J
   result=weights*basis.residual(coeff)
   if args.regularization:result=np.r_[result,args.regularization*coeff]
   return result
  def fun(z):
   global calls,best
   ans=system(z);calls+=1;cost=float(ans@ans/2)
   if cost<best:
    best=cost
    np.savez_compressed(root/(tag+'_best.npz'),coefficients=(z[:-1] if args.free_beta else z),beta=(z[-1] if args.free_beta else beta0),resolution=np.array([args.angular,args.tails,args.radial]),training_points=points,cost=cost)
   if calls==1 or calls%10==0:
    record['history'].append({'calls':calls,'cost':cost,'best':best,'elapsed':time.monotonic()-runstart,'beta':float(z[-1]) if args.free_beta else beta0,'coefficient_max':float(abs(z[:n]).max())});save();print(tag,'call',calls,'cost',cost,'best',best,'elapsed',time.monotonic()-runstart,flush=True)
   return ans
  bounds=(-np.inf,np.inf)
  if args.free_beta:bounds=(np.r_[np.full(n,-np.inf),2.],np.r_[np.full(n,np.inf),8.])
  fit=least_squares(fun,z0,jac=lambda z:system(z,True),bounds=bounds,method='trf',x_scale='jac',max_nfev=args.nfev,ftol=1e-11,xtol=1e-11,gtol=1e-10)
  beta=float(fit.x[-1]) if args.free_beta else beta0;coeff=fit.x[:-1] if args.free_beta else fit.x
  saved=root/(tag+'_final.npz');np.savez_compressed(saved,coefficients=coeff,beta=beta,resolution=np.array([args.angular,args.tails,args.radial]),training_points=points,cost=fit.cost)
  J=system(fit.x,True);sv=np.linalg.svd(J,compute_uv=False)
  ev=GlobalBasis(evalpoints,beta,resolution);diag=ev.diagnostics(coeff)
  record.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-runstart,beta=beta,cost=float(fit.cost),optimality=float(fit.optimality),nfev=fit.nfev,njev=fit.njev,termination=fit.message,coefficients_path=str(saved),jacobian_singular_max=float(sv[0]),jacobian_singular_min=float(sv[-1]),jacobian_smallest10=sv[-10:].tolist(),diagnostics=diag)
  save();print(tag,'COMPLETE','beta',beta,'cost',fit.cost,'optimality',fit.optimality,'svmin',sv[-1],'elapsed',time.monotonic()-runstart,flush=True)
manifest['status']='COMPLETE';manifest['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('ALL COMPLETE',manifest['elapsed_seconds'],flush=True)
