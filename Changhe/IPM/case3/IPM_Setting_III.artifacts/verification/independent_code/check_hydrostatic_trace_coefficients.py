"""Manufactured arithmetic and integral checks for result208."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import mpmath as mp
import sympy as sp
from hydrostatic_trace_coefficients import *
r=Path('research/hydrostatic_trace_compatibility_diagnostic/verification');checks=[];start=time.monotonic()
def ck(n,b,d=None):checks.append(dict(name=n,pass_=bool(b),detail=d))
z=sp.symbols('z')
for k,T in enumerate(angular_polynomials(12)):
 ck('integerChebyshev'+str(k),sp.expand(sum(v*z**j for j,v in enumerate(T))-sp.chebyshevt(k,2*z-1))==0)
p,x,y=sp.symbols('p x y',positive=True)
for j in range(4):
 m=2*j;t=p-1-2*j;f=x**m*y*(x*x+y*y)**(t/2)
 expected=y*(m*(m-1)*(1+y*y)**(t/2)+t*(2*m+1)*(1+y*y)**(t/2-1)+t*(t-2)*(1+y*y)**(t/2-2))
 ck('Cartesiansecondderivative'+str(j),sp.simplify(sp.diff(f,x,2).subs(x,1)-expected)==0)
for ps in ['0.3333333333333333333333333333333333','0.5','0.75']:
 with mp.workdps(50):
  p=mp.mpf(ps);reference=[(p+5)/(2*(p+2)),(1-p)/(2*(p+2))]
  ck('referenceCp0 '+ps,abs(moments(monomials(reference),p)['Cp'])<mp.mpf('1e-46'))
  for name,b in [('mode0',[1]),('mode3',[0,0,0,1]),('combination',[mp.mpf(1),mp.mpf('0.13'),mp.mpf('-.07')])]:
   a=monomials(b);exact=moments(a,p);ii=integral_check(a,p,4,96)
   for field in ['moment','q']:ck(name+field+ps,abs(ii[field]-exact['Cp'])<mp.mpf('1e-42')*(1+abs(exact['Cp'])),mp.nstr(abs(ii[field]-exact['Cp']),12))
  for eps in [mp.mpf('0.1'),mp.mpf('0.01'),mp.mpf('0.001')]:
   er=[abs(t)**p-((t*t+eps*eps)**(p/2)-eps**p)for t in [mp.mpf(0),eps/10,eps,mp.mpf('.01'),mp.mpf('.1'),mp.mpf(1)]]
   ck('analyticcuspapproximation '+ps+' '+str(eps),min(er)>-mp.mpf('1e-48')and max(er)<=eps**p*(1+mp.mpf('1e-45')))
# First two coefficients of the inverse radial relation and nonlinear density.
zeta,P,b,bp,k=sp.symbols('zeta P b bp k',positive=True)
w=zeta/2-zeta*zeta/(8*P)
ck('radialinverseorder2',sp.series(2*w*(1-w)**(-1/(2*P)),zeta,0,3).removeO()==zeta)
term=sp.series(w*(1-w)**k*(b-2*w*bp),zeta,0,3).removeO()
ck('A2formula',sp.expand(term).coeff(zeta,2)==-b/(8*P)-k*b/4-bp/2)
out=dict(utc=datetime.now(timezone.utc).isoformat(),elapsed=time.monotonic()-start,checks=checks,pass_count=sum(t['pass_']for t in checks),fail_count=sum(not t['pass_']for t in checks),module_sha256=hashlib.sha256(Path('independent_code/hydrostatic_trace_coefficients.py').read_bytes()).hexdigest())
(r/'MANUFACTURED.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['elapsed'],out['pass_count'],'PASS',out['fail_count'],'FAIL')
for t in checks:
 if not t['pass_']:print('FAIL',t)
if out['fail_count']:raise SystemExit(1)
