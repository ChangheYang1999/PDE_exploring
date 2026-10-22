"""Independent physical and characteristic identities for P224."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import sympy as s
start=time.monotonic();now=datetime.now(timezone.utc).isoformat();r=Path('research/224_foliation_constant_sign');vdir=r/'verification';checks={};diffs={}
def test(n,b):checks[n]=bool(b)
def zero(n,e):
 d=s.simplify(s.expand(e.doit()));checks[n]=(d==0);diffs[n]=str(d)
x,y,k,t=s.symbols('x y k t',real=True);a=s.Function('a')(y);A=s.Function('A')(y);C=s.Function('C');H=s.Function('H');kap=x/a;Dphys=4*A+C(kap)
w1=x*s.diff(a,y)*Dphys/a**2;w2=Dphys/a
# Differentiate in physical coordinates before evaluating on the curve.
zero('physical_divergence',s.diff(w1,x)+s.diff(w2,y).subs(s.diff(A,y),a)-4)
zero('physical_k_transport',w1*s.diff(kap,x)+w2*s.diff(kap,y))
zero('physical_temperature_transport',w1*s.diff(H(kap),x)+w2*s.diff(H(kap),y))
omega=(s.diff(w1,y)-s.diff(w2,x)).subs(s.diff(A,y),a)
B=s.diff(a,y,2)/a-2*s.diff(a,y)**2/a**2
D=4*A+C(k);formula=4*k*s.diff(a,y)+k*D*B-(1+k*k*s.diff(a,y)**2)*s.diff(C(k),k)/a**2
zero('negative_curl_formula',omega.subs(x,k*a)-formula)
vel=D/a;p=s.diff(a,y)*vel/a
zero('vprime',s.diff(vel,y).subs(s.diff(A,y),a)-4+p)
zero('apprime',a*s.diff(p,y).subs(s.diff(A,y),a)-4*s.diff(a,y)-D*B)
g=s.diff(C(k),k)/k
zero('r_decomposition',formula/k-a*s.diff(p,y).subs(s.diff(A,y),a)+g*(1+k*k*s.diff(a,y)**2)/a**2)
# Fixed k physical characteristic derivative for a completely generic scalar.
R=s.Function('R');scalar=R(kap,y)
zero('generic_material_derivative',(w1*s.diff(scalar,x)+w2*s.diff(scalar,y)).subs(x,k*a)-vel*s.diff(R(k,y),y))
zero('temperature_source_on_curve',s.diff(H(kap),x).subs(x,k*a)/k-s.diff(H(k),k)/(k*a))
# At D=0, substitute A=-C(k)/4 after differentiating.
rootrule={A:-C(k)/4}
zero('v_root',vel.subs(rootrule));zero('p_root',p.subs(rootrule))
zero('vprime_root',s.diff(vel,y).subs(s.diff(A,y),a).subs(rootrule)-4)
zero('pprime_root',s.diff(p,y).subs(s.diff(A,y),a).subs(rootrule)-4*s.diff(a,y)/a)
rr=s.Function('r')(t);aa=s.Function('along_a')(t);h=s.symbols('h',nonzero=True)
zero('integrating_factor',(s.diff(s.exp(t)*rr,t)).subs(s.diff(rr,t),h/aa-rr)-s.exp(t)*h/aa)
T=s.symbols('T',positive=True);M=s.symbols('M',positive=True)
zero('bounded_boundary_term',s.limit(M*s.exp(-T),T,s.oo))
zero('constant_equilibrium_integral',s.integrate(s.exp(t),(t,-s.oo,0))-1)
ymin,ymax=s.symbols('ymin ymax',positive=True)
zero('D_integral_identity',s.diff(D,y).subs(s.diff(A,y),a)-4*a)
Y=s.symbols('Y',positive=True)
zero('bounded_end_comparison',s.diff(s.Rational(4,3)*s.log(y/Y),y)-4/(3*y))
test('comparison_power_gt1',s.Rational(4,3)>1)
# The sign product is the un-divided product over a positive square.
cp,hp=s.symbols('cp hp',real=True)
zero('sign_product_equivalence',(hp/k)*(cp/k)-hp*cp/k**2)
apos,rpos,qpos,hpos=s.symbols('apos rpos qpos hpos',positive=True);gpos=s.symbols('gpos',nonnegative=True)
test('strict_positive_sign_even_gzero',(rpos/apos+gpos*qpos/apos**3).is_positive)
test('strict_negative_sign_even_gzero',(-rpos/apos-gpos*qpos/apos**3).is_negative)
zero('basepoint_derivative_invariant',s.diff(C(k)+s.Symbol('constant'),k)-s.diff(C(k),k))
prior=json.loads(Path('research/223_polynomial_foliation_constant/verification/checks.json').read_text());test('polynomial_prior33pass',prior['all_passed'] and len(prior['checks'])==33)
before=json.loads((vdir/'proof_before_code.json').read_text());test('proof_precedes_code',before['utc']<now);test('proof_hash',hashlib.sha256((r/'PROOF.md').read_bytes()).hexdigest()==before['sha256'])
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':checks,'all_passed':all(checks.values()),'algebraic_differences':diffs,'scope':'Symbolic controls of identities. Global zero existence, backward compactness, strict positivity of the integral and nonexistence contradiction are proved in PROOF.md, not by sampling.','code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(vdir/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('controls',len(checks),'failed',[n for n,b in checks.items() if not b])
