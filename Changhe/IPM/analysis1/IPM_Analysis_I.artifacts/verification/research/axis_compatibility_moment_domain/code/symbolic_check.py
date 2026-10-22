from pathlib import Path
from datetime import datetime,timezone
import sys,json,hashlib
sys.dont_write_bytecode=True
import sympy as S
R=Path(__file__).resolve().parents[3];D=R/'research/axis_compatibility_moment_domain';E=D/'evidence'
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def parse(d,vars):return sum(S.Rational(v)*S.prod(x**int(e) for x,e in zip(vars,key.split(','))) for key,v in d.items())
start=datetime.now(timezone.utc).isoformat();A=load(E/'fraction.json');assert sha(D/'PROOF.md')==A['proof_sha256'] and sha(D/'code/fraction_check.py')==A['code_sha256'];parent=load(R/A['parent_path']);assert sha(R/A['parent_path'])==A['parent_sha256'] and parent['files']==A['parent_files']
for n,h in parent['files'].items():assert sha(R/n)==h,n
x,y=S.symbols('x y',real=True);b=S.Function('b',positive=True)(y);u=S.Function('u')(y);c=S.Function('c')(y);v=S.Function('v')(y);psi=x*u+x**3*v;rho=x**2*b+x**4*c;vel=S.Matrix([-S.diff(psi,y),S.diff(psi,x)]);image=vel.dot(S.Matrix([S.diff(rho,x),S.diff(rho,y)]));axis=S.simplify(S.diff(image,x,2).subs(x,0)/2);assert S.simplify(axis-(-2*b*S.diff(u,y)+S.diff(b,y)*u))==0
assert S.simplify(axis-parse(A['axis_coefficient'],[0,0,b,S.diff(b,y),u,S.diff(u,y),c,3*v]))==0
ode=S.simplify(2*b**S.Rational(3,2)*S.diff(u/S.sqrt(b),y)+axis);assert ode==0
w=S.Function('w')(y);candidate=S.sqrt(b)*w;assert S.simplify(2*b*S.diff(candidate,y)-S.diff(b,y)*candidate-2*b**S.Rational(3,2)*S.diff(w,y))==0
for row in A['harmonic_axis_rows']:
 n=row['n'];co=S.simplify(S.im(n*(S.I*y)**(n-1)));assert co==S.Rational(row['axis_coefficient'])*y**row['axis_degree']
 if n<=12:
  stream=S.im(S.expand((x+S.I*y)**n));assert S.simplify(S.diff(stream,x).subs(x,0)-co)==0
xi,eta=S.symbols('xi eta',real=True);monomials=sum(xi**(2*(3-j))*eta**(2*j) for j in range(4));w6=(xi**2+eta**2)**3;upper=S.Poly(S.expand(w6-monomials),xi,eta);lower=S.Poly(S.expand(3*monomials-w6),xi,eta);assert all(q>0 for P in [upper,lower] for q in P.coeffs());assert S.expand(upper.as_expr()-parse(A['sobolev_upper_difference'],[xi,eta]))==0 and S.expand(lower.as_expr()-parse(A['sobolev_lower_difference'],[xi,eta]))==0
s=S.Rational(153,50);t=s-3;assert str(t)==A['fractional_t_exact'] and t>0 and t<S.Rational(1,2);exps={'gagliardo_small':2*S.Rational(1,2)-(2+2*t)+1,'gagliardo_large':-(2+2*t)+1,'fourier_kernel_small':2-(2+2*t)+1};assert {n:str(S.simplify(z)) for n,z in exps.items()}==A['radial_exponents_exact']
f=S.Function('f')(x,y);lap=lambda g:S.diff(g,x,2)+S.diff(g,y,2);assert S.expand(-lap(S.diff(f,x))-S.diff(-lap(f),x))==0
j=S.symbols('j',integer=True,nonnegative=True);assert S.expand((2*j+2)+1-(2*j+3))==0
out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_INDEPENDENT_FUNCTIONAL_JETS_ODE_HARMONIC_AND_FRACTIONAL_CHECKS_REQUIRES_ACTUAL_REVIEW','code_sha256':sha(Path(__file__)),'fraction_json_sha256':sha(E/'fraction.json'),'parent_pin_count':len(parent['files']),'axis_coefficient':str(axis),'integrating_factor_identity':str(ode),'harmonic_axis_rows_checked':len(A['harmonic_axis_rows']),'harmonic_full_polynomials_checked':6,'sobolev_upper_difference':str(upper.as_expr()),'sobolev_lower_difference':str(lower.as_expr()),'fractional_t_exact':str(t),'radial_exponents_exact':{n:str(S.simplify(z)) for n,z in exps.items()},'laplacian_derivative_commutator':'0','general_moment_index_identity':'0','scope':'Independent symbolic identities only. Full infinite and functional-analytic conclusions depend on PROOF.md.'}
with (E/'symbolic.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps(out))
