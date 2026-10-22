"""Independent P198 controls: exact algebra, native coefficient fields, Duffy inverse."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
import sympy as S
from r2_state_values import R2State
from cartesian_inverse import CartesianInverse,InverseSettings

root=Path('research/198_scaling_and_projected_jacobian/verification');start=time.monotonic();checks=[]
x,y,l,b,ep,lam=S.symbols('x y l beta eps lam',real=True,nonzero=True)
F=1+2*y+3*x*x+5*y*y+x*x*y
H=2+3*y+5*x*x-7*y*y+2*x*x*y
Psi=x*H;Om=-S.diff(Psi,x,2)-S.diff(Psi,y,2);G=S.cancel(Om/x);Th=x*x*F
sub=lambda f:S.expand(f.subs({x:x/l,y:y/l},simultaneous=True))
def exact(label,v):
 if isinstance(v,S.MatrixBase):ok=all(S.simplify(a)==0 for a in v)
 else:ok=S.simplify(v)==0
 assert ok,label
 checks.append(label)
for name,Q,weight,physical in [('G',G,-1,Om),('F',F,-1,Th),('H',H,1,Psi)]:
 Ql=l**weight*sub(Q); tangent=weight*Q-x*S.diff(Q,x)-y*S.diff(Q,y)
 exact(name+' tangent',S.diff(Ql,l).subs(l,1)-tangent)
 if name=='G':exact('divided omega',x*Ql-sub(physical))
 if name=='F':exact('divided theta',x*x*Ql-l*sub(physical))
 if name=='H':exact('divided stream',x*Ql-l*l*sub(physical))
exact('strain invariant',S.diff(l*l*sub(Psi),x,y).subs({x:0,y:0})-S.diff(Psi,x,y).subs({x:0,y:0}))
exact('wrong strain derivative',S.diff(S.diff(l**3*sub(Psi),x,y).subs({x:0,y:0}),l).subs(l,1)-S.diff(Psi,x,y).subs({x:0,y:0}))
U=S.Matrix([-S.diff(Psi,y),S.diff(Psi,x)]);U-=U.subs({x:0,y:0})
Sf=x*(2+y+x*x+3*y*y);Vf=S.Matrix([-S.diff(Sf,y),S.diff(Sf,x)]);Vf-=Vf.subs({x:0,y:0})
coord=S.Matrix([x,y]);grad=lambda f:S.Matrix([S.diff(f,x),S.diff(f,y)])
W=b*coord+ep*U+lam*Vf
RO=(W.dot(grad(Om))+Om-S.diff(Th,x)).expand();RT=(W.dot(grad(Th))-(b-2)*Th).expand()
Ol=sub(Om);Tl=l*sub(Th);Ul=l*U.subs({x:x/l,y:y/l},simultaneous=True);Wl=b*coord+ep*Ul+lam*Vf;Dl=Vf-l*Vf.subs({x:x/l,y:y/l},simultaneous=True)
exact('forced vorticity scaling',Wl.dot(grad(Ol))+Ol-S.diff(Tl,x)-sub(RO)-lam*Dl.dot(grad(Om).subs({x:x/l,y:y/l},simultaneous=True))/l)
exact('forced thermal scaling',Wl.dot(grad(Tl))-(b-2)*Tl-l*sub(RT)-lam*Dl.dot(grad(Th).subs({x:x/l,y:y/l},simultaneous=True)))
exact('source tangent',S.diff(Dl,l).subs(l,1)-(Vf.jacobian([x,y])*coord-Vf))
for n in (2,3,5):
 c=S.Matrix([[S.Rational(i+2,i+1)for i in range(n)]]);q=S.Matrix([(-1)**i*(i+1)for i in range(n)]);cq=(c*q)[0];assert cq!=0
 P=S.eye(n)-q*c/cq;B=S.Matrix(n,n,lambda i,j:S.Rational((i+1)*(j+2),i+j+1));J=B*P;A=J-S.eye(n)
 exact(f'projection q n{n}',P*q);exact(f'JT zero n{n}',J*q);exact(f'A minusq n{n}',A*q+q)
 exact(f'P idempotent n{n}',P*P-P)
for h in (S.Rational(1,100),S.Rational(1,1000000)):
 for target in (S.Rational(-3),S.Rational(0),S.Rational(29,7)):
  t=S.symbols('t');zero=t*(t-h/10)*(t-h)*(t-10*h);den=S.diff(zero,t).subs(t,0);f=t+(target-1)*zero/den
  for step in (h/10,h,10*h):exact(f'FD node{h}_{target}_{step}',f.subs(t,step)-step)
  exact(f'FD actual derivative{h}_{target}',S.diff(f,t).subs(t,0)-target)
for M in (S.Rational(1),S.Rational(20),S.Rational(10000)):
 A=S.Matrix([[1,M],[0,1]]);D=S.diag(M,1);exact('similarity'+str(M),A-D*S.Matrix([[1,1],[0,1]])*D.inv());exact('singular test'+str(M),A*S.Matrix([-M,1])-S.Matrix([0,1]))

# Native-state checks at independently generated Cartesian samples including axes.
radii=np.r_[0.,1e-6,1e-4,.02,.3,1.,3.,10.,100.,1e4,1e6];phi=np.array([0.,.13,.7,1.1,np.pi/2,2.3,np.pi]);rr,pp=np.meshgrid(radii,phi,indexing='ij');xx=(rr*np.sin(pp)).ravel();yy=(-rr*np.cos(pp)).ravel();r=np.hypot(xx,yy);eta=np.divide(-yy,r,out=np.zeros_like(r),where=r!=0)
source_root=Path('research/196_forced_tail_coefficients/verification');state_rows=[]
# Seven-point coefficients for d/dell at ell=1.
weights=np.array([-1,9,-45,0,45,-9,1],dtype=float)/60
for file in sorted(source_root.glob('*.npz')):
 s=R2State(file);z=np.exp(-np.log1p((r/s.L)**2)/(2*s.bb));t=1-z;w=r*r/(r*r+s.L*s.L);odd=r/np.hypot(r,s.L)
 ang=np.cos(np.arccos(eta)[:,None]*np.arange(s.K));row={'archive':file.name,'sha256':s.sha256,'beta':s.beta,'K':s.K,'points':len(r),'checks':[]}
 for kind,spline,power in [('G',s.Gs,s.bb+1),('F',s.Fs,s.bb+2)]:
  C=spline(t);Ct=spline.derivative()(t);fact=np.ones_like(C);fact[:,1::2]=odd[:,None];df=np.zeros_like(C);df[:,1::2]=(odd*(1-w))[:,None]
  radial=z[:,None]**power*((-power*w/s.bb)[:,None]*C*fact+(z*w/s.bb)[:,None]*Ct*fact+C*df)
  base=s.divided(xx,yy,kind);tangent=-base-np.sum(radial*ang,axis=1)
  for h in (.002,.001,.0005):
   terms=np.array([s.divided(xx/(1+j*h),yy/(1+j*h),kind)/(1+j*h)for j in range(-3,4)])
   fd=(weights@terms)/h;scale=np.maximum(1.,abs(tangent));error=float(np.max(abs(fd-tangent)/scale))
   row['checks'].append({'kind':kind,'ell_step':h,'maximum_scaled_FD_error':error,'center_true_tangent':float(tangent[0]),'center_wrong_tangent':0.})
  # Exact scaling of the ideal representation checked without mutating archive.
  savedL=s.L; savedSpline=s.Fs if kind=='F' else s.Gs
  for ell in (.5,1.75,3.):
   desired=s.divided(xx/ell,yy/ell,kind)/ell;s.L=savedL*ell
   actual=s.divided(xx,yy,kind)/ell;s.L=savedL
   row['checks'].append({'kind':kind,'ell':ell,'maximum_representation_identity_error':float(np.max(abs(actual-desired)/np.maximum(1.,abs(desired))))})
 row['c_self']=s.strain();row['true_strain_dilation_error']=[];c=s.strain()
 for ell in (.5,1.75,3.):
  old=s.L;s.L=old*ell;c_unweighted=s.strain();s.L=old
  row['true_strain_dilation_error'].append({'ell':ell,'corrected_error':c_unweighted/ell-c,'unweighted_strain':c_unweighted,'predicted_unweighted_strain':ell*c})
 state_rows.append(row)

# Shifted Gaussian: independent Cartesian full-plane inverse, no spectral solver.
d=.7
omega=lambda x,y:x*np.exp(-(x*x+(y-d)**2))
def psi_f(s):return -np.expm1(-s)/(4*s)
def psi_fp(s):return ((s+1)*np.exp(-s)-1)/(4*s*s)
def vel(x,y):
 ss=x*x+(y-d)**2;hp=psi_fp(ss);return np.column_stack((-2*x*(y-d)*hp,psi_f(ss)+2*x*x*hp))
pts=np.array([[.1,.2],[.4,-.2],[.9,1.3],[1.2,-1.5],[2.1,.6]])
u0=np.array([0.,psi_f(d*d)]);truth=vel(pts[:,0],pts[:,1])-u0
inverse=[]
for ell in (.5,1.,2.):
 for order in (20,36):
  fn=lambda x,y:omega(x/ell,y/ell)
  inv=CartesianInverse(fn,InverseSettings(radius=8*ell,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1.))
  vv=inv.relative(ell*pts);err=float(np.max(abs(vv-ell*truth)));inverse.append({'ell':ell,'order':order,'maximum_absolute_velocity_error':err})
  assert err<2e-8
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_checks_count':len(checks),'exact_checks':checks,'states':state_rows,'inverse':inverse,'all_passed':True,'scope':'Exact algebra and sampled floating controls of the representation and inverse scaling. Does not certify continuum Jacobian or existence.'}
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_checks':len(checks),'states':len(state_rows),'inverse_checks':len(inverse),'inverse_max':max(z['maximum_absolute_velocity_error']for z in inverse),'elapsed_seconds':out['elapsed_seconds']},indent=2))
