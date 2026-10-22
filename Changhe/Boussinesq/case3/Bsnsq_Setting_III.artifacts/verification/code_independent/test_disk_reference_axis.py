"""Independent packet123 disk-reference controls, based on Cartesian derivatives.

DOP853 evolves log(a),log(Q); Radau evolves an integrating factor and its
positive primitive. Narrow cutoff transitions are step-resolved in log radius.
All positivity statements here are sampled controls, not interval proofs.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
import json,math,hashlib
import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import expit
from global_axis_base import BaseAxis

class DiskAxis(BaseAxis):
 def __init__(self,beta,rho,a0=1.):
  super().__init__(beta,a0);self.rho=rho
 def values(self,logr,side):
  t=np.asarray(logr);r=np.exp(t);y=side*r
  vr,bp,lq=super().values(t,side)
  vr=np.array(vr,copy=True);bp=np.array(bp,copy=True);lq=np.array(lq,copy=True)
  inner=r<=self.rho
  vr=np.where(inner,self.mu,vr);bp=np.where(inner,self.mu,bp);lq=np.where(inner,math.log(4*self.a0/self.beta),lq)
  select=(r>self.rho)&(r<2*self.rho)
  if np.any(select):
   yy=np.atleast_1d(y)[np.atleast_1d(select)];rr=abs(yy);uu=rr/self.rho-1
   zz=1/uu-1/(1-uu);zzp=-1/uu**2-1/(1-uu)**2;zzpp=2/uu**3-2/(1-uu)**3
   chi=expit(zz);chip=chi*(1-chi)*zzp;chipp=chi*(1-chi)*((1-2*chi)*zzp**2+zzpp)
   cy=chip*side/self.rho;cyy=chipp/self.rho**2
   ss=self.L**2+(yy-self.h)**2
   g1=self.ell*(ss/self.S0)**self.p
   g1p=self.ell*2*self.p*(yy-self.h)/self.S0*(ss/self.S0)**(self.p-1)
   g1pp=self.ell*(2*self.p/self.S0*(ss/self.S0)**(self.p-1)+4*self.p*(self.p-1)*(yy-self.h)**2/self.S0**2*(ss/self.S0)**(self.p-2))
   # Stable g1_ref-ell is formed from g1_e-ell, not subtraction of large numbers.
   gd=self.ell*np.expm1(self.p*np.log1p((yy*yy-2*self.h*yy)/self.S0))
   d1=self.c*yy-gd;d1p=self.c-g1p;d1pp=-g1pp
   new_vr=self.beta+(gd+chi*d1)/yy
   new_bp=self.beta+g1p+cy*d1+chi*d1p
   g3=-self.B*self.p*ss**(self.p-1)
   d3=-4*self.a0/self.beta/6-g3
   new_g3=g3+chi*d3+chip*d1/(2*self.rho*rr)
   new_g1pp=g1pp+cyy*d1+2*cy*d1p+chi*d1pp
   qref=-new_g1pp-6*new_g3
   if np.min(qref)<=0:raise ValueError('sampled disk reference lost positive axis slope')
   if t.ndim==0:return float(new_vr[0]),float(new_bp[0]),float(np.log(qref[0]))
   vr[select]=new_vr;bp[select]=new_bp;lq[select]=np.log(qref)
  return vr,bp,lq
 def solve_checked(self,side,radii,form,rtol=1e-10):
  t0=math.log(self.rho/2);ts=np.log(radii)
  if form=='direct':
   def rhs(t,z):
    vr,bp,_=self.values(t,side)
    return [(2*bp-3*self.beta-2)/vr,(2*math.exp(z[0]-z[1])-(2*self.beta+1-bp))/vr]
   initial=[math.log(self.a0),math.log(4*self.a0/self.beta)];method='DOP853'
  else:
   rho0=(self.beta+1)/self.mu
   def rhs(t,z):
    vr,_,_=self.values(t,side)
    return [self.mu/vr-1,rho0-1+math.exp(-rho0*z[0]-z[1])]
   initial=[0.,-math.log1p(-rho0)];method='Radau'
  # First segment contains the whole cutoff transition and is forced to resolve it.
  split=math.log(4*self.rho);parts=[];nfev=0
  for lo,hi,step in [(t0,split,.015),(split,float(ts[-1]),1.0)]:
   sol=solve_ivp(rhs,(lo,hi),initial,method=method,rtol=rtol,atol=rtol*.03,max_step=step,dense_output=True)
   if not sol.success:raise RuntimeError(sol.message)
   parts.append(sol);initial=sol.y[:,-1];nfev+=sol.nfev
  zs=np.column_stack([parts[0 if t<=split else 1].sol(t)for t in ts]);vr,bp,lq=self.values(ts,side)
  if form=='direct':la,lQ=zs
  else:
   Z,LJ=zs;P=(2*self.beta+1)/self.mu
   la=math.log(self.a0)-2*math.log(self.mu)+2*np.log(vr)-2*Z
   lQ=math.log(2*self.a0)-2*math.log(self.mu)+np.log(vr)-P*Z+LJ
  return {'log_a':la,'log_Q':lQ,'ratio':np.exp(lQ-lq),'nfev':nfev}

if __name__=='__main__':
 root=Path('research/123_whole_axis_flat_realization/verification');root.mkdir(parents=True,exist_ok=True)
 start=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[]}
 for beta,rho in [(4.,.1),(4.,.05),(3.,.03)]:
  fld=DiskAxis(beta,rho)
  for side in [1,-1]:
   checkr=np.r_[np.geomspace(rho/10,1e8,501),rho*np.linspace(1,2,301)]
   v,b,q=fld.values(np.log(checkr),side)
   assert min(b)>(beta-2)/4 and min(v)>0
   radii=np.unique(np.r_[rho*np.array([.5,.65,.9,1,1.1,1.5,2.,4.]),1,10,100,1e4,1e8,1e24,1e48])
   direct=fld.solve_checked(side,radii,'direct',3e-11)
   factor=fld.solve_checked(side,radii,'factor',3e-11)
   refined=fld.solve_checked(side,radii,'direct',3e-12)
   err=max(float(np.max(abs(direct[k]-factor[k])))for k in ['log_a','log_Q'])
   er2=max(float(np.max(abs(direct[k]-refined[k])))for k in ['log_a','log_Q'])
   assert err<1e-7 and er2<1e-7,(beta,rho,side,err,er2)
   inner=radii<rho
   assert max(abs(direct['log_a'][inner]-math.log(fld.a0)))<2e-13
   assert max(abs(direct['log_Q'][inner]-math.log(4*fld.a0/beta)))<2e-13
   out['cases'].append({'beta':beta,'rho':rho,'side':side,'method_log_difference':err,'refinement_log_difference':er2,
    'minimum_sampled_bprime':float(min(b)),'minimum_sampled_qref':float(np.exp(min(q))),
    'nfev':[direct['nfev'],factor['nfev'],refined['nfev']],
    'rows':[{'r':float(r),'log_a':float(direct['log_a'][i]),'Q_over_qref':float(direct['ratio'][i])}for i,r in enumerate(radii)]})
   (root/'disk_axis_tests.json').write_text(json.dumps(out,indent=2)+'\n')
   print(beta,rho,side,'method/refine',err,er2,'Qratio_last',direct['ratio'][-1],flush=True)
 out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-start,
  scope='Sampled and ODE consistency controls only; global positivity and disk exactness are proved in PROOF.md.',
  code_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path(__file__).with_name('global_axis_base.py')]})
 (root/'disk_axis_tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
