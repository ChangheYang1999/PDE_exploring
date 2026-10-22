"""Exact controls for P228. Independent of all lead/numerics implementations."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as s
root=Path(__file__).resolve().parents[1];out=root/'research/228_finite_horizontal_polynomial/verification'
t0=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks={};diffs={}
def eq(name,left,right=0):
 d=s.factor(s.cancel(left-right));checks[name]=(d==0);diffs[name]=str(d)
def yes(name,value):checks[name]=bool(value)
x,y,R,beta=s.symbols('x y R beta',positive=True); n=s.symbols('n',integer=True,positive=True)
lambda_=beta-2;K=(n-1)*beta+2;p=K/beta
# Generic highest-degree and forced coefficient identities.
eq('positive_K_formula',n*beta-lambda_,K)
yes('positive_K',K.is_positive)
eq('power_exponent',p,n-1+2/beta)
eq('source_mismatch_at_critical_top_coefficient',n*beta-lambda_,K)
# Explicit finite-degree limits, with independent polynomial fixtures.
f=s.Function('f')(y)
for N in [1,2,3,4,6]:
 theta=f*x**N+sum(s.Rational(j+1,j+2)*(y**2+j)*x**j for j in range(N))
 eq(f'N{N}_highest_temperature',s.limit(theta/x**N,x,s.oo),f)
 eq(f'N{N}_highest_xderivative',s.limit(s.diff(theta,x)/x**(N-1),x,s.oo),N*f)
 eq(f'N{N}_highest_yderivative',s.limit(s.diff(theta,y)/x**N,x,s.oo),s.diff(f,y))
 crit=s.diff(theta,y).subs(s.diff(f,y),0)
 # admissible sublinear W2 of order sqrt(x) tests the lost lower-degree term.
 eq(f'N{N}_critical_yterm_limit',s.limit(s.sqrt(x)*crit/x**N,x,s.oo),0)
 W1=beta*x+1/(1+x*x)
 W2=(lambda_*theta-W1*s.diff(theta,x))/s.diff(theta,y)
 eq(f'N{N}_quotient_limit',s.limit(W2,x,s.oo),-((N-1)*beta+2)*f/s.diff(f,y))
# Rectangle flux is checked exactly with beta-linear vertical limit.
a,b,d=s.symbols('a b d',real=True)
flux_h=s.integrate(beta*2*R-beta*R,(y,a,b))
flux_v=s.integrate((beta*b+d)-(beta*a+d),(x,R,2*R))
eq('rectangle_horizontal_flux',flux_h/R,beta*(b-a))
eq('rectangle_vertical_flux',flux_v/R,beta*(b-a))
eq('rectangle_total_divergence',flux_h+flux_v,2*beta*R*(b-a))
z=s.symbols('z',positive=True)
eq('average_vanishing_power_error',s.limit(s.integrate(1/x,(x,R,2*R))/R,R,s.oo),0)
eq('constant_average',s.integrate(d,(x,R,2*R))/R,d)
# Work on either sign component with explicit linear coordinate z>0.
fpos=y**(-p)
eq('scalar_ode_positive_halfline',s.diff(fpos,y)/fpos,-p/y)
eq('manufactured_isotropic_transport',beta*x*s.diff(x**n*fpos,x)+beta*y*s.diff(x**n*fpos,y),lambda_*x**n*fpos)
eq('recovered_affine_g',-K*fpos/s.diff(fpos,y),beta*y)
yes('singular_power_exponent',p.is_positive)
yes('singular_boundary_not_zero',s.limit(y**(-p),y,0,dir='+')==s.oo)
yes('finite_nonzero_boundary_not_zero',(z**(-p)).is_positive)
# Signed f and reflected half-line, with t=-y>0, same scalar equation.
t=s.symbols('t',positive=True)
fneg=-t**(-p); dfdy=-s.diff(fneg,t)
eq('negative_halfline_signed_g',-K*fneg/dfdy,-beta*t)
# Dropping isotropic asymptotic permits exact transport/divergence counterexample.
alpha=lambda_/2;W1=alpha*x;W2=(2*beta-alpha)*y;theta=x*x
eq('anisotropic_control_divergence',s.diff(W1,x)+s.diff(W2,y),2*beta)
eq('anisotropic_control_transport',W1*s.diff(theta,x)+W2*s.diff(theta,y),lambda_*theta)
yes('anisotropic_control_fails_horizontal_limit',s.simplify(alpha-beta)!=0)
# Constant Theta at beta2 illustrates that f0 need not vanish without axis condition.
eq('constant_temperature_beta2',s.S.Zero,(beta-2).subs(beta,2))
# Coefficient C1 recovery needs values only, not N derivatives.
for N in [1,2,4]:
 V=s.Matrix([[s.Integer(i)**j for j in range(N+1)] for i in range(N+1)])
 yes(f'Vandermonde_recovery_degree{N}',V.det()!=0)
proof=out.parent/'PROOF.md'; stamp=json.loads((out/'proof_before_checks.json').read_text())
yes('proof_precedes_controls',stamp['written_utc']<start)
end=datetime.now(timezone.utc).isoformat();report={'started_utc':start,'ended_utc':end,'elapsed_seconds':time.monotonic()-t0,'all_passed':all(checks.values()),'checks':checks,'algebraic_differences':diffs,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'scope':'Exact finite controls support the standalone proof. No finite controls imply the theorem for arbitrary polynomial degree; the general proof uses its top coefficient and integrated divergence. Not an unrestricted B2 exclusion.'}
(out/'checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[k for k,v in checks.items() if not v])
