"""Independent exact and finite-rotation controls for research154."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib,sys
import numpy as np
import sympy as sp
from numpy.polynomial.legendre import leggauss
start=time.monotonic();root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);checks=[]
def exact(name,v,w=0):
 d=sp.simplify(sp.expand_trig(v-w));checks.append({'name':name,'difference':str(d),'pass':d==0});assert d==0,(name,d)
u,v,cx,cy,beta,eps,k,kr,r=sp.symbols('u v cx cy beta eps k kr r',real=True)
a=sp.symbols('alpha',real=True);ca,sa=sp.cos(a),sp.sin(a);Rot=sp.Matrix([[ca,-sa],[sa,ca]]);J=sp.Matrix([[0,-1],[1,0]]);z=sp.Matrix([u,v]);W=sp.Matrix(sp.symbols('W1 W2',real=True));c=sp.Matrix([cx,cy]);A=W-beta*z;B=kr/r*J*z*(z.dot(W));D=Rot*(sp.eye(2)+eps*kr/r*(J*z)*z.T)
exact('twist_area',D.det(),1)
for i in range(2):exact('directional_derivative_component_'+str(i),(D*W)[i],(Rot*(W+eps*B))[i])
Vnew=Rot*(A+eps*B)-beta*c;Vold=A-beta*c
exact('kinetic_square', (Vnew.dot(Vnew)-Vold.dot(Vold))/2, eps**2*B.dot(B)/2+eps*A.dot(B)-beta*c.dot((Rot-sp.eye(2))*A+eps*Rot*B))
S=sp.diag(-1,1);exact('reflection_rotation',sum((S*Rot*S-sp.Matrix([[ca,sa],[-sa,ca]]))),0)
x,y,q=sp.symbols('x y q',real=True);cc=1+beta/2;Wx=(beta-cc)*x;Wy=(beta+cc)*y-q*x*x/2
exact('polynomial_divergence',sp.diff(Wx,x)+sp.diff(Wy,y),2*beta)
th=sp.symbols('theta',real=True);dotz=u*Wx.subs(x,cx+u)+v*Wy.subs({x:cx+u,y:cy+v})
flux=sp.integrate(sp.expand_trig(dotz.subs({u:r*sp.cos(th),v:r*sp.sin(th)})),(th,0,2*sp.pi));exact('circle_flux',flux,2*sp.pi*beta*r*r)
exact('thermal_polynomial',Wx*2*x-(beta-2)*x*x)
# An exact affine field achieves the Cauchy lower bound after centering its dilation.
dot_aff=beta*r*r;exact('cauchy_equality_dilation',sp.integrate(dot_aff**2,(th,0,2*sp.pi)),2*sp.pi*beta**2*r**4)

def manufacture(b,a0,n):
 t,w=leggauss(n);r0=.45;dr=.25;rr=r0+dr*t;wr=dr*w
 kap=np.exp(1-1/(1-t*t));kp=kap*(-2*t)/(dr*(1-t*t)**2)
 angles=2*np.pi*(np.arange(96)+.37)/96
 z=np.stack((rr[:,None]*np.cos(angles),rr[:,None]*np.sin(angles)),axis=-1)
 wt=wr[:,None]*rr[:,None]*np.ones((1,len(angles)))*2*np.pi/len(angles)
 c=np.array([1.9,.4]);Y=z+c;cc=1+b/2;q=4*a0/b
 def field(P):
  xx,yy=P[...,0],P[...,1];return np.stack(((b-cc)*xx,(b+cc)*yy-q*xx*xx/2),axis=-1)
 W=field(Y);V=W-b*Y;A=W-b*z;B=kp[:,None,None]/rr[:,None,None]*np.stack((-z[...,1],z[...,0]),axis=-1)*np.sum(z*W,axis=-1)[...,None]
 aa=float(np.sum(wt*np.sum(B*B,axis=-1)))
 low=float(2*np.pi*b*b*np.sum(wr*kp*kp*rr**5))
 # Bound applies to pair of disks and includes bounded potential contribution.
 c1=float(2*np.sum(wt*(np.linalg.norm(A,axis=-1)*np.linalg.norm(B,axis=-1)+b*np.linalg.norm(c)*np.linalg.norm(B,axis=-1))))
 c0=float(4*b*np.linalg.norm(c)*np.sum(wt*np.linalg.norm(A,axis=-1))+4*.8*np.sum(wt*np.abs(a0*Y[...,0]**2)))
 assert aa>=low*(1-1e-12)>0
 rows=[]
 for e in [-256.,-64.,-8.,-1.,1.,8.,64.,256.]:
  alpha=e*kap;cs=np.cos(alpha)[:,None];sn=np.sin(alpha)[:,None]
  def rotate(v):return np.stack((cs*v[...,0]-sn*v[...,1],sn*v[...,0]+cs*v[...,1]),axis=-1)
  Phi=c+rotate(z);jz=np.stack((-z[...,1],z[...,0]),axis=-1)
  inner=W+e*kp[:,None,None]/rr[:,None,None]*jz*np.sum(z*W,axis=-1)[...,None]
  Vp=rotate(inner)-b*Phi
  dk=.5*np.sum(Vp*Vp-V*V,axis=-1);dp=(Phi[...,1]-Y[...,1])*a0*Y[...,0]**2
  energy=float(2*np.sum(wt*(dk+dp)))
  expansion=aa*e*e+2*e*np.sum(wt*np.sum(A*B,axis=-1))-2*b*np.sum(wt*np.sum(c*(rotate(A)-A+e*rotate(B)),axis=-1))+2*np.sum(wt*dp)
  err=abs(energy-expansion);assert err<=2e-11*(1+abs(energy))
  remainder=energy-aa*e*e;assert abs(remainder)<=c0+c1*abs(e)+1e-9
  # Independently reflect both point and rotation sign and reconstruct Jacobian action.
  CL=np.array([-c[0],c[1]]);ZL=z*np.array([-1,1]);YL=CL+ZL;WL=field(YL)
  def rotleft(v):return np.stack((cs*v[...,0]+sn*v[...,1],-sn*v[...,0]+cs*v[...,1]),axis=-1)
  PL=CL+rotleft(ZL);JL=np.stack((-ZL[...,1],ZL[...,0]),axis=-1)
  VL=rotleft(WL-e*kp[:,None,None]/rr[:,None,None]*JL*np.sum(ZL*WL,axis=-1)[...,None])-b*PL
  left=.5*np.sum(VL*VL-(WL-b*YL)**2,axis=-1)+(PL[...,1]-YL[...,1])*a0*YL[...,0]**2
  reflerr=float(np.max(np.abs(left-dk-dp)));assert reflerr<=1e-10*(1+np.max(abs(left)))
  rows.append({'epsilon':e,'energy_difference_pair':energy,'energy_over_epsilon2':energy/e**2,'exact_decomposition_error':float(err),'reflection_error':reflerr,'remainder':float(remainder),'proven_algebraic_bound':c0+c1*abs(e)})
 return {'beta':b,'a0':a0,'radial_order':n,'angular_order':96,'quadratic_coefficient':aa,'divergence_lower_bound':low,'rows':rows}
numeric=[manufacture(b,a,n) for b,a in [(2.25,1.),(3.5,1.),(6.,-1.)] for n in [48,96,192]]
for group in [numeric[0:3],numeric[3:6],numeric[6:9]]:
 assert abs(group[-1]['quadratic_coefficient']/group[-2]['quadratic_coefficient']-1)<1e-9
 for row in group[-1]['rows']:
  if abs(row['epsilon'])==256:assert abs(row['energy_over_epsilon2']/group[-1]['quadratic_coefficient']-1)<.1
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','exact_checks':checks,'numeric_cases':numeric,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256(Path('research/154_unbounded_compact_energy/PROOF.md').read_bytes()).hexdigest(),'scope':'Genuine C-infinity annular twist; compact energy differences on a polynomial manufactured background only, not a global B2 configuration or numerical proof'}
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(checks),'exact',len(numeric),'cases',out['elapsed_seconds'],flush=True)
