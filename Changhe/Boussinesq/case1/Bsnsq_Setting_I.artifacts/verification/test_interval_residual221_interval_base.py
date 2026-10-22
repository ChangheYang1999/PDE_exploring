from pathlib import Path
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
import os,sys,json,hashlib
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS']:os.environ[k]='1'
import sympy as sp
from interval_residual221 import Jet,I,B,physical,cheb_basis,cheb_derivative_bound,Field
if sys.flags.optimize:raise RuntimeError('optimized checks prohibited')
checks=[]
def ck(n,b):
 if not b:raise RuntimeError(n)
 checks.append(n)
def ff(v):return F(int(sp.numer(v)),int(sp.denom(v)))
# Complete high-degree derivative-bound checks at1, through all required orders.
b=cheb_basis(Jet.var(1,0),97)
for n,row in enumerate(b):
 for k in range(5):ck('degree96 bound endpoint '+str((n,k)),row.c[k,0].contains(F(cheb_derivative_bound(n,k),factorial(k))))
x,h=sp.symbols('x h');G=x*h*(1+x*x/7+h*h/11);A=sp.diff(G,x,h);C=sp.diff(G,x,2);Y=sp.diff(G,x);S=3*x*Y+h*sp.diff(G,h)-6*G
Dx=lambda f:sp.diff(f,x)-C/A*sp.diff(f,h);Dy=lambda f:sp.diff(f,h)/A
u1=-Dy(S);u2=Dx(S);om=-Dx(Dx(S))-Dy(Dy(S));expr={'A':A,'C':C,'y':Y,'U1':u1,'U2':u2,'Omega':om,'Omega_x':Dx(om),'Omega_y':Dy(om),'Theta':600*h,'Theta_x':-600*C/A,'Theta_y':600/A}
xx,hh=F(1,5),F(2,5);wid=F(1,2**60);eta=I(I.of(hh-wid).lo,I.of(hh+wid).hi);X,H=Jet.var(xx,0),Jet.var(eta,1);got=physical(X*H*(1+X*X/7+H*H/11),X,H)
for off in [-wid,F(0),wid]:
 sub={x:sp.Rational(xx),h:sp.Rational(hh+off)}
 for k,v in expr.items():ck('interval physical '+str((off,k)),got[k].contains(ff(v.subs(sub))))
# Interface semantics used by midpoint arithmetic.
ck('Iinteger unit',I(B).contains(1)and I(B).lo==I(B).hi==B)
a=I(-10,20);ck('Iof preserves I',I.of(a)is a)
try:a**-1
except ArithmeticError:ck('reciprocal zero refuses',True)
else:ck('reciprocal zero refuses',False)
X,H=Jet.var(0,0),Jet.var(F(2,5),1);got=physical(X*H*(1+X*X/7+H*H/11),X,H);ck('axis D undefined otherfieldsretained',got['D']is None and got['Omega']is not None and got['R']is not None)
j={'beta':'3','M':3,'alpha':'3','s':'1','a':'599','outer':[['1']],'patches':[]}
try:Field(j)
except ValueError:ck('wrong amplitude refuses',True)
else:ck('wrong amplitude refuses',False)
now=datetime.now(timezone.utc).isoformat();paths=[__file__,'code/interval_residual221.py','code/dyadic_root220.py','research/interval_residual221/PROOF.md'];out={'utc':now,'status':'PASS_INTERVAL_BASE_PHYSICAL_AND_FULL_DEGREE_CHECKS','check_count':len(checks),'checks':checks,'scope':'Finite rational checks through degree96 and interval-base physical differentiation. No candidate evaluated.','hashes':{str(Path(p).resolve()):hashlib.sha256(Path(p).read_bytes()).hexdigest()for p in paths}};Path('research/interval_residual221/verification/interval_base.json').write_text(json.dumps(out,indent=2)+'\n');print(now,out['status'],len(checks))
