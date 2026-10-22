"""Independent finite coefficient, endpoint and inverse controls for P278."""
from pathlib import Path
from datetime import datetime,timezone
import time,json,hashlib
import sympy as s
R=Path('research/278_all_axis_jets_compact_extension/verification')
started=datetime.now(timezone.utc).isoformat();tick=time.monotonic();checks=[]
def check(name,ok,detail=None): checks.append({'name':name,'passed':bool(ok),'detail':detail})
def zero(name,expr):
 z=s.simplify(s.expand(expr));check(name,z==0,None if z==0 else str(z))
x,y=s.symbols('x y',real=True);beta=s.symbols('beta',positive=True);A,c0=s.symbols('A c0',real=True,nonzero=True)
d=(3*beta+2)/2;M=6
b=s.Function('b')(y);a={n:s.Function('a'+str(n))(y)for n in range(1,M+2)}
v={0:b};v.update({j:s.Function('v'+str(j))(y)for j in range(1,M+2)})
q={n:s.Function('q'+str(n))(y)for n in range(M+1)}
Theta=sum(a[n]*x**(2*n)for n in a)
W1=(2*beta-s.diff(b,y))*x-sum(s.diff(v[j],y)*x**(2*j+1)/s.Integer(2*j+1)for j in range(1,M+2))
W2=b+sum(v[j]*x**(2*j)for j in range(1,M+2))
Omega=sum(q[n]*x**(2*n+1)for n in q)
RT=s.Poly(s.expand(W1*s.diff(Theta,x)+W2*s.diff(Theta,y)-(beta-2)*Theta),x)
RO=s.Poly(s.expand(W1*s.diff(Omega,x)+W2*s.diff(Omega,y)+Omega-s.diff(Theta,x)),x)
for n in range(1,M+2):
 rhs=sum(s.Rational(2*(n-j),2*j+1)*s.diff(v[j],y)*a[n-j]-v[j]*s.diff(a[n-j],y)for j in range(1,n))
 lhs=b*s.diff(a[n],y)+((4*n-1)*beta+2-2*n*s.diff(b,y))*a[n]
 zero('thermal_coefficient_'+str(n),RT.coeff_monomial(x**(2*n))-(lhs-rhs))
for n in range(M+1):
 rhs=2*(n+1)*a[n+1]+sum(s.Rational(2*(n-j)+1,2*j+1)*s.diff(v[j],y)*q[n-j]-v[j]*s.diff(q[n-j],y)for j in range(1,n+1))
 lhs=b*s.diff(q[n],y)+((4*n+2)*beta+1-(2*n+1)*s.diff(b,y))*q[n]
 zero('vorticity_coefficient_'+str(n),RO.coeff_monomial(x**(2*n+1))-(lhs-rhs))
Curl=s.Poly(s.expand(s.diff(W1,y)-s.diff(W2,x)),x)
for n in range(M+1):zero('negative_curl_'+str(n),Curl.coeff_monomial(x**(2*n+1))+s.diff(v[n],y,2)/s.Integer(2*n+1)+(2*n+2)*v[n+1])
zero('divergence',s.diff(W1,x)+s.diff(W2,y)-2*beta)
for label,field,parity in [('Theta',Theta,1),('Omega',Omega,-1),('W1',W1,-1),('W2',W2,1)]:zero('parity_'+label,field.subs(x,-x)-parity*field)
zero('axis_temperature',Theta.subs(x,0))
zero('axis_velocity',W2.subs(x,0)-b)
# Derivation from an independently formed stream polynomial.
V0=b-beta*y+c0
Psi=V0*x+sum(v[j]*x**(2*j+1)/s.Integer(2*j+1)for j in range(1,M+2))
zero('stream_W1',beta*x-s.diff(Psi,y)-W1)
zero('stream_W2',beta*y+s.diff(Psi,x)-c0-W2)
zero('stream_negative_Laplacian',-s.diff(Psi,x,2)-s.diff(Psi,y,2)-(s.diff(W1,y)-s.diff(W2,x)))
# All identities in the explicit center neighborhood.
P=c0*x+(d-beta)*y*x-A*x**3/(3*beta);T=A*x*x/2
U1=-s.diff(P,y);U2=s.diff(P,x);O=-s.diff(P,x,2)-s.diff(P,y,2)
V1=beta*x+U1;V2=beta*y+U2-c0
zero('center_temperature_PDE',V1*s.diff(T,x)+V2*s.diff(T,y)-(beta-2)*T)
zero('center_vorticity_PDE',V1*s.diff(O,x)+V2*s.diff(O,y)+O-s.diff(T,x))
zero('center_velocity_horizontal',U1.subs({x:0,y:0}))
zero('center_velocity_vertical',U2.subs({x:0,y:0})-c0)
zero('center_strain',s.diff(P,x,y).subs({x:0,y:0})-(1+beta/2))
zero('center_omega_jet',s.diff(O,x)-2*A/beta)
zero('center_temperature_jet',s.diff(T,x,2)-A)
zero('beta2_center_equilibrium_curve',V2.subs({beta:2,y:A*x*x/8}))
zero('beta2_center_horizontal',V1.subs(beta,2))
n=s.symbols('n',integer=True,positive=True)
zero('thermal_center_indicial',((4*n-1)*beta+2-2*n*d)-(n-1)*(beta-2))
zero('vorticity_center_indicial',((4*n+2)*beta+1-(2*n+1)*d)-(beta/2+n*(beta-2)))
# Both endpoint signs are differentiated from b(y), not asserted.
tau=s.symbols('tau',positive=True);K=s.symbols('K',nonzero=True);lam=3*beta+2;alpha=2*beta+1
for end,bb,tt in [('positive',(y-3)**2,1/(3-y)),('negative',-(y+3)**2,1/(3+y))]:
 zero('endpoint_transport_'+end,bb*s.diff(tt,y)-1)
 zero('endpoint_bprime_'+end,s.diff(bb,y)+2/tt)
 zero('endpoint_v1_constant_'+end,-s.diff(bb,y,2)/2-(-1 if end=='positive'else 1))
base=K*tau**-4*s.exp(-lam*tau)
zero('thermal_endpoint_exact',s.diff(base,tau)+(lam+4/tau)*base)
H=s.Function('H')(tau);qbase=tau**-2*s.exp(-alpha*tau)*H
qres=s.diff(qbase,tau)+(alpha+2/tau)*qbase
zero('vorticity_endpoint_factor',qres-tau**-2*s.exp(-alpha*tau)*s.diff(H,tau))
zero('vorticity_endpoint_forcing',qres.subs(s.diff(H,tau),2*K*tau**-2*s.exp(-(lam-alpha)*tau))-2*base)
zero('lambda_minus_alpha',lam-alpha-(beta+1))
zero('thermal_endpoint_gap',(4*n-1)*beta+2-lam-4*(n-1)*beta)
zero('vorticity_endpoint_gap',(4*n+2)*beta+1-alpha-4*n*beta)
zero('thermal_endpoint_invpower',-2*n*(-2/tau)-4*n/tau)
zero('vorticity_endpoint_invpower',-(2*n+1)*(-2/tau)-(4*n+2)/tau)
# Check the integrating factor with completely free forcing.
cc,nu=s.symbols('c nu',real=True);Z=s.Function('Z')(tau)
z=tau**(-nu)*s.exp(-cc*tau)*Z
zero('linear_ODE_integrating_factor',s.diff(z,tau)+(cc+nu/tau)*z-tau**(-nu)*s.exp(-cc*tau)*s.diff(Z,tau))
mu,sig=s.symbols('mu sigma',real=True)
f=tau**mu*s.exp(-sig*tau)
zero('spatial_derivative_positive',tau*tau*s.diff(f,tau)-tau**(mu+1)*s.exp(-sig*tau)*(mu-sig*tau))
zero('spatial_derivative_negative',-tau*tau*s.diff(f,tau)+tau**(mu+1)*s.exp(-sig*tau)*(mu-sig*tau))
# Harmonic recurrence outside J.
for j in range(1,7):
 vj=(-1)**j*s.diff(b,y,2*j)/s.factorial(2*j)
 vn=(-1)**(j+1)*s.diff(b,y,2*(j+1))/s.factorial(2*(j+1))
 zero('outer_curl_recurrence_'+str(j),-s.diff(vj,y,2)/(s.Integer(2*j+1)*(2*j+2))-vn)
# Independent canonical-inverse moments for Gaussian stream modes.
rr,phi=s.symbols('r phi',positive=True,real=True)
Pg=c0*x*s.exp(-x*x-y*y);Og=-s.diff(Pg,x,2)-s.diff(Pg,y,2)
zero('Gaussian_omega',Og-c0*x*(8-4*(x*x+y*y))*s.exp(-x*x-y*y))
center=s.integrate(s.cos(phi)**2,(phi,0,2*s.pi))*s.integrate(rr*(8-4*rr*rr)*s.exp(-rr*rr),(rr,0,s.oo))*c0/(2*s.pi)
zero('Gaussian_fullplane_center_velocity',center-c0)
cs=s.symbols('cs',real=True);Ps=cs*x*y*s.exp(-x*x-y*y);Os=-s.diff(Ps,x,2)-s.diff(Ps,y,2)
zero('Gaussian_strain_omega',Os-cs*x*y*(12-4*(x*x+y*y))*s.exp(-x*x-y*y))
strain=s.integrate(s.cos(phi)**2*s.sin(phi)**2,(phi,0,2*s.pi))*s.integrate(rr*(12-4*rr*rr)*s.exp(-rr*rr),(rr,0,s.oo))*cs/s.pi
zero('Gaussian_fullplane_strain',strain-cs)
# Direct divergence identity supplies the global defect sign.
zero('product_divergence_identity',s.diff(W1*Theta**2,x)+s.diff(W2*Theta**2,y)-2*Theta*(W1*s.diff(Theta,x)+W2*s.diff(Theta,y))-2*beta*Theta**2)
zero('integrated_temperature_defect_coefficient',-beta-(beta-2)-2*(1-beta))
for betav in [2,s.Rational(5,2),3,7]:check('negative_global_defect_beta_'+str(betav),2*(1-betav)<0)
# The cutoff exponents leave room to control all prescribed seminorms.
for j in range(1,9):
 check('stream_cutoff_exponent_'+str(j),2*j+1-j>0)
 check('temperature_cutoff_exponent_'+str(j),2*j-j>0)
proof=R.parent/'PROOF.md';pre=json.loads((R/'proof_before_checks.json').read_text())
check('proof_precedes_controls',pre['written_utc']<started)
check('proof_unchanged',hashlib.sha256(proof.read_bytes()).hexdigest()==pre['proof_sha256'])
result={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'passed':sum(a['passed']for a in checks),'total':len(checks),'checks':checks,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':pre['proof_sha256'],'scope':'Finite exact algebraic controls supplement the complete all-order informal proof. The constructed fields do not solve the full PDE. No numerical existence claim.'}
(R/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(result['passed'],result['total'],result['elapsed_seconds']);print([a for a in checks if not a['passed']])
