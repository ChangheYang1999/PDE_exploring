"""Independent exact/finite-time controls for P206; imports no teammate code.
The manufactured fields test geometry. They do not solve the coupled PDE.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, time
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp
import mpmath as mp

ROOT=Path(__file__).resolve().parents[1]
V=ROOT/'research/206_accumulating_endpoint_phase/verification'
started=datetime.now(timezone.utc).isoformat(); tick=time.monotonic()
s,z,u,v,a,q=sp.symbols('s z u v a q', real=True)
g=sp.Function('g'); gp=sp.diff(g(s),s)
W=sp.Matrix([g(s),(4-gp)*z])
omega=-(sp.diff(W[1],s)-sp.diff(W[0],z))
res=sp.expand(W[0]*sp.diff(omega,s)+W[1]*sp.diff(omega,z)+omega)
res_expected=z*(g(s)*sp.diff(g(s),s,3)+(5-gp)*sp.diff(g(s),s,2))
checks={}; values={}
def zero(name,x):
 y=sp.simplify(x); checks[name]=(y==0); values[name]=str(y)
zero('physical_divergence',sp.diff(W[0],s)+sp.diff(W[1],z)-4)
zero('physical_vorticity_sign',omega-z*sp.diff(g(s),s,2))
zero('physical_vorticity_residual',res-res_expected)
xi=u*sp.exp(-a*v)
A=sp.exp(a*v)*g(xi)+a*u*v*(4-sp.Subs(gp,s,xi))
B=v*(4-sp.Subs(gp,s,xi))
zero('coordinate_divergence',sp.diff(A,u)+sp.diff(B,v)-4-a*v*(4-sp.Subs(gp,s,xi)))
# The polynomial provides an exact root without imposing symbolic Function substitutions.
poly=s**2*(q-s)
Ap=sp.exp(a*v)*poly.subs(s,xi)+a*u*v*(4-sp.diff(poly,s).subs(s,xi))
Bp=v*(4-sp.diff(poly,s).subs(s,xi))
J=sp.Matrix([Ap,Bp]).jacobian([u,v]).subs({u:q,v:0})
lam=-q**2; nu=4+q**2
zero('equilibrium_trace',sp.trace(J)-4)
zero('equilibrium_characteristic_polynomial',(J-lam*sp.eye(2)).det())
zero('fast_eigenvector_component_u',(J*sp.Matrix([a*q,1])-nu*sp.Matrix([a*q,1]))[0])
zero('fast_eigenvector_component_v',(J*sp.Matrix([a*q,1])-nu*sp.Matrix([a*q,1]))[1])
sigma=q*sp.exp(a*v)
zero('barrier_tangency',Ap.subs(u,sigma)-sp.diff(sigma,v)*Bp.subs(u,sigma))
zero('origin_graph_invariance',Ap.subs(u,0))
polyres=sp.expand(z*(poly*sp.diff(poly,s,3)+(5-sp.diff(poly,s))*sp.diff(poly,s,2)))
exact_res=sp.simplify(polyres.subs({q:sp.Rational(1,4),s:sp.Rational(1,8),z:sp.Rational(1,10)}))
checks['polynomial_is_not_PDE_solution']=(exact_res==-sp.Rational(161,1280))
values['polynomial_residual_at_q1_4_s1_8_z1_10']=str(exact_res)
values['coordinate_divergence_defect']=str(sp.factor(sp.diff(Ap,u)+sp.diff(Bp,v)-4))
checks['coordinate_divergence_is_not_constant4']=not sp.simplify(sp.diff(Ap,u)+sp.diff(Bp,v)-4)==0
osc=sp.exp(-1/s**2)*sp.sin(1/s)
oscprime=sp.simplify(sp.diff(osc,s).subs(s,1/sp.pi))
oscdouble=sp.simplify(sp.diff(osc,s,2).subs(s,1/sp.pi))
zero('accumulating_first_root_derivative',oscprime-sp.pi**2*sp.exp(-sp.pi**2))
zero('accumulating_first_root_second_derivative',oscdouble-sp.exp(-sp.pi**2)*(4*sp.pi**5-2*sp.pi**3))
mp.mp.dps=70
oscres=sp.Rational(1,10)*(5-oscprime)*oscdouble
values['accumulating_first_root_residual_z1_10']=str(sp.N(oscres,55))
checks['accumulating_kinematic_field_is_not_PDE_solution']=float(oscres)>0
values['first_four_roots_and_fast_eigenvalues']=[]
for n in range(1,5):
 k=n*mp.pi; d=-mp.exp(-k*k)*k*k*((-1)**n)
 values['first_four_roots_and_fast_eigenvalues'].append({'n':n,'q':str(1/k),'lambda':str(d),'nu':str(4-d)})
checks['accumulating_fast_gap_samples']=all(abs(mp.mpf(r['lambda']))<1 for r in values['first_four_roots_and_fast_eigenvalues'])
# Independent finite-time chart integration, explicitly no infinite-time certificate.
a0=1/3; q0=1/4; rho=1/10; nu0=4+q0*q0
Afn=sp.lambdify((u,v),Ap.subs({a:a0,q:q0}),'numpy')
Bfn=sp.lambdify((u,v),Bp.subs({a:a0,q:q0}),'numpy')
def rev(t,y):return [-float(Afn(*y)),-float(Bfn(*y))]
controls=[]
for tol in [1e-8,1e-10,1e-12]:
 for s0 in [0.0,.125,q0]:
  for z0 in [-.08,.08]:
   y0=[s0*np.exp(a0*z0),z0]
   ans=solve_ivp(rev,[0,6],y0,method='DOP853',rtol=tol,atol=tol*.001,dense_output=True)
   ts=np.linspace(0,6,121); ys=ans.sol(ts); ss=ys[0]*np.exp(-a0*ys[1]); bound=q0*np.exp(a0*ys[1])
   row={'rtol':tol,'s0':s0,'z0':z0,'success':bool(ans.success),'nfev':ans.nfev,'s_min':float(ss.min()),'s_max':float(ss.max()),'u_min':float(ys[0].min()),'right_edge_overshoot':float(np.max(ys[0]-bound)),'abs_v_max':float(np.max(abs(ys[1]))),'last_s':float(ss[-1])}
   if s0==q0:
    exactv=z0*np.exp(-nu0*ts);exactu=q0*np.exp(a0*exactv)
    row['exact_fast_curve_max_abs_error']=float(np.max(np.abs(ys-np.vstack([exactu,exactv]))))
   controls.append(row)
checks['finite_trajectory_controls_succeed']=all(r['success'] for r in controls)
checks['finite_trajectory_box_checks']=all(r['s_min']>=-1e-11 and r['s_max']<=q0+1e-11 and r['abs_v_max']<=rho for r in controls)
checks['finite_fast_curve_refinement']=max(r.get('exact_fast_curve_max_abs_error',0) for r in controls if r['rtol']==1e-12)<1e-11
values['finite_trajectory_controls']=controls
# Verify all replacement anchors independently in the frozen report; no report mutation.
candidate=V/'frozen_sources/05_enter_xx_text_v1.md'; base=V/'frozen_sources/03_analysis_FINAL_REPORT.md'
text=candidate.read_text(); basetext=' '.join(base.read_text().split()); anchors=[]
for match in re.finditer(r'^## (E[0-9]+b?)\.[^\n]*\n(.*?)(?=^## |\Z)',text,re.M|re.S):
 label,body=match.groups()
 if label=='E8':continue
 quoted=re.findall(r'"([^"]*)"',body,re.S)
 if len(quoted)!=2:raise ValueError((label,len(quoted)))
 old,new=[' '.join(x.split()) for x in quoted]
 anchors.append({'label':label,'old_matches':basetext.count(old),'old':old,'new':new})
checks['candidate_all_twelve_replacement_anchors_unique']=len(anchors)==12 and all(r['old_matches']==1 for r in anchors)
checks['candidate_insertion_anchor_unique']=basetext.count('filling the closed half circle on the side of gamma (4.7(xix)).')==1
values['candidate_anchor_checks']=anchors
for n in [1,2,3]:checks[f'candidate_Z{n}_present']=f'## Z{n}.' in text
inputs=[Path(__file__).resolve(),ROOT/'research/206_accumulating_endpoint_phase/PROOF.md',candidate,base]
result={'started_utc':started,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-tick,'purpose':'Independent exact geometry and negative PDE controls, finite-time ODE refinement, candidate-anchor audit. None certifies a B2 solution or infinite-time numerical behavior.','inputs':[{'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputs],'checks':checks,'values':values}
(V/'endpoint_controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':result['elapsed_seconds'],'passed':sum(checks.values()),'total':len(checks),'failed':[k for k,v in checks.items() if not v],'polynomial_residual':str(exact_res),'oscillatory_residual':values['accumulating_first_root_residual_z1_10']},indent=2))
if not all(checks.values()):raise SystemExit(1)
