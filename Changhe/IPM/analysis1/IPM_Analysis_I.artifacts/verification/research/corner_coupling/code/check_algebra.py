"""Exact independent polynomial and differential checks of the corner proof."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math,random
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as s
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/corner_coupling/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
x,y=s.symbols('x y',real=True)
def direct_remainder(f,N,M):
 # Differentiate and subtract coordinate Taylor polynomials literally.
 tx=sum(x**i*s.diff(f,x,i).subs(x,0)/math.factorial(i) for i in range(N))
 rx=s.expand(f-tx)
 ty=sum(y**j*s.diff(rx,y,j).subs(y,0)/math.factorial(j) for j in range(M))
 return s.expand(rx-ty)
def groups(f,N,M):
 out={}
 for (p,q),c in s.Poly(f,x,y).terms():
  i,j=min(p,N),min(q,M);out[i,j]=out.get((i,j),0)+c*x**(p-i)*y**(q-j)
 return out

def main():
 count={'taylor_product_identities':0,'coefficient_derivative_bounds':0,'coupling_extraction':0,'beta_derivative_formulas':0,'kernel_derivatives':0,'strain_sign':0,'weight_windows':0,'grouped_constants':0,'far_factorials':0,'elementary_integrals':0,'homogeneity':0}
 rng=random.Random(20261020)
 for N,M in [(5,2),(4,3),(4,2),(0,0),(0,3),(5,0),(1,1)]:
  for rep in range(3):
   beta=sum(s.Rational(rng.randrange(-9,10),rng.randrange(1,7))*x**rng.randrange(0,9)*y**rng.randrange(0,7) for unused in range(7))
   f=sum(s.Rational(rng.randrange(-7,8),rng.randrange(1,8))*x**rng.randrange(0,8)*y**rng.randrange(0,6) for unused in range(7))
   left=direct_remainder(beta*f,N,M);right=0
   for (i,j),g in groups(beta,N,M).items():right+=x**i*y**j*g*direct_remainder(f,N-i,M-j)
   assert s.expand(left-right)==0;count['taylor_product_identities']+=1
 # Integral remainder coefficient integrates (1-t)^(n-1)/(n-1)! to1/n!.
 t=s.symbols('t',real=True)
 for n in range(1,9):assert s.integrate((1-t)**(n-1),(t,0,1))/math.factorial(n-1)==s.Rational(1,math.factorial(n));count['coefficient_derivative_bounds']+=1
 alpha=s.Function('alpha')(x,y);b1=2*alpha+x*s.diff(alpha,x);b2=alpha+y*s.diff(alpha,y);b0=3*alpha+x*s.diff(alpha,x)+y*s.diff(alpha,y)
 for p in range(6):
  for q in range(4):
   if p+q>7:continue
   a=s.diff(alpha,x,p,y,q)
   assert s.expand(s.diff(b1,x,p,y,q)-(2+p)*a-x*s.diff(a,x))==0
   assert s.expand(s.diff(b2,x,p,y,q)-(1+q)*a-y*s.diff(a,y))==0
   count['beta_derivative_formulas']+=2
 assert s.expand(s.diff(b0,x,4,y,2)-9*s.diff(alpha,x,4,y,2)-x*s.diff(alpha,x,5,y,2)-y*s.diff(alpha,x,4,y,3))==0;count['beta_derivative_formulas']+=1
 for rep in range(3):
  al=1+s.Rational(rep+1,7)*x**2+x**4*y**2-y**6
  u1=x+x**3-2*x*y**2+x**7+x**5*y**4;u2=-y+x**2*y+y**5+x**4*y**3
  c=s.Rational(rep+2,5);rho=x**2*y*al
  g=(u1+c*x/3)*s.diff(rho,x)+(u2+c*y/3)*s.diff(rho,y)
  b1=2*al+x*s.diff(al,x);b2=al+y*s.diff(al,y);b0=3*al+x*s.diff(al,x)+y*s.diff(al,y)
  rhs=x*y*direct_remainder(b1*u1,5,2)+x**2*direct_remainder(b2*u2,4,3)+c*x**2*y*direct_remainder(b0,4,2)/3
  assert s.expand(direct_remainder(g,6,3)-rhs)==0;count['coupling_extraction']+=1
 z=x+s.I*y;kernel=z**(-2)/(2*s.pi)
 for p in range(8):
  for q in range(8-p):
   rhs=(-1)**(p+q)*s.I**q*math.factorial(p+q+1)*z**(-2-p-q)/(2*s.pi)
   assert s.cancel(s.diff(kernel,x,p,y,q)-rhs)==0;count['kernel_derivatives']+=1
 k1=-x*y/(s.pi*(x*x+y*y)**2)
 # -partial_x K1(-X)=Im(z^-3)/(-pi)=y(3x²-y²)/(pi r^6).
 strain=-s.diff(k1,x).subs({x:-x,y:-y},simultaneous=True)
 assert s.cancel(strain-y*(3*x*x-y*y)/(s.pi*(x*x+y*y)**3))==0;count['strain_sign']+=1
 for a,b in [(F(129,20),F(307,100)),(F(1299,200),F(3403,1000))]:
  expected={};first=second=0
  for i in range(6):
   for j in range(3):
    N,M=5-i,2-j;u,v=a-1-i,b-1-j
    assert (u-N+F(1,2),N+F(1,2)-u)==(a-F(11,2),F(13,2)-a)
    assert (v-M+F(1,2),M+F(1,2)-v)==(b-F(5,2),F(7,2)-b)
    assert min(u-N+F(1,2),N+F(1,2)-u,v-M+F(1,2),M+F(1,2)-v)>0
    expected[N,M]=expected.get((N,M),F(0))+(F(5,2)+i)/(math.factorial(i)*math.factorial(j));count['weight_windows']+=1;first+=1
  for i in range(5):
   for j in range(4):
    N,M=4-i,3-j;u,v=a-2-i,b-j
    assert (u-N+F(1,2),N+F(1,2)-u)==(a-F(11,2),F(13,2)-a)
    assert (v-M+F(1,2),M+F(1,2)-v)==(b-F(5,2),F(7,2)-b)
    assert min(u-N+F(1,2),N+F(1,2)-u,v-M+F(1,2),M+F(1,2)-v)>0
    expected[N,M]=expected.get((N,M),F(0))+(F(3,2)+j)/(math.factorial(i)*math.factorial(j));count['weight_windows']+=1;second+=1
  assert first==18 and second==20 and len(expected)==23
  for (N,M),c in expected.items():
   formula=(F(15,2)-N)/(math.factorial(5-N)*math.factorial(2-M)) if M<=2 else F(0)
   if N<=4:formula+=(F(9,2)-M)/(math.factorial(4-N)*math.factorial(3-M))
   assert c==formula;count['grouped_constants']+=1
 for N,M in [(5,2),(4,3)]:
  for p in range(N+1):
   for q in range(M+1):
    assert F(math.comb(N,p)*math.comb(M,q),math.factorial(N)*math.factorial(M))==F(1,math.factorial(p)*math.factorial(N-p)*math.factorial(q)*math.factorial(M-q));count['far_factorials']+=1
 A,g,d=s.symbols('A g d',positive=True)
 # Radial primitive and monomial norms; derivative checks avoid heuristic integration domains.
 r=s.symbols('r',positive=True)
 assert s.simplify(s.diff(r**(2*A-4)/(2*A-4),r)-r**(2*A-5))==0;count['elementary_integrals']+=1
 assert s.simplify(s.diff(r**(2*g-4)/(2*g-4),r)-r**(2*g-5))==0;count['elementary_integrals']+=1
 av,bv=s.symbols('a b',real=True)
 assert s.expand((13-2*av)+(7-2*bv)-(20-2*(av+bv)))==0;count['homogeneity']+=1
 for q in range(1,8):assert -2-q<=-3;count['homogeneity']+=1
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ALGEBRA','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/corner_coupling/PROOF.md'),'sympy_version':s.__version__,'checks':count,'scope':'Exact identities and representative parameter checks supporting the separate analytic proof. No numerical sampling proves the full strict window.'}
 (E/'algebra.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
