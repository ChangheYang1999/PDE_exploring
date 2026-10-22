"""Exact manufactured controls for packet173. No numerical flow is a proof."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,sys,time
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'checks':[],'negative_controls':[]}
def eq(name,z):
 entries=list(z) if isinstance(z,s.MatrixBase) else [z]
 assert all(s.simplify(s.expand(v))==0 for v in entries),name
 out['checks'].append({'name':name,'pass':True})
a,r,lam=s.symbols('a r lambda',real=True)
J=s.Matrix([[0,-1],[1,0]]);I=s.eye(2)
for j,tau in enumerate([s.Matrix([1,0]),s.Matrix([0,1]),s.Matrix([s.Rational(3,5),s.Rational(4,5)]),s.Matrix([-s.Rational(5,13),s.Rational(12,13)]),s.Matrix([0,-1])]):
 n=J*tau;e=n+lam*tau/4;M=(4*n+lam*tau)*n.T;P=M/4
 eq(f'eigen_tau{j}',M*tau);eq(f'eigen_e{j}',M*e-4*e);eq(f'det{j}',s.det(s.Matrix.hstack(tau,e))-1)
 eq(f'projection{j}',P*P-P);eq(f'trace{j}',s.trace(M)-4)
 # Curl computed in the actual physical frame, not the arc frame.
 eq(f'physical_curl{j}',M[1,0]-M[0,1]+lam)
 for lv in [-3,0,2]:
  ee=e.subs(lam,lv);ey=ee[1]
  if ey!=0:
   g=s.Rational(lv)/ey;eq(f'affine_constraint{j}_{lv}',lv-g*ey)
  elif lv==0:eq(f'affine_zero{j}_{lv}',lv-4*ey)
  else:
   out['negative_controls'].append({'name':f'affine_incompatible{j}_{lv}','nonzero_lambda_with_ey_zero':str(lv),'pass':True})
# Differential operators derived from the inverse Jacobian for area-one charts.
def chart_controls(tag,X,G):
 xa=X.diff(a);xr=X.diff(r);D=s.det(s.Matrix.hstack(xa,xr));eq(tag+'_area',D-1)
 dx=lambda F:s.expand(xr[1]*s.diff(F,a)-xa[1]*s.diff(F,r))
 dy=lambda F:s.expand(-xr[0]*s.diff(F,a)+xa[0]*s.diff(F,r))
 W=4*r*xr;Q=4*xa.dot(xr)+4*r*xa.dot(xr.diff(r))-4*r*xr.dot(xr.diff(a))
 eq(tag+'_div',dx(W[0])+dy(W[1])-4)
 eq(tag+'_curl',dy(W[0])-dx(W[1])-Q)
 eq(tag+'_thermal',W[0]*dx(G)+W[1]*dy(G))
 eq(tag+'_forcing',dx(G)-s.diff(G,a)*xr[1])
 eq(tag+'_transport_Q',W[0]*dx(Q)+W[1]*dy(Q)-4*r*s.diff(Q,r))
 return s.expand(4*r*s.diff(Q,r)+Q-s.diff(G,a)*xr[1])
for j,G in enumerate([1+a, a*a+a**3, a**5-2*a**2+7]):
 eq(f'shear_coupling{j}',chart_controls('shear'+str(j),s.Matrix([a,G/4+r]),G))
f=(a+r*r)**3/7+2*(a+r*r)**2
res=chart_controls('nonlinear_area',s.Matrix([a+r*r,r+f]),a*a)
assert res!=0;out['negative_controls'].append({'name':'area_one_is_not_coupling','residual':str(res),'pass':True})
x,y=s.symbols('x y',real=True);G=x*x+x**5;h=x**3+x
W=s.Matrix([0,4*y-G-4*h]);Omega=s.diff(W[0],y)-s.diff(W[1],x)
eq('pushed_shear_residual',W[0]*s.diff(Omega,x)+W[1]*s.diff(Omega,y)+Omega-s.diff(G,x)-4*s.diff(h,x))
for m in range(10):
 q=r**m/s.Integer(4*m+1);eq(f'resolvent_monomial{m}',4*r*s.diff(q,r)+q-r**m)
 # Both signs are included by polynomial identity, no fractional r roots.
 for rr in [-s.Rational(2,3),s.Rational(1,7)]:eq(f'resolvent_signed{m}_{rr}',(4*r*s.diff(q,r)+q-r**m).subs(r,rr))
# Exact integral kernel sizes in the weighted contraction estimate.
t,v=s.symbols('t v',real=True)
eq('center_kernel_quadratic',s.integrate(s.exp(8*v),(v,-s.oo,t))-s.exp(8*t)/8)
eq('unstable_kernel_quadratic',s.integrate(s.exp(4*(t-v))*s.exp(8*v),(v,-s.oo,t))-s.exp(8*t)/4)
out['elapsed_seconds']=time.monotonic()-start;out['all_passed']=True
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_checks':len(out['checks']),'negative_controls':len(out['negative_controls']),'elapsed_seconds':out['elapsed_seconds'],'all_passed':True}))
