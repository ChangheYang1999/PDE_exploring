import os
for name in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[name]='1'
from pathlib import Path
from fractions import Fraction
from datetime import datetime,timezone
import argparse,json,hashlib,time
import numpy as np
from scipy.optimize import least_squares
from negative_slope_dictionary import dictionary,affine,start,evaluate,residual
P=argparse.ArgumentParser();P.add_argument('--cl',default='2');P.add_argument('--a0',type=float,default=-4);P.add_argument('--M',type=int,default=4);P.add_argument('--J',type=int,default=4);P.add_argument('--L',type=int,default=3);P.add_argument('--cap',type=int,default=180);P.add_argument('--name',default='cl2_M4_J4_L3_a0m4');args=P.parse_args()
R=Path('research/negative_slope_independent_trials');V=R/'verification';dest=V/'trials'/args.name
if dest.exists():raise RuntimeError('do not overwrite a trial')
dest.mkdir(parents=True);sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
gate=json.loads((V/'DICTIONARY_CHECKS.json').read_text())
assert gate['status']=='PASS' and gate['count']==653 and all(z['passed']for z in gate['checks'])
assert gate['module_sha256']==sha(Path('independent_code/negative_slope_dictionary.py')) and gate['addendum_sha256']==sha(R/'DICTIONARY_ADDENDUM.md')
cl=Fraction(args.cl);p=1/cl;rows=dictionary(p,args.M,args.J,args.L);base,T,k,s,c=affine(rows,p);theta=np.r_[(np.arange(24)+.5)*np.pi/48,np.pi/2]
rr,tt=np.meshgrid(np.geomspace(1e-4,1e3,72),theta,indexing='ij');r=rr.ravel();th=tt.ravel();x=r*np.cos(th);y=r*np.sin(th);weights=1/(np.sqrt(len(r))*r*(1+r*r)**((float(p)-1)/2)*np.sin(th))
fields=evaluate(rows,x,y);z0=start(rows,p,args.a0);lo=np.full(len(z0),-1e6);hi=np.full(len(z0),1e6);lo[0]=-1e4;hi[0]=-1e-5
np.savez_compressed(dest/'TRAINING.npz',x=x,y=y,weights=weights,initial=z0,lower=lo,upper=hi)
started=datetime.now(timezone.utc).isoformat();clock0=time.monotonic();calls=0;cache={};history=[]
def calc(z,record):
 global calls
 if 'z' in cache and np.array_equal(cache['z'],z):return cache['F'],cache['J']
 a=base+T@z;res,_,_,jac,_=residual(fields,a,x,y,float(cl));F=np.r_[weights*res,10*(float(cl)+c@a-1)];J=np.vstack([weights[:,None]*(jac@T),10*c@T])
 cache.update(z=z.copy(),F=F,J=J)
 if record:
  calls+=1;row=dict(call=calls,elapsed=time.monotonic()-clock0,objective=float(F@F/2),a0=float(s@a),center_defect=float(float(cl)+c@a-1),coefficient_max=float(np.max(abs(a))))
  history.append(row)
  if calls==1 or calls%10==0:
   (dest/'PROGRESS.json').write_text(json.dumps(row,indent=2)+'\n');print(json.dumps(row),flush=True)
 return F,J
try:
 fit=least_squares(lambda z:calc(z,True)[0],z0,jac=lambda z:calc(z,False)[1],bounds=(lo,hi),max_nfev=args.cap,x_scale='jac',ftol=1e-11,xtol=1e-11,gtol=1e-11)
 z=fit.x;a=base+T@z
 theta2=np.r_[(np.arange(31)+.371)*np.pi/62,np.pi/2];rv,tv=np.meshgrid(np.geomspace(7e-5,1.7e3,91),theta2,indexing='ij')
 rad=np.r_[rv.ravel(),np.geomspace(2e3,1e7,24)];ang=np.r_[tv.ravel(),np.full(24,np.pi/2)];xx=rad*np.cos(ang);yy=rad*np.sin(ang)
 ff=evaluate(rows,xx,yy);res,nf,nv,_,dd=residual(ff,a,xx,yy,float(cl));rf=np.divide(abs(res),nf,out=np.full_like(res,np.nan),where=nf>0);rvv=np.divide(abs(res),nv,out=np.full_like(res,np.nan),where=nv>0)
 np.savez_compressed(dest/'VALIDATION.npz',x=xx,y=yy,r=rad,theta=ang,R=res,Nf=nf,Nv=nv,rho=dd['rho'],ux=dd['ux'],uy=dd['uy'],dx=dd['dx'],dy=dd['dy'])
 regions={}
 for name,mask in [('all',np.ones(len(rad),bool)),('tiny',rad<.01),('inner',(rad>=.01)&(rad<1)),('core',(rad>=1)&(rad<100)),('far',rad>=100)]:
  ids=np.flatnonzero(mask);vals={}
  for key,v in [('absolute',abs(res)),('Rf',rf),('Rv',rvv)]:
   w=int(ids[np.nanargmax(v[ids])]);vals[key]=dict(value=float(v[w]),point_index=w,x=float(xx[w]),y=float(yy[w]))
  regions[name]=dict(count=len(ids),maxima=vals)
 ax=np.isclose(ang,np.pi/2,rtol=0,atol=1e-15)
 out=dict(status='DONE',interpretation='finite exploratory fit only; independent MP candidate validation pending',started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-clock0,arguments=vars(args),c_l=str(cl),p=str(p),dictionary=rows,coefficients_hex=[float(v).hex()for v in a],coordinates_hex=[float(v).hex()for v in z],a0=float(s@a),K=float(k@a),strain=float(c@a),center_defect=float(float(cl)+c@a-1),coefficient_max=float(np.max(abs(a))),slope_bound_distance=float(min(z[0]-lo[0],hi[0]-z[0])),other_bound_distance=float(np.min(np.minimum(z[1:]-lo[1:],hi[1:]-z[1:]))),optimizer=dict(status=int(fit.status),message=fit.message,nfev=fit.nfev,njev=fit.njev,cost=float(fit.cost),optimality=float(fit.optimality),actual_objective_calls=calls),regions=regions,axis_positive_samples=int(np.sum(dd['rho'][ax]>0)),axis_negative_samples=int(np.sum(dd['rho'][ax]<0)),undefined_Nf=int(np.sum(nf<=0)),undefined_Nv=int(np.sum(nv<=0)),proof_sha256=sha(R/'PROOF.md'),addendum_sha256=sha(R/'DICTIONARY_ADDENDUM.md'),protocol_sha256=sha(R/'SOLVER_PROTOCOL.md'),module_sha256=sha(Path('independent_code/negative_slope_dictionary.py')),driver_sha256=sha(Path(__file__)),gate_sha256=sha(V/'DICTIONARY_CHECKS.json'))
 (dest/'HISTORY.json').write_text(json.dumps(history,indent=2)+'\n');(dest/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({key:out[key]for key in ['status','elapsed_seconds','a0','center_defect','optimizer','regions']},indent=2),flush=True)
except Exception as exc:
 (dest/'FAILURE.json').write_text(json.dumps(dict(utc=datetime.now(timezone.utc).isoformat(),error_type=type(exc).__name__,error=str(exc),history=history),indent=2)+'\n');raise
