"""Own stream-space manufactured zero and forcing continuation, single thread."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,time,hashlib,argparse,resource
import numpy as np
from scipy.optimize import least_squares
from stream_basis import StreamBasis,FitProblem,diagnostic_fields
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
ap=argparse.ArgumentParser();ap.add_argument('root',type=Path);ap.add_argument('--reference-root',type=Path,default=Path('verification/stream_basis_search_20261021T0216'));args=ap.parse_args();root=args.root;root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','scope':'artificial forcing control; unforced candidate only atlambda0 and only after checks','code_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path(__file__).with_name('stream_basis.py')]},'families':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
def grid(r,a):return np.stack([np.repeat(r,len(a))*np.tile(np.sin(a),len(r)),-np.repeat(r,len(a))*np.tile(np.cos(a),len(r))],axis=1)
def fraction(v):return str(Fraction(float(v)))
rng=np.random.default_rng(20261021)
for beta in [2.5,3.25]:
 label=f'b{beta:g}_i6_j7';basis=StreamBasis(beta,6,7);src=args.reference_root/(label+'_state.json');data=json.loads(src.read_text());C=np.array([float(Fraction(v))for v in data['C']]);D=np.array([float(Fraction(v))for v in data['D']]);zref=np.r_[basis.Cnull.T@(C-basis.Cbase),basis.Dnull.T@(D-basis.Dbase)];zstar=zref+.015*rng.standard_normal(basis.size)
 points=grid(np.geomspace(.015,3000,30),np.unique(np.r_[np.linspace(.03,np.pi-.03,20),.003,.01,np.pi-.01,np.pi-.003]));held=grid(np.unique(np.r_[np.geomspace(1e-4,1e7,41),.1,.3,1,3,10]),np.unique(np.r_[np.linspace(.015,np.pi-.015,31),.001,np.pi-.001]));holddata=basis.prepare(held)
 starC,starD=basis.coefficients(zstar);starfile=root/(label+'_forcing_state.json');starfile.write_text(json.dumps({'beta':fraction(beta),'a0':'1','ni':6,'nj':7,'shifts':[0,1],'labels':basis.labels,'C':[fraction(v)for v in starC],'D':[fraction(v)for v in starD],'source_fit':str(src),'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'definition':'fstar=F(star),gstar=G(star) as exact mathematical functions; stored rational coefficient values'},indent=2)+'\n')
 starhold=basis.fields(holddata,starC,starD);fam={'beta':beta,'label':label,'parameters':basis.size,'training_points':len(points),'heldout_points':len(held),'forcing_state_sha256':hashlib.sha256(starfile.read_bytes()).hexdigest(),'calibration':[],'continuation':[]};out['families'].append(fam);save()
 for reg,initial in [(0.,'zero'),(0.,'near_star'),(1e-5,'zero'),(1e-5,'near_star')]:
  prob=FitProblem(basis,points,regularization=reg);star=prob.residual(zstar);force=star.copy();force[2*len(points):]=0.;assert np.max(abs((prob.residual(zstar)-force)[:2*len(points)]))==0
  def fun(z):return prob.residual(z)-force
  z0=np.zeros(basis.size)if initial=='zero'else zstar+.003*rng.standard_normal(basis.size)
  fit=least_squares(fun,z0,jac=prob.jacobian,method='trf',max_nfev=500,ftol=3e-11,xtol=3e-11,gtol=2e-10,x_scale='jac');rr=fun(fit.x);cc,dd=basis.coefficients(fit.x);h=basis.fields(holddata,cc,dd);rec={'regularization':reg,'initial':initial,'nfev':fit.nfev,'optimizer_success':bool(fit.success),'weighted_PDE_norm':float(np.linalg.norm(rr[:2*len(points)])),'penalty_norm':float(np.linalg.norm(rr[2*len(points):])),'coefficient_distance_to_star':float(np.linalg.norm(fit.x-zstar)),'heldout_forced_absolute_F':float(np.max(abs(h['F']-starhold['F']))),'heldout_forced_absolute_G':float(np.max(abs(h['G']-starhold['G'])))};fam['calibration'].append(rec);save();print('CALIBRATE',beta,reg,initial,rec,flush=True)
 prob=FitProblem(basis,points,regularization=1e-5);star=prob.residual(zstar);force=star.copy();force[2*len(points):]=0;z=zstar.copy()
 for lam in [1.,.95,.9,.8,.65,.5,.35,.2,.1,0.]:
  def fun(z):return prob.residual(z)-lam*force
  fit=least_squares(fun,z,jac=prob.jacobian,method='trf',max_nfev=500,ftol=3e-11,xtol=3e-11,gtol=2e-10,x_scale='jac');z=fit.x;rr=fun(z);cc,dd=basis.coefficients(z);h=basis.fields(holddata,cc,dd);state={'beta':fraction(beta),'a0':'1','ni':6,'nj':7,'shifts':[0,1],'labels':basis.labels,'C':[fraction(v)for v in cc],'D':[fraction(v)for v in dd],'lambda':fraction(lam),'forcing_file':starfile.name,'center_float_defects':{'strain':float((basis.Cconstraint@cc-basis.Ctarget)[0]),'b0':float((basis.Cconstraint@cc-basis.Ctarget)[1]),'a0':float((basis.Dconstraint@dd-basis.Dtarget)[0])}}
  statefile=root/(label+f'_lambda{lam:g}.json');statefile.write_text(json.dumps(state,indent=2)+'\n');forced={}
  for f,n in [('F','NF'),('G','NG')]:
   numerator=abs(h[f]-lam*starhold[f]);denom=h[n]+lam*abs(starhold[f]);rat=np.divide(numerator,denom,out=np.where(numerator==0,0.,np.inf),where=denom!=0);idx=int(np.argmax(rat));forced[f]={'max_ratio':float(rat[idx]),'max_absolute':float(numerator.max()),'max_ratio_point':held[idx].tolist(),'zero_denominators':int((denom==0).sum())}
  rec={'lambda':lam,'nfev':fit.nfev,'optimizer_success':bool(fit.success),'optimizer_message':fit.message,'weighted_PDE_norm':float(np.linalg.norm(rr[:2*len(points)])),'penalty_norm':float(np.linalg.norm(rr[2*len(points):])),'unforced_heldout':diagnostic_fields(h),'forced_heldout':forced,'coefficient_norm':float(np.linalg.norm(z)),'state_file':statefile.name,'state_sha256':hashlib.sha256(statefile.read_bytes()).hexdigest()};fam['continuation'].append(rec);save();print('PATH',beta,lam,rec['weighted_PDE_norm'],forced['F']['max_ratio'],forced['G']['max_ratio'],rec['unforced_heldout']['F']['max_ratio'],rec['unforced_heldout']['G']['max_ratio'],flush=True)
  if lam==0.:np.savez_compressed(root/(label+'_lambda0_heldout.npz'),points=held,**h)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat());save();print('COMPLETE',out['elapsed_seconds'],flush=True)
