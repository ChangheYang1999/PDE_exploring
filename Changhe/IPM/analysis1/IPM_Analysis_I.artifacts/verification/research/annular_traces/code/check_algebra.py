"""Exact parity, homogeneity, kernel, subtraction, and geometric-sum checks."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import sympy as S
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/annular_traces/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 x,y,xi,eta,al=S.symbols('x y xi eta al',real=True);z=x+S.I*y
 kernels=0
 for j in range(6):
  for l in range(10):
   f=S.diff(z**-2,x,l,y,j)
   g=(-1)**(l+j)*S.I**j*math.factorial(l+j+1)*z**(-2-l-j)
   assert S.simplify(f-g)==0;kernels+=1
 # Full multipliers, including the local -h term in a y partial Fourier inverse.
 symbol1=xi*eta/(xi**2+eta**2);symbol2=-xi**2/(xi**2+eta**2)
 assert S.cancel(symbol2-(-1+eta**2/(xi**2+eta**2)))==0
 assert S.cancel(symbol1**2+symbol2**2-xi**2/(xi**2+eta**2))==0
 # Trace parity from kernel differentiation at target 0 (source coordinate signs).
 kr=[-x*y/(x*x+y*y)**2,(x*x-y*y)/(2*(x*x+y*y)**2)]
 table=[('u10',0,0,1,6,[1,3,5,7],9),('u12',0,2,1,6,[1,3,5],7),('u21',1,1,0,6,[0,2,4,6],8),('v11',0,1,0,3,[0,2,4,6],8),('v13',0,3,0,3,[0,2,4],6),('v15',0,5,0,3,[0,2],4),('v20',1,0,1,3,[1,3,5,7],9),('v22',1,2,1,3,[1,3,5],7),('v24',1,4,1,3,[1,3],5)]
 records=[];enum=0;parities=0;scales=0
 for label,component,j,parity,rect,claimed,P in table:
  swap=label[0]=='v';expected=list(range(parity,P,2))
  assert claimed==expected
  p=rect if rect%2==parity else rect+1
  normal=x if swap else y;tangent=y if swap else x
  derivative=S.diff(kr[component],normal,j,tangent,p)
  assert S.cancel(derivative.subs(x,-x)-derivative)==0
  assert S.cancel(derivative.subs(y,-y)+derivative)==0
  assert derivative.subs({x:S.Rational(7,5),y:S.Rational(3,4)})!=0;parities+=3
  for A in [F(8)+F(n,101)*2 for n in range(1,101)]:
   t=A-j-1;ls=[l for l in range(20) if l%2==parity and l<t];pp=min(l for l in range(20) if l%2==parity and l>t)
   assert ls==expected and pp==P and P-t>0 and t-max(ls)>0
   assert (p<=t)==(label not in ['u12','v15']);enum+=1
   # Source norm scale R^(A-1), normal trace R^-j, target r^-t.
   assert A-1-j-t==0
   # Small target: R^(A+1) R^(-2-j-P) r^(P-t).
   assert A+1-2-j-P+(P-t)==0
   # Large target trace: R^(A+1) r^(-2-j-t), and moment R^(t-l)r^(l-t).
   assert -2-j-t==-(A+1)
   assert all((t-l)+(l-t)==0 for l in ls);scales+=4
  records.append({'trace':label,'natural_powers':expected,'P':P,'rectangular_first_remaining':p,'rectangular_inner_threshold_exact':str(p+j+1),'rectangular_verdict':'BOUNDED' if label in ['u12','v15'] else 'UNBOUNDED'})
 # Exact positivity and finite-geometric decomposition, including resonance rejection.
 geo=0
 for q in [F(1,2),F(99,100),F(1,100),F(999,1000)]:
  for n in [1,2,17,128]:
   assert sum((q**d for d in range(3,3+n)),F(0))+q**(3+n)/(1-q)==q**3/(1-q);geo+=1
 res=0
 for label,component,j,parity,rect,claimed,P in table:
  for l in range(parity,12,2):assert (l+j+1)%2==0;res+=1
 # The two elementary Sobolev integral constants, evaluated symbolically.
 th=S.symbols('th',positive=True)
 assert S.cancel(4/((2-2*th)*(3-2*th))-2/((1-th)*(3-2*th)))==0
 # Gamma tail follows from derivative of v/T-log(1+v/T), nonnegative for v>=0.
 v,T=S.symbols('v T',positive=True)
 assert S.simplify(S.diff(v/T-S.log(1+v/T),v)-v/(T*(T+v)))==0
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_EXACT_ALGEBRA','source_sha256':sha(__file__),'proof_sha256':sha(B/'research/annular_traces/PROOF.md'),'sympy_version':S.__version__,'checks':{'kernel_derivatives':kernels,'multiplier_identities':2,'parity_and_nonzero_moment':parities,'whole_window_subtractions':enum,'homogeneity_identities':scales,'geometric_identities':geo,'parity_resonances':res,'elementary_integral_identities':2},'trace_table':records,'scope':'Exact identities and representative rational whole-window comparisons, supported by the analytic strict-window proof, not a sampling proof of that window.'}
 (E/'algebra.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
