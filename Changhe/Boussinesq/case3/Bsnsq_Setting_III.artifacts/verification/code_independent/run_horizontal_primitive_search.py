"""Own stream-only horizontal primitive least squares, after128 controls."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import argparse,json,time,hashlib
import numpy as np
from scipy.optimize import least_squares
from horizontal_primitive_stream import PrimitiveProblem,FreeBetaPrimitive
from free_beta_stream import make_chart,grid

ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--max-nfev',type=int,default=100);a=ap.parse_args();root=a.root;root.mkdir(exist_ok=True)
control=Path('verification/primitive128_controls_20261021T0530Z/tests.json')
if json.loads(control.read_text()).get('status')!='ALL_CONTROLS_PASSED':raise RuntimeError('128 controls have not passed')
rng=np.random.default_rng(1282026);start=time.perf_counter();summary={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','controls_sha256':hashlib.sha256(control.read_bytes()).hexdigest(),'states':[],
 'scope':'Independent stream-only pilot. Levels change domain and resolution together, so are not an isolated convergence study. No automatic YES; finite quadrature vorticity residual requires independent differentiation. Unknown beta retained in free runs.'}
def save():
 summary['elapsed_seconds']=time.perf_counter()-start;(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
def exact_center(beta,labels,C):
 beta=Q.from_float(float(beta));C=list(map(lambda x:Q.from_float(float(x)),C));p0=labels.index((0,0,0));p1=labels.index((0,1,0));C[p0]=C[p1]=Q(0)
 c=b=Q(0)
 for (i,j,d),cc in zip(labels,C):
  v=0 if j%2 else (-1)**(j//2);w=0 if not j%2 else j*(-1)**((j-1)//2);k=1-1/beta-d
  c+=cc*w;b-=cc*(4*(k-2*i*i/beta)-j*j)*v
 C[p1]=1+beta/2-c;C[p0]=(4/beta-b)/(-4*(1-1/beta))
 return str(beta),list(map(str,C))
levels=[(2,4,10.,13,13),(3,5,30.,17,17),(4,6,100.,21,21)]
for free in [False,True]:
 for seed,initial_beta in enumerate([2.25,2.75,3.5]):
  previous=None;beta=initial_beta
  for ni,nj,rmax,nr,na in levels:
   label=f'{"free"if free else"fixed"}_s{seed}_b{initial_beta}_n{ni}_J{nj}'
   points=grid(np.geomspace(.025,rmax,nr),np.linspace(0,np.pi,na));b=make_chart(beta,ni,nj)
   if previous is None:z=rng.normal(size=b.nc)*([0.,.013,.05][seed])
   else:
    oldC={tuple(l):v for l,v in zip(previous['labels'],previous['C'])};z=np.array([oldC.get(b.labels[k],0.)for k in b.freeC])
   problem=FreeBetaPrimitive(ni,nj,points,initial_beta,32,'sinh',1e-7)if free else PrimitiveProblem(b,points,32,'sinh',1e-7,initial_beta)
   init=np.r_[beta,z]if free else z;calls=[0];tic=time.perf_counter();history=[]
   def fun(v):
    rr=problem.residual(v);calls[0]+=1
    history.append({'call':calls[0],'seconds':time.perf_counter()-tic,'objective_norm':float(np.linalg.norm(rr)),'beta':float(v[0])if free else beta})
    if calls[0]==1 or calls[0]%10==0:print(label,history[-1],flush=True)
    return rr
   lo=np.r_[2.05,np.full(len(z),-np.inf)]if free else -np.inf
   hi=np.r_[5.,np.full(len(z),np.inf)]if free else np.inf
   fit=least_squares(fun,init,jac=problem.jacobian,bounds=(lo,hi),max_nfev=a.max_nfev,xtol=1e-9,ftol=1e-9,gtol=1e-9,x_scale='jac')
   if free:beta=float(fit.x[0]);z=fit.x[1:];case=problem.case(beta);b=case.basis
   else:z=fit.x;case=problem
   C=b.Cbase+b.Cnull@z;ratbeta,ratC=exact_center(beta,b.labels,C);storedC=np.array([float(Q(cc))for cc in ratC])
   state={'schema':'independent_horizontal_primitive_stream_v1','beta':ratbeta,'a0':'1','labels':[list(q)for q in b.labels],'C':ratC,'ni':ni,'nj':nj,'shifts':[0,1],
      'temperature':'Theta(x,y)=integral_0^x[(beta X+grad_perp Psi-grad_perp Psi(0)).grad(-Delta Psi)-Delta Psi](s,y) ds',
      'stream_basis':'x R^(1-1/beta-shift) T_i(2R^(-1/beta)-1) T_j(y/R), R=sqrt(1+x^2+y^2), relative linear stream gauge',
      'coefficient_rounding_correction_max':float(abs(storedC-C).max()),'fit_quadrature_order':32,'fit_quadrature_rule':'sinh','free_beta':free,'initial_beta':initial_beta,
      'fit_domain_radius':rmax,'fit_points':len(points),'created_utc':datetime.now(timezone.utc).isoformat()}
   path=root/(label+'_state.json');path.write_text(json.dumps(state,indent=2)+'\n')
   (root/(label+'_history.json')).write_text(json.dumps(history,indent=2))
   held=grid(np.r_[np.geomspace(1e-5,1e4,37),.017,.117,1.17],np.linspace(0,np.pi,34))
   # Reproject independently serialized rational coefficients as a fixed field.
   from types import SimpleNamespace
   holder=SimpleNamespace(beta=beta,s=1/beta,a0=1.,psi=b.psi,Cbase=storedC,Cnull=np.zeros((b.n,0)))
   audit=PrimitiveProblem(holder,held,64,'sinh');diag,fields=audit.diagnostics(np.zeros(0))
   singular=np.linalg.svd(fit.jac,compute_uv=False)
   row={'label':label,'state_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'beta':beta,'seed':seed,'free_beta':free,'nfev':fit.nfev,'status':int(fit.status),'message':fit.message,
      'objective_norm':float(np.linalg.norm(fit.fun)),'optimality':float(fit.optimality),'seconds':time.perf_counter()-tic,
      'jacobian_singular_largest':float(singular[0]),'jacobian_singular_smallest':float(singular[-1]),'max_absolute_C':float(abs(storedC).max()),'diagnostics':diag,
      'beta_bound_distance':min(beta-2.05,5-beta)if free else None,'verdict':'NO_ACCEPTED_CANDIDATE'}
   summary['states'].append(row);save();print('DONE',label,'beta',beta,'F',diag['thermal_divided']['max_ratio'],'seconds',row['seconds'],flush=True)
   # Small sampled artifacts only, no large quadrature matrices retained.
   np.savez_compressed(root/(label+'_heldout.npz'),points=held,**{k:fields[k]for k in ['RF','NF','Theta','Omega','S','Sy','H','A','B']})
   previous={'labels':b.labels,'C':storedC};del audit,fields,problem,case
summary['status']='COMPLETE_NO_CANDIDATE';summary['ended_utc']=datetime.now(timezone.utc).isoformat();save();print('COMPLETE',len(summary['states']),summary['elapsed_seconds'],flush=True)
