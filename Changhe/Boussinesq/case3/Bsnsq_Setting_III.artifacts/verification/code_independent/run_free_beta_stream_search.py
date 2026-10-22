"""Single-threaded free-beta pilot with exact coefficient JSON and axis checks."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import argparse,json,time,hashlib,resource
import numpy as np
from scipy.optimize import least_squares
from free_beta_stream import FreeBetaProblem,grid,diagnose
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--starts',default='2.25,2.75,3.25,4.25,6.5');ap.add_argument('--levels',default='4:5,6:7');ap.add_argument('--max-nfev',type=int,default=140);ap.add_argument('--beta-min',type=float,default=2.02);ap.add_argument('--beta-max',type=float,default=8.);ap.add_argument('--regularization',type=float,default=0.);args=ap.parse_args();root=args.root;root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
summary={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','bounds_beta':[args.beta_min,args.beta_max],'states':[],'method':'free beta, fixed-pivot center chart, symbolic divided residuals, analytic coefficient Jacobian and centered beta finite difference; reference-beta envelope frozen per initial seed','scope':'restricted finite stream basis and finite grid; no endpoint inferred','code_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('free_beta_stream.py'),Path(__file__).with_name('stream_basis.py')]}}
def save():summary['elapsed_seconds']=time.monotonic()-start;(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
hr=np.unique(np.r_[np.geomspace(1e-5,1e8,49),.03,.3,1.,3.]);ha=np.unique(np.r_[np.linspace(0,np.pi,41),.0003,.003,.012,np.pi-.012,np.pi-.003,np.pi-.0003]);heldout=grid(hr,ha)
for seed_index,beta_start in enumerate(map(float,args.starts.split(','))):
 previous=None
 for ni,nj in [tuple(map(int,s.split(':'))) for s in args.levels.split(',')]:
  label=f's{seed_index}_b{beta_start:g}_i{ni}_j{nj}';t0=time.monotonic();tr=np.geomspace(.012,3000,max(20,5*ni));ta=np.unique(np.r_[np.linspace(0,np.pi,max(18,2*nj+8)),.003,np.pi-.003]);points=grid(tr,ta);problem=FreeBetaProblem(ni,nj,points,beta_start,regularization=args.regularization)
  initial_beta=beta_start if previous is None else previous[0].beta;basis=problem.case(initial_beta).basis
  if previous is None:
   rng=np.random.default_rng(11400+seed_index);initial=np.r_[initial_beta,rng.normal(0,.003,basis.size)]
  else:
   old,C0,D0=previous;C=np.zeros(basis.n);D=np.zeros(basis.n)
   for k,l in enumerate(old.labels):i=basis.labels.index(l);C[i]=C0[k];D[i]=D0[k]
   initial=np.r_[initial_beta,C[basis.freeC],D[basis.freeD]]
  state={'label':label,'beta_start':beta_start,'initial_beta_at_level':initial_beta,'ni':ni,'nj':nj,'parameters_including_beta':len(initial),'training_points':len(points),'heldout_points':len(heldout),'reference_beta_for_weights':beta_start,'regularization':args.regularization,'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat()};summary['states'].append(state)
  calls=0;best=float('inf');bestx=initial.copy()
  def write_state(z,kind):
   b=problem.case(z[0]).basis;C,D=b.coefficients(z[1:]);fr=lambda v:str(Fraction(float(v)))
   data={'kind':kind,'label':label,'beta':fr(b.beta),'a0':fr(b.a0),'ni':ni,'nj':nj,'shifts':b.shifts,'labels':b.labels,'C':[fr(v) for v in C],'D':[fr(v) for v in D],'coordinate_vector':[fr(v) for v in z],'reference_beta_for_weights':fr(beta_start),'center_float_defects':{'strain':float((b.Cconstraint@C-b.Ctarget)[0]),'b0':float((b.Cconstraint@C-b.Ctarget)[1]),'a0':float((b.Dconstraint@D-b.Dtarget)[0])},'code_sha256':summary['code_sha256']}
   p=root/(label+'_state.json');p.write_text(json.dumps(data,indent=2)+'\n');return b,C,D,p,data['center_float_defects']
  def fun(z):
   global calls,best,bestx
   r=problem.residual(z);calls+=1;loss=float(r@r)
   if loss<best:best=loss;bestx=z.copy()
   if calls==1 or calls%15==0:
    write_state(bestx,'checkpoint');state.update(calls=calls,best_objective=best,best_beta=float(bestx[0]),elapsed_seconds=time.monotonic()-t0);save();print(label,'calls',calls,'beta',bestx[0],'objective',best,'seconds',time.monotonic()-t0,flush=True)
   return r
  state['initial_objective']=float(np.dot(problem.residual(initial),problem.residual(initial)));save()
  lower=np.r_[args.beta_min,np.full(basis.size,-np.inf)];upper=np.r_[args.beta_max,np.full(basis.size,np.inf)]
  try:
   fit=least_squares(fun,initial,jac=problem.jacobian,bounds=(lower,upper),max_nfev=args.max_nfev,ftol=2e-9,xtol=2e-9,gtol=2e-8,x_scale='jac')
  except Exception as exc:
   write_state(bestx,'failed_fit_checkpoint');state.update(status='FAILED',exception_type=type(exc).__name__,exception=str(exc),elapsed_seconds=time.monotonic()-t0);save();print('FAILED',label,type(exc).__name__,str(exc),flush=True);break
  b,C,D,path,defects=write_state(fit.x,'completed_fit');diag,arrays=diagnose(b,C,D,heldout);train,_=diagnose(b,C,D,points)
  J=problem.jacobian(fit.x);jb=J[:,0];jc=J[:,1:];fit_beta,_,rank,singular=np.linalg.lstsq(jc,jb,rcond=1e-10);rel=float(np.linalg.norm(jb-jc@fit_beta)/np.linalg.norm(jb)) if np.linalg.norm(jb) else 0.
  colnorm=np.linalg.norm(J,axis=0);Js=J/np.where(colnorm>0,colnorm,1.);sv=np.linalg.svd(Js,compute_uv=False)
  state.update(status='COMPLETE',beta=float(b.beta),objective=float(2*fit.cost),nfev=fit.nfev,njev=fit.njev,optimizer_success=bool(fit.success),optimizer_message=fit.message,optimality=float(fit.optimality),center_float_defects=defects,heldout=diag,train=train,elapsed_seconds=time.monotonic()-t0,state_file=path.name,state_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),basis_rebuilds=problem.rebuilds,beta_bound_distance=[float(b.beta-args.beta_min),float(args.beta_max-b.beta)],conditioning={'coefficient_rank_at_rcond_1e_10':int(rank),'coefficient_columns':jc.shape[1],'relative_beta_column_after_coefficient_projection':rel,'column_normalized_singular_values':sv.tolist(),'scope':'coordinate/weight dependent finite-grid diagnostics, not proof of exponent determination'})
  radii=np.linalg.norm(heldout,axis=1);regions={}
  for name,mask in [('inner',radii<.1),('core',(radii>=.1)&(radii<=10)),('outer',(radii>10)&(radii<=1000)),('far',radii>1000)]:regions[name]=diagnose(b,C,D,heldout[mask])[0]
  state['regions']=regions;np.savez_compressed(root/(label+'_heldout.npz'),**arrays);previous=(b,C,D);save();print('DONE',label,'beta',b.beta,'F/G',diag['divided_F']['max_ratio'],diag['divided_G']['max_ratio'],'seconds',state['elapsed_seconds'],flush=True)
summary.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',summary['elapsed_seconds'],flush=True)
