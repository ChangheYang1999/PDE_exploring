"""Independent controls for the smooth cone-supported endpoint deformation.

No fitting-lane code, servers, JS, GPU, or cluster use. Nonanalyticity and the
canonical inverse are proved in the accompanying informal proof, not sampled.
"""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
import numpy as np
import sympy as sp
from scipy.special import expit,erfcx
from scipy.integrate import solve_ivp
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','exact':[],'flows':[]}
x,y,d,e=sp.symbols('x y d e',positive=True)
z=sp.Function('eta')(y)
W=sp.Matrix([-4*y*sp.diff(z,y),4*y])
omega=-(sp.diff(W[1],x)-sp.diff(W[0],y))
f=4*y*sp.diff(omega,y)+omega
expeta=e*sp.exp(-d*d/(y*y));omexpected=-16*e*d*d*sp.exp(-d*d/y**2)*(d*d-y*y)/y**5
fexpected=-16*e*d*d*sp.exp(-d*d/y**2)*(8*d**4/y**7-27*d*d/y**5+11/y**3)
checks={
 'divergence_four':sp.diff(W[0],x)+sp.diff(W[1],y)-4,
 'prompt_vorticity_sign':omega+4*(sp.diff(z,y)+y*sp.diff(z,y,2)),
 'curve_vorticity_residual':f+4*sp.diff(z,y)+36*y*sp.diff(z,y,2)+16*y*y*sp.diff(z,y,3),
 'exponential_vorticity':omega.subs(z,expeta).doit()-omexpected,
 'exponential_residual':f.subs(z,expeta).doit()-fexpected,
 'shear_determinant':sp.Matrix([[1,-sp.diff(z,y)],[0,1]]).det()-1,
 'curve_tangency_x':W[0]-4*y*sp.diff(-z,y),
 'curve_tangency_y':W[1]-4*y,
 'residual_numerator_at_four':8*sp.Integer(4)**2-27*4+11-31,
 'positive_numerator_derivative_shift':sp.diff(8*x*x-27*x+11,x).subs(x,x+4)-(16*x+37)
}
for name,val in checks.items():
 simp=sp.simplify(val);out['exact'].append({'name':name,'value':str(simp),'pass':simp==0})
assert all(q['pass'] for q in out['exact'])

def cutoff(q,a,b):
 u=abs(q)
 if u<=a:return 1.,0.,0.
 if u>=b:return 0.,0.,0.
 t=(u-a)/(b-a);c=expit(1/t-1/(1-t));P=1/t**2+1/(1-t)**2;Pp=-2/t**3+2/(1-t)**3
 return c,-c*(1-c)*P*np.sign(q)/(b-a),c*(1-c)*((1-2*c)*P*P-Pp)/(b-a)**2

class Hamiltonian:
 def __init__(self,delta):self.A=3.;self.y0=2.;self.delta=delta;self.eps=delta/100
 def plus(self,x,y):
  Y=y-self.y0;u=x-self.A
  if Y==0 or abs(Y)>=self.delta or abs(u)>=abs(Y)/2:return 0.,np.zeros(2),np.zeros((2,2))
  D=self.delta;v=abs(Y);a=D/v;ex=np.exp(-a*a)
  eta=self.eps*ex;etap=eta*2*D*D/Y**3
  H=self.eps*np.sign(Y)*ex*(v-D*np.sqrt(np.pi)*erfcx(a))
  C,Cp,Cpp=cutoff(u/Y,.25,.5);Z,Zp,Zpp=cutoff(Y/D,.5,1.)
  Zp/=D;Zpp/=D*D
  K=H*Z;Kp=eta*Z+H*Zp;Kpp=etap*Z+2*eta*Zp+H*Zpp;q=u/Y
  hx=K*Cp/Y;hy=Kp*C-K*Cp*q/Y
  hxx=K*Cpp/Y**2;hxy=Kp*Cp/Y-K*(Cpp*q+Cp)/Y**2
  hyy=Kpp*C-2*Kp*Cp*q/Y+K*(Cpp*q*q+2*Cp*q)/Y**2
  return K*C,np.array([hx,hy]),np.array([[hxx,hxy],[hxy,hyy]])
 def all(self,x,y):
  a,g,H=self.plus(x,y);b,k,L=self.plus(-x,y)
  return a-b,np.array([g[0]+k[0],g[1]-k[1]]),np.array([[H[0,0]-L[0,0],H[0,1]+L[0,1]],[H[1,0]+L[1,0],H[1,1]-L[1,1]]])
 def ode(self,t,z):
  _,g,H=self.all(*z[:2]);vel=np.array([-g[1],g[0]]);A=np.array([-H[1],H[0]])
  return np.r_[vel,(A@z[2:].reshape(2,2)).ravel()]
 def flow(self,p,t=1.,rtol=2e-11):
  r=solve_ivp(self.ode,(0,t),np.r_[p,np.eye(2).ravel()],method='DOP853',rtol=rtol,atol=rtol*.01)
  assert r.success
  return r.y[:2,-1],r.y[2:,-1].reshape(2,2),r.nfev

for D in [.4,.8]:
 h=Hamiltonian(D);points=[]
 for Yf in [.2,.35,.5,-.35]:points.append(('exact_curve',[3.,2.+Yf*D]))
 for q,Yf in [(.35,.7),(-.35,.7),(.2,.85),(.4,-.75)]:points.append(('transition',[3.+q*Yf*D,2.+Yf*D]))
 for p in [[0.,0.],[.5,.2],[3.-.2*D,2.-.01*D],[3.+.2*D,2.+.01*D],[3.,2.],[8.,-3.]]:points.append(('protected',p))
 for rtol in [2e-10,2e-12]:
  for kind,p in points:
   p=np.array(p);a,J,n=h.flow(p,rtol=rtol);back,_,_=h.flow(a,t=-1,rtol=rtol);b,Jb,_=h.flow(p*np.array([-1.,1.]),rtol=rtol)
   errors={'inverse':float(np.max(abs(back-p))),'determinant':float(abs(np.linalg.det(J)-1)),'reflection':float(np.max(abs(b-a*np.array([-1.,1.]))))}
   if kind=='exact_curve':
    Y=p[1]-2.;et=h.eps*np.exp(-D*D/Y**2);expected=p+np.array([-et,0.]);jp=np.array([[1.,-2*D*D*et/Y**3],[0.,1.]])
    errors['exact_curve']=float(np.max(abs(a-expected)));errors['exact_jacobian']=float(np.max(abs(J-jp)))
   if kind=='protected':errors['fixed']=float(np.max(abs(a-p)))
   row={'delta':D,'rtol':rtol,'kind':kind,'initial':p.tolist(),'image':a.tolist(),'nfev':n,'errors':errors,'pass':max(errors.values())<5e-8};out['flows'].append(row)
   assert row['pass'],row
# The variational Jacobian is also compared against finite differences of the
# actual nonlinear flow in both cutoff transitions, so area preservation alone
# cannot hide an incorrect Hamiltonian Hessian.
out['flow_jacobian_differences']=[]
for D in [.4,.8]:
 h=Hamiltonian(D)
 for q,Yf in [(.35,.7),(-.35,.7),(.2,.85),(.4,-.75)]:
  p=np.array([3.+q*Yf*D,2.+Yf*D]);_,J,_=h.flow(p,rtol=2e-12)
  for relative_step in [1e-4,5e-5,2.5e-5]:
   step=D*relative_step;cols=[]
   for j in range(2):
    dv=np.eye(2)[j]*step
    plus,_,_=h.flow(p+dv,rtol=2e-12);minus,_,_=h.flow(p-dv,rtol=2e-12)
    cols.append((plus-minus)/(2*step))
   error=float(np.max(abs(np.column_stack(cols)-J)))
   row={'delta':D,'initial':p.tolist(),'relative_step':relative_step,'absolute_error':error,'pass':error<2e-7}
   out['flow_jacobian_differences'].append(row)
   assert row['pass'],row

out.update(status='PASS',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['proof_sha256']=hashlib.sha256(Path('research/159_nonanalytic_endpoint_deformation/PROOF.md').read_bytes()).hexdigest()
out['max_errors']={key:max(row['errors'].get(key,0.) for row in out['flows']) for key in ['inverse','determinant','reflection','exact_curve','exact_jacobian','fixed']}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({key:out[key] for key in ['started_utc','status','ended_utc','elapsed_seconds','max_errors']},indent=2))
