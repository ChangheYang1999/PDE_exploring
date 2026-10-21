"""Exact checks of the source estimate; the quadrature is illustrative only."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
import sympy as S
from scipy.integrate import quad
import math
ROOT=Path(__file__).resolve().parents[1]
A=S.symbols('A',positive=True); beta=S.symbols('beta',real=True)
g,lam,delta=S.symbols('g lam delta',positive=True)
w,wp,v,vp=S.symbols('w wp v vp',real=True)
checks={}
checks['normalized_log_derivative']=S.cancel(vp/(w+v)+(A-wp)*v/(w*(w+v))-((wp+vp-A)/(w+v)-(wp-A)/w))==0
baseW=A**(beta-2)*g**(1-beta)*delta**(beta-2)
cpp=-lam**(-3)*lam**(1-beta)*baseW/(2*g**3)
expected=-A**(beta-2)*delta**(beta-2)/(2*(lam*g)**(beta+2))
checks['exact_source_multiplier_vpp']=S.simplify(cpp-expected)==0
cp=-lam**(-2)*lam**(1-beta)*baseW/(2*A*g**2*delta)
checks['exact_source_multiplier_vp']=S.simplify(cp-expected*lam*g/(A*delta))==0
s=S.symbols('s',positive=True)
checks['integrated_weight']=S.expand((beta-2)*(beta-3)+(s/A)*(beta-3)-(3-beta)*(2-beta-s/A))==0
K=(1-beta)*(3-beta)*(2-beta-s/A)/(6*A*s**(beta+2))
b=2/A;gs=2*A-2
checks['exceptional_K_zero']=S.simplify(K.subs({beta:b,s:gs}))==0
kp=S.diff(K,s).subs(beta,b).subs(s,gs)
checks['exceptional_derivative']=S.simplify(kp+(1-b)*(3-b)/(6*A*A*gs**(b+2)))==0
I=S.symbols('I',positive=True)
checks['quadratic_plateau_limit']=S.simplify(kp*A*gs*I+(1-b)*(3-b)*I/(6*A*gs**(b+1)))==0
x=S.symbols('x',real=True)
w0=-4*x*(1-x*x/12)/(1+x*x/12);g0=x*x/(1+x*x/12)
checks['example_axis_equation']=S.cancel(w0*S.diff(g0,x)-(S.diff(w0,x)-4)*g0)==0
checks['example_source_value']=S.simplify(g0.subs(x,S.sqrt(12))-6)==0
assert all(checks.values()),checks
L=math.sqrt(12);D=.125
def chi(t):
 if t<=0:return 0.
 if t>=1:return 1.
 a=-1/t;b=-1/(1-t);m=max(a,b)
 return math.exp(a-m)/(math.exp(a-m)+math.exp(b-m))
def integrand(d):
 if d==0:return 0.
 xx=L-d
 ww=-4*xx*d*(2*L-d)/(12+xx*xx)
 return d**2.5*chi(math.log(D/d))/(ww*ww)
num,err=quad(integrand,0,D,points=[D/math.e],epsabs=1e-14,epsrel=1e-12,limit=150)
kappa=(1-.5)*(3-.5)*num/(6*4*6**1.5)
out={'date':datetime.now(timezone.utc).isoformat(),'exact_checks':checks,
     'diagnostic_only':{'A':4,'L':'sqrt12','g_source':6,'d0':D,'I_infinity':num,'quadrature_error_estimate':err,'negative_jump':-kappa,'scope':'Floating illustration, not an interval certificate and not part of the proof.'},
     'dependencies':[{'file':str(p.relative_to(ROOT.parent.parent)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in [Path(__file__),ROOT/'PROOF.md',ROOT.parent/'critical-norm/PROOF.md']]}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
