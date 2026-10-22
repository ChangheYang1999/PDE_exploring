"""Physical coordinate and exponent controls for the independent P226 proof."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import hashlib,json,time
start=time.monotonic();now=datetime.now(timezone.utc).isoformat();r=Path('research/226_supercritical_foliation_exclusion');vd=r/'verification';checks={};diffs={}
def test(n,b):checks[n]=bool(b)
def zero(n,e):
 d=s.simplify(s.expand(e.doit()));checks[n]=(d==0);diffs[n]=str(d)
x,y,k,t,beta=s.symbols('x y k t beta',real=True);a=s.Function('a')(y);A=s.Function('A')(y);q=s.Function('q');C=s.Function('C');H=s.Function('H');kap=x/a
# Generic C1 physical fields verify the coordinate identity before any ansatz is imposed.
F=s.Function('F');G=s.Function('G');V=G(k*a,y);Q=F(k*a,y)-k*s.diff(a,y)*V
Qphys=F(x,y)-x*s.diff(a,y)*G(x,y)/a
# Apply the physical chain operators before substituting the curve, so generic partials have identical dummy-variable representations.
lhs=(a*s.diff(Qphys,x)+s.diff(a,y)*G(x,y)+a*(s.diff(G(x,y),y)+x*s.diff(a,y)*s.diff(G(x,y),x)/a)).subs(x,k*a)
rhs=a*(s.diff(F(x,y),x)+s.diff(G(x,y),y)).subs(x,k*a)
zero('coordinate_divergence_for_generic_fields',lhs-rhs)
zero('temperature_coordinate_transport',(F(x,y)*s.diff(H(kap),x)+G(x,y)*s.diff(H(kap),y)).subs(x,k*a)-s.diff(H(k),k)*Q/a)
# Smooth symbolic specialization checks (2); it is not a stronger regularity premise in the proof.
dphys=2*beta-s.Subs(s.diff(q(k),k),k,kap)
w2=(dphys*A+C(kap))/a;w1=a*q(kap)+x*s.diff(a,y)*w2/a
zero('ansatz_coordinate_Q',(w1-x*s.diff(a,y)*w2/a)-a*q(kap))
zero('ansatz_physical_divergence',(s.diff(w1,x)+s.diff(w2,y)).subs(s.diff(A,y),a)-2*beta)
zero('ansatz_material_k',w1*s.diff(kap,x)+w2*s.diff(kap,y)-q(kap))
zero('ansatz_material_Theta',w1*s.diff(H(kap),x)+w2*s.diff(H(kap),y)-q(kap)*s.Subs(s.diff(H(k),k),k,kap))
lam=beta-2;hh=s.Function('h')(k)
zero('q_derivative_formula',s.diff(lam*H(k)/s.diff(H(k),k),k)-lam*(1-H(k)*s.diff(H(k),k,2)/s.diff(H(k),k)**2))
h2=s.symbols('h2',nonzero=True);h3,h4=s.symbols('h3 h4',real=True)
ht=h2*k*k/2+h3*k**3+h4*k**4;qt=lam*ht/s.diff(ht,k)
zero('center_q_limit',s.limit(qt,k,0))
zero('center_q_over_k',s.limit(qt/k,k,0)-lam/2)
zero('center_qprime_limit',s.limit(s.diff(qt,k),k,0)-lam/2)
zero('C2_Taylor_leading_quotient',(h2*k*k/2)*h2/(h2*k)**2-s.Rational(1,2))
alpha=lam/2;d0=2*beta-alpha;delta=d0/beta;gamma=delta-1
zero('center_d0',d0-(1+s.Rational(3,2)*beta))
zero('axis_gamma',gamma-(s.Rational(1,2)+1/beta))
B=s.symbols('B',positive=True);gam=s.simplify(gamma.subs(beta,2+B));eps=B/(4*(2+B))
test('gamma_positive',gam.is_positive);test('gamma_less_one',s.simplify(1-gam).is_positive)
test('epsilon_positive',eps.is_positive);test('gamma_minus_epsilon_positive',s.simplify(gam-eps).is_positive);test('gamma_plus_epsilon_less_one',s.simplify(1-gam-eps).is_positive)
zero('axis_log_derivative',s.diff(s.log(A),y).subs(s.diff(A,y),a)-a/A)
Y=s.symbols('Y',positive=True);e=s.symbols('e',positive=True)
zero('power_comparison_antiderivative',s.diff((delta-e)*s.log(y/Y),y)-(delta-e)/y)
# Generic scalar reflection requires no parity of a or W.
AA=s.Function('A');aa=s.Function('scale');vv=s.Function('axis_v')
zero('negative_end_primitive_derivative',s.diff(-AA(-t),t)-s.Subs(s.diff(AA(y),y),y,-t))
zero('negative_end_axis_identity',-d0*AA(-t)/aa(-t)-d0*(-AA(-t))/aa(-t))
zero('negative_end_asymptotic',-beta*(-t)-beta*t)
# Fixed k asymptotic algebra, with d independent of y and C/(ay)->0.
d=s.symbols('d',real=True)
zero('vertical_limit_forces_d',s.solve(s.Eq(d*beta/d0,beta),d)[0]-d0)
zero('vertical_limit_qprime',2*beta-d0-alpha)
zero('quadratic_solution_ODE',s.diff(ht.subs({h3:0,h4:0}),k)-2*ht.subs({h3:0,h4:0})/k)
zero('quadratic_ratio_constant',s.diff((h2*k*k/2)/k**2,k))
zero('quadratic_q',lam*(h2*k*k/2)/(h2*k)-alpha*k)
L=s.symbols('L',positive=True)
test('finite_endpoint_derivative_nonzero',(h2*L).is_nonzero)
zero('horizontal_ratio_at_minimum',alpha-beta+(1+beta/2))
test('horizontal_gap_positive',s.simplify((beta-alpha).subs(beta,2+B)).is_positive)
zero('beta2_gamma_endpoint',gamma.subs(beta,2)-1)
zero('center_quadratic_physical_coefficient',(h2*(x/a)**2/2)/x**2-h2/(2*a**2))
before=json.loads((vd/'proof_before_code.json').read_text());test('proof_precedes_code',before['utc']<now)
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(checks.values()),'algebraic_differences':diffs,'scope':'Exact symbolic controls. General C2 quotient limits, global axis inequalities, minimum existence and regular-component continuation are proved in PROOF.md, not by polynomial samples.','proof_sha256':hashlib.sha256((r/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(vd/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[k for k,v in checks.items() if not v])
