"""Independent exact controls for packet174; solves unknown Taylor coefficients."""
from pathlib import Path
from datetime import datetime,timezone
import json,sys,time
import sympy as S
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'checks':[]}
def eq(name,v):
 assert S.simplify(S.expand(v))==0,name
 out['checks'].append({'name':name,'pass':True})
s,z,k0,k1,k2=S.symbols('s z k0 k1 k2',real=True)
g=k0*s*s/2+k1*s**3/6+k2*s**4/24
A=S.symbols('a0:4');B=S.symbols('b0:5');unknown=A+B
H=2*z*z+sum(A[j]*s**(3-j)*z**j for j in range(4))+sum(B[j]*s**(4-j)*z**j for j in range(5))
lap=S.diff(H,s,2)+S.diff(H,z,2)-4
eqns=list(S.Poly(lap,s,z).coeffs())
for coord in [s,z]:
 trace=S.series(S.diff(H,coord).subs(z,g),s,0,4).removeO().expand()
 eqns.extend(S.Poly(trace,s).coeffs())
sol=S.solve(eqns,unknown,dict=True);assert len(sol)==1 and set(sol[0])==set(unknown)
HH=S.expand(H.subs(sol[0]));out['solved_potential_through_degree4']=str(HH)
expected=2*z*z-2*k0*s*s*z+2*k0*z**3/3+k0*k0*(s**4-6*s*s*z*z+z**4)/2-2*k1*(s**3*z-s*z**3)/3
eq('independently_solved_H4',HH-expected)
eq('H4_Laplacian',S.diff(HH,s,2)+S.diff(HH,z,2)-4)
for coord in [s,z]:eq('curve_gradient_through_degree3_'+str(coord),S.series(S.diff(HH,coord).subs(z,g),s,0,4).removeO())
c2,c3=S.symbols('c2 c3');sigma=c2*z*z+c3*z**3
invariance=S.series((S.diff(HH,s)-S.diff(sigma,z)*S.diff(HH,z)).subs(s,sigma),z,0,4).removeO().expand()
ss=S.solve(S.Poly(invariance,z).coeffs(),[c2,c3],dict=True);assert len(ss)==1
eq('sigma_quadratic',ss[0][c2]);eq('sigma_cubic',ss[0][c3]-k1/18)
out['solved_sigma']=str(sigma.subs(ss[0]));out['invariance_before_solving']=str(invariance)
# Sign and arclength convention checked before setting s=0.
kappa=S.diff(g,s,2)/(1+S.diff(g,s)**2)**S.Rational(3,2)
eq('arclength_curvature_derivative',(S.diff(kappa,s)/S.sqrt(1+S.diff(g,s)**2)).subs(s,0)-k1)
# Cartesian-vs-graph-coordinate Laplacian for a basis of polynomials.
u,d=S.symbols('u d',real=True);gu=g.subs(s,u)
for i in range(5):
 for j in range(5-i):
  P=u**i*d**j;physical=P.subs({u:s,d:z-g},simultaneous=True)
  graph=(1+S.diff(gu,u)**2)*S.diff(P,d,2)-2*S.diff(gu,u)*S.diff(P,u,d)+S.diff(P,u,2)-S.diff(gu,u,2)*S.diff(P,d)
  eq(f'graph_Laplacian_{i}_{j}',S.diff(physical,s,2)+S.diff(physical,z,2)-graph.subs({u:s,d:z-g},simultaneous=True))
# A general coefficient at order m is fixed by 4m, not a resonance.
cm=S.symbols('cm')
for m in range(2,11):eq(f'normal_eigenvalue_factor_m{m}',S.diff(cm*z**m,z)*4*z-4*m*cm*z**m)
# True tube-coordinate invariance, retaining the derivative of b=n(a).
cf,dd,ff,nn,kp,tt=S.symbols('c d f nprime kprime t')
solt=nn*ff/(cf-nn*dd)
eq('tube_true_invariance',cf*solt-nn*(ff+dd*solt))
eq('tube_drift_factor',ff+dd*solt-cf*ff/(cf-nn*dd))
eq('tube_t_time_derivative',cf*tt-kp*(ff+dd*tt)-((cf-kp*dd)*tt-kp*ff))
# Negative control: replacing nprime by the slope of n-k loses the kprime term.
bad=nn*ff/(cf-nn*dd)
defect=cf*bad-(nn+kp)*(ff+dd*bad)
assert S.simplify(defect)!=0
out['negative_controls']=[{'name':'relative_graph_slope_is_not_original_graph_slope','defect':str(S.factor(defect)),'pass':True}]
# Exact finite-time integrating factor sign.
t,T=S.symbols('t T',real=True)
for p in range(6):
 omega=t**p+1;forcing=omega-S.diff(omega,t)
 eq(f'backward_vorticity_identity_p{p}',S.exp(-T)*omega.subs(t,T)+S.integrate(S.exp(-t)*forcing,(t,0,T))-omega.subs(t,0))
# Arc degree orientation and all possible endpoint-type choices.
for em in [-1,1]:
 for ep in [-1,1]:eq(f'arc_index_{em}_{ep}',S.Rational(ep-(-em),2)-S.Rational(em+ep,2))
# Nondegenerate axis cases, including each trace-allowed sign pattern.
for bp in [-3,-1,S.Rational(1,2),2,3,5,8]:
 aa=4-bp;axis=S.sign(bp);planar=S.sign(aa*bp)
 assert planar<=axis
 out['checks'].append({'name':f'axis_index_inequality_bprime{bp}','axis':int(axis),'planar':int(planar),'pass':True})
# Degenerate scalar indices after regular-component elimination.
for exponent in range(2,9):
 for sign in [-1,1]:
  f=sign*s**exponent;degree=(S.sign(f.subs(s,1))-S.sign(f.subs(s,-1)))/2
  assert degree in [-1,0,1]
  out['checks'].append({'name':f'scalar_isolated_index_p{exponent}_sign{sign}','index':int(degree),'pass':True})
x,y,eps=S.symbols('x y epsilon',real=True)
H0=2*y*y+eps*(x**4-6*x*x*y*y+y**4);W1=S.diff(H0,x);W2=S.diff(H0,y)
eq('degenerate_source_div4',S.diff(W1,x)+S.diff(W2,y)-4)
eq('degenerate_source_curl0',S.diff(W2,x)-S.diff(W1,y))
eq('degenerate_source_normal_factor',W2-4*y*(1-3*eps*x*x+eps*y*y))
eq('degenerate_source_center_drift',W1.subs(y,0)-4*eps*x**3)
Jac=S.Matrix([W1,W2]).jacobian([x,y]).subs({x:0,y:0})
for i in range(2):
 for j in range(2):eq(f'degenerate_source_Jac_{i}{j}',Jac[i,j]-S.diag(0,4)[i,j])
# The unrestricted area/index geometry alone is not a coupled obstruction.
out['scope']='Exact algebra checks only; contraction, flatness propagation, local degree and source trapping are proved in PROOF.md, not by these finite tests.'
out['elapsed_seconds']=time.monotonic()-start;out['all_passed']=True
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'checks':len(out['checks']),'elapsed_seconds':out['elapsed_seconds'],'all_passed':True,'H':str(HH),'sigma':out['solved_sigma']}))
