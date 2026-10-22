"""Independent generic symbolic checks of packet137; no fitting/NUM imports."""
from pathlib import Path
import json,sys,time
from datetime import datetime,timezone
import sympy as S
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True);tic=time.perf_counter();checks=[]
x,y,k=S.symbols('x y k');u=S.Function('u')(x,y);v=S.Function('v')(x,y);o=S.Function('o')(x,y);theta=S.Function('theta')(x,y)
def compatibility(W,omega):
 u,v=W;J=S.diff(v,x);F=u*S.diff(omega,x)+v*S.diff(omega,y)+omega
 D=(k-S.diff(u,x))*F-u*S.diff(F,x)-v*S.diff(F,y)
 Z=u*F*J+v*D
 return S.expand(J*S.diff(Z,y)-Z*S.diff(J,y)-k*D*J)
def residual_operator(W,h):
 u,v=W;J=S.diff(v,x);d=(k-S.diff(u,x))*h-u*S.diff(h,x)-v*S.diff(h,y);z=u*J*h+v*d
 return S.expand(J*S.diff(z,y)-S.diff(J,y)*z-k*J*d)
f=u*S.diff(o,x)+v*S.diff(o,y)+o-S.diff(theta,x)
t=u*S.diff(theta,x)+v*S.diff(theta,y)-k*theta
J=S.diff(v,x)
M=J**2*S.diff(t,y)-J*v*S.diff(t,x,y)+(v*S.diff(J,y)+J*(k-S.diff(v,y)))*S.diff(t,x)
assert S.expand(compatibility((u,v),o)-residual_operator((u,v),f)-M)==0
checks.append({'generic_two_residual_identity':True})
h=S.Function('h')(x,y);L=residual_operator((u,v),h)
h_derivs=[d for d in L.atoms(S.Derivative)if d.expr==h]
assert max(len(d.variables)for d in h_derivs)<=2
assert max(len(d.variables)for d in L.atoms(S.Derivative)if d.expr in[u,v])<=2
E=compatibility((u,v),o)
assert max(len(d.variables)for d in E.atoms(S.Derivative)if d.expr==o)<=3
assert max(len(d.variables)for d in E.atoms(S.Derivative)if d.expr in[u,v])<=2
checks.append({'differential_orders':{'L_scalar':2,'L_velocity':2,'E_vorticity':3,'E_velocity':2},'passed':True})
# Direct polynomial manufactured thermal solution, no PDE solver involved.
W=(x,7*y-x*x/2);omega=x*(1+y);th=x*x;beta=S.Integer(4)
F=S.expand(W[0]*S.diff(omega,x)+W[1]*S.diff(omega,y)+omega);res=F-S.diff(th,x)
assert res==9*x*y-x**3/2
assert S.expand(W[0]*S.diff(th,x)+W[1]*S.diff(th,y)-2*th)==0
Et=S.expand(compatibility(W,omega).subs(k,2));Lt=S.expand(residual_operator(W,res).subs(k,2));assert Et==Lt
integral=S.integrate(Et**2,(x,-1,1),(y,-1,1));assert integral>0
checks.append({'manufactured_f':str(res),'manufactured_E':str(Et),'positive_square_integral_on_unit_square':str(integral),'passed':True})
# A true local polynomial profile gives E=0, including the line J=0.
assert compatibility(W,x).subs(k,2)==0
checks.append({'local_polynomial_profile_and_zero_J_axis':True})
# The detector is not sufficient: J identically0 makes E identically0 even
# for generic source fields. This explicit negative control prevents overclaim.
assert compatibility((x,7*y),omega).subs(k,2)==0
checks.append({'non_sufficiency_J_identically_zero':True})
# Moment blindness: FTC for phi=x² eta(x²+y²) with arbitrary radial eta.
eta=S.Function('eta');phi=x*x*eta(x*x+y*y);ff=S.diff(phi,x)
assert S.simplify(ff.subs(x,-x)+ff)==0
assert phi.subs(x,0)==0
checks.append({'compact_radial_bump_moment_primitive':str(ff),'odd_source':True,'axis_primitive_zero':True,'scope':'Choose eta smooth compactly supported; endpoint at infinity is then0 by support, so FTC gives zero horizontal moment.'})
j={'status':'ALL_EXACT_CONTROLS_PASSED','utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-tic,'checks':checks};(out/'tests.json').write_text(json.dumps(j,indent=2)+'\n');print(j['status'],j['elapsed_seconds'],flush=True)
