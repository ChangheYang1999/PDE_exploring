"""Whole-plane quadrature of smooth radial blobs plus a prescribed algebraic tail.

The inverse is evaluated from enclosed circulation of each radial blob and the
analytic tail stream. No numerical-lane source or inversion routine is used.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,shutil
import numpy as np
from scipy.special import exp1
from numpy.polynomial.legendre import leggauss
root=Path('verification/strain_blob_beta2_20261020T2123');root.mkdir(parents=True,exist_ok=True)
pi=np.pi;Fone=np.exp(-1.)-exp1(1.);beta=2.;nu=1/beta;q=(1-nu)/2;s=(1+2*nu)/2;cstar=1+beta/2;mu=.001;a0=2*beta*q*mu
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','beta':beta,'mu':mu,'a0':a0,'bump_normalizer':Fone,'radial_pairs':[],'construction':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
def kernel(X):
 r2=np.sum(X*X,axis=-1);return np.stack((X[...,1],-X[...,0]),axis=-1)/(2*pi*r2[...,None])
def df(X):
 x,y=X[:,0],X[:,1];h=x*x+y*y
 return np.column_stack((y*(y*y-3*x*x)/h**3,x*(x*x-3*y*y)/h**3))
def dg(X):
 x,y=X[:,0],X[:,1];h=x*x+y*y
 return np.column_stack((12*x*y*(x*x-y*y)/h**4,-3*(x**4-6*x*x*y*y+y**4)/h**4))
def blob_velocity(X,A,radius,mass):
 Z=X-np.array(A);rr=np.sum(Z*Z,axis=1);z2=rr/radius**2;M=np.ones(len(X));inside=(z2<1)&(z2>=1e-12)
 v=1-z2[inside];M[inside]=1-(v*np.exp(-1/v)-exp1(1/v))/Fone
 ratio=np.empty(len(X));ordinary=z2>=1e-12;ratio[ordinary]=M[ordinary]/rr[ordinary]
 ratio[~ordinary]=np.exp(-1)/Fone/radius**2
 return mass/(2*pi)*np.column_stack((Z[:,1],-Z[:,0]))*ratio[:,None]
def pair_velocity(X,A,radius,mass):
 A=np.array(A);mirror=A*np.array([-1,1]);zero=np.zeros((1,2))
 return (blob_velocity(X,A,radius,mass)+blob_velocity(X,mirror,radius,-mass)
         -blob_velocity(zero,A,radius,mass)-blob_velocity(zero,mirror,radius,-mass))
def mass_nodes(A,radius,nr,na):
 z,w=leggauss(nr);u=(z+1)/2;w=w/2;ang=2*pi*(np.arange(na)+.371)/na
 rr=np.sqrt(u);pts=np.array(A)+radius*np.stack((rr[:,None]*np.cos(ang),rr[:,None]*np.sin(ang)),axis=-1)
 weights=w*np.exp(-1/(1-u))/Fone
 return pts.reshape(-1,2),np.repeat(weights/na,na)
def pair_N(A,radius,mass,nr,na):
 X,w=mass_nodes(A,radius,nr,na);mirror=np.array(A)*[-1,1]
 # A radial blob's own nonlinear contribution integrates to zero exactly.
 V=blob_velocity(X,mirror,radius,-mass)-blob_velocity(np.zeros((1,2)),A,radius,mass)-blob_velocity(np.zeros((1,2)),mirror,radius,-mass)
 return 2*mass*float(w@np.sum(V*df(X),axis=1))
def tail(X):
 x,y=X[:,0],X[:,1];r2=x*x+y*y;h=1+r2;B=2+(q+1)*r2
 V=np.column_stack((2*q*x*y*h**(q-1),-np.expm1(q*np.log1p(r2))-2*q*x*x*h**(q-1)))
 om=4*q*x*h**(q-2)*B;th=a0*x*x*h**(-s)
 return V,om,th
for ratio in [1.,.5]:
 A=np.array([1.,ratio]);mass=1.;c=2*ratio/(pi*(1+ratio**2)**2);limit=(ratio**2-3)*(1-3*ratio**2)/(2*pi*(1+ratio**2)**4)
 for radius in [.2,.1,.05,.025]:
  val=pair_N(A,radius,mass,48,256);X,w=mass_nodes(A,radius,48,256);measured_c=2*mass/pi*float(w@(X[:,0]*X[:,1]/np.sum(X*X,axis=1)**2))
  out['radial_pairs'].append({'a':1.,'b':ratio,'radius':radius,'mass':mass,'c':measured_c,'c_exact':c,'N':val,'point_limit':limit,'N_minus_limit':val-limit});save()
A=np.array([1.,1.]);radius=.1;mass=cstar/(1/(2*pi));Hcenter=np.array([.02,.1]);Hradius=.004
# Each angular quadrature is on the full circle, with a shifted grid.
radial_breaks=np.array([0,.01,.03,.06,.1,.2,.4,.7,1.,1.2,1.3,1.4,1.5,1.6,1.8,2.2,3.,5.,10.,30.,100.,300.,1000.,np.inf])
u_breaks=(1+radial_breaks)**(-nu)
for nr,na in [(12,192),(18,384),(24,768)]:
 z,w=leggauss(nr);uu=[];uw=[]
 for hi,lo in zip(u_breaks[:-1],u_breaks[1:]):
  uu.extend((hi+lo)/2+(hi-lo)*z/2);uw.extend((hi-lo)*w/2)
 u=np.array(uu);wr=np.array(uw);r=u**(-beta)-1;wr=wr*beta*u**(-beta-1)*r
 angles=2*pi*(np.arange(na)+.371)/na;X=np.stack((r[:,None]*np.cos(angles),r[:,None]*np.sin(angles)),axis=-1).reshape(-1,2);weights=np.repeat(wr*2*pi/na,na)
 Vb=pair_velocity(X,A,radius,mass);Vt,om,th=tail(X);V=Vb+mu*Vt
 Nt=float(weights@(mu*om*np.sum(V*df(X),axis=1)));B0=float(weights@(th*np.sum(V*dg(X),axis=1)))
 Xb,wb=mass_nodes(A,radius,48,256);vtb,_,_=tail(Xb)
 Nb=pair_N(A,radius,mass,48,256)+2*mass*mu*float(wb@np.sum(vtb*df(Xb),axis=1));N=Nb+Nt
 Xh,wh=mass_nodes(Hcenter,Hradius,48,256);Vh=pair_velocity(Xh,A,radius,mass)+mu*tail(Xh)[0]
 BH=float(wh@np.sum(Vh*dg(Xh),axis=1)) # H has mass1, half on each reflected bump.
 tcoef=(2*(N-pi*cstar)-B0)/BH
 row={'radial_order':nr,'angular_points':na,'plane_nodes':len(X),'blob_radius':radius,'blob_mass':mass,'c_exact':cstar,'N_blob_and_cross':Nb,'N_tail':Nt,'N':N,'B_base':B0,'B_bump':BH,'bump_multiplier_from_this_grid':tcoef,'construction_margin':N-pi*cstar,'abs_integral_tail_N':float(weights@abs(mu*om*np.sum(V*df(X),axis=1))),'abs_integral_base_B':float(weights@abs(th*np.sum(V*dg(X),axis=1)))}
 out['construction'].append(row);save();print('grid',nr,na,'N',N,'B0',B0,'t',tcoef,flush=True)
tfixed=out['construction'][1]['bump_multiplier_from_this_grid'];out['fixed_bump_multiplier']=tfixed
for row in out['construction']:
 row['S_defect_with_fixed_middle_multiplier']=row['N']-.5*(row['B_base']+tfixed*row['B_bump'])-pi*cstar
# Nonzero PDE residuals far along y=0, independently differentiated analytically.
out['ray_checks']=[]
for x in [10.,30.,100.,300.,1000.]:
 X=np.array([[x,0.]]);Vt,om,th=tail(X);V=pair_velocity(X,A,radius,mass)+mu*Vt;h=1+x*x;B=2+(q+1)*x*x
 tx=a0*(2*x*h**(-s)-2*s*x**3*h**(-s-1));ox=mu*4*q*(B*h**(q-2)+2*x*x*((q+1)*h**(q-2)+(q-2)*B*h**(q-3)))
 rt=float((beta*x+V[0,0])*tx-(beta-2)*th[0]);rv=float((beta*x+V[0,0])*ox+mu*om[0]-tx)
 out['ray_checks'].append({'x':x,'RTheta':rt,'RTheta_over_Theta_times_x2':rt/th[0]*x*x,'ROmega':rv,'ROmega_times_x_power_2nu':rv*x**(2*nu),'ROmega_times_x_power_nu_plus2':rv*x**(nu+2)})
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),scope='Manufactured smooth nonprofiles satisfying one integral identity by a bump adjustment. Ordinary quadrature with refinement, no interval certificate and no PDE or existence claim.')
shutil.copyfile(__file__,root/'code_snapshot.py');out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();save();print('COMPLETE',out['elapsed_seconds'],flush=True)
