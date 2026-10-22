"""Meaningful independent controls for packet114's new axis and beta calculus."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
import mpmath as mp
from scipy.optimize import least_squares
from free_beta_stream import make_chart,FreeBetaProblem,prepare_divided,divided_fields,grid
start=time.monotonic();root=Path('research/114_free_beta_stream_solver/verification');root.mkdir(exist_ok=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','jacobians':[],'axis_mp':[]};rng=np.random.default_rng(421114)
points=np.array([[0,0],[0,.2],[0,-1.4],[.001,.3],[.1,-.2],[-.1,-.2],[1.1,.8],[3,-2],[10,5]],float)
for beta in [2.4,3.,4.5]:
 pr=FreeBetaProblem(3,4,points,beta);base=pr.case(beta).basis;z=np.r_[beta,rng.normal(0,.025,base.size)]
 J=pr.jacobian(z);direction=rng.normal(size=len(z));direction/=np.linalg.norm(direction)
 errors=[]
 for h in [2e-5,1e-5]:
  fd=(pr.residual(z-2*h*direction)-8*pr.residual(z-h*direction)+8*pr.residual(z+h*direction)-pr.residual(z+2*h*direction))/(12*h)
  error=np.linalg.norm(fd-J@direction)/max(1.,np.linalg.norm(fd));errors.append(float(error));assert error<2e-6,(beta,error)
 out['jacobians'].append({'beta':beta,'directional_5point_relative_errors':errors})
 # A direct elementary-function expression, differentiated by mpmath, is independent
 # of the monomial division and derivative implementation used in the new evaluator.
 mp.mp.dps=50;C,D=base.coefficients(z[1:]);cm=list(map(mp.mpf,C));dm=list(map(mp.mpf,D));bb=mp.mpf(beta);s=1/bb
 gauge=sum(c*mp.chebyt(j,0) for c,(i,j,d) in zip(cm,base.labels))
 def psi(x,y):
  R=mp.sqrt(1+x*x+y*y);u=2*R**(-s)-1;v=y/R
  return sum(c*x*R**(1-s-d)*mp.chebyt(i,u)*mp.chebyt(j,v) for c,(i,j,d) in zip(cm,base.labels))-gauge*x
 def theta(x,y):
  R=mp.sqrt(1+x*x+y*y);u=2*R**(-s)-1;v=y/R
  return sum(c*x*x*R**(-1-2*s-d)*mp.chebyt(i,u)*mp.chebyt(j,v) for c,(i,j,d) in zip(dm,base.labels))
 for yy in [0.,.35,-1.2]:
  y=mp.mpf(yy);A=bb-mp.diff(psi,(0,y),(1,1));B=bb*y+mp.diff(psi,(0,y),(1,0))
  f=mp.diff(theta,(0,y),(2,0))/2;fy=mp.diff(theta,(0,y),(2,1))/2
  g=-mp.diff(psi,(0,y),(3,0))-mp.diff(psi,(0,y),(1,2));gy=-mp.diff(psi,(0,y),(3,1))-mp.diff(psi,(0,y),(1,3))
  ref={'A':A,'B':B,'f':f,'fy':fy,'g':g,'gy':gy,'RF':(2*A-bb+2)*f+B*fy,'RG':(A+1)*g+B*gy-2*f}
  own=divided_fields(base,prepare_divided(base,np.array([[0,yy]],float)),C,D)
  errs={k:float(abs(mp.mpf(float(own[k][0]))-v)/max(1,abs(v))) for k,v in ref.items()}
  assert max(errs.values())<3e-10,(beta,yy,errs)
  out['axis_mp'].append({'beta':beta,'y':yy,'relative_to_max_1_errors':errs,'reference':{k:mp.nstr(v,35) for k,v in ref.items()}})
# Exact integer-beta identity: R^-1=(1+u)^3/8.
b=make_chart(3.,4,4);weights=[5/16,15/32,3/16,1/32];kernel=[]
for j in [0,1,2,3]:
 C=np.zeros(b.n);C[b.labels.index((0,j,1))]=1
 for i,w in enumerate(weights):C[b.labels.index((i,j,0))]-=w
 data=b.prepare(points);errs={k:float(np.max(abs(m@C))) for k,m in (data['psi']|data['theta']).items()}
 assert max(errs.values())<1e-9,(j,errs);kernel.append({'angular_j':j,'absolute_field_errors':errs})
out['integer_beta_kernel']={'beta':3,'shift0_coefficients':['5/16','15/32','3/16','1/32'],'checks':kernel}
# A manufactured finite-dimensional residual. This is an algorithm control, not B2.
pts=grid(np.geomspace(.03,20,10),np.linspace(0,np.pi,11));p=FreeBetaProblem(3,4,pts,3.17);bs=p.case(3.17).basis
truth=np.r_[3.17,rng.normal(0,.012,bs.size)];forcing=p.residual(truth);initial=truth+rng.normal(0,.001,len(truth));initial[0]+=.025
fit=least_squares(lambda z:p.residual(z)-forcing,initial,jac=p.jacobian,bounds=(np.r_[2.01,np.full(bs.size,-np.inf)],np.r_[8.,np.full(bs.size,np.inf)]),max_nfev=100,ftol=1e-12,xtol=1e-12,gtol=1e-10,x_scale='jac')
err=float(np.max(abs(p.residual(fit.x)-forcing)));out['manufactured_fit']={'maximum_weighted_residual':err,'nfev':fit.nfev,'njev':fit.njev,'beta_target':3.17,'beta_returned':float(fit.x[0]),'optimizer_message':fit.message,'optimality':float(fit.optimality),'parameter_distance_from_target':float(np.linalg.norm(fit.x-truth)),'meaning':'forced finite-dimensional consistency test, not a profile; coefficients/beta need not be unique'}
assert err<2e-8,out['manufactured_fit']
out.update(status='CONFIRMED',elapsed_seconds=time.monotonic()-start,code_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('free_beta_stream.py'),Path(__file__).with_name('stream_basis.py')]})
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'elapsed_seconds':out['elapsed_seconds'],'jacobian_max':max(max(q['directional_5point_relative_errors'])for q in out['jacobians']),'axis_max':max(max(q['relative_to_max_1_errors'].values())for q in out['axis_mp']),'manufactured':out['manufactured_fit']},indent=2),flush=True)
