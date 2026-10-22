"""P220 symbolic checks of a manufactured transport field, not a PDE solution."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import time,json,hashlib
v=Path('research/220_compact_foliation_manufactured/verification');start=time.monotonic();now=datetime.now(timezone.utc).isoformat()
x,y=s.symbols('x y',real=True);a=s.sqrt(1+y*y);k=x/a;q=2*s.asinh(y)/a;A=(y*a+s.asinh(y))/2
psi=x*q-k**3/3;theta=k*k;omega=-s.diff(psi,x,2)-s.diff(psi,y,2);U=s.Matrix([-s.diff(psi,y),s.diff(psi,x)]);W=s.Matrix([2*x,2*y])+U
R=W[0]*s.diff(omega,x)+W[1]*s.diff(omega,y)+omega-s.diff(theta,x)
checks={}
def ck(n,e):
 z=s.simplify(e);checks[n]={'difference':str(z),'pass':z==0}
at=lambda e:s.simplify(e.subs({x:0,y:0}))
ck('A_primitive',s.diff(A,y)-a);ck('q_identity',q-(4*A/a-2*y));ck('core_velocity_formula1',W[0]-k*s.diff(a,y)*(4*A-k*k)/a);ck('core_velocity_formula2',W[1]-(4*A-k*k)/a)
ck('core_level_transport',W[0]*s.diff(k,x)+W[1]*s.diff(k,y));ck('core_temperature_transport',W[0]*s.diff(theta,x)+W[1]*s.diff(theta,y));ck('divergence4',s.diff(W[0],x)+s.diff(W[1],y)-4);ck('Poisson_definition',-s.diff(psi,x,2)-s.diff(psi,y,2)-omega)
ck('center_U1',at(U[0]));ck('center_U2',at(U[1]));ck('center_a0',at(s.diff(theta,x,2))/2-1);ck('center_c',at(s.diff(psi,x,y))-2);ck('center_b0',at(s.diff(omega,x))-2)
ck('residual_linear_x_zero',at(s.diff(R,x)));ck('residual_mixed_derivative40',at(s.diff(R,x,y))-40)
ck('psi_xodd',psi.subs(x,-x)+psi);ck('omega_xodd',omega.subs(x,-x)+omega);ck('theta_xeven',theta.subs(x,-x)-theta)
ck('no_imposed_psi_y_parity',psi.subs(y,-y)+psi+2*k**3/3)
# Exact differentiated Green kernel away from zero; distributional mass is proved in PROOF.
phi=-s.log(x*x+y*y)/(4*s.pi);K=s.Matrix([-s.diff(phi,y),s.diff(phi,x)])
ck('kernel_sign1',K[0]-y/(2*s.pi*(x*x+y*y)));ck('kernel_sign2',K[1]+x/(2*s.pi*(x*x+y*y)));ck('kernel_divergence_off_origin',s.diff(K[0],x)+s.diff(K[1],y));ck('kernel_curl_off_origin',s.diff(K[1],x)-s.diff(K[0],y))
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(t['pass'] for t in checks.values()),'exact_residual_mixed_derivative':40,'core_psi':str(psi),'scope':'Symbolic checks where cutoff=1, enough for all center jets and transport on support of Hprime. Global cutoff and inverse are established in complete informal proof, not by finite sampling.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()};(v/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(len(checks),'checks',result['all_passed'],result['elapsed_seconds']);assert result['all_passed']
