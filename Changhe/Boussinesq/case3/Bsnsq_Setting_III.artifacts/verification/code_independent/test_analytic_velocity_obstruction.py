"""Packet124 independent exact polynomial and arbitrary-function controls.

The proof is written first. Rational base Taylor data are serialized and then
checked by a separate SymPy Cartesian differentiation implementation.
"""
from pathlib import Path
from datetime import datetime,timezone
from time import monotonic
from fractions import Fraction as Q
import hashlib,json
import sympy as s
import exact_bivariate as P
from formal_center_recursion import base_stream,velocity
root=Path('research/124_analytic_prescribed_velocity_obstruction/verification');root.mkdir(exist_ok=True)
start=monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','cases':[]}
x,y=s.symbols('x y');k=s.Symbol('k');wx=s.Function('wx')(x,y);wy=s.Function('wy')(x,y);tt=s.Function('T')(x,y)
F=s.diff(tt,x);J=s.diff(wy,x);D=(k-s.diff(wx,x))*F-wx*s.diff(F,x)-wy*s.diff(F,y)
Z=wx*F*J+wy*D;E=J*s.diff(Z,y)-Z*s.diff(J,y)-k*D*J
RT=wx*s.diff(tt,x)+wy*s.diff(tt,y)-k*tt
rhs=J*J*s.diff(RT,y)+(k*J-J*s.diff(wy,y)+wy*s.diff(J,y))*s.diff(RT,x)-J*wy*s.diff(RT,x,y)
assert s.expand(E-rhs)==0
out['arbitrary_function_differential_identity_exact']=True

def calc_exact(beta,psi):
 N=8;W=velocity(beta,psi);omega=P.scale(P.lap(psi),-1);kk=beta-2
 F=P.add(P.dot_grad(W,omega,N),omega);J=P.diff(W[1],0)
 D=P.add(P.mul(P.add({(0,0):kk},P.scale(P.diff(W[0],0),-1)),F,N),P.scale(P.dot_grad(W,F,N),-1))
 Z=P.add(P.mul(P.mul(W[0],F,N),J,N),P.mul(W[1],D,N))
 E=P.add(P.mul(J,P.diff(Z,1),N),P.scale(P.mul(Z,P.diff(J,1),N),-1),P.scale(P.mul(D,J,N),-kk))
 return E

def expr(rows):return sum(s.Rational(z['coefficient'])*x**z['x_power']*y**z['y_power']for z in rows)
def tr(e,n=6):return sum(v*x**ij[0]*y**ij[1]for ij,v in s.Poly(s.expand(e),x,y).terms()if sum(ij)<=n)
def calc_sympy(beta,ps):
 kk=beta-2;W1=beta*x-s.diff(ps,y);W2=beta*y+s.diff(ps,x)
 oo=-s.diff(ps,x,2)-s.diff(ps,y,2)
 f=tr(W1*s.diff(oo,x)+W2*s.diff(oo,y)+oo);j=s.diff(W2,x)
 d=tr((kk-s.diff(W1,x))*f-W1*s.diff(f,x)-W2*s.diff(f,y))
 z=tr(W1*f*j+W2*d)
 ee=tr(j*s.diff(z,y)-z*s.diff(j,y)-kk*d*j)
 return s.Poly(ee,x,y)
for bs,av in [('4','1'),('9','1'),('25/9','3/2')]:
 beta,a0=Q(bs),Q(av);psi,pars=base_stream(beta,a0,8)
 E=calc_exact(beta,psi);q0=4*a0/beta;mu=1+3*beta/2;M=2*beta+1
 qp=32*a0*a0*(3*beta+5)/(9*beta*beta*(beta+1)*(beta+2))
 wanted=q0*(2*beta+4)*mu*M*qp
 assert E.get((2,1))==wanted>0
 cert={'parameters':pars,'psi':P.serialize(psi),'E_through_degree3':P.serialize(P.trunc(E,3)),
       'coefficient_x2y':str(wanted),'scope':'base Taylor polynomial control; complete analytic theorem is PROOF.md'}
 path=root/('base_b'+bs.replace('/','_')+'_certificate.json');path.write_text(json.dumps(cert,indent=2)+'\n')
 loaded=json.loads(path.read_text());check=calc_sympy(s.Rational(bs),expr(loaded['psi']))
 actual=check.coeff_monomial(x*x*y);assert actual==s.Rational(loaded['coefficient_x2y'])
 if bs=='4':assert actual==s.Rational(476,5)
 # Full polynomial exact local B2 solution must have E identically zero.
 c=1+beta/2;poly={(1,1):c,(3,0):-q0/6}
 assert calc_exact(beta,poly)=={}
 out['cases'].append({'beta':bs,'a0':av,'coefficient_x2y':str(actual),'expected':str(wanted),
  'rational_vs_Cartesian_SymPy_agree':True,'polynomial_exact_solution_E_zero':True,
  'certificate':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
 print('passed',bs,'coefficient',actual,flush=True)
# This identity is necessary only: J=0 forces E=0 even for incompatible data.
# W=(x,0), k=1, Omega=x^2 gives F=3x^2. Theta_x=F implies
# Theta=x^3+C(y); transport would require C(y)=2x^3 on an open set.
W1=x;W2=s.Integer(0);oo=x*x;ff=W1*s.diff(oo,x)+oo
assert ff==3*x*x
out['necessary_not_sufficient_degenerate_control']=True
out.update(status='CONFIRMED',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=monotonic()-start,
 code_sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in [Path(__file__),Path('code_independent/exact_bivariate.py'),Path('code_independent/formal_center_recursion.py')]})
(root/'tests.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
