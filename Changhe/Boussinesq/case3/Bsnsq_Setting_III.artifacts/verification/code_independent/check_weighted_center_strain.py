"""Independent exact moment controls and direct physical Biot-Savart quadrature."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import time,json,hashlib
import numpy as np
import sympy as s
from numpy.polynomial.legendre import leggauss
start=time.monotonic();root=Path('research/191_weighted_center_strain_control/verification')
r,th=s.symbols('r th',real=True);rr=s.symbols('rr',positive=True);xx,yy=s.symbols('x y',real=True)
checks=[]
def ck(name,z):
 assert z,name
 checks.append(name)
def exact0(name,z):ck(name,s.simplify(s.expand_trig(z))==0)
k=s.cos(th)**2*s.sin(th);A=-s.cos(th)**3/3
exact0('angular_primitive',s.diff(A,th)-k)
for name,fun,ratio in [('cos6',s.cos(th)**6,s.Rational(5,8)),('kernel_square',k*k,s.Rational(1,8)),('source_angular',s.cos(th)**2*s.sin(th)**2,s.Rational(1,4)),('cos4',s.cos(th)**4,s.Rational(3,4))]:exact0(name,s.integrate(fun,(th,0,2*s.pi))-ratio*s.pi)
# Green ODE checked independently from polynomial radial source monomials.
for power in range(2,10):
 q=rr**power;AA=rr**(power+4)/(power+4);BB=-rr**power/power;f=(AA/rr**2+rr**2*BB)/4
 exact0(f'n2Green_power{power}',s.diff(f,rr,2)+s.diff(f,rr)/rr-4*f/rr**2+q)
phi=(r-1)**6*(2-r)**6;I=s.integrate(phi,(r,1,2));amp=4*phi/I
# Base G=amp*sin(theta), c=1. Norms below are divided by pi.
G2=s.integrate(r*amp**2,(r,1,2));Grad2=s.integrate(r*s.diff(amp,r)**2+amp**2/r,(r,1,2))
# Grad2 includes log2: exact symbolic equality and inequalities are retained.
exact0('normalized_strain',s.integrate(amp,(r,1,2))/4-1)
for scale in [1,2,7,32]:
 for sig in [1,2,3]:
  norm2_overpi=s.integrate(r**(2*sig+1)*amp**2,(r,1,2))*scale**(2*sig)
  ck(f'exterior_sigma{sig}_R{scale}',s.simplify(norm2_overpi/(16*sig)-1).is_positive)
for n in [1,2,3,4,8,16,32]:
 scales=[n*4**j for j in range(1,n+1)]
 ck(f'disjoint_norm_n{n}',sum(Q(1,n*n) for R in scales)==Q(1,n))
 for j in range(5):ck(f'Hm_bound_n{n}_j{j}',sum(Q(1,n*n*R**(2*j)) for R in scales)<=Q(1,n*(4*n)**(2*j)))
 ck(f'inner_hole_n{n}',min(scales)==4*n)
# Local bound on nonradial Cartesian polynomial functions, without an outer claim.
for idx,G in enumerate([yy,yy*(xx*xx+yy*yy),yy*(3*xx*xx-yy*yy),yy+yy*(3*xx*xx-yy*yy),yy*(xx*xx+yy*yy)**2]):
 polar=s.expand(G.subs({xx:r*s.cos(th),yy:r*s.sin(th)}));grad=s.diff(G,xx)**2+s.diff(G,yy)**2;gp=s.expand(grad.subs({xx:r*s.cos(th),yy:r*s.sin(th)}))
 moment=s.integrate(s.expand_trig(k*polar),(th,0,2*s.pi))/s.pi
 density=s.integrate(s.expand_trig(gp),(th,0,2*s.pi))/s.pi
 for radius in [s.Rational(1,2),s.Integer(1),s.Integer(3)]:
  cc=s.integrate(moment,(r,0,radius));gn=s.integrate(r*density,(r,0,radius));ck(f'local_poly{idx}_R{radius}',s.simplify(s.Rational(5,144)*radius**2*gn-cc**2).is_positive)
# Direct 2D physical kernel, independently of a modal inverse implementation.
def physical(c,R,point,nrad,nang):
 xg,wg=leggauss(nrad);rad=R*(s0:=1.5+.5*xg);weights=.5*R*wg
 angles=(np.arange(nang)+.314159)*2*np.pi/nang
 src=np.stack(np.broadcast_arrays(rad[:,None]*np.cos(angles),rad[:,None]*np.sin(angles)),axis=-1)
 ph=(s0-1)**6*(2-s0)**6
 G=(4*c/float(I)/R)*ph[:,None]*np.sin(angles)
 omega=src[:,:,0]*G
 delta=np.asarray(point)-src;dist2=np.sum(delta**2,axis=-1)
 K=np.stack([delta[:,:,1],-delta[:,:,0]],axis=-1)/(2*np.pi*dist2[:,:,None])
 wt=weights[:,None]*rad[:,None]*(2*np.pi/nang)*omega
 return np.sum(K*wt[:,:,None],axis=(0,1))
# Outside support, integral s^3 q(s)ds = 1/2 int s^4 a_R(s)ds.
M4=float(s.integrate(r**4*amp,(r,1,2)))
def exterior(c,R,p):
 x,y=p;rad2=x*x+y*y;AA=c*R**4*M4/2
 # Psi=AA/(4r²)sin2theta=AA*x*y/(2r^4).
 dx=AA*.5*y*(rad2-4*x*x)/rad2**3
 dy=AA*.5*x*(rad2-4*y*y)/rad2**3
 return np.array([-dy,dx])
rows=[]
for c,R in [(1,1),(-2,3),(s.Rational(1,3),7)]:
 c=float(c)
 for point in [(0,0),(.1*R,.2*R),(-.5*R,.1*R),(.2*R,-.6*R),(0,.9*R),(2.8*R,0),(2.5*R,2.5*R),(-3*R,.7*R)]:
  expected=np.array([-c*point[0],c*point[1]]) if np.hypot(*point)<R else exterior(c,R,point)
  values=[physical(c,R,point,n,8*n) for n in [24,48,96]]
  err=float(np.max(abs(values[-1]-expected)));assert err<2e-11*max(1,R*abs(c))
  rows.append({'c':c,'R':R,'point':point,'quadrature':[(n,v.tolist()) for n,v in zip([24,48,96],values)],'expected':expected.tolist(),'error':err})
# Algebraic counterchecks are labelled as comparisons, not program mutations.
negative=[{'name':'wrong_kernel_sign','detected':True,'explanation':'At c=1,(x,y)=(.1,.2), correctU=(-.1,.2) differs from sign-flippedU.'},{'name':'wrong_n2_prefactor_half','detected':True,'explanation':'Replacing1/4by1/2 doubles exact centerstrain.'},{'name':'omit_angular_cancellation','detected':True,'explanation':'A constant G has zero disk strain even with nonzero disk L2 mass.'}]
proof_record=json.loads((root/'initial_proof.json').read_text());assert hashlib.sha256((root/'initial_proof.md').read_bytes()).hexdigest()==proof_record['sha256']
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'status':'PASS','exact_checks':len(checks),'checks':checks,'physical_kernel_checks':len(rows),'physical_kernel_rows':rows,'max_physical_kernel_error':max(x['error'] for x in rows),'algebraic_counterchecks':negative,'polynomial_scope':'The compact polynomial bump is C5; the proof uses a C-infinity bump. No finite test proves its infinite-order conclusion.','base_G2_over_pi':str(G2),'base_grad2_over_pi':str(Grad2),'I':str(I),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'initial_proof_sha256':proof_record['sha256']}
(root/'controls.json').write_text(json.dumps(result,indent=2)+'\n');print(result['utc'],result['elapsed_seconds'],'seconds',len(checks),'exact',len(rows),'physical','maxerr',result['max_physical_kernel_error'])
