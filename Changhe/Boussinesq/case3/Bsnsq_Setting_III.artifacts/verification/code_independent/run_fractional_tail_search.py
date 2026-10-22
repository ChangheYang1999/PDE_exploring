"""Own stream search in packet116, all exact center/tail constraints retained."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as Q
import argparse,hashlib,json,resource,time
import numpy as np
from scipy.optimize import least_squares
from fractional_tail_chart import keys,moments,exact_state,verify_exact_state,FractionalTailProblem
from stream_fractional_tail_certificate import checks
from free_beta_stream import grid,diagnose
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path)
ap.add_argument('--levels',default='3:3,5:5');ap.add_argument('--max-nfev',type=int,default=140)
ap.add_argument('--modes',default='fixed,free');ap.add_argument('--starts',default='2.2:-1,2.5:0,2.8:1')
a=ap.parse_args();root=a.root;root.mkdir(parents=True,exist_ok=True);started=time.monotonic()
sources=[Path(__file__),Path(__file__).with_name('fractional_tail_chart.py'),Path(__file__).with_name('stream_basis.py'),Path(__file__).with_name('free_beta_stream.py'),Path(__file__).with_name('stream_fractional_tail_certificate.py')]
summary={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','states':[],
 'reference_beta_for_all_weights':2.5,'free_beta_bounds':[2.02,2.98],'regularization':0.,
 'method':'packet116 center chart and first fractional-tail identities, analytic eta/coefficient Jacobian and centered beta derivative, own monomial calculus',
 'scope':'finite-dimensional fit only; exact chart coefficients reconstructed from binary-rational coordinates, compared against floating fit fields; no endpoint inferred',
 'code_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in sources}}
def save():
 summary['elapsed_seconds']=time.monotonic()-started
 (root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
hr=np.unique(np.r_[np.geomspace(1e-5,1e8,49),.03,.3,1.,3.]);ha=np.unique(np.r_[np.linspace(0,np.pi,41),.0003,.003,.012,np.pi-.012,np.pi-.003,np.pi-.0003]);heldout=grid(hr,ha)
for mode in a.modes.split(','):
 for seed_index,(beta_start,eta_start) in enumerate(tuple(map(float,v.split(':')))for v in a.starts.split(',')):
  previous=None
  for n,J in [tuple(map(int,v.split(':')))for v in a.levels.split(',')]:
   label=f'{mode}_s{seed_index}_b{beta_start:g}_n{n}_J{J}';t0=time.monotonic()
   tr=np.geomspace(.012,3000,max(20,5*n));ta=np.unique(np.r_[np.linspace(0,np.pi,max(18,2*J+8)),.003,np.pi-.003]);points=grid(tr,ta)
   problem=FractionalTailProblem(n,J,points,reference_beta=2.5)
   initial_beta=beta_start if previous is None else previous['beta']
   initial_eta=eta_start if previous is None else previous['eta']
   case=problem.case(initial_beta)
   if previous is None:
    rng=np.random.default_rng(11600+seed_index);free=rng.normal(0,.003,case.size)
   else:
    parts=[]
    for stream,key in [(True,'freeC'),(False,'freeD')]:
     old=dict(zip(keys(previous['n'],previous['J'],stream),previous[key]))
     parts.extend([old.get(k,0.)for k in keys(n,J,stream)])
    free=np.array(parts)
   z0=np.r_[initial_beta,initial_eta,free]
   initial=z0 if mode=='free' else z0[1:]
   to_full=(lambda v:v)if mode=='free'else(lambda v:np.r_[beta_start,v])
   calls=0;best=float('inf');bestz=z0.copy()
   state={'label':label,'mode':mode,'status':'RUNNING','n':n,'J':J,
          'beta_start':beta_start,'eta_start':eta_start,'initial_beta_at_level':initial_beta,
          'initial_eta_at_level':initial_eta,'parameter_count':len(initial),
          'training_points':len(points),'heldout_points':len(heldout),
          'started_utc':datetime.now(timezone.utc).isoformat()};summary['states'].append(state)
   def write_state(z,kind):
    c=problem.case(z[0]);C,D=c.coefficients(z[1],z[2:])
    exact=exact_state(float(z[0]),float(z[1]),1,n,J,list(map(float,z[2:2+c.nc])),list(map(float,z[2+c.nc:])))
    exact=json.loads(json.dumps(exact));assert verify_exact_state(exact)
    check=checks(exact);assert not check['stream_nonzero']and not check['temperature_nonzero']
    assert Q(check['constant_vertical'])==Q(float(z[1]))
    cr,dr=[np.array([float(Q(v))for v in exact[k]])for k in ['C','D']]
    center=moments(float(z[0]),C,n,J);tcenter=moments(float(z[0]),D,n,J,False)
    defects={'gamma_plus_eta':float(center[0]+z[1]),'strain':float(center[1]-1-z[0]/2),
             'b0':float(center[2]-4/z[0]),'a0':float(tcenter-1)}
    exact.update(kind=kind,label=label,code_sha256=summary['code_sha256'],
       floating_fit_C=[str(Q(float(v)))for v in C],floating_fit_D=[str(Q(float(v)))for v in D],
       center_float_defects=defects,
       rounded_exact_vs_floating_coefficients={'C':float(np.max(abs(cr-C))),'D':float(np.max(abs(dr-D)))})
    path=root/(label+'_state.json');path.write_text(json.dumps(exact,indent=2)+'\n')
    certpath=root/(label+'_tail_certificate.json');check.update(source_path=str(path.resolve()),source_sha256=hashlib.sha256(path.read_bytes()).hexdigest())
    certpath.write_text(json.dumps(check,indent=2)+'\n')
    return c,C,D,cr,dr,path,defects,exact['rounded_exact_vs_floating_coefficients']
   def fun(v):
    global calls,best,bestz
    z=to_full(v);r=problem.residual(z);calls+=1;loss=float(r@r)
    if loss<best:best=loss;bestz=z.copy()
    if calls==1 or calls%15==0:
     write_state(bestz,'checkpoint');state.update(calls=calls,best_objective=best,best_beta=float(bestz[0]),best_eta=float(bestz[1]),elapsed_seconds=time.monotonic()-t0);save()
     print(label,'calls',calls,'beta/eta',bestz[:2],'objective',best,'seconds',time.monotonic()-t0,flush=True)
    return r
   jac=(lambda v:problem.jacobian(v))if mode=='free'else(lambda v:problem.case(beta_start).jacobian_eta_coefficients(v[0],v[1:]))
   bounds=(np.r_[2.02,np.full(len(initial)-1,-np.inf)],np.r_[2.98,np.full(len(initial)-1,np.inf)])if mode=='free'else(-np.inf,np.inf)
   state['initial_objective']=float(np.linalg.norm(problem.residual(z0))**2);save()
   try:
    fit=least_squares(fun,initial,jac=jac,bounds=bounds,max_nfev=a.max_nfev,
        ftol=2e-9,xtol=2e-9,gtol=2e-8,x_scale='jac')
   except Exception as exc:
    write_state(bestz,'failed_fit_checkpoint');state.update(status='FAILED',exception_type=type(exc).__name__,exception=str(exc),elapsed_seconds=time.monotonic()-t0);save();print('FAILED',label,type(exc).__name__,str(exc),flush=True);break
   z=to_full(fit.x);c,C,D,cr,dr,path,defects,rounding=write_state(z,'completed_fit')
   diag,arrays=diagnose(c.basis,C,D,heldout);train,_=diagnose(c.basis,C,D,points)
   rounded_diag,rounded_arrays=diagnose(c.basis,cr,dr,heldout)
   Jm=jac(fit.x);colnorm=np.linalg.norm(Jm,axis=0);Jscaled=Jm/np.where(colnorm>0,colnorm,1)
   singular=np.linalg.svd(Jscaled,compute_uv=False)
   state.update(status='COMPLETE',beta=float(z[0]),eta=float(z[1]),objective=float(2*fit.cost),
      nfev=fit.nfev,njev=fit.njev,optimizer_success=bool(fit.success),optimizer_message=fit.message,
      optimality=float(fit.optimality),center_float_defects=defects,rounded_exact_vs_floating_coefficients=rounding,
      maximum_abs_coefficient={'C':float(np.max(abs(C))),'D':float(np.max(abs(D)))},
      heldout=diag,rounded_exact_heldout=rounded_diag,train=train,
      rounded_exact_vs_floating_field_maxima={k:float(np.max(abs(rounded_arrays[k]-arrays[k])))for k in arrays if k!='points'},
      elapsed_seconds=time.monotonic()-t0,state_file=path.name,state_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
      conditioning={'column_normalized_rank_at_rcond_1e_10':int(np.sum(singular>singular[0]*1e-10)),
                    'columns':Jm.shape[1],'column_normalized_singular_values':singular.tolist(),
                    'scope':'coordinate-dependent finite-grid diagnostic'},
      basis_rebuilds=problem.rebuilds,beta_bound_distance=[float(z[0]-2.02),float(2.98-z[0])])
   radii=np.linalg.norm(heldout,axis=1)
   state['regions']={name:diagnose(c.basis,C,D,heldout[mask])[0]for name,mask in
       [('inner',radii<.1),('core',(radii>=.1)&(radii<=10)),('outer',(radii>10)&(radii<=1000)),('far',radii>1000)]}
   np.savez_compressed(root/(label+'_heldout.npz'),**arrays)
   previous={'n':n,'J':J,'beta':float(z[0]),'eta':float(z[1]),
             'freeC':z[2:2+c.nc].tolist(),'freeD':z[2+c.nc:].tolist()}
   save();print('DONE',label,'beta/eta',z[:2],'F/G',diag['divided_F']['max_ratio'],diag['divided_G']['max_ratio'],'seconds',state['elapsed_seconds'],flush=True)
summary.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save()
print('COMPLETE',summary['elapsed_seconds'],flush=True)
