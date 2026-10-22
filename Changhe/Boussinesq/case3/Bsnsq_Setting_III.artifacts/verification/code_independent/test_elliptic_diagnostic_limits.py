"""Exact counterexamples accompanying171; never import the NUM evaluator."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import json,sys,time
import sympy as s
start=time.monotonic();rows=[]
def eq(name,value,expected=0):
 assert s.simplify(value-expected)==0,name
 rows.append({'name':name,'value':str(value),'expected':str(expected),'pass':True})
for eps,M in [(Q(1,10**4),Q(3)),(Q(1,10**8),Q(10**6)),(Q(1,2),Q(2))]:
 E=[eps,eps];N=[Q(1),eps/M]
 assert max(E)/max(N)==eps and max(e/n for e,n in zip(E,N))==M
 rows.append({'name':'separate_maxima_do_not_bound_pointwise','epsilon':str(eps),'actual_max_ratio':str(M),'pass':True})
phi=s.Rational(2,3)*s.pi;eq('physical_vorticity_cancellation',s.sin(phi)+s.sin(2*phi));eq('error_remains_nonzero',s.sin(phi),s.sqrt(3)/2)
t,h=s.symbols('t h',real=True,positive=True)
f=t*(t*t-h*h)*(t*t-4*h*h)
D=lambda q,a:s.cancel((q.subs(t,a)-q.subs(t,-a))/(2*a))
eq('Richardson_Dh',D(f,h));eq('Richardson_D2h',D(f,2*h));eq('Richardson_combination',(4*D(f,h)-D(f,2*h))/3);eq('Richardson_difference',(D(f,h)-D(f,2*h))/3);eq('actual_derivative',s.diff(f,t).subs(t,0),4*h**4)
# Simultaneous failure at the three seven-point scales used in the audit,
# an exact finite-sampling counterexample, not a claim about actual errors.
A=sorted({s.Rational(k,2**j) for k in [1,2,3] for j in [0,1,2]});f=t*s.prod(t*t-a*a for a in A);weights=[s.Rational(v,60) for v in [-1,9,-45,0,45,-9,1]]
for hh in [s.Rational(1),s.Rational(1,2),s.Rational(1,4)]:eq(f'finite_stencils_all_zero_h{hh}',sum(w*f.subs(t,k*hh) for w,k in zip(weights,range(-3,4)))/hh)
expected=s.prod(-a*a for a in A);assert expected!=0;eq('finite_stencil_true_derivative',s.diff(f,t).subs(t,0),expected)
x,y,sigma=s.symbols('x y sigma',real=True);psi=-sigma*x*y;v=[-s.diff(psi,y),s.diff(psi,x)]
eq('harmonic_error_curl',s.diff(v[0],y)-s.diff(v[1],x));eq('harmonic_error_divergence',s.diff(v[0],x)+s.diff(v[1],y));eq('harmonic_error_center1',v[0].subs({x:0,y:0}));eq('harmonic_error_center2',v[1].subs({x:0,y:0}));eq('harmonic_error_strain',s.diff(psi,x,y),-sigma)
# Whole-plane x-odd format: the actual r2 representation uses only sine modes.
z=s.symbols('z',nonzero=True)
sinm=lambda k:(z**k-z**(-k))/(2*s.I)
cosm=lambda k:(z**k+z**(-k))/2
for k in range(8):eq(f'angular_product_k{k}',s.cancel(sinm(1)*cosm(k)),sinm(1) if k==0 else s.cancel((sinm(k+1)-sinm(k-1))/2))
out={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'checks':rows,'all_passed':True}
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'count':len(rows),'all_passed':True,'elapsed_seconds':out['elapsed_seconds']},indent=2))
