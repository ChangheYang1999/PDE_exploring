"""Independent exact controls for177, written after its complete proof draft."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time
import sympy as s
root=Path('research/177_incoming_endpoint_isothermal_side/verification')
start=time.monotonic();now=datetime.now(timezone.utc).isoformat();data=json.loads((root/'inputs.json').read_text());rows=[];negative=[]
def check(name,v):
 ok=bool(s.simplify(v)==0);rows.append({'name':name,'difference':str(s.simplify(v)),'pass':ok});assert ok,(name,v)
def predicate(name,v,detail=''):
 ok=bool(v);rows.append({'name':name,'detail':detail,'pass':ok});assert ok,(name,detail)
x,y,t,L=s.symbols('x y t L',real=True)
for n in data['harmonic_degrees']:
 for amplitude in data['harmonic_amplitudes']:
  # Construct Re(z^n) from integer binomial coefficients, not complex expansion.
  P=sum((-1)**j*s.binomial(n,2*j)*x**(n-2*j)*y**(2*j) for j in range(n//2+1))
  H=2*y*y+amplitude*P;W=s.Matrix([s.diff(H,x),s.diff(H,y)]);Om=-(s.diff(W[1],x)-s.diff(W[0],y));Theta=L
  tag=f'harmonic_degree{n}_amplitude{amplitude}'
  check(tag+'_divergence',s.diff(W[0],x)+s.diff(W[1],y)-4)
  check(tag+'_vorticity',Om)
  check(tag+'_thermal',sum(W[j]*s.diff(Theta,[x,y][j]) for j in range(2)))
  check(tag+'_vorticity_transport',sum(W[j]*s.diff(Om,[x,y][j]) for j in range(2))+Om-s.diff(Theta,x))
  check(tag+'_center_line_invariant',W[1].subs(y,0))
  check(tag+'_center_drift',W[0].subs(y,0)-n*amplitude*x**(n-1))
  DW=W.jacobian([x,y]).subs({x:0,y:0});predicate(tag+'_spectrum',DW==s.diag(0,4))
  plus=amplitude;minus=amplitude*(-1)**(n-1);index=Q(plus-minus,2)
  expected=amplitude if n%2==0 else 0
  predicate(tag+'_index',index==expected,str(index))
# The inequality is checked by exact rationals including negative v and both B extremes.
for i,d in enumerate(data['normal_form_bounds']):
 M=Q(d['M']);k=Q(d['k']);D=Q(d['D']);assert k>M/2 and D>2
 for bv in [-M,Q(0),M]:
  for vv in map(Q,data['v_values']):
   expr=-vv*bv-k*D*abs(vv)
   predicate(f'weighted_backward_bound_{i}_{bv}_{vv}',expr<=(M-2*k)*abs(vv)<=0,str(expr))
# Direct differentiation of the integrating factor for either incoming/outgoing drift.
u=s.Function('u')(t);v=s.Function('v')(t);B=s.Function('B')(t);I=s.Function('I')(t);g=s.Function('g');D=s.Function('D')(t)
for sign in [-1,1]:
 h=sign*u*s.exp(I)
 deriv=s.diff(h,t).subs({s.diff(u,t):-g(u)-u*v*B,s.diff(I,t):v*B})
 check(f'integrating_factor_sign_{sign}',deriv+sign*s.exp(I)*g(u))
# Local conservation identities with arbitrary time-dependent values.
z=s.Function('z')(t);force=s.Function('f')(t)
check('forward_vorticity_integrating_factor',s.diff(s.exp(t)*z,t).subs(s.diff(z,t),force-z)-s.exp(t)*force)
# Constant positive divergence gives area growth even with a stable direction.
for i,A in enumerate([s.diag(1,3),s.diag(-1,5),s.Matrix([[0,1],[0,4]]),s.Matrix([[2,-3],[3,2]])]):
 check(f'liouville_matrix_{i}',s.det(s.exp(A*t))-s.exp(4*t))
# Flat incoming scalar center drift, u'=-exp(-1/u^2) for u>0.
r=s.symbols('r',positive=True)
speed=s.exp(-1/r**2)
predicate('flat_speed_increasing',s.diff(speed,r).is_positive)
for txt in data['flat_start_values']:
 a=s.Rational(txt);upper=(1-a)*s.exp(1/a**2)
 predicate('flat_arrival_upper_finite_'+txt,upper.is_finite and upper.is_positive,str(upper))
# Negative control: divergence zero permits an exact homoclinic loop.
a=s.symbols('a',positive=True);X=2*s.sqrt(2)*a/(1+a*a);Y=2*s.sqrt(2)*a*(1-a*a)/(1+a*a)**2
check('homoclinic_parameter_x',a*s.diff(X,a)-Y)
check('homoclinic_parameter_y',a*s.diff(Y,a)-(X-X**3))
check('homoclinic_first_integral',Y**2/2-X**2/2+X**4/4)
check('homoclinic_alpha_x',s.limit(X,a,0));check('homoclinic_alpha_y',s.limit(Y,a,0));check('homoclinic_omega_x',s.limit(X,a,s.oo));check('homoclinic_omega_y',s.limit(Y,a,s.oo))
negative.append({'name':'positive_divergence_cannot_be_dropped','field':['y','x-x^3'],'divergence':0,'exact_homoclinic_checks_passed':True,'verdict':'The invariant-loop exclusion fails without positive divergence.'})
# Negative control: knowing only branch values of Theta is not open constant data.
thermal=x**5*y;W=s.Matrix([-x,5*y]);check('stable_branch_value_only_T',sum(W[j]*s.diff(thermal,[x,y][j]) for j in range(2)));check('stable_branch_value',thermal.subs(y,0))
residual=-s.diff(thermal,x);predicate('branch_value_not_open_constant',residual!=0)
negative.append({'name':'pointwise_branch_values_do_not_supply_open_data','Theta':'x^5*y','W':['-x','5*y'],'Omega':0,'thermal_equation':True,'vorticity_residual':str(residual),'verdict':'A transport-only nonexample; it fails the coupled vorticity equation and is not a B2 counterexample.'})
# Negative control: trace4 alone does not bound backward trajectories.
negative.append({'name':'asymptotic_hypothesis_needed','W':['-x','5*y'],'backward_orbit_from_1_0':['exp(T)','0'],'divergence':4,'verdict':'Backward orbit is unbounded; W=2X+o(|X|) fails.'})
result={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_checks':rows,'negative_controls':negative,'all_passed':all(q['pass'] for q in rows),'proof_status':'OPEN pending written model audits; finite controls are not the proof'}
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['exact_checks','negative_controls']},indent=2));print('exact_checks',len(rows),'negative_controls',len(negative))
