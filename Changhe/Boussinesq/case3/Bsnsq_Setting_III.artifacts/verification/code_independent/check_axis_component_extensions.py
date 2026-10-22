from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import hashlib,json,time
v=Path('research/237_axis_component_extensions/verification');tick=time.monotonic();start=datetime.now(timezone.utc).isoformat();checks={}
def ck(k,x):checks[k]=bool(x)
y=s.symbols('y',real=True);beta,A0=s.symbols('beta A0',positive=True);a=s.Function('a')(y);A=s.Function('A')(y);phi=s.Function('phi')(y);eta=s.Function('eta')(y)
L=1+3*beta/2;H=A0/a**2
axis=phi*s.diff(H,y)+(3*beta+2-2*s.diff(phi,y))*H
ck('axis_scale_identity',s.simplify(axis+2*H/a*(s.diff(a*phi,y)-L*a))==0)
ck('integrated_axis_identity',s.simplify(s.diff(a*(L*A/a),y).subs(s.diff(A,y),a)-L*a)==0)
r=a*eta
vort=phi*s.diff(eta,y)+(2*beta+1-s.diff(phi,y))*eta-A0/a**2
ck('positive_trace_transformation',s.simplify((phi*s.diff(r,y)+beta*r/2-A0/a-a*vort).subs(s.diff(phi,y),L-phi*s.diff(a,y)/a))==0)
for b in [s.Rational(2),s.Rational(12,5),s.Rational(3),s.Rational(20)]:ck('L_greater_beta_'+str(b),1+3*b/2>b)
# Explicit equation transform for v=a^(-n-1), no reliance on the lead's checker.
n,K=s.symbols('n K',real=True);p=s.diff(a,y)/a;vv=a**(-n-1)
aa=s.symbols('aa',positive=True);ap,app=s.symbols('ap app',real=True)
expr=s.diff(vv,y,2)+(n+1)*K*vv+(n+1)*vv*(s.diff(p,y)-(n+1)*p*p-K)
ck('linear_ODE_transform',s.simplify(expr.subs({s.diff(a,y,2):app,s.diff(a,y):ap,a:aa}))==0)
h=s.Function('h')(y);vv=(h/A0)**((n+1)/2)
ck('finite_endpoint_derivative',s.simplify(s.diff(vv,y)-(n+1)/2*(h/A0)**((n-1)/2)*s.diff(h,y)/A0)==0)
t=s.symbols('t',positive=True)
for degree in [2,4,8]:
 for order in [1,2,3,4]:
  vv=t**s.Rational(order*(degree+1),2)
  ck(f'finite_zero_limit_n{degree}_Horder{order}',s.limit(vv,t,0,dir='+')==0 and s.limit(s.diff(vv,t),t,0,dir='+')==0)
ck('n1_is_not_sufficient_for_double_zero',s.limit(s.diff(t,t),t,0,dir='+')!=0)
# Reflection sends both transport equations to the advertised signs.
x,z=s.symbols('x z');u1=s.Function('u1')(x,z);u2=s.Function('u2')(x,z);T=s.Function('T')(x,z);O=s.Function('O')(x,z)
R1=u1.subs(z,-y);R2=-u2.subs(z,-y);RT=-T.subs(z,-y);RO=-O.subs(z,-y)
oldT=u1*s.diff(T,x)+u2*s.diff(T,z)-(beta-2)*T
oldO=u1*s.diff(O,x)+u2*s.diff(O,z)+O-s.diff(T,x)
ck('reflection_temperature',s.simplify(R1*s.diff(RT,x)+R2*s.diff(RT,y)-(beta-2)*RT+oldT.subs(z,-y))==0)
ck('reflection_vorticity',s.simplify(R1*s.diff(RO,x)+R2*s.diff(RO,y)+RO-s.diff(RT,x)+oldO.subs(z,-y))==0)
ck('reflection_negative_curl',s.simplify(s.diff(R1,y)-s.diff(R2,x)+(s.diff(u1,z)-s.diff(u2,x)).subs(z,-y))==0)
# The strict exponent gaps persist when only one infinite end is used.
for b in [s.Rational(201,100),s.Rational(3),s.Rational(4),s.Rational(5),s.Rational(8),s.Rational(801,100)]:
 N=2*int(s.floor(3*b/(2*(b-2))));M=2*N+4
 ck('velocity_gap_'+str(b),all(j*(s.Rational(1,2)-1/b)-s.Rational(3,2)>0 for j in range(N+2,2*N+3,2)))
 ck('scalar_gap_'+str(b),all((s.Rational(ell,2)-1)*(1-2/b)>0 for ell in range(4,M+1,2)))
 ck('finite_degree_gap_'+str(b),M-1>2*N+1)
# Exact local arithmetic dependencies and source fidelity, without rerunning work already checked.
for number,topic,count in [(230,'finite_axis_jet_obstruction',81),(231,'critical_finite_axis_ratios',32)]:
 root=Path(f'research/{number}_{topic}');q=json.loads((root/'verification/checks.json').read_text())
 ck(f'P{number}_complete_exact_record',q['all_passed'] and len(q['checks'])==count)
 ck(f'P{number}_frozen_unchanged',(v/f'P{number}_PROOF.md').read_bytes()==(root/'PROOF.md').read_bytes())
proof=(v.parent/'PROOF.md').read_text();p231=(v/'P231_PROOF.md').read_text();append=p231[p231.index('Write E1=-F1,E3=-F3.'):p231.index('For every nonzero y, A has the sign of y')]
append=append.replace('## 5. Finite elimination forces','### Finite elimination forces').replace('## 6. Smooth uniqueness, without analyticity','### Smooth uniqueness, without analyticity')
ck('full_local_critical_calculation_included',append in proof)
ck('proof_precedes_new_controls',json.loads((v/'proof_before_controls.json').read_text())['written_utc']<start)
ck('finite_endpoint_hypothesis_explicit','because n>=2 and H' in proof)
ck('bounded_component_not_excluded','A bounded J supplies no infinite-end reduction' in proof)
ck('no_em_dash','\u2014' not in proof)
out={'started_utc':start,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'checks':checks,'all_passed':all(checks.values()),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'proof_sha256':hashlib.sha256((v.parent/'PROOF.md').read_bytes()).hexdigest(),'scope':'Exact identities and boundary-power controls; full informal argument supplies the theorem, no code from other lanes.'}
(v/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('CHECKS',len(checks),'PASS',sum(checks.values()),'FAILED',[k for k,b in checks.items() if not b],out['started_utc'],out['ended_utc'],out['elapsed_seconds'])
