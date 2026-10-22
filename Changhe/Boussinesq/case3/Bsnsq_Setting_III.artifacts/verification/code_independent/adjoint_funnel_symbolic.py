"""Exact algebra underlying packets73 and77; no formal/PDE existence claim."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s,json,hashlib
x,y=s.symbols('x y',real=True);b=s.symbols('beta',positive=True);d=s.symbols('d',real=True)
lam=(b-2)/2;mu=(3*b+2)/2;c=1+b/2;k=3*d/(mu-2*lam);a0=-3*b*d/2
W=s.Matrix([lam*x,mu*y+3*d*x*x]);Om=-6*d*x;Th=a0*x*x
q=(2*b-1)/lam;kap=mu/lam
checks={
 'local_curl':s.diff(W[0],y)-s.diff(W[1],x)-Om,
 'local_vorticity_transport':W.dot(s.Matrix([s.diff(Om,x),s.diff(Om,y)]))+Om-s.diff(Th,x),
 'local_temperature_transport':W.dot(s.Matrix([s.diff(Th,x),s.diff(Th,y)]))-(b-2)*Th,
 'triangular_coordinate':W.dot(s.Matrix([s.diff(y+k*x*x,x),s.diff(y+k*x*x,y)]))-mu*(y+k*x*x),
 'center_source_jet':s.diff(Om,x)-4*a0/b,
 'q_minus_four':q-4-3/lam,
 'kappa_minus_three':kap-3-4/lam}
r=s.sqrt(x*x+y*y);chi=s.Function('chi');psi=(c*x*y+d*x**3)*chi(r)
Wr=s.Matrix([b*x-s.diff(psi,y),b*y+s.diff(psi,x)])
checks['radial_cutoff_cancellation']=Wr.dot(s.Matrix([x,y]))-(b*r*r+c*chi(r)*(y*y-x*x)+3*d*chi(r)*x*x*y)
u=s.symbols('u',positive=True);z,qs,ks,K=s.symbols('z q kappa k',real=True);A=s.Function('A')
Y=s.Matrix([u,u**ks*z-K*u*u]);checks['funnel_area']=Y.jacobian([u,z]).det()-u**ks
F=u**(-qs)*A(z);zx=2*K*u**(1-ks)-ks*z/u
checks['physical_derivative']=s.diff(F,u)+zx*s.diff(F,z)-(2*K*u**(-qs+1-ks)*s.diff(A(z),z)+u**(-qs-1)*(-qs*A(z)-ks*z*s.diff(A(z),z)))
checks['weighted_density_exponent']=2+(-qs+1-ks)+ks-(3-qs)
result={k:str(s.simplify(v)) for k,v in checks.items()}
out=dict(time=datetime.now(timezone.utc).isoformat(),checks=result,all_zero=all(v=='0' for v in result.values()),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
p=Path('research/77_adjoint_derivative_integrability/verification/exact_checks.json');p.write_text(json.dumps(out,indent=2)+'\n')
print('packet77 exact checks',len(checks),out['all_zero'])
# Preserve a reproducible version of the earlier packet73 inline checker.
D=s.symbols('D');f=s.Function('f')(x);g=s.Function('g')(x)
U=s.Matrix([f,(D-s.diff(f,x))*y+g]);omega=s.diff(f,x,2)*y-s.diff(g,x)
res=U.dot(s.Matrix([s.diff(omega,x),s.diff(omega,y)]))+omega
expected=(f*s.diff(f,x,3)+(D+1-s.diff(f,x))*s.diff(f,x,2))*y-f*s.diff(g,x,2)+g*s.diff(f,x,2)-s.diff(g,x)
I=f*s.diff(f,x,2)-s.diff(f,x)**2+(D+1)*s.diff(f,x)
v73={'curl':s.diff(U[0],y)-s.diff(U[1],x)-omega,'transport':res-expected,'first_integral_derivative':s.diff(I,x)-(f*s.diff(f,x,3)+(D+1-s.diff(f,x))*s.diff(f,x,2)),'quotient_identity':s.diff((s.diff(f,x)-(D+1))/f,x)-I/f**2}
z73={k:str(s.simplify(v)) for k,v in v73.items()};Path('research/73_local_affine_detachment/verification/reproducible_checks.json').write_text(json.dumps(dict(time=out['time'],checks=z73,all_zero=all(v=='0' for v in z73.values()),code_sha256=out['code_sha256']),indent=2)+'\n');print('packet73 checks',all(v=='0' for v in z73.values()))
