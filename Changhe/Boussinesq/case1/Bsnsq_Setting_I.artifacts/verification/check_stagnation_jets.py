"""Exact symbolic checks of local identities; no existence or global claims."""
from pathlib import Path
import datetime,hashlib,json,platform
import sympy as s

x,y,beta,c,d=s.symbols('x y beta c d',real=True)
b=beta-2
Z=s.Matrix([x,y]); A=s.Matrix([[beta-c,-d],[-d,beta+c]])
# Rational, nonsymmetric nonlinear terms from one stream function.
psi=c*x*y+d*(y*y-x*x)/2
for n in range(3,6):
 for i in range(n+1): psi+=s.Rational((-1)**(n+i)*(2*i+1),n+i+3)*x**i*y**(n-i)
U=s.Matrix([-s.diff(psi,y),s.diff(psi,x)]); W=beta*Z+U
Omega=-s.diff(psi,x,2)-s.diff(psi,y,2)
Theta=sum(s.Rational((-1)**i*(i+2),n+i+1)*x**i*y**(n-i) for n in range(2,6) for i in range(n+1))
origin={x:0,y:0}
grad=lambda f:s.Matrix([s.diff(f,x),s.diff(f,y)])
RT=(W.dot(grad(Theta))-b*Theta).expand()
RO=(W.dot(grad(Omega))+Omega-s.diff(Theta,x)).expand()
H=s.hessian(Theta,(x,y)).subs(origin); v=grad(Omega).subs(origin)

def zero(expr):
 return all(s.expand(e)==0 for e in expr) if isinstance(expr,s.MatrixBase) else s.expand(expr)==0

def homogeneous(f,n):
 return sum(co*x**i*y**j for (i,j),co in s.Poly(s.expand(f),x,y).terms() if i+j==n)

checks={
 'W_origin_zero':zero(W.subs(origin)),
 'Theta_and_gradient_origin_zero':Theta.subs(origin)==0 and zero(grad(Theta).subs(origin)),
 'Omega_origin_zero':Omega.subs(origin)==0,
 'DW_origin_A':zero(W.jacobian(Z).subs(origin)-A),
 'A_symmetric_trace':A==A.T and s.trace(A)==2*beta,
 'Omega_sign':zero(Omega+s.diff(U[1],x)-s.diff(U[0],y)),
 'RT_hessian_identity':zero(s.hessian(RT,(x,y)).subs(origin)-(A.T*H+H*A-b*H)),
 'RO_gradient_identity':zero(grad(RO).subs(origin)-((A.T+s.eye(2))*v-H*s.Matrix([1,0]))),
}
for n in range(2,6):
 pn=homogeneous(Theta,n)
 rhs=(A*Z).dot(grad(pn))-b*pn
 for k in range(2,n):
  wk=s.Matrix([homogeneous(z,k) for z in W-A*Z])
  rhs+=wk.dot(grad(homogeneous(Theta,n-k+1)))
 checks[f'degree_{n}_inhomogeneous_identity']=zero(homogeneous(RT,n)-rhs)
# An exact local coupled example, without the A1 global/parity hypotheses.
psiex=-(beta-b/2)*x*y
uex=s.Matrix([-s.diff(psiex,y),s.diff(psiex,x)])
wex=beta*Z+uex; tex=y*y; oex=-s.diff(psiex,x,2)-s.diff(psiex,y,2)
checks.update({
 'example_divergence':zero(s.diff(uex[0],x)+s.diff(uex[1],y)),
 'example_P1':zero(wex.dot(grad(oex))+oex-s.diff(tex,x)),
 'example_P2':zero(wex.dot(grad(tex))-b*tex),
 'example_elliptic':zero(oex),
 'example_invertible_DW_formula':zero(wex.jacobian(Z).det()-(2*beta-b/2)*b/2),
})
# General nonsymmetric DW discriminates all transposes, although these data
# have Omega(0) nonzero and hence do not satisfy the stagnation PDE hypothesis.
rotation=s.symbols('rotation',real=True)
psi_ns=psi+rotation*(x*x+y*y)/2
U_ns=s.Matrix([-s.diff(psi_ns,y),s.diff(psi_ns,x)])
W_ns=beta*Z+U_ns;A_ns=W_ns.jacobian(Z).subs(origin)
O_ns=-s.diff(psi_ns,x,2)-s.diff(psi_ns,y,2)
v_ns=grad(O_ns).subs(origin)
RT_ns=W_ns.dot(grad(Theta))-b*Theta
RO_ns=W_ns.dot(grad(O_ns))+O_ns-s.diff(Theta,x)
checks['nonsymmetric_RT_hessian']=zero(s.hessian(RT_ns,(x,y)).subs(origin)-(A_ns.T*H+H*A_ns-b*H))
checks['nonsymmetric_RO_gradient']=zero(grad(RO_ns).subs(origin)-((A_ns.T+s.eye(2))*v_ns-H*s.Matrix([1,0])))
checks['test_discriminates_wrong_hessian_transpose']=not zero(A_ns.T*H+H*A_ns-(A_ns*H+H*A_ns))
checks['test_discriminates_wrong_gradient_transpose']=not zero((A_ns.T-A_ns)*v_ns)
l1,l2=s.symbols('lambda1 lambda2',real=True)
for m in range(2,9):
 for i in range(m+1):
  j=m-i; mon=x**i*y**j
  assert zero((s.diag(l1,l2)*Z).dot(grad(mon))-(i*l1+j*l2)*mon)
checks['monomial_rule_degrees_2_to_8']=True
out=Path('research/stagnation_jets/verification');out.mkdir(parents=True,exist_ok=True)
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'all_passed':all(checks.values()),'method':'Exact rational polynomial differentiation, coefficient extraction, and symbolic beta identities. This is a manufactured identity check; the general proof is PROOF.md.','versions':{'python':platform.python_version(),'sympy':s.__version__},'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(out/'symbolic_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2));assert result['all_passed']
