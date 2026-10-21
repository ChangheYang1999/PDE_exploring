"""Exact exponent/phase checks and finite illustrations of the moment sign."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,math
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
if not __debug__:raise RuntimeError('Checks require assertions')
x=sp.symbols('x');exact=[]
for n in range(1,7):
 e=sp.cos(x)-sum((-1)**k*x**(2*k)/sp.factorial(2*k)for k in range(n+1))
 prev=sp.cos(x)-sum((-1)**k*x**(2*k)/sp.factorial(2*k)for k in range(n))
 assert sp.simplify(sp.diff(e,x,2)+prev)==0
 assert e.subs(x,0)==sp.diff(e,x).subs(x,0)==0
 exact.append({'cosine_recurrence_n':n,'verdict':'PASS'})
examples=[]
for A in [Q(6,5),Q(3,2),Q(2),Q(3),Q(10)]:
 for j in [1,3,7]:
  for m in [1,2,3,4]:
   g=j-1+A*m;q=2*(A-1);b=g/q
   assert j-2+A*m-g-q==-1-q
   assert m-2*b==-(m+j-1)/(A-1)<0
   assert (1+g-j)/A==m
   for a in range(m):assert j-2+A*a-g < -1
   phase=(1j)**(j+m+1)
   if m%2==0:assert phase.imag==0 and abs(phase)==1
   values=[]
   for order in [64,128]:
    u,w=np.polynomial.legendre.leggauss(order);bump=np.exp(-1/(1-u*u));power=float(m-2*b)
    moment=float(.1*np.dot(w*bump,(1.1+.1*u)**power-(1.9+.1*u)**power))
    assert moment>0;values.append(moment)
   assert abs(values[1]-values[0])<1e-9*values[1]
   examples.append({'A':str(A),'j':j,'m':m,'g':str(g),'power':str(m-2*b),'I64':values[0],'I128':values[1],'relative_difference':abs(values[1]-values[0])/values[1]})
for m in range(1,7):
 for a in range(m):
  expr=(x**(a-m)-1)/(m-a)
  assert sp.simplify(sp.diff(expr,x)+x**(a-m-1))==0
 exact.append({'critical_tail_m':m,'verdict':'PASS'})
files=[ROOT/'PROOF.md',Path(__file__)];out={'utc':datetime.now(timezone.utc).isoformat(),'exact_checks':exact,'examples':examples,'verdict':'PASS','pins':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in files},'scope':'Exact algebra and floating compact-moment illustrations. Gaussian agreement is not a rigorous quadrature enclosure or proof of the axis asymptotic.'}
(ROOT/'verification/check.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(exact),'exact recurrence/antiderivative checks;',len(examples),'parameter examples; max moment relative difference',max(r['relative_difference']for r in examples))
