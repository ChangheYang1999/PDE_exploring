"""Exact principal-value boundary coefficient and scaling checks."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
from fractions import Fraction as F
import sympy as s,json,hashlib,time
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];D=B/'research/source_local_estimate';E=D/'evidence';start=time.monotonic()
t,x,y=s.symbols('t x y',real=True);pi=s.pi
terms=[s.sin(t)**2*s.cos(t)**2,s.sin(t)**4,(s.sin(t)**2-s.cos(t)**2)*s.sin(t)*s.cos(t),(s.sin(t)**2-s.cos(t)**2)*s.sin(t)**2]
exact=[s.Rational(1,8),s.Rational(3,8),s.Rational(0),s.Rational(1,4)]
for expr,value in zip(terms,exact):assert s.simplify(s.integrate(s.expand_trig(expr),(t,0,2*pi))/(2*pi)-value)==0
assert s.simplify(s.diff((y*y-x*x)/(2*pi*(x*x+y*y)**2),y)-y*(3*x*x-y*y)/(pi*(x*x+y*y)**3))==0
# A separate exact angular-moment recurrence gives the same constants.
from math import factorial
moment=lambda a,b:F(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
assert moment(0,2)==F(3,8) and moment(1,1)==F(1,8)
assert F(1,2)-(moment(0,2)-moment(1,1))==F(1,4)
sv=F(31,10);sc={}
for amp,name in [(F(0),'chi'),(F(1),'q'),(F(0),'T')]:
 exponent=min(amp,amp-1,amp+1-sv);assert exponent==amp+1-sv;sc[name]=str(exponent)
assert (2-sv)-sv+(1-sv)==3-3*sv
assert min(1-sv,(1-sv)+(2-sv))==3-2*sv
assert min(-3,(1-sv)-3,-sv+1)==-sv-2
pins={str(p.relative_to(B)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),D/'PROOF.md',D/'ADDENDUM.md']}
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ADDENDUM','symbolic_angular_integrals':4,'symbolic_kernel_derivatives':1,'independent_exact_moment_checks':3,'exact_scaling_identities':6,'circular_PV_local_strain_coefficient':'1/4','multiplier_scaling':sc,'files':pins,'seconds':time.monotonic()-start}
(E/'addendum_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
