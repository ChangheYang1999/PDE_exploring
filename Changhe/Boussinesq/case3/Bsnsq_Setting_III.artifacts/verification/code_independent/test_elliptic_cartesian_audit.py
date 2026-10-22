"""Exact manufactured algebra plus Cartesian differentiation and inverse tests."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,sys
import sympy as sp
import numpy as np
from elliptic_cartesian_audit import Manufactured,jacobian,residuals,summarize
from adaptive_modal_inverse import AdaptiveModalInverse,ModalSettings
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'exact':[],'floating':[]}
def exact(name,lhs,rhs=0):
 assert sp.simplify(lhs-rhs)==0,name
 out['exact'].append({'name':name,'pass':True})
w=[sp.Rational(v,60) for v in [-1,9,-45,0,45,-9,1]]
for k in range(8):exact(f'stencil_moment_{k}',sum(wj*sp.Integer(j)**k for j,wj in zip(range(-3,4),w)),1 if k==1 else 36 if k==7 else 0)
exact('absolute_weight_sum',sum(abs(z) for z in w),sp.Rational(11,6));exact('seventh_error_constant',sp.Rational(36,sp.factorial(7)),sp.Rational(1,140))
r=sp.symbols('r',positive=True)
for p in [sp.Rational(5,3),sp.Rational(7,4)]:
 for n in [1,2,4,7]:
  a=(p-n)/2;q=r**n*(1+r*r)**a
  om=-4*a*r**n*((n+1)+(n+a)*r*r)*(1+r*r)**(a-2)
  exact(f'radial_Poisson_p{p}_n{n}',-sp.diff(q,r,2)-sp.diff(q,r)/r+n*n*q/(r*r),om)
  exact(f'radial_derivative_p{p}_n{n}',sp.diff(q,r),q/r*(n+2*a*r*r/(1+r*r)))
# Polynomial Cartesian fields test signs, derivative orientation and exact moments.
p=np.array([[.1,.2],[-.4,.3],[0.,0.],[2.,-1.]])
def pv(p):
 x,y=p.T;return np.stack((-3*y*y+2*x,2*y+4*x**3),axis=-1)
j=jacobian(pv,p,np.full(len(p),.01));x,y=p.T
expected=np.stack([np.stack([2+0*x,-6*y],axis=-1),np.stack([12*x*x,2+0*x],axis=-1)],axis=1)
assert np.max(abs(j-expected))<5e-12
out['floating'].append({'name':'polynomial_cartesian_jacobian','max_error':float(np.max(abs(j-expected))),'pass':True})
for power in [5/3,7/4]:
 m=Manufactured(power);radii=np.array([1e-3,.03,.3,1.,3.,30.,1e3,1e6]);angles=np.array([.23,.87,1.7,2.63])
 pts=(radii[:,None,None]*np.stack((np.sin(angles),-np.cos(angles)),axis=-1)[None,:,:]).reshape(-1,2);rad=np.repeat(radii,len(angles))
 om=m.omega(pts)
 for eta in [2e-4,1e-4,5e-5]:
  j=jacobian(m.velocity,pts,eta*np.maximum(1,rad));res=residuals(j,om)
  mx=float(np.max(abs(res['E'])));scaled=float(np.max(abs(res['E'])/(1+abs(om))))
  assert scaled<2e-8
  out['floating'].append({'name':f'analytic_velocity_p{power}_eta{eta}','E':summarize(res['E'],pts),'scaled_by_1_plus_abs_omega':scaled,'max_abs_div':float(np.max(abs(res['div']))),'pass':True})
 inv=AdaptiveModalInverse(m.radial_source,m.count,ModalSettings(decay=2-power,epsabs=2e-12,epsrel=2e-12,limit=2000))
 # Closed-form mode and velocity comparisons at each radius, independent of differential identity.
 er=[]
 for rr in radii:
  pr,dp=inv.radial(rr);p0,d0=m.radial_velocity(rr);er.append(max(np.max(abs(pr-p0)/(1+abs(p0))),np.max(abs(dp-d0)/(1+abs(d0)))))
 v=inv.relative(pts);v0=m.velocity(pts);ev=float(np.max(abs(v-v0)/(1+abs(v0))))
 assert max(er)<2e-9 and ev<2e-9
 # Separate smaller stencil sample makes the control inexpensive while exercising all scales.
 pt2=pts[::4];rad2=rad[::4];j=jacobian(inv.relative,pt2,1e-4*np.maximum(1,rad2));res=residuals(j,m.omega(pt2));scaled=float(np.max(abs(res['E'])/(1+abs(m.omega(pt2)))))
 assert scaled<2e-7
 out['floating'].append({'name':f'full_plane_inverse_p{power}','max_scaled_modal_error':max(er),'max_scaled_velocity_error':ev,'E':summarize(res['E'],pt2),'max_scaled_E':scaled,'max_abs_div':float(np.max(abs(res['div']))),'radial_calls':len(inv.cache),'failed_inner':sum(not z['inner_success'] for z in inv.evidence),'failed_outer':sum(not z['outer_success'] for z in inv.evidence),'pass':True})
 assert all(e['inner_success'] and e['outer_success'] for e in inv.evidence)
out['all_passed']=True;out['elapsed_seconds']=time.monotonic()-start
p=Path(sys.argv[1]);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
