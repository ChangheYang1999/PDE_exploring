"""Independent audit of separately interpolated P/r^2 and P'/r.
Analytic smooth Gaussian modes, NumPy polynomial interpolation, and Cartesian
finite differences. No numerics-lane source is imported or executed.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,time
import numpy as np
from numpy.polynomial import Polynomial
from numpy.polynomial.legendre import leggauss

class InnerInterpolator:
 def __init__(self,beta=3.,L=1.5,Nt=40,grade=1.5,ng=7):
  self.beta,self.L,self.edge=beta,L,Nt**(-grade)
  xi,_=leggauss(ng);t=self.edge*(xi+1)/2
  self.nodes=L*np.sqrt(np.expm1(-2*beta*np.log1p(-t)))
  self.ks=np.array([1,2,3]);self.powers=np.array([3,2,3]);self.coeffs=np.array([-1/(2*beta),-(1+beta/2)/2,.2])
  self.p=[];self.d=[];self.a=[]
  for k,m,c in zip(self.ks,self.powers,self.coeffs):
   r=self.nodes;v=c*r**m*np.exp(-r*r);der=c*r**(m-1)*(m-2*r*r)*np.exp(-r*r)
   self.p.append(Polynomial.fit(xi,v/r**2,ng-1,domain=[-1,1]))
   self.d.append(Polynomial.fit(xi,der/r,ng-1,domain=[-1,1]))
   self.a.append(Polynomial.fit(xi,c*np.exp(-r*r),ng-1,domain=[-1,1]))
 def t_and_der(self,r):
  v=np.log1p(r*r/self.L**2);z=np.exp(-v/(2*self.beta))
  return -np.expm1(-v/(2*self.beta)),r/(self.beta*self.L**2)*z**(2*self.beta+1)
 def radial(self,r,kind):
  r=np.atleast_1d(r);t,tp=self.t_and_der(r);xi=2*t/self.edge-1;xp=2*tp/self.edge
  if kind=='exact':
   P=np.array([c*r**m*np.exp(-r*r) for m,c in zip(self.powers,self.coeffs)])
   D=np.array([c*r**(m-1)*(m-2*r*r)*np.exp(-r*r) for m,c in zip(self.powers,self.coeffs)])
   return P,D,D
  if kind=='separate':
   P=np.array([r*r*p(xi) for p in self.p]);D=np.array([r*d(xi) for d in self.d])
   Pprime=np.array([2*r*p(xi)+r*r*p.deriv()(xi)*xp for p in self.p]);return P,D,Pprime
  if kind=='single_regular_factor':
   P=np.array([r**m*a(xi) for m,a in zip(self.powers,self.a)])
   D=np.array([m*r**(m-1)*a(xi)+r**m*a.deriv()(xi)*xp for m,a in zip(self.powers,self.a)]);return P,D,D
  raise ValueError(kind)
 def velocity(self,points,kind):
  points=np.atleast_2d(points);x,y=points.T;r=np.hypot(x,y);phi=np.arctan2(x,-y)
  P,D,Pprime=self.radial(r,kind);sn=np.sin(self.ks[:,None]*phi);cs=np.cos(self.ks[:,None]*phi)
  dr=(D*sn).sum(0);dp=(self.ks[:,None]*P*cs).sum(0)
  return np.column_stack((np.cos(phi)*dr-np.sin(phi)*dp/r,np.sin(phi)*dr+np.cos(phi)*dp/r))
 def div_exact_of_interpolant(self,points,kind):
  points=np.atleast_2d(points);x,y=points.T;r=np.hypot(x,y);phi=np.arctan2(x,-y)
  P,D,Pprime=self.radial(r,kind)
  return ((self.ks[:,None]/r)*(D-Pprime)*np.cos(self.ks[:,None]*phi)).sum(0)
 def div_fd(self,points,kind):
  points=np.atleast_2d(points);r=np.linalg.norm(points,axis=1);h=r*1e-3;out=np.zeros(len(points))
  for j in (0,1):
   dx=np.zeros_like(points);dx[:,j]=h
   derivative=(self.velocity(points-2*dx,kind)-8*self.velocity(points-dx,kind)+8*self.velocity(points+dx,kind)-self.velocity(points+2*dx,kind))/(12*h[:,None])
   out+=derivative[:,j]
  return out

start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Manufactured interpolation audit, not a B2 profile. No numerics-lane code executed.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[]}
for beta in (2.5,3.):
 for Nt in (32,40,64):
  model=InnerInterpolator(beta=beta,Nt=Nt);row={'beta':beta,'Nt':Nt,'L':model.L,'first_node':float(model.nodes[0]),'first_cell_t_width':model.edge,'interpolated_P_over_r2_at0':[float(p(-1)) for p in model.p],'interpolated_D_over_r_at0':[float(d(-1)) for d in model.d],'by_radius':[]}
  for r in (1e-2,1e-3,1e-4,1e-5):
   ph=np.array([.17,.43,.86,1.23,2.1]);pts=r*np.column_stack((np.sin(ph),-np.cos(ph)));exact=model.velocity(pts,'exact');record={'radius':r}
   for kind in ('separate','single_regular_factor'):
    v=model.velocity(pts,kind);div=model.div_exact_of_interpolant(pts,kind);fd=model.div_fd(pts,kind)
    record[kind]={'maximum_velocity_error':float(np.max(abs(v-exact))),'maximum_divergence':float(np.max(abs(div))),'fd_divergence_max':float(np.max(abs(fd))),'formula_fd_discrepancy':float(np.max(abs(div-fd))),'maximum_velocity_error_divided_by_r':float(np.max(abs(v-exact))/r)}
   row['by_radius'].append(record)
  out['runs'].append(row)
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-start
Path('verification/interpolated_velocity_audit.json').write_text(json.dumps(out,indent=2)+'\n')
for row in out['runs']:print(row['beta'],row['Nt'],row['first_node'],row['by_radius'][-1],flush=True)
print('COMPLETE',out['elapsed_seconds'],flush=True)
