"""Exact finite-Taylor coefficient controls for packet139 extension."""
from pathlib import Path
from datetime import datetime,timezone
import sympy as s
import json,sys,time
start=time.perf_counter();root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True)
x,y=s.symbols('x y');rows=[]
for beta in [s.Rational(1),s.Rational(2),s.Rational(9,4),s.Rational(7,2)]:
 a=1+3*beta/2;k=beta-2;b=a*y+s.Rational(2,7)*y*y
 for m in [1,3,5,7,9]:
  j=2+y+x*x*(1+3*y)+x**4/7;j0=j.subs(x,0);V=b+s.integrate(x**m*j,(x,0,x));J=s.diff(V,x)
  assert s.expand(J-x**m*j)==0
  for ell in range(m):
   # Lower h coefficients are zero, as in the induction.
   h0=1+y+2*y*y;T=x**(ell+1)*h0/(ell+1)+s.Rational(3,11)*x**(ell+3)*y
   h=s.diff(T,x)
   cleared=s.expand(x**m*j*j*s.diff(T,y)-j*V*s.diff(h,y)+(V*s.diff(j,y)+j*(k-s.diff(V,y)))*h)
   actual=cleared.coeff(x,ell)
   expected=-b*j0*s.diff(h0,y)+(b*s.diff(j0,y)+j0*(k-s.diff(b,y)))*h0
   assert s.expand(actual-expected)==0
   rows.append({'beta':str(beta),'m':m,'ell':ell,'passed':True})
result={'utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.perf_counter()-start,'count':len(rows),'cases':rows,'scope':'Finite exact coefficient identities, not an inference from Taylor series or an existence theorem.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(result['count'],'passed',result['elapsed_seconds'])
