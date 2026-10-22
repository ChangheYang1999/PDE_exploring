from pathlib import Path
import time,json
import numpy as np
import mpmath as mp
from stream_basis import StreamBasis,FitProblem,evaluate_terms
from cartesian_inverse import CartesianInverse,InverseSettings
start=time.monotonic();mp.mp.dps=60;out={'value_checks':[],'jacobian_checks':[],'inverse_checks':[]}
for b in [2.5,3.25]:
 basis=StreamBasis(b,4,5);bs=mp.mpf(b);s=1/bs
 for label in [(0,0,0),(1,1,0),(3,4,1),(2,3,1)]:
  i,j,shift=label;k=basis.labels.index(label)
  def raw(x,y):
   R=mp.sqrt(1+x*x+y*y);return x*R**(1-s-shift)*mp.chebyt(i,2*R**(-s)-1)*mp.chebyt(j,y/R)
  gauge=mp.diff(lambda x:raw(x,mp.mpf(0)),mp.mpf(0))
  def psi(x,y):return raw(x,y)-gauge*x
  def td(x,y):
   R=mp.sqrt(1+x*x+y*y);return x*x*R**(-1-2*s-shift)*mp.chebyt(i,2*R**(-s)-1)*mp.chebyt(j,y/R)
  def diff(fun,a,c,x,y):return mp.diff(lambda xx:mp.diff(lambda yy:fun(xx,yy),y,c),x,a)
  for point in [('.2','.3'),('2','-1'),('100','31')]:
   x,y=map(mp.mpf,point);ref={'Psi':psi(x,y),'U1':-diff(psi,0,1,x,y),'U2':diff(psi,1,0,x,y),'Omega':-diff(psi,2,0,x,y)-diff(psi,0,2,x,y),'Omega_x':-diff(psi,3,0,x,y)-diff(psi,1,2,x,y),'Omega_y':-diff(psi,2,1,x,y)-diff(psi,0,3,x,y),'Theta':td(x,y),'Theta_x':diff(td,1,0,x,y),'Theta_y':diff(td,0,1,x,y)}
   errors={}
   for key,v in ref.items():
    terms=(basis.psi[k]if key in basis.psi[k]else basis.theta[k])[key];got=float(evaluate_terms(terms,float(x),float(y),basis.s));errors[key]=abs(got-float(v))/max(1,abs(float(v)))
   assert max(errors.values())<2e-9,(b,label,point,errors);out['value_checks'].append({'beta':b,'label':label,'point':point,'relative_errors':errors})
 pts=np.array([[.1,.2],[.7,-.3],[1.4,2.1],[7,-4.]])
 prob=FitProblem(basis,pts);rng=np.random.default_rng(927);z=rng.normal(size=basis.size)*.02;direction=rng.normal(size=basis.size);direction/=np.linalg.norm(direction);exact=prob.jacobian(z)@direction
 for hh in [1e-5,3e-6]:
  measured=(prob.residual(z+hh*direction)-prob.residual(z-hh*direction))/(2*hh);err=float(np.max(abs(measured-exact))/max(1,np.max(abs(exact))));assert err<1e-7;out['jacobian_checks'].append({'beta':b,'step':hh,'relative_error':err})
 C,D=basis.coefficients(np.zeros(basis.size));points=np.array([[.4,-.7],[2.1,1.3]]);f=basis.fields(basis.prepare(points),C,D);ref=np.column_stack([f['U1'],f['U2']]);source=basis.omega_callable(C)
 for order in [24,48]:
  inv=CartesianInverse(source,InverseSettings(radius=8,core_radial_order=14,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/b));got=inv.relative(points);err=float(np.max(abs(got-ref)));out['inverse_checks'].append({'beta':b,'order':order,'max_absolute_error':err,'values':got.tolist(),'reference':ref.tolist()})
 assert out['inverse_checks'][-1]['max_absolute_error']<2e-7,out['inverse_checks'][-1]
out['elapsed_seconds']=time.monotonic()-start;out['status']='CONFIRMED';Path('research/108_independent_stream_basis_solver/verification/own_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],'MP values',len(out['value_checks']),'Jacobian',len(out['jacobian_checks']),'full-plane inverse',len(out['inverse_checks']),'seconds',out['elapsed_seconds'],flush=True)
