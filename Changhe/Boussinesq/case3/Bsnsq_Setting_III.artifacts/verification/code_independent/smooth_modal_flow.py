"""C1 velocity from C2 quintic stream interpolation, independent of fitting code."""
import numpy as np
from scipy.interpolate import BPoly,PPoly
from scipy.integrate import solve_ivp

class SmoothModalFlow:
 def __init__(self,beta,radii,pr,dp,H):
  self.beta=float(beta);self.radii=np.asarray(radii);self.s=np.log(self.radii)
  self.n=np.arange(1,np.shape(pr)[1]+1,dtype=float)
  fs=dp-pr;fss=(self.n**2-1)*pr-2*fs-self.radii[:,None]*H
  data=np.stack((pr,fs,fss),axis=1)
  self.poly=PPoly.from_bernstein_basis(BPoly.from_derivatives(self.s,data),extrapolate=False)
 def values(self,X):
  X=np.asarray(X,dtype=float);r=float(np.hypot(*X))
  if r<self.radii[0] or r>self.radii[-1]:raise ValueError(f'Point outside interpolation annulus: r={r}')
  s=np.log(r);f=self.poly(s);fs=self.poly(s,1);fss=self.poly(s,2)
  ph=np.arctan2(X[0],-X[1]);sn=np.sin(self.n*ph);cs=np.cos(self.n*ph)
  er=X/r;et=np.array([-er[1],er[0]])
  qr=np.dot(f+fs,sn);qt=np.dot(self.n*f,cs)
  V=-qt*er+qr*et
  Hrr=np.dot(fs+fss,sn)/r;Hrt=np.dot(self.n*fs,cs)/r;Htt=np.dot((1-self.n**2)*f+fs,sn)/r
  Q=np.column_stack((er,et));Hess=Q@np.array([[Hrr,Hrt],[Hrt,Htt]])@Q.T
  DV=np.array([[0.,-1.],[1.,0.]])@Hess
  return self.beta*X+V,self.beta*np.eye(2)+DV,-np.trace(Hess)
 def W(self,X):return self.values(X)[0]
 def DW(self,X):return self.values(X)[1]

def reconstruct(flow,Y,beta,a0,cutoff=1e-3,rtol=1e-10,atol=1e-13,max_time=250.,exact_seed=None,compatible_seed=False):
 Y=np.array(Y,dtype=float);rho=beta-2
 def event(t,X):return np.hypot(*X)-cutoff
 event.terminal=True;event.direction=-1
 back=solve_ivp(lambda t,X:-flow.W(X),(0.,max_time),Y,method='DOP853',events=event,dense_output=True,rtol=rtol,atol=atol,max_step=.2)
 if not back.success or not len(back.t_events[0]):
  return {'status':'BACKWARD_FAILED','message':back.message,'last_point':back.y[:,-1].tolist(),'last_time':float(back.t[-1])}
 T=float(back.t_events[0][0]);seed=back.y_events[0][0];theta0=a0*seed[0]**2;g0=np.array([2*a0*seed[0],0.]);o0=4*a0*seed[0]/beta
 if exact_seed is not None:theta0,g0,o0=exact_seed(seed)
 correction=np.zeros(2)
 if compatible_seed:
  normal=seed/np.linalg.norm(seed);Ws=flow.W(seed);flux=float(np.dot(Ws,normal))
  if flux<=0:raise ValueError('Cutoff boundary is not outgoing at the hit point')
  correction=normal*(rho*theta0-np.dot(Ws,g0))/flux;g0=g0+correction
 def rhs(s,v):
  point=back.sol(T-s);mat=rho*np.eye(2)-flow.DW(point).T
  return np.r_[mat@v[:2],v[0]-v[2]]
 fwd=solve_ivp(rhs,(0.,T),np.r_[g0,o0],method='DOP853',rtol=rtol,atol=atol,max_step=.2)
 return {'status':'COMPLETE' if fwd.success else 'FORWARD_FAILED','point':Y.tolist(),'cutoff':cutoff,'rtol':rtol,'atol':atol,
         'time_to_cutoff':T,'seed_point':seed.tolist(),'compatible_seed':compatible_seed,'gradient_seed_correction':correction.tolist(),'Theta':float(np.exp(rho*T)*theta0),'gradient':fwd.y[:2,-1].tolist(),
         'Omega':float(fwd.y[2,-1]),'backward_nfev':back.nfev,'forward_nfev':fwd.nfev}
