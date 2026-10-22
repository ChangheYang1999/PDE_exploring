"""Bounded, single-thread independent physical-stream least-squares pilot."""
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import argparse,json,time,hashlib,resource,sys
import numpy as np
from scipy.optimize import least_squares
from stream_basis import StreamBasis,FitProblem,diagnostic_fields
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--betas',default='2.25,2.5,2.75,3.25,3.5,4.25');ap.add_argument('--levels',default='4:5,6:7');ap.add_argument('--max-nfev',type=int,default=350);ap.add_argument('--regularization',type=float,default=1e-5);args=ap.parse_args();root=args.root;root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();summary={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','scope':'independent trial-space search; no candidate acceptance','states':[]};betas=[float(x)for x in args.betas.split(',')];levels=[tuple(map(int,x.split(':')))for x in args.levels.split(',')]
codefiles=[Path(__file__),Path(__file__).with_name('stream_basis.py')];summary['code_sha256']={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in codefiles}
def save_summary():
 summary['elapsed_seconds']=time.monotonic()-start;(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
def grid(radii,angles):return np.stack([np.repeat(radii,len(angles))*np.tile(np.sin(angles),len(radii)),-np.repeat(radii,len(angles))*np.tile(np.cos(angles),len(radii))],axis=1)
heldout=grid(np.unique(np.r_[np.geomspace(1e-4,1e7,41),.1,.3,1.,3.,10.]),np.unique(np.r_[np.linspace(.015,np.pi-.015,31),.001,np.pi-.001]))
for beta in betas:
 if abs(beta-round(beta))<1e-12:raise ValueError('First pilot excludes integer beta logarithmic resonance')
 old=None
 for ni,nj in levels:
  label=f'b{beta:g}_i{ni}_j{nj}';t0=time.monotonic();basis=StreamBasis(beta,ni,nj);radii=np.geomspace(.015,3000,max(20,ni*5));angles=np.unique(np.r_[np.linspace(.03,np.pi-.03,max(16,2*nj+6)),.003,.01,np.pi-.01,np.pi-.003]);points=grid(radii,angles);prob=FitProblem(basis,points,args.regularization);z0=np.zeros(basis.size)
  if old is not None:
   oldbasis,oldC,oldD=old;C=np.zeros(basis.n);D=np.zeros(basis.n)
   for k,l in enumerate(oldbasis.labels):kk=basis.labels.index(l);C[kk]=oldC[k];D[kk]=oldD[k]
   z0=np.r_[basis.Cnull.T@(C-basis.Cbase),basis.Dnull.T@(D-basis.Dbase)]
  best={'loss':float('inf'),'calls':0};state={'label':label,'beta':beta,'ni':ni,'nj':nj,'shifts':[0,1],'parameters':basis.size,'training_points':len(points),'heldout_points':len(heldout),'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat()};summary['states'].append(state);save_summary()
  def write_state(z,kind):
   C,D=basis.coefficients(z);f=lambda val:str(Fraction(float(val)));data={'kind':kind,'label':label,'beta':f(beta),'a0':f(1.),'ni':ni,'nj':nj,'shifts':[0,1],'labels':basis.labels,'C':[f(v)for v in C],'D':[f(v)for v in D],'center_float_defects':{'strain':float((basis.Cconstraint@C-basis.Ctarget)[0]),'b0':float((basis.Cconstraint@C-basis.Ctarget)[1]),'a0':float((basis.Dconstraint@D-basis.Dtarget)[0])},'code_sha256':summary['code_sha256']};path=root/(label+'_state.json');path.write_text(json.dumps(data,indent=2)+'\n');return C,D,path
  def fun(z):
   rr=prob.residual(z);best['calls']+=1;loss=float(np.dot(rr,rr))
   if loss<best['loss']:
    best['loss']=loss
    if best['calls']==1 or best['calls']%20==0:write_state(z,'checkpoint')
   if best['calls']%20==0:print(label,'calls',best['calls'],'best objective',format(best['loss'],'.7g'),'seconds',round(time.monotonic()-t0,2),flush=True)
   return rr
  baseline=prob.residual(z0);state['initial_objective']=float(np.dot(baseline,baseline));print('START',label,'parameters',basis.size,'grid',len(points),'objective',state['initial_objective'],flush=True)
  fit=least_squares(fun,z0,jac=prob.jacobian,method='trf',max_nfev=args.max_nfev,ftol=2e-10,xtol=2e-10,gtol=2e-9,x_scale='jac')
  C,D,path=write_state(fit.x,'completed_fit');train=basis.fields(prob.data,C,D);hold=basis.fields(basis.prepare(heldout),C,D);state.update(status='COMPLETE',optimizer_success=bool(fit.success),optimizer_message=fit.message,nfev=fit.nfev,njev=fit.njev,objective=float(2*fit.cost),optimality=float(fit.optimality),train=diagnostic_fields(train),heldout=diagnostic_fields(hold),elapsed_seconds=time.monotonic()-t0,state_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),state_file=path.name)
  regions={};hr=np.linalg.norm(heldout,axis=1)
  for region,mask in [('inner',hr<.1),('core',(hr>=.1)&(hr<=10)),('outer',(hr>10)&(hr<=1e3)),('far',hr>1e3)]:regions[region]=diagnostic_fields({k:v[mask]for k,v in hold.items()})
  state['regions']=regions;np.savez_compressed(root/(label+'_heldout.npz'),points=heldout,**hold);old=(basis,C,D);save_summary();print('DONE',label,'objective',state['objective'],'heldout F/G ratios',state['heldout']['F']['max_ratio'],state['heldout']['G']['max_ratio'],'seconds',state['elapsed_seconds'],flush=True)
summary['status']='COMPLETE';summary['ended_utc']=datetime.now(timezone.utc).isoformat();save_summary();print('COMPLETE',summary['elapsed_seconds'],flush=True)
