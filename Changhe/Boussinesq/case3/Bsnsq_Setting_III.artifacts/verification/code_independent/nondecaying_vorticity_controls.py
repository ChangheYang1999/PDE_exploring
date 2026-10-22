"""Independent symbolic and physical-space controls of P255's nonprofile.

No numerical-lane code is read or imported. The inverse is evaluated by rays
centered at the observation point, using the full compact source on R2.
The exact infinite construction is proved in PROOF.md, not by these samples.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,time
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss
R=Path('research/255_nondecaying_vorticity_transport/verification')
t0=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks=[]
def check(name,ok,detail=None):checks.append({'name':name,'passed':bool(ok),'detail':detail})
def zero(name,v):check(name,s.simplify(v)==0,str(v))
x,y,z=s.symbols('x y z',real=True);a,C,r,eps,kappa,p=s.symbols('a C r eps kappa p',positive=True)
F=s.E/4*s.exp(-1/(1-z));phi=F.subs(z,x*x+y*y)
omega=-s.diff(phi,x,2)-s.diff(phi,y,2)
rad=-4*(s.diff(F,z)+z*s.diff(F,z,2))
zero('radial_laplacian',omega-rad.subs(z,x*x+y*y))
zero('center_vorticity',omega.subs({x:0,y:0})-1)
for v,n in [(phi,'stream'),(omega,'vorticity')]:
 zero(n+'_x_even',v.subs(x,-x)-v);zero(n+'_y_even',v.subs(y,-y)-v)
 for axis in [x,y]:zero(n+'_center_gradient_'+str(axis),s.diff(v,axis).subs({x:0,y:0}))
scaled=a*phi.subs({x:(x-r)/eps,y:y/eps},simultaneous=True)
scaled_omega=-s.diff(scaled,x,2)-s.diff(scaled,y,2)
zero('scaled_center_amplitude',scaled_omega.subs({x:r,y:0})-a/eps**2)
for axis in [x,y]:zero('scaled_center_vorticity_gradient_'+str(axis),s.diff(scaled_omega,axis).subs({x:r,y:0}))
zero('scaled_center_velocity_x',-s.diff(scaled,y).subs({x:r,y:0}));zero('scaled_center_velocity_y',s.diff(scaled,x).subs({x:r,y:0}))
exp_a=-kappa-2;exp_eps=-kappa-1
zero('velocity_exponent',exp_a-exp_eps+1)
zero('vorticity_exponent',exp_a-2*exp_eps-kappa)
l=s.symbols('l',nonnegative=True);zero('derivative_exponent',exp_a-(l+2)*exp_eps-(kappa+(kappa+1)*l))
E=p*exp_a+(2-2*p)*exp_eps
zero('Lp_exponent',E-(p*kappa-2*kappa-2));zero('L1_exponent',E.subs(p,1)+kappa+2);zero('L2_exponent',E.subs(p,2)+2);zero('critical_Lp',E.subs(p,2+2/kappa))
zero('absolute_inverse_tail_power',exp_a-1+kappa+3)
psi_b=2*C*y/x;ob=-s.diff(psi_b,x,2)-s.diff(psi_b,y,2);ub=s.Matrix([-s.diff(psi_b,y),s.diff(psi_b,x)]);wb=s.Matrix([2*x,2*y])+ub
zero('exact_strip_vorticity',ob+4*C*y/x**3)
zero('strip_center_base_vorticity',ob.subs({x:r,y:0}));zero('strip_center_base_transport',wb.dot(s.Matrix([s.diff(ob,x),s.diff(ob,y)])).subs({x:r,y:0}))
# The added radial bump has zero velocity and source gradient at its center.
zero('full_vorticity_residual_center', (wb.dot(s.Matrix([s.diff(ob,x),s.diff(ob,y)]))+ob).subs({x:r,y:0})+r**kappa-r**kappa)
corepsi=2*x*y-a*x**3/3;coretheta=a*x*x;coreomega=-s.diff(corepsi,x,2)-s.diff(corepsi,y,2);corew=s.Matrix([2*x-s.diff(corepsi,y),2*y+s.diff(corepsi,x)])
zero('core_temperature_transport',corew.dot(s.Matrix([s.diff(coretheta,x),s.diff(coretheta,y)])))
zero('core_vorticity_equation',corew.dot(s.Matrix([s.diff(coreomega,x),s.diff(coreomega,y)]))+coreomega-s.diff(coretheta,x))
zero('core_divergence',s.diff(corew[0],x)+s.diff(corew[1],y)-4)
zero('core_center_strain',s.diff(corepsi,x,y).subs({x:0,y:0})-2)
zero('core_normalization',coreomega.diff(x)-2*a)
# Separate nonradial polynomial checks the compact Hamiltonian stream formula.
eta=x**3+y*x**2+2*x*y**2;psi=x*x*y+3*x*y*y+x
J=lambda v:s.Matrix([-v[1],v[0]])
W=s.Matrix([2*x,2*y])+J(s.Matrix([psi.diff(x),psi.diff(y)]));H=J(s.Matrix([eta.diff(x),eta.diff(y)]))
bracket=H.jacobian([x,y])*W-W.jacobian([x,y])*H
stream=W.dot(s.Matrix([eta.diff(x),eta.diff(y)]))-4*eta
for i in range(2):zero('Hamiltonian_push_component_'+str(i),bracket[i]-J(s.Matrix([stream.diff(x),stream.diff(y)]))[i])

def source(x,y):
 z=x*x+y*y;t=1-z
 out=np.zeros_like(t);m=t>0;tm=t[m];zm=z[m]
 # All quadrature nodes are strictly interior; the mask also defines the flat exterior.
 f=np.exp(1-1/tm)/4
 out[m]=4*f*(tm**-2-zm*tm**-4+2*zm*tm**-3)
 return out

def direct_velocity(X,nr,nt):
 # Y = X - rho u. The 1/rho kernel cancels the area Jacobian exactly.
 th=2*np.pi*(np.arange(nt)+.3141592653589793)/nt
 ux,uy=np.cos(th),np.sin(th);dot=X[0]*ux+X[1]*uy
 upper=dot+np.sqrt(1-np.dot(X,X)+dot*dot)
 q,w=leggauss(nr);rho=upper[:,None]*(q[None,:]+1)/2
 values=source(X[0]-rho*ux[:,None],X[1]-rho*uy[:,None])
 radial=values@(w/2)*upper
 return np.array([np.mean(uy*radial),-np.mean(ux*radial)])

def exact_velocity(X):
 z=np.dot(X,X);f=np.exp(1-1/(1-z))/4;fp=-f/(1-z)**2
 return np.array([-2*X[1]*fp,2*X[0]*fp])
rows=[]
points=[(0.,0.),(.2,.1),(.5,0.),(.1,.7),(-.3,.4)]
for nr,nt in [(48,64),(96,128),(192,256)]:
 for X in points:
  X=np.array(X);got=direct_velocity(X,nr,nt);want=exact_velocity(X);err=float(np.max(abs(got-want)))
  rows.append({'point':X.tolist(),'radial_nodes':nr,'angular_nodes':nt,'quadrature_velocity':got.tolist(),'analytic_velocity':want.tolist(),'maximum_absolute_error':err})
for i,X in enumerate(points):
 arow,brow,crow=[rows[k*5+i]for k in range(3)]
 check('physical_inverse_finest_'+str(i),crow['maximum_absolute_error']<2e-11,crow)
 check('physical_inverse_refinement_'+str(i),crow['maximum_absolute_error']<=arow['maximum_absolute_error']+2e-14,[arow['maximum_absolute_error'],brow['maximum_absolute_error'],crow['maximum_absolute_error']])
result={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-t0,'passed':sum(c['passed']for c in checks),'total':len(checks),'checks':checks,'physical_space_quadrature':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((R.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Finite controls of identities and individual compact bumps. The locally finite infinite construction is justified by the proof, not numerical samples. No B2 profile or full endpoint.'}
(R/'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(result['passed'],result['total'],result['elapsed_seconds']);print('maximum_finest_error',max(a['maximum_absolute_error']for a in rows if a['radial_nodes']==192));print('failures',[c for c in checks if not c['passed']])
