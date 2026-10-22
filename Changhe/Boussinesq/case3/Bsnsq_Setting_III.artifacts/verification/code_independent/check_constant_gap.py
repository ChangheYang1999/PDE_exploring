"""Exact Cartesian homogeneity and exponent bookkeeping for the restricted gap theorem."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import sympy as sp,json,time,hashlib
root=Path('research/99_constant_gap_noninteger_beta/verification');start=time.monotonic();stamp=datetime.now(timezone.utc).isoformat();rows=[]
for numerator in range(9,81):
 b=Fraction(numerator,4)
 if b<=2 or b.denominator==1:continue
 N=b.numerator//b.denominator;s=1/b
 assert (N+1)*s<1+s<(N+2)*s
 assert 1<(N+1)*s<2
 assert (N+2)*s>1+s and 1+2*s>1+s
 for j in range(1,N+1):
  for k in range(1,N+2):
   assert j*s+k*s !=1+s
 rows.append({'beta':str(b),'N':N,'constant_power':str(1+s),'next_ladder_power':str((N+2)*s)})
x,y=sp.symbols('x y',positive=True);rr=x*x+y*y;checks=[]
for b in [sp.Rational(5,2),sp.Rational(7,2),sp.Rational(13,4)]:
 s=1/b;N=int(b)
 for j in range(1,N+1):
  p=2-j*s;psi=x*rr**((p-1)/2);u=(-sp.diff(psi,y),sp.diff(psi,x));om=(1-p*p)*x*rr**(-(1+j*s)/2)
  assert sp.simplify(-sp.diff(psi,x,2)-sp.diff(psi,y,2)-om)==0
  for comp in u:assert sp.simplify(x*sp.diff(comp,x)+y*sp.diff(comp,y)-(1-j*s)*comp)==0
  checks.append({'beta':str(b),'j':j,'Poisson':'EXACT','velocity_homogeneity':'EXACT'})
 a=x*rr**(-(1+s)/2);dy=-(1+s)*x*y*rr**(-(3+s)/2)
 assert sp.simplify(sp.diff(a,y)-dy)==0
 assert dy.subs({x:1,y:1})!=0
out=dict(started_utc=stamp,ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='COMPLETE',exact_exponent_cases=rows,Cartesian_checks=checks,limitations='Exact algebraic consistency tests accompany the complete informal proof; they do not replace its analytic inverse estimates or prove a full B2 exclusion.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],len(rows),len(checks),flush=True)
