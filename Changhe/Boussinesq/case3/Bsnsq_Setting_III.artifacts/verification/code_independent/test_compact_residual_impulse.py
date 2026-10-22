"""Independent exact stress controls and direct compact-perturbation quadrature.

No field inverse or fitting-lane code is reused. Finite tests use C5 compact
polynomial cutoffs, enough for every identity, while the theorem is smooth.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time,hashlib
import sympy as S
import numpy as np
from numpy.polynomial.legendre import leggauss
start=time.monotonic();root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
x,y=S.symbols('x y',real=True);beta=S.symbols('beta',real=True)
p=S.Function('p')(x,y);t=S.Function('T')(x,y)
px=S.diff(p,x);py=S.diff(p,y);v=S.Matrix([-py,px]);om=-S.diff(p,x,2)-S.diff(p,y,2);w=beta*S.Matrix([x,y])+v
D=lambda f:S.Matrix([S.diff(f,x),S.diff(f,y)])
div=lambda a:S.diff(a[0],x)+S.diff(a[1],y)
f=(w.dot(D(om))+om-S.diff(t,x));rt=w.dot(D(t))-(beta-2)*t
checks={}
def ck(name,e):
 z=S.simplify(S.expand(e));checks[name]=(z==0)
 if z!=0:raise AssertionError((name,z))
ck('stress_horizontal',v[0]*om-S.diff(px*py,x)-S.diff((py**2-px**2)/2,y))
ck('stress_vertical',v[1]*om-S.diff((py**2-px**2)/2,x)+S.diff(px*py,y))
ck('div_W',div(w)-2*beta)
ck('f_divergence',f-div(w*om)-(1-2*beta)*om+S.diff(t,x))
ck('t_divergence',rt-div(w*t)+(3*beta-2)*t)
# Exact affine weighted local divergence identities, avoiding infinity.
for ell in [S.Integer(1),x,y]:
 ck('laplacian_affine_'+str(ell),ell*(-S.diff(p,x,2)-S.diff(p,y,2))+div(ell*D(p)-p*D(ell)))
# The x impulse has a flux representation with a compact difference.
C=w*om-S.Matrix([t,0]);flux=x*C-S.Matrix([px*py,(py**2-px**2)/2])
ck('x_impulse_flux',x*f-div(flux)-(1-3*beta)*x*om-t)
fluxy=y*C-S.Matrix([(py**2-px**2)/2,-px*py])
ck('y_impulse_flux',y*f-div(fluxy)-(1-3*beta)*y*om)
# Exact thermal conjugacy first variation of integral temperature is divergence.
eta=S.Function('eta')(x,y);h=S.Matrix([-S.diff(eta,y),S.diff(eta,x)])
ck('thermal_pullback_divergence',-h.dot(D(t))+div(h*t))

u,z=S.symbols('u z',real=True)
bump=(1-u*u)**6*(1-z*z)**6
chi_expr=u*bump*(1+z/3)+bump/5
tau_expr=bump*(1+z/4+u/7)
# Test one positive-x square and its reflection. chi is reflected oddly and tau
# evenly. Their support is separated from x=0 and the moving center.
cd={};td={}
for a in range(4):
 for b in range(4-a):
  cd[a,b]=S.lambdify((u,z),S.factor(S.diff(chi_expr,u,a,z,b)),'numpy',cse=True)
for a,b in [(0,0),(1,0),(0,1)]:td[a,b]=S.lambdify((u,z),S.factor(S.diff(tau_expr,u,a,z,b)),'numpy',cse=True)
rows=[]
for be,aa,eps,teps in [(2.25,1.,.03,.08),(3.,1.2,-.2,.13),(3.5,-.7,.07,-.05),(2.,1.,.12,.0),(2/3,1.,-.02,.1)]:
 c=1+be/2;q=4*aa/be
 for n in [32,48,64]:
  gn,gw=leggauss(n);uu,yy=np.meshgrid(gn,gn,indexing='ij');wt=gw[:,None]*gw[None,:]
  sums=np.zeros(6);absmax=np.zeros(2)
  for sign in [1.,-1.]:
   xx=sign*(2+uu)
   C={ab:eps*sign**(ab[0]+1)*np.asarray(fun(uu,yy)) for ab,fun in cd.items()}
   T={ab:teps*sign**ab[0]*np.asarray(fun(uu,yy)) for ab,fun in td.items()}
   v0x=-c*xx;v0y=c*yy-q*xx**2/2;om0=q*xx;om0x=q;om0y=0.
   w0x=be*xx+v0x;w0y=be*yy+v0y;th0=aa*xx**2;th0x=2*aa*xx;th0y=0.
   dvx=-C[0,1];dvy=C[1,0];dom=-C[2,0]-C[0,2]
   domx=-C[3,0]-C[1,2];domy=-C[2,1]-C[0,3]
   f0=w0x*om0x+w0y*om0y+om0-th0x
   f1=(w0x+dvx)*(om0x+domx)+(w0y+dvy)*(om0y+domy)+om0+dom-th0x-T[1,0]
   t0=w0x*th0x+w0y*th0y-(be-2)*th0
   t1=(w0x+dvx)*(th0x+T[1,0])+(w0y+dvy)*(th0y+T[0,1])-(be-2)*(th0+T[0,0])
   df=f1-f0;dt=t1-t0
   sums+=np.array([np.sum(wt*a) for a in [df,xx*df,yy*df,dt,T[0,0],dom]])
   absmax=np.maximum(absmax,[np.max(np.abs(df)),np.max(np.abs(dt))])
  mass,imp,yimp,thermal,taum,omass=sums
  errors=[mass,yimp,imp-taum,thermal+(3*be-2)*taum,thermal+(3*be-2)*imp,omass]
  row={'beta':be,'a0':aa,'chi_amplitude':eps,'tau_amplitude':teps,'gauss_order':n,'integrals':{'delta_f':mass,'x_delta_f':imp,'y_delta_f':yimp,'delta_t':thermal,'tau':taum,'delta_omega':omass},'max_identity_error':max(map(abs,errors)),'max_pointwise_residual_change':absmax.tolist()}
  if row['max_identity_error']>2e-10:raise AssertionError(row)
  rows.append(row)
out={'status':'ALL_PASSED','utc':datetime.now(timezone.utc).isoformat(),'exact_checks':checks,'finite_compact_controls':rows,'elapsed_seconds':time.monotonic()-start,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'controls supplement the smooth compact-difference proof; no reference135 impulse is evaluated'}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'exact':len(checks),'finite':len(rows),'seconds':out['elapsed_seconds'],'maxerror':max(r['max_identity_error'] for r in rows)},indent=2))
