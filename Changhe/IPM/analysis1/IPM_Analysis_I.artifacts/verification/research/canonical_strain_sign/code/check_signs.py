"""Canonical signs, boundary moments, and rank-one correction, independently reconstructed."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
from pathlib import Path
import sys,json,hashlib
from fractions import Fraction as Q
from datetime import datetime,timezone
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_strain_sign';E=D/'evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
x,y,th,xi,eta,sg=s.symbols('x y theta xi eta sigma',real=True);r2=x*x+y*y;G=s.log(r2)/(4*s.pi);ids={}
def check(name,v):assert s.simplify(v)==0,(name,v);ids[name]='0'
check('velocity_kernel1',s.diff(G,x,y)+x*y/(s.pi*r2**2))
check('velocity_kernel2',-s.diff(G,x,2)-(x*x-y*y)/(2*s.pi*r2**2))
check('opposite_strain_kernel',s.diff(G,x,2,y)-y*(3*x*x-y*y)/(s.pi*r2**3))
check('canonical_U1',-s.diff(sg*x*y,y)+sg*x);check('canonical_U2',s.diff(sg*x*y,x)-sg*y)
psihat=s.I*xi/(xi*xi+eta*eta)
check('canonical_poisson',(xi*xi+eta*eta)*psihat-s.I*xi)
check('canonical_velocity_symbol1',-s.I*eta*psihat-xi*eta/(xi*xi+eta*eta))
check('canonical_velocity_symbol2',s.I*xi*psihat+xi*xi/(xi*xi+eta*eta))
check('canonical_strain_symbol',-xi*eta*psihat+s.I*xi*xi*eta/(xi*xi+eta*eta))
check('second_derivative_boundary',s.integrate(s.cos(th)**2,(th,0,2*s.pi))/(2*s.pi)-s.Rational(1,2))
check('third_derivative_boundary',s.integrate((s.sin(th)**2-s.cos(th)**2)*s.sin(th)**2,(th,0,2*s.pi))/(2*s.pi)-s.Rational(1,4))
for name,test in [('constant',1),('linear_x',s.cos(th)),('linear_y',s.sin(th))]:check('strain_moment_'+name,s.integrate(s.sin(3*th)*test,(th,0,2*s.pi)))
# A fresh rational moment calculation uses integral sin^(2a) cos^(2b)/(2pi).
from math import factorial
moment=lambda a,b:Q(factorial(2*a)*factorial(2*b),4**(a+b)*factorial(a)*factorial(b)*factorial(a+b))
assert moment(0,1)==Q(1,2) and moment(2,0)-moment(1,1)==Q(1,4)
assert -Q(1,2)+(moment(2,0)-moment(1,1))==-Q(1,4)
# Independent exact finite-dimensional rank-one example with visibly distinct signs.
A=s.Matrix([[2,1],[0,3]]);ell=s.Matrix([1,2]);old=s.Matrix([[1,0]]);canonical=-old;v=A.inv()*ell
correct=1+(canonical*v)[0];wrong=1+(old*v)[0]
assert correct==s.Rational(5,6) and wrong==s.Rational(7,6) and correct!=wrong
candidate=A.inv()-v*canonical*A.inv()/correct
for i in range(2):
 for j in range(2):check('rankone_inverse_'+str(i)+str(j),((A+ell*canonical)*candidate-s.eye(2))[i,j])
paths=[Path(__file__),D/'PROOF.md',E/'proof_first.json',B/'PROMPT.md',B/'research/source_local_estimate/PROOF.md',B/'research/source_local_estimate/ADDENDUM.md',B/'research/source_local_estimate/evidence/verdict.json',B/'research/source_semigroup/PROOF.md',B/'research/source_semigroup/evidence/verdict.json']
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_CANONICAL_SIGN_CORRECTION','counts':{'symbolic_identities':len(ids),'independent_exact_boundary_checks':3,'distinct_rankone_denominators':2},'exact':{'canonical_local_strain_coefficient':'-1/4','example_canonical_denominator':str(correct),'example_old_plus_denominator':str(wrong)},'identities':ids,'files':{str(p.relative_to(B)):sha(p) for p in paths}}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['files','identities']},indent=2))
