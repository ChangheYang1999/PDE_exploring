"""Manufactured checks for172; exact algebra before archive diagnostics."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import sympy as s
import numpy as np
from center_moment_inverse import CenterMomentInverse
from elliptic_cartesian_audit import Manufactured,jacobian,residuals
from adaptive_modal_inverse import ModalSettings
ap=argparse.ArgumentParser();ap.add_argument('output');ap.add_argument('--exact-only',action='store_true');arg=ap.parse_args()
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'exact':[],'floating':[]}
def eq(name,z):
 assert s.simplify(z)==0,name
 out['exact'].append({'name':name,'pass':True})
r,L,b=s.symbols('r L b',positive=True);tt=1-(1+(r/L)**2)**(-1/(2*b))
eq('odd_source_G_dr_equals_bL_dt',(1-tt)**(b+1)*r/s.sqrt(L*L+r*r)-b*L*s.diff(tt,r))
x,y,M=s.symbols('x y M',real=True);psi=-M*x*y/2
eq('center_strain_sign',s.diff(psi,x,y)+M/2)
# Direct monomial source tests on finite inner intervals, independent of Green code.
for n in [2,3,4,7,16]:
 for power in [n,n+2,n+4]:
  aa=r**power/(n+power+2);dd=r**power/(power-n+2)
  q=M*r**n/(2*n)+r*r*(aa-dd)/(2*n)
  eq(f'radial_poisson_n{n}_h_power{power}',-s.diff(q,r,2)-s.diff(q,r)/r+n*n*q/r**2-r**power)
  eq(f'radial_derivative_n{n}_h_power{power}',s.diff(q,r)-(M*r**(n-1)/2-r*(aa+dd)/2))
# Exact manufactured moment via integration of a radial total derivative.
for n in [2,3,4,7]:
 for p in [s.Rational(5,3),s.Rational(7,4)]:
  q=r**n*(1+r*r)**((p-n)/2)
  h=-s.diff(q,r,2)-s.diff(q,r)/r+n*n*q/r**2
  primitive=r**(1-n)*s.diff(q,r)+n*r**(-n)*q
  eq(f'manufactured_moment_antiderivative_n{n}_p{p}',s.diff(primitive,r)+r**(1-n)*h)
  eq(f'manufactured_moment_origin_n{n}_p{p}',s.limit(primitive,r,0)-2*n)
  eq(f'manufactured_moment_infinity_n{n}_p{p}',s.limit(primitive,r,s.oo))
if not arg.exact_only:
 for p in [5/3,7/4]:
  m=Manufactured(p);sw=.1
  inv=CenterMomentInverse(m.radial_source,m.count,ModalSettings(decay=2-p,epsabs=2e-14,epsrel=2e-13,limit=3000),switch=sw,exact_M2=4*m.weights[1])
  expected=2*m.n[1:]*m.weights[1:]*sw**(m.n[1:]-2)
  # M2 is checked before its exact replacement.
  me=max(float(np.max(abs(inv.C-expected))),abs(inv.moment_evidence['M2_quadrature_error_vs_exact_rounded']))
  assert me<2e-11
  radii=np.geomspace(1e-6,sw*.8,12);ang=np.array([.23,.87,1.7,2.63]);pts=(radii[:,None,None]*np.stack([np.sin(ang),-np.cos(ang)],axis=-1)[None,:,:]).reshape(-1,2)
  v=inv.relative(pts);v0=m.velocity(pts);verr=float(np.max(abs(v-v0)))
  assert verr<2e-11
  rows=[]
  for hh in [2e-4,1e-4,5e-5]:
   j=jacobian(inv.relative,pts,np.full(len(pts),hh));res=residuals(j,m.omega(pts));e=float(np.max(abs(res['E'])));div=float(np.max(abs(res['div'])))
   assert e<2e-9 and div<2e-9
   rows.append({'h':hh,'max_abs_E':e,'max_abs_div':div})
  # Direct integral and local representation on the same interface radius.
  pr,dp=inv.radial(sw);from adaptive_modal_inverse import AdaptiveModalInverse
  old=AdaptiveModalInverse(m.radial_source,m.count,inv.settings);p0,d0=old.radial(sw);gap=max(float(np.max(abs(pr-p0))),float(np.max(abs(dp-d0))))
  assert gap<2e-11
  out['floating'].append({'p':p,'max_scaled_moment_error':me,'max_abs_velocity_error':verr,'interface_modal_gap':gap,'cartesian':rows,'moment':inv.moment_evidence,'local_calls':len(inv.local_evidence),'failed_local':sum(not z['success'] for z in inv.local_evidence),'pass':True})
  assert all(z['success'] for z in inv.local_evidence)
out['elapsed_seconds']=time.monotonic()-start;out['all_passed']=True;out['exact_only']=arg.exact_only
Path(arg.output).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'exact_count':len(out['exact']),'floating_count':len(out['floating']),'elapsed_seconds':out['elapsed_seconds'],'all_passed':True}))
