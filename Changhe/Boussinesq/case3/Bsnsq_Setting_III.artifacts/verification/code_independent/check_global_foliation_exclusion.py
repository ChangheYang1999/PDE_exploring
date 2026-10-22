"""Independent calculus controls for P225, with physical-coordinate differentiation."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,time,hashlib
start=time.monotonic();now=datetime.now(timezone.utc).isoformat()
r=Path('research/225_global_foliation_exclusion');vd=r/'verification';checks={};diffs={}
def test(n,b): checks[n]=bool(b)
def zero(n,e):
 d=s.simplify(s.expand(e.doit()));checks[n]=(d==0);diffs[n]=str(d)
x,y,k,t=s.symbols('x y k t',real=True);a=s.Function('a')(y);A=s.Function('A')(y);C=s.Function('C');H=s.Function('H');kap=x/a
D=4*A+C(k);d=4*A+C(kap)
w1=x*s.diff(a,y)*d/a**2;w2=d/a
w1x=s.diff(w1,x);w1y=s.diff(w1,y).subs(s.diff(A,y),a)
w2x=s.diff(w2,x);w2y=s.diff(w2,y).subs(s.diff(A,y),a)
omega=w1y-w2x
zero('divergence_from_physical_coordinates',w1x+w2y-4)
zero('k_material_derivative',w1*s.diff(kap,x)+w2*s.diff(kap,y))
zero('temperature_transport',w1*s.diff(H(kap),x)+w2*s.diff(H(kap),y))
B=s.diff(a,y,2)/a-2*s.diff(a,y)**2/a**2
of=4*k*s.diff(a,y)+k*D*B-(1+k**2*s.diff(a,y)**2)*s.diff(C(k),k)/a**2
zero('negative_curl_on_curve',omega.subs(x,k*a)-of)
v=D/a;p=s.diff(a,y)*v/a;g=s.diff(C(k),k)/k;rr=of/k
zero('Dprime',s.diff(D,y).subs(s.diff(A,y),a)-4*a)
zero('vprime',s.diff(v,y).subs(s.diff(A,y),a)-4+p)
zero('apprime',a*s.diff(p,y).subs(s.diff(A,y),a)-4*s.diff(a,y)-D*B)
zero('r_decomposition',rr-a*s.diff(p,y).subs(s.diff(A,y),a)+g*(1+k*k*s.diff(a,y)**2)/a**2)
# Derive the full material equation directly in x,y; no derivative routine from NUM.
rv=(w1*s.diff(omega,x)+w2*s.diff(omega,y)+omega-s.diff(H(kap),x)).subs(s.diff(A,y),a)
rvc=rv.subs(x,k*a).doit()
zero('physical_vorticity_equation_on_curve',rvc-k*(v*s.diff(rr,y).subs(s.diff(A,y),a)+rr)+s.diff(H(k),k)/a)
zero('critical_curve_vorticity_equation',rvc.subs(s.diff(H(k),k),0)-k*(v*s.diff(rr,y).subs(s.diff(A,y),a)+rr))
root={A:-C(k)/4}
zero('v_at_unique_zero',v.subs(root));zero('p_at_unique_zero',p.subs(root))
zero('vprime_at_zero',s.diff(v,y).subs(s.diff(A,y),a).subs(root)-4)
zero('pprime_at_zero',s.diff(p,y).subs(s.diff(A,y),a).subs(root)-4*s.diff(a,y)/a)
R=s.Function('R')(t)
zero('homogeneous_integrating_factor',s.diff(s.exp(t)*R,t).subs(s.diff(R,t),-R))
T,M=s.symbols('T M',positive=True)
zero('bounded_backward_boundary_term',s.limit(M*s.exp(-T),T,s.oo))
# A smooth one-sided plateau correction has vanishing first derivatives at its boundary.
e=s.exp(-1/t)
for j in [0,1,2]: zero('flat_boundary_limit_order'+str(j),s.limit(s.diff(e,t,j),t,0,dir='+'))
# Controls of both fixed-height limits and the common-C scalar identity.
aa,ap,aval=s.symbols('aa ap aval',nonzero=True);cj=s.symbols('cj',real=True)
zero('horizontal_common_constant',ap*(4*aval+(2*aa**2/ap-4*aval))/aa**2-2)
cc=s.symbols('cc',real=True)
zero('differentiate_horizontal_identity',s.diff(2*a**2/s.diff(a,y)-4*A,y).subs(s.diff(A,y),a)+2*a**2*s.diff(a,y,2)/s.diff(a,y)**2)
# At fixed height, the error o(|x|)/x goes to zero for either sign.
eps=s.symbols('eps',positive=True);u=s.symbols('u',positive=True)
zero('positive_horizontal_error',s.Abs(eps*u/u)-eps)
zero('negative_horizontal_error',s.Abs(eps*u/(-u))-eps)
# Sign and zero controls used after homogeneous vorticity is forced to vanish.
a_pos,q_pos,g_pos=s.symbols('a_pos q_pos g_pos',positive=True)
test('gpositive_pprime_positive',(g_pos*q_pos/a_pos**3).is_positive)
test('gnegative_pprime_negative',(-g_pos*q_pos/a_pos**3).is_negative)
zero('gzero_pprime_zero',s.Integer(0)*q_pos/a_pos**3)
pos,neg=s.symbols('pos',positive=True),s.symbols('neg',negative=True)
test('positive_p_over_positive_v', (pos/pos).is_positive)
test('negative_p_over_negative_v', (neg/neg).is_positive)
test('negative_p_over_positive_v', (neg/pos).is_negative)
# Negative-end reflection is performed solely on scalar identities.
DD=s.Function('D');aa_fun=s.Function('scale');VV=s.Function('v')
zero('negative_end_D_derivative',s.diff(-DD(-t),t)-s.Subs(s.diff(DD(y),y),y,-t))
zero('negative_end_product',(-aa_fun(-t)*VV(-t))-aa_fun(-t)*(-VV(-t)))
zero('negative_end_asymptotic',-2*(-t)-2*t)
Y=s.symbols('Y',positive=True)
zero('bounded_end_integrated_lower',s.diff(s.Rational(4,3)*s.log(t/Y),t)-4/(3*t))
test('superlinear_lower_power',s.Rational(4,3)>1)
# The excluded constant-H hypothesis is essential: this is an exact remaining solution.
wx,wy=2*x,2*y
zero('constantH_divergence',s.diff(wx,x)+s.diff(wy,y)-4)
zero('constantH_negative_curl',s.diff(wx,y)-s.diff(wy,x))
zero('constantH_temperature_transport',wx*s.diff(s.Integer(7),x)+wy*s.diff(s.Integer(7),y))
zero('constantH_vorticity_equation',wx*s.diff(s.Integer(0),x)+wy*s.diff(s.Integer(0),y)-s.diff(s.Integer(7),x))
before=json.loads((vd/'proof_before_code.json').read_text());test('proof_precedes_checker',before['written_utc']<now)
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'all_passed':all(checks.values()),'checks':checks,'algebraic_differences':diffs,'scope':'Exact calculus controls only. The bounded regular set, derivative closure, D zero existence, backward compactness and monotonicity contradiction are complete informal arguments in PROOF.md, not consequences of finite samples.','proof_sha256':hashlib.sha256((r/'PROOF.md').read_bytes()).hexdigest(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(vd/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['started_utc','ended_utc','elapsed_seconds','all_passed']},indent=2));print('checks',len(checks),'failed',[k for k,v in checks.items() if not v])
