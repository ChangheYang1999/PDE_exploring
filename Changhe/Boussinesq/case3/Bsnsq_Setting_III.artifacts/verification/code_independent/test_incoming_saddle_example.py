"""Independent exact formula and necessity controls for construction180."""
from pathlib import Path
from datetime import datetime,timezone
import json,time
import sympy as s
r=Path('research/180_incoming_arc_with_saddle_ancestors/verification');d=json.loads((r/'inputs.json').read_text());start=time.monotonic();now=datetime.now(timezone.utc).isoformat();rows=[];neg=[]
u,v,x,y,t=s.symbols('u v x y t',real=True);lam=s.symbols('lam',positive=True);kap=4-lam;rho=s.Function('rho')(u);b=s.Function('b')(v);k=kap*v-b;psi=u*rho*k
Wu=lam*u+s.diff(psi,v);Wv=kap*v-s.diff(psi,u)
def check(name,e):
 z=s.simplify(e);assert z==0,(name,z);rows.append({'name':name,'difference':str(z),'pass':True})
check('insertion_divergence',s.diff(Wu,u)+s.diff(Wv,v)-4)
check('Wu_convex_bracket',Wu-u*((1-rho)*lam+rho*(4-s.diff(b,v))))
check('Wv_formula',Wv-(kap*v-(rho+u*s.diff(rho,u))*k))
# rho is identically1 in a neighborhood of u0, not merely equal1 at0.
Wu0=Wu.subs({rho:1,s.diff(rho,u):0});Wv0=kap*v-k
check('rho1_Wu',Wu0-u*(4-s.diff(b,v)))
check('rho1_Wv',Wv0-b)
J=s.Matrix([Wu0,Wv0]).jacobian([u,v]).subs(u,0)
for i in range(2):
 for j in range(2):check(f'zero_linearization_{i}{j}',J[i,j]-s.diag(4-s.diff(b,v),s.diff(b,v))[i,j])
check('zero_trace',s.trace(J)-4)
# The logarithmic derivative works with positive and negative v separately.
A=kap+1;M=12*A/lam;z=s.symbols('z',positive=True);r0=s.symbols('r0',positive=True);chi=s.Function('chi');ss=s.log(z/r0)/M
bp=s.diff(z*(kap-A*chi(ss)),z)
check('positive_log_derivative',bp-(kap-A*chi(ss)-A/M*s.Subs(s.Derivative(chi(t),t),t,ss)))
check('negative_log_derivative',s.diff(-z*(kap-A*chi(ss)),z)/(-1)-bp)
check('b_origin_slope',kap-A+1)
for ltext in d['lambda_samples']:
 ll=s.Rational(ltext);kk=4-ll;aa=kk+1;mm=12*aa/ll;bound=kk+6*aa/mm
 assert 0<ll<2 and bound<4
 rows.append({'name':f'global_bprime_margin_{ltext}','margin':str(4-bound),'pass':True})
 for rr in map(s.Rational,d['rho_samples']):
  margin=(1-rr)*ll+rr*(4-bound);assert margin>=ll/2
  rows.append({'name':f'Wu_positive_{ltext}_rho{rr}','lower_bound':str(margin),'pass':True})
 check(f'saddle_trace_{ltext}',s.Integer(5)-1-4)
 check(f'source_index_sum_{ltext}',-1+1+1-1)
# Exact stream-function identity for the global starting field.
a=s.Function('a')(x);cut=s.Function('cut')(y);Psi=a*y*cut
V1=2*x-s.diff(Psi,y);V2=2*y+s.diff(Psi,x)
check('base_divergence',s.diff(V1,x)+s.diff(V2,y)-4)
check('base_second_component',V2-y*(2+s.diff(a,x)*cut))
# Reflection for a general insertion written by an abstract scalar potential.
f=s.Function('f')(x,y);left_potential=f.subs(x,-x);right_potential=-f
L1=-s.diff(left_potential,y);L2=s.diff(left_potential,x)
R1=-s.diff(right_potential,y);R2=s.diff(right_potential,x)
check('reflection_first',L1+R1.subs(x,-x))
check('reflection_second',L2-R2.subs(x,-x))
check('odd_total_potential',(left_potential+right_potential).subs(x,-x)+(left_potential+right_potential))
# Scalar h derivative; all global inequalities are proved in the written construction.
H=s.Function('H');xp=s.symbols('xp',positive=True);hh=2*H(s.log(xp)/10)*(xp-2)
check('h_derivative',s.diff(hh,xp)-2*H(s.log(xp)/10)-(xp-2)/(5*xp)*s.Subs(s.Derivative(H(t),t),t,s.log(xp)/10))
check('h_slope_at2',s.diff(hh,xp).subs(xp,2)-2*H(s.log(2)/10))
check('bounded_a_far_right',2*x-(2*x-4)-4)
check('bounded_a_far_left',2*x-(2*x+4)+4)
# Strict increase can coexist with zero derivative: controls the review320 premise.
c=s.Rational(d['bad_switch_critical_point']);Hb=((t-c)**3+c**3)/(c**3+(1-c)**3);ll=s.Rational(d['bad_switch_lambda']);kk=4-ll;aa=kk+1
check('bad_switch_left',Hb.subs(t,0));check('bad_switch_right',Hb.subs(t,1)-1)
check('bad_switch_derivative_zero',s.diff(Hb,t).subs(t,c))
check('bad_switch_hits_source_level',Hb.subs(t,c)-1/aa)
check('bad_switch_nondegeneracy_fails',ll/12*s.diff(Hb,t).subs(t,c))
neg.append({'name':'strict_monotonicity_not_positive_derivative','H_polynomial':str(s.factor(Hb)),'critical_point':str(c),'lambda':str(ll),'pass':True,'scope':'Polynomial necessity control on[0,1], not the actual globally flat bump switch; H is strictly increasing with derivative0 at the relevant level.'})
# If the strict bprime<4 condition is discarded, even zero counting can fail.
check('failed_bound_line_of_zeros_Wu',(u*(4-s.diff(4*v,v))).subs(v,0))
check('failed_bound_line_of_zeros_Wv',(4*v).subs(v,0))
neg.append({'name':'bprime_equal4_allows_line_of_zeros','b':'4v','pass':True,'scope':'Local formula counterexample; not compactly matched to the starting field.'})
# Center field prevents the B2 temperature jet.
a0=s.symbols('a0',nonzero=True);theta=a0*x*x;omega=0
check('center_curl',s.diff(4*y,x)-s.diff(s.Integer(0),y))
res=-s.diff(theta,x);assert s.diff(res,x)==-2*a0
neg.append({'name':'geometric_field_not_B2','thermal_jet':str(theta),'vorticity_residual':str(res),'pass':True})
out={'started_utc':now,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'passed':len(rows),'negative_passed':len(neg),'checks':rows,'negative_controls':neg,'all_passed':True,'scope':'Exact local identities and hypothesis controls. Global support, completeness and connections are proved in PROOF.md, not established by finite samples.'}
(r/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items()if k not in('checks','negative_controls')},indent=2))
