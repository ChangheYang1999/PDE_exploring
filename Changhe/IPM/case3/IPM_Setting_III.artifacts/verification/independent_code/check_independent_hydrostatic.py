"""Manufactured gate for result185. Producer code is not imported."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,math,time
import numpy as np
import mpmath as mp
from scipy.special import erf
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf
from independent_hydrostatic import CartesianQJet,VerticalInverse,exact_hydrostatic_center,quadrature_hydrostatic_center,AnisotropicRegauge
root=Path('research/independent_hydrostatic_evaluator/verification');root.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();rows=[];start=time.monotonic()
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),status='RUNNING',code_sha256=sha(__file__),evaluator_sha256=sha('independent_code/independent_hydrostatic.py'),proof_sha256=sha(root.parent/'PROOF.md'),checks=rows)
def save():(root/'GATE.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,value,tol,**extra):
 row=dict(name=name,error=float(value),tolerance=tol,passed=bool(value<=tol),**extra);rows.append(row);save()
 if not row['passed']:print(json.dumps(row),flush=True)
# Gaussian inverse: exact, with several scales and all quadrant parities.
for tau in [.125,1.,3.]:
 def jet(x,y):
  x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));f=np.exp(-x*x-tau*y*y)
  return np.stack([y*f,-2*x*y*f,(1-2*tau*y*y)*f,(4*x*x-2)*y*f],axis=-1)
 inv=VerticalInverse(jet,.5,order=20,tail_order=80,tail_scale=32.)
 for x,y in [(0.,0.),(0.,.7),(.3,.5),(2.,3.),(-.3,.5),(.3,-.5),(-.3,-.5),(1.2,0.)]:
  val=inv.at(x,y);expected=[x*np.exp(-x*x-tau*y*y)/tau,(4*x*x-2)*np.exp(-x*x)*np.sqrt(np.pi)*erf(np.sqrt(tau)*y)/(4*tau**1.5)]
  phi=-x*np.exp(-x*x)*np.sqrt(np.pi)*erf(np.sqrt(tau)*y)/(2*tau**1.5)
  check('Gaussian full inverse',max(abs(np.array(val['V'])-expected).max(),abs(val['Phi']-phi)),5e-12,tau=tau,point=[x,y])
 check('Gaussian center',abs(inv.center()+1/tau),5e-12,tau=tau)
 x,y=.3,.7;h=.0004
 div=(inv.at(x+h,y)['V'][0]-inv.at(x-h,y)['V'][0]+inv.at(x,y+h)['V'][1]-inv.at(x,y-h)['V'][1])/(2*h)
 pyy=(inv.at(x,y+h)['Phi']-2*inv.at(x,y)['Phi']+inv.at(x,y-h)['Phi'])/h**2
 check('Gaussian divergence finite difference',abs(div),2e-6,tau=tau)
 check('Gaussian hydrostatic Poisson finite difference',abs(-pyy-jet(x,y)[1]),2e-7,tau=tau)
# Polynomial manufactures, including a shifted basis with exact saved nodes.
for basis,M in [('cheb',1),('cheb',4),('local',4)]:
 N=6;tk=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1));cc=[]
 for k in range(M):
  c=np.array([((-1.)**(j+k))/(2.**(2*j+2*k+1))for j in range(N+1-k)]);cc.append(c)
 path=root/f'manufacture_{basis}_M{M}.npz';np.savez_compressed(path,u=np.concatenate(cc),N=N,M=M,basis=basis,tk=tk,L=.75,p=1.5,cl=3.)
 q=QLocalCheckpoint(path);j=CartesianQJet(q);coeff=q.exact_coefficients();exact=exact_hydrostatic_center(coeff,F(q.kappa))
 for order in [4,8,20]:check('exact polynomial center vs Gauss',abs(quadrature_hydrostatic_center(q,order)-float(exact)),8e-13,basis=basis,M=M,order=order,center_exact=str(exact))
 for order,ntail,scale in [(16,64,32.),(24,128,128.),(32,256,512.)]:
  inv=VerticalInverse(j.jet,j.p,order=order,tail_order=ntail,tail_scale=scale,inner_scale=.2)
  check('full vertical center vs rational',abs(inv.center()-float(exact)),3e-8 if ntail==64 else 2e-9,basis=basis,M=M,order=order,tail_order=ntail,scale=scale)
  if M==1:
   for x,y in [(.3,.5),(2.,3.),(1.,0.)]:
    expected=x*float(q.rho(x,y)/y)if y else x*float(j.jet(x,0.)[2])
    check('radial exact V1',abs(inv.at(x,y)['V'][0]-expected),3e-8 if ntail==64 else 2e-9,point=[x,y],order=order)
 with mp.workdps(75):
  mm=MPQDensity.__new__(MPQDensity);mm.coeff=[[mf(v)for v in row]for row in coeff];mm.L=mf(q.L);mm.kappa=mf(q.kappa);mm.ell=mf(q.cl)
  def rho(x,y):
   r=mp.sqrt(x*x+y*y)
   if not r:return mp.mpf(0)
   return r*mm.at(r,mp.atan2(y,x))[0]
  for x,y in [(.3,.5),(2.,3.),(.002,.003),(0.,.7),(-.3,.5),(.3,-.5),(1.2,0.)]:
   v=j.jet(x,y);X,Y=mf(x),mf(y);ref=[rho(X,Y),mp.diff(lambda t:rho(t,Y),X),mp.diff(lambda t:rho(X,t),Y),mp.diff(lambda t:rho(t,Y),X,2)]
   errors=[float(abs(mf(vv)-rr))for vv,rr in zip(v,ref)]
   check('Cartesian analytic jet vs MP scalar differentiation',max(errors),3e-10,basis=basis,M=M,point=[x,y],errors=errors,mp_values=[mp.nstr(z,70)for z in ref])
   h=1e-3*max(1.,abs(x),abs(y));f=lambda z:float(q.rho(z,y));fd=(-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h*h)
   check('Cartesian second finite difference',abs(fd-v[3]),2e-5,basis=basis,M=M,point=[x,y],h=h)
 a=float(q.polynomial(0,np.array(-1.)));K=sum((-1)**k*sum(row)for k,row in enumerate(coeff))*F(.5);K=float(K)*q.L**(1/q.kappa)
 if a>0 and K>0:
  ag=AnisotropicRegauge(j,a,K);original=VerticalInverse(j.jet,j.p,24,128,128.,.2);transformed=VerticalInverse(ag.jet,ag.p,24,128,128.,.2)
  for x,y in [(.3,.5),(0.,.7),(1.,0.)]:
   before=original.at(ag.h*x/ag.length,y/ag.length);after=transformed.at(x,y);ref=np.array(before['V'])*np.array([ag.length/ag.h,ag.length])
   check('anisotropic inverse scaling',max(abs(np.array(after['V'])-ref)),2e-8,basis=basis,M=M,point=[x,y])
  check('anisotropic exact center invariance',abs(transformed.center()-float(exact)),2e-8,basis=basis,M=M)
out.update(status='PASS'if all(r['passed']for r in rows)else 'FAIL',finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print(json.dumps({k:v for k,v in out.items()if k!='checks'}));print('checks',len(rows),'failed',sum(not r['passed']for r in rows))
