"""Exact identities supporting packet135, not a functional-analytic certification."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time
import sympy as S

root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
t0=time.monotonic();results=[]
def check(name,expression):
    value=S.simplify(S.expand(expression))
    assert value==0,(name,value)
    results.append({'name':name,'exact_zero':True})

x,y,beta,c=S.symbols('x y beta c',real=True)
psi=x*y+x**3/7+x*y**2/11+x**3*y/13+x*y**3/17
th=x*x*(1+y+x*x/5+y*y/7)
v=S.Matrix([-S.diff(psi,y),S.diff(psi,x)])
v=v-v.subs({x:0,y:0});W=S.Matrix([beta*x,beta*y])+v
P=S.Matrix([S.diff(th,x),S.diff(th,y)])
T=(W.dot(P)-(beta-2)*th)
DP=P.jacobian([x,y]);Dv=v.jacobian([x,y])
for i in range(2):check('differentiated_thermal_component_'+str(i),S.diff(T,[x,y][i])-(DP*W+2*P+Dv.T*P)[i])
chi=S.Function('chi')(x,y);pot=S.Function('pot')(x,y)
lap=lambda f:S.diff(f,x,2)+S.diff(f,y,2)
comp=-2*(S.diff(chi,x)*S.diff(pot,x)+S.diff(chi,y)*S.diff(pot,y))-pot*lap(chi)
check('cutoff_compensating_vorticity',-lap(chi*pot)-chi*(-lap(pot))-comp)

r,s,k,H,ur,gamma,eps=S.symbols('r s k H ur gamma eps',positive=True)
log_weight=(gamma+k-1-eps)*S.log(r)+H*r**(-s)/2
a=1/s+ur/r
raw=gamma/s+k/s-1/s-r*a*S.diff(log_weight,r)
expected=eps/s-(gamma+k-1-eps)*ur/r+H*s*a*r**(-s)/2
check('weighted_transport_coercivity',raw-expected)
check('energy_gap_one_quarter',expected.subs(eps,s/4)-(S.Rational(1,4)-(gamma+k-1-s/4)*ur/r+H*s*a*r**(-s)/2))
D=S.symbols('D',positive=True)
log_current=log_weight.subs({gamma:s,eps:s/4,H:8*D*(k+2)})
log_previous=log_weight.subs({gamma:s,eps:s/4,H:8*D*(k+1),k:k-1},simultaneous=True)
# Compute the previous index directly to avoid a substitution-order assumption.
log_previous=(s+k-2-s/4)*S.log(r)+4*D*(k+1)*r**(-s)
check('adjacent_energy_weight_ratio',log_current-S.log(r)-log_previous-4*D*r**(-s))
for kval in range(30):
 for sval in [S.Rational(1,100),S.Rational(1,9),S.Rational(1,4),S.Rational(49,100)]:
  for gval in [sval,2*sval]:
   assert abs(gval+kval-1-sval/4)+(kval+1)<=2*(kval+2)
results.append({'name':'coercivity_margin_rational_controls','cases':240,'passed':True,'scope':'The all-order inequality is proved in PROOF.md; these are controls.'})

# Differentiate the anisotropic homogeneous stream independently for rational p.
B,nu=S.symbols('B nu',positive=True)
Q=x*x+nu*y*y
for sval in [S.Rational(1,4),S.Rational(1,3),S.Rational(2,5)]:
 p=(1-sval)/2;hom=-B*x*Q**p
 om=-lap(hom)
 wanted=2*B*p*x*Q**(p-2)*((2-sval+nu)*x*x+nu*(3-sval*nu)*y*y)
 check('anisotropic_leading_vorticity_s_'+str(sval),S.powsimp(om-wanted,force=True))

# Scaling and residual elimination. R^s is represented by 1/delta;
# the exponent identities m-1=-2s and 1-s-s=-2s are checked separately.
delta,rho,refop,etheta,rtheta,inter,ecorr,gR=S.symbols('delta rho refop etheta rtheta inter ecorr gR')
check('temperature_scaling_power',(1-2*s)-1+2*s)
scaled=refop/delta+delta*inter+ecorr-etheta
check('scaled_residual_identity',scaled.subs(refop,delta*(gR+rtheta))-(gR+delta*inter+ecorr-(etheta-rtheta)))
fixed=rho*(-gR+(etheta-rtheta)-delta*inter)
check('compact_forcing_residual',scaled.subs({refop:delta*(gR+rtheta),ecorr:fixed})-(rho-1)*((etheta-rtheta)-gR-delta*inter))
check('top_order_recurrence',4*4**(-s)*(4*delta**2*S.Symbol('L')*4**(-s))-16*delta**2*S.Symbol('L')*4**(-2*s))

out={'utc':datetime.now(timezone.utc).isoformat(),'status':'ALL_EXACT_CONTROLS_PASSED','elapsed_seconds':time.monotonic()-t0,'checks':results,'scope':'Selected exact algebra and rational controls. No numerical proof of Banach completeness, Sobolev estimates, smoothness or a B2 profile is claimed.'}
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
