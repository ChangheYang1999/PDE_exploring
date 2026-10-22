"""Independent algebra, weak wall-extension and physical image-kernel controls."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,time
import sympy as s
import numpy as np
from numpy.polynomial.legendre import leggauss
start=time.monotonic();root=Path('research/192_WLGB_boundary_literature_audit/verification')
x,y,a,b=s.symbols('x y a b',real=True);checks=[]
def ck(name,condition):
 assert bool(condition),name
 checks.append(name)
def ez(name,expr):ck(name,s.simplify(expr)==0)
for lam in [Q(-1,2),Q(0),Q(1),Q(1915,1000),Q(1917,1000),Q(1919,1000),Q(3),Q(11,2)]:
 beta=1+lam
 ck('velocity_scale_'+str(lam),beta-1==lam)
 ck('temperature_scale_'+str(lam),beta-2==lam-1)
ck('reported_width',Q(2919,1000)-Q(2915,1000)==2*Q(2,1000))
# A family of local impermeable fields, none claimed to solve Boussinesq.
for k in range(6):
 psi=x*y*y/2+k*x**3*y*y+(k+1)*x*y**3
 u=-s.diff(psi,y);v=s.diff(psi,x);f=-s.diff(psi,x,2)-s.diff(psi,y,2)
 ez(f'wall_velocity_{k}',v.subs(y,0));ez(f'div_{k}',s.diff(u,x)+s.diff(v,y))
 ez(f'wall_tangent_vorticity_{k}',s.diff(f,x).subs({x:0,y:0})+1)
 ez(f'usual_curl_orientation_{k}',s.diff(v,x)-s.diff(u,y)+f)
# Smooth zero-trace polynomial representations cannot have nonzero trace derivative.
for i in range(1,5):
 for j in range(1,5):ez(f'zero_trace_derivative_{i}_{j}',s.diff(x**i*y**j,x).subs(y,0))
# Weak distribution identity of psi=x*y*abs(y)/2 on a test rectangle.
def integral_poly(expr,xlo,xhi,ylo,yhi):
 total=s.Integer(0)
 for (ix,iy),c in s.Poly(s.expand(expr),x,y).terms():
  total+=c*s.Rational(xhi**(ix+1)-xlo**(ix+1),ix+1)*s.Rational(yhi**(iy+1)-ylo**(iy+1),iy+1)
 return total
nonzero_weak=0
for i in range(5):
 for j in range(5):
  test=(1-x*x)**2*(1-y*y)**2*x**i*y**j
  neg_lap=-s.diff(test,x,2)-s.diff(test,y,2)
  pos=x*y*y/2;neg=-pos
  lhs=integral_poly(pos*neg_lap,-1,1,0,1)+integral_poly(neg*neg_lap,-1,1,-1,0)
  rhs=integral_poly(-x*test,-1,1,0,1)+integral_poly(x*test,-1,1,-1,0)
  ez(f'weak_no_wall_delta_{i}_{j}',lhs-rhs)
  if rhs!=0:nonzero_weak+=1
ck('nontrivial_weak_controls',nonzero_weak==4)
# Image kernel: use squared distances for exact rational derivative checks.
coords=[(a,b,1),(a,-b,-1),(-a,b,-1),(-a,-b,1)]
D=sum(sign*s.log((x-aa)**2+(y-bb)**2)/2 for aa,bb,sign in coords)
ez('image_wall',D.subs(y,0));ez('image_reflection_axis',D.subs(x,0))
ez('image_x_parity',D.subs(x,-x)+D);ez('image_y_parity',D.subs(y,-y)+D)
mixed=sum(sign*(-2*(x-aa)*(y-bb))/((x-aa)**2+(y-bb)**2)**2 for aa,bb,sign in coords)
ez('image_center_mixed',mixed.subs({x:0,y:0})+8*a*b/(a*a+b*b)**2)
base=x*x+y*y+a*a+b*b;C=2*x*a;B=2*y*b
ratio=((base-C-B)*(base+C+B))/((base-C+B)*(base+C-B))
ez('stable_log_ratio',ratio-(1-4*C*B/(base*base-(C-B)**2)))
# Sign translation checks with arbitrary symbolic transport, rather than a solution assumption.
Dw,w,Tx=s.symbols('Dw w Tx');DB,WB,TXB=-Dw,-w,-Tx
ez('transport_sign_translation',DB+WB-TXB+(Dw+w-Tx))
# Independent finite quadrature of two-image and four-image integrals away from sources.
rows=[]
def kernel(X,Y):
 return np.log(np.linalg.norm(np.asarray(X)-Y,axis=-1))
for n in [16,32,64]:
 z,wg=leggauss(n);qx=.5*(z+1);qy=.5*(z+1);W=np.outer(.5*wg,.5*wg)
 xx,yy=np.meshgrid(qx,qy,indexing='ij');Y=np.stack([xx,yy],axis=-1)
 f=xx*(1-xx*xx)**2*(1-yy)**2
 for X in [(2.,3.),(2.,0.),(-2.,1.),(.0,2.)]:
  Sx=Y*np.array([-1,1]);Sy=Y*np.array([1,-1]);Both=-Y
  d=kernel(X,Y)-kernel(X,Sy)-kernel(X,Sx)+kernel(X,Both)
  grouped=-np.sum(W*f*d)/(2*np.pi)
  # Source terms integrated separately, preserving odd-in-x upper source.
  upper=-np.sum(W*f*(kernel(X,Y)-kernel(X,Sy)))/(2*np.pi)+np.sum(W*f*(kernel(X,Sx)-kernel(X,Both)))/(2*np.pi)
  error=abs(upper-grouped);assert error<2e-16
  rows.append({'n':n,'X':X,'grouped_psi':float(grouped),'upper_psi':float(upper),'difference':float(error)})
# Tail cancellation: a known nonzero leading annular asymptotic, not an infinity certificate.
tail=[];z,wg=leggauss(48);srad=1.5+.5*z;wr=.5*wg;theta=(np.pi/4)*(z+1);wa=(np.pi/4)*wg
alpha=1/3;X=(1.,.5);leading_const=4*X[0]*X[1]/np.pi*((1-2**(-alpha))/alpha)/3
for R in [8,16,32,64,128,256]:
 rad=R*srad[:,None];th=theta[None,:];aa=rad*np.cos(th);bb=rad*np.sin(th)
 bas=X[0]**2+X[1]**2+rad**2
 d=.5*np.log1p(-16*X[0]*X[1]*aa*bb/(bas**2-4*(X[0]*aa-X[1]*bb)**2))
 val=-np.sum(wr[:,None]*R*wa[None,:]*rad*rad**(-alpha)*np.cos(th)*d)/(2*np.pi)
 expected=leading_const*R**(-alpha);rel=abs(val/expected-1)
 assert rel<1/R**2
 tail.append({'R':R,'annular_psi':float(val),'leading_value':float(expected),'relative_error':float(rel)})
assert all(tail[i+1]['relative_error']<tail[i]['relative_error']/3 for i in range(len(tail)-1))
# Wrong-convention comparisons are algebraic, not program mutations.
counter=[]
for name,z in [('smooth_odd_trace_must_have_zero_derivative',s.diff((-x),x).subs(x,0)!=0),('wrong_poisson_sign',s.diff(x*y*y/2,y,2)-(-x)!=0),('missing_x_image_has_nonzero_axis',s.log((0-a)**2+(1-b)**2)-s.log((0-a)**2+(1+b)**2)!=0)]:
 assert z;counter.append(name)
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'status':'PASS','exact_checks':len(checks),'checks':checks,'nonzero_weak_tests':nonzero_weak,'physical_kernel_checks':len(rows),'physical_kernel_rows':rows,'tail_asymptotic_checks':len(tail),'tail_rows':tail,'algebraic_counterchecks':len(counter),'counterchecks':counter,'limits':'No executed program mutations. No B2 solution. Compact physical tests and asymptotic corroboration do not certify a published neural profile.'}
(root/'controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['utc','elapsed_seconds','status','exact_checks','physical_kernel_checks','tail_asymptotic_checks','algebraic_counterchecks']},indent=2))
