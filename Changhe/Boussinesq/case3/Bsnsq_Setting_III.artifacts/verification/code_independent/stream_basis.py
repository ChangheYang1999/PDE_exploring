"""Independent smooth physical stream basis and analytic monomial derivatives.

No numerics/lead imports, spline calculus, automatic differentiation, or FFT.
See research/108_independent_stream_basis_solver/PROOF.md.
"""
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
from scipy.linalg import null_space

@lru_cache(None)
def cheb_poly(n,offset=0,scale=1):
 if n==0:return (1,)
 if n==1:return (offset,scale)
 p=list(cheb_poly(n-1,offset,scale));q=list(cheb_poly(n-2,offset,scale));ans=[0]*(len(p)+1)
 for i,v in enumerate(p):ans[i]+=2*offset*v;ans[i+1]+=2*scale*v
 for i,v in enumerate(q):ans[i]-=v
 return tuple(ans)

def add_term(out,key,value):
 if value:out[key]=out.get(key,0)+value

def derivative(terms,axis,s):
 out={}
 for (a,b,ns,nc),v in terms.items():
  powers=[a,b];n=powers[axis]
  if n:
   pp=powers.copy();pp[axis]-=1;add_term(out,(*pp,ns,nc),v*n)
  pp=powers.copy();pp[axis]+=1;add_term(out,(*pp,ns,nc-2),v*(ns*s+nc))
 return {k:v for k,v in out.items()if v!=0}

def combine(*args):
 out={}
 for scale,terms in args:
  for k,v in terms.items():add_term(out,k,scale*v)
 return {k:v for k,v in out.items()if v!=0}

def evaluate_terms(terms,x,y,s):
 x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));rr=1+x*x+y*y;out=np.zeros_like(rr)
 for (a,b,ns,nc),v in terms.items():out+=v*x**a*y**b*rr**((ns*s+nc)/2)
 return out

class StreamBasis:
 def __init__(self,beta,ni,nj,shifts=(0,1),a0=1.):
  assert beta>2 and ni>=1 and nj>=3
  self.beta=float(beta);self.s=1/self.beta;self.a0=float(a0);self.ni=ni;self.nj=nj;self.shifts=tuple(shifts);self.labels=[];self.psi=[];self.theta=[]
  for shift in shifts:
   for i in range(ni):
    for j in range(nj):
     self.labels.append((i,j,shift));p={};th={}
     for ri,ci in enumerate(cheb_poly(i,-1,2)):
      for aj,cj in enumerate(cheb_poly(j)):
       if not ci*cj:continue
       add_term(p,(1,aj,-(ri+1),1-aj-shift),ci*cj)
       add_term(th,(2,aj,-(ri+2),-1-aj-shift),ci*cj)
     px=derivative(p,0,self.s);gauge=float(evaluate_terms(px,0,0,self.s));add_term(p,(1,0,0,0),-gauge)
     px=derivative(p,0,self.s);py=derivative(p,1,self.s);pxx=derivative(px,0,self.s);pyy=derivative(py,1,self.s);om=combine((-1,pxx),(-1,pyy));omx=derivative(om,0,self.s);omy=derivative(om,1,self.s)
     self.psi.append({'Psi':p,'U1':combine((-1,py)),'U2':px,'Omega':om,'Omega_x':omx,'Omega_y':omy,'strain':derivative(px,1,self.s)})
     self.theta.append({'Theta':th,'Theta_x':derivative(th,0,self.s),'Theta_y':derivative(th,1,self.s),'a0':combine((.5,derivative(derivative(th,0,self.s),0,self.s)))})
  self.n=len(self.labels)
  ec=lambda data,key:np.array([float(evaluate_terms(row[key],0,0,self.s))for row in data])
  self.Cconstraint=np.vstack([ec(self.psi,'strain'),ec(self.psi,'Omega_x')]);self.Dconstraint=ec(self.theta,'a0')[None,:]
  self.Ctarget=np.array([1+self.beta/2,4*self.a0/self.beta]);self.Dtarget=np.array([self.a0]);self.Cnull=null_space(self.Cconstraint,rcond=1e-13);self.Dnull=null_space(self.Dconstraint,rcond=1e-13)
  self.Cbase=np.zeros(self.n);self.Dbase=np.zeros(self.n);self.Cbase[self.labels.index((0,0,0))]=-self.a0/(self.beta-1);self.Cbase[self.labels.index((0,1,0))]=1+self.beta/2;self.Dbase[self.labels.index((0,0,0))]=self.a0
  assert np.max(abs(self.Cconstraint@self.Cbase-self.Ctarget))<1e-10
  assert np.max(abs(self.Dconstraint@self.Dbase-self.Dtarget))<1e-10
  self.nc=self.Cnull.shape[1];self.nd=self.Dnull.shape[1];self.size=self.nc+self.nd
 def coefficients(self,z):return self.Cbase+self.Cnull@z[:self.nc],self.Dbase+self.Dnull@z[self.nc:]
 def prepare(self,points):
  points=np.asarray(points);x,y=points.T
  ps={key:np.stack([evaluate_terms(row[key],x,y,self.s)for row in self.psi],axis=1)for key in ['Psi','U1','U2','Omega','Omega_x','Omega_y']}
  th={key:np.stack([evaluate_terms(row[key],x,y,self.s)for row in self.theta],axis=1)for key in ['Theta','Theta_x','Theta_y']}
  return {'points':points,'psi':ps,'theta':th}
 def fields(self,prepared,C,D):
  p=prepared['points'];out={key:m@C for key,m in prepared['psi'].items()};out.update({key:m@D for key,m in prepared['theta'].items()});out['W1']=self.beta*p[:,0]+out['U1'];out['W2']=self.beta*p[:,1]+out['U2'];out['F']=out['W1']*out['Theta_x']+out['W2']*out['Theta_y']-(self.beta-2)*out['Theta'];out['G']=out['W1']*out['Omega_x']+out['W2']*out['Omega_y']+out['Omega']-out['Theta_x'];out['NF']=abs(out['W1']*out['Theta_x'])+abs(out['W2']*out['Theta_y'])+abs((self.beta-2)*out['Theta']);out['NG']=abs(out['W1']*out['Omega_x'])+abs(out['W2']*out['Omega_y'])+abs(out['Omega'])+abs(out['Theta_x']);return out
 def omega_callable(self,C):
  terms=combine(*[(c,row['Omega'])for c,row in zip(C,self.psi)])
  return lambda x,y:evaluate_terms(terms,x,y,self.s)

class FitProblem:
 def __init__(self,basis,points,regularization=1e-5,tail_weight=True):
  self.basis=basis;self.data=basis.prepare(points);self.ps={key:m@basis.Cnull for key,m in self.data['psi'].items()};self.th={key:m@basis.Dnull for key,m in self.data['theta'].items()};self.reg=float(regularization);x,y=np.asarray(points).T;R=np.sqrt(1+x*x+y*y);s=basis.s
  extra=s if tail_weight else 0.;self.wF=1/(basis.a0*x*x*R**(-1-2*s-extra));self.wG=1/(basis.a0*x*R**(-1-s-extra));self.scale=1/np.sqrt(len(x));self.last=None
 def residual(self,z):
  C,D=self.basis.coefficients(z);f=self.basis.fields(self.data,C,D);self.last=(z.copy(),f);return np.r_[self.scale*self.wF*f['F'],self.scale*self.wG*f['G'],self.reg*z]
 def jacobian(self,z):
  if self.last is None or not np.array_equal(z,self.last[0]):self.residual(z)
  f=self.last[1];ps=self.ps;th=self.th;beta=self.basis.beta
  fc=f['Theta_x'][:,None]*ps['U1']+f['Theta_y'][:,None]*ps['U2'];fd=f['W1'][:,None]*th['Theta_x']+f['W2'][:,None]*th['Theta_y']-(beta-2)*th['Theta']
  gc=f['Omega_x'][:,None]*ps['U1']+f['Omega_y'][:,None]*ps['U2']+f['W1'][:,None]*ps['Omega_x']+f['W2'][:,None]*ps['Omega_y']+ps['Omega'];gd=-th['Theta_x']
  return np.vstack([self.scale*self.wF[:,None]*np.hstack([fc,fd]),self.scale*self.wG[:,None]*np.hstack([gc,gd]),self.reg*np.eye(self.basis.size)])

def diagnostic_fields(fields):
 out={}
 for key,norm in [('F','NF'),('G','NG')]:
  a=abs(fields[key]);b=fields[norm];ratio=np.divide(a,b,out=np.where(a==0,0.,np.inf),where=b!=0)
  out[key]={'max_absolute':float(a.max()),'rms_absolute':float(np.sqrt(np.mean(a*a))),'max_ratio':float(ratio.max()),'rms_ratio':float(np.sqrt(np.mean(ratio*ratio)))}
 out['minimum_Omega']=float(np.min(fields['Omega']));out['minimum_Theta']=float(np.min(fields['Theta']));out['minimum_Theta_x']=float(np.min(fields['Theta_x']));return out
