from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import quad
import json,time,hashlib
from smooth_modal_flow import reconstruct
start=time.monotonic();root=Path('verification/characteristic_manufactured');root.mkdir(exist_ok=True,parents=True)
class Flow:
 beta=3.;lam=.5;mu=5.5;a=.3
 def jet(self,x):return x+self.a*x**3,1+3*self.a*x*x,6*self.a*x,6*self.a
 def W(self,X):
  x,y=X;f,p,q,u=self.jet(x);A=self.lam*f*q/p**2
  return np.array([self.lam*f/p,(self.mu+A)*y])
 def DW(self,X):
  x,y=X;f,p,q,u=self.jet(x);A=self.lam*f*q/p**2;Ax=self.lam*(q/p+f*u/p**2-2*f*q*q/p**3)
  return np.array([[self.lam*(1-f*q/p**2),0.],[Ax*y,self.mu+A]])
 def values(self,X):
  x,y=X;f,p,q,u=self.jet(x)
  def integral(t):
   xi=np.exp(-self.lam*t)*f
   xx=2/np.sqrt(3*self.a)*np.sinh(np.arcsinh(1.5*np.sqrt(3*self.a)*xi)/3)
   return np.exp(-(1+self.lam)*t)*self.jet(xx)[1]
  v,e=quad(integral,0.,45.,epsabs=1e-12,epsrel=1e-12)
  return f*f,np.array([2*f*p,0.]),2*f*v
flow=Flow();out={'started_utc':datetime.now(timezone.utc).isoformat(),'rows':[]}
for point in [[.4,.8],[1.,-1.],[2.,2.]]:
 th,gr,om=flow.values(point)
 for delta in [.03,.01,.003,.001]:
  r=reconstruct(flow,point,3.,1.,cutoff=delta,rtol=1e-12,atol=1e-15)
  assert r['status']=='COMPLETE'
  r.update(Theta_error=abs(r['Theta']-th),gradient_max_error=float(np.max(abs(np.array(r['gradient'])-gr))),Omega_error=abs(r['Omega']-om),exact_Theta=th,exact_gradient=gr.tolist(),independent_Omega_resolvent=om)
  out['rows'].append(r)
 print(point,[(r['cutoff'],r['Theta_error'],r['gradient_max_error'],r['Omega_error']) for r in out['rows'] if r['point']==point],flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Nontrivial cubic weak-coordinate manufacture tests cutoff convergence, not the coupled curl equation.')
(root/'cutoff_results.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'])
