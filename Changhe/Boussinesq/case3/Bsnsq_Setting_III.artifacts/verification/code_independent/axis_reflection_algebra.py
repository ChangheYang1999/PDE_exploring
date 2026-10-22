"""Independent finite exact algebra for the reflection-point identities."""
import os
os.environ['OMP_NUM_THREADS']='1'
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,time
start=time.monotonic()
beta,B,J,Q,R=s.symbols('beta B J Q R',nonzero=True)
A=(beta+1)*Q/2
Ap=(B*R-J*Q)/2
App=(3*beta+1)*R/2
res1=s.expand(B*Ap+(beta+2)*A)
res2=s.expand(B*App+(2*beta+2)*Ap-2*J*A)
sol=s.solve([res1,res2],(R,J),dict=True)[0]
expectedBJ=(beta+1)*(beta+2)*(5*beta+3)/(beta-1)
expectedB2R=4*(beta+1)**2*(beta+2)*Q/(beta-1)
checks={
 'BJ_exact_zero':str(s.factor(B*sol[J]-expectedBJ)),
 'B2R_exact_zero':str(s.factor(B**2*sol[R]-expectedB2R)),
 'residual1':str(s.factor(res1)),
 'residual2':str(s.factor(res2)),
 'J_solution':str(s.factor(sol[J])),
 'R_solution':str(s.factor(sol[R])),
}
x,y,h=s.symbols('x y h',real=True)
S=x*x+(y-h)**2
F=s.Function('F')
psi=-x*F(S)
omega=-(s.diff(psi,x,2)+s.diff(psi,y,2))
expected=4*x*(2*s.Subs(s.diff(F(s.Symbol('z')),s.Symbol('z')),s.Symbol('z'),S)+S*s.Subs(s.diff(F(s.Symbol('z')),s.Symbol('z'),2),s.Symbol('z'),S))
checks['radial_curl_zero']=str(s.simplify(omega-expected))
assert checks['BJ_exact_zero']==checks['B2R_exact_zero']==checks['radial_curl_zero']=='0'
checks['ended_utc']=datetime.now(timezone.utc).isoformat()
checks['elapsed_seconds']=time.monotonic()-start
Path('research/49_axis_reflection_exclusions/verification/algebra.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
